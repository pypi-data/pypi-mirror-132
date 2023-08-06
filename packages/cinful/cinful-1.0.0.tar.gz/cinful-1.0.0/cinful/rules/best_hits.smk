import pandas as pd
from Bio import SeqIO
import pyTMHMM

SAMPLES, = glob_wildcards("{sample}.fna")

def prodigalFa2DF(fa):
  prodigalDict = {"id":[],"seq":[],"contig":[],"start":[],"stop":[],"strand":[]}
  for seq_record in SeqIO.parse(fa,"fasta"):
    descriptionParts = seq_record.description.split("#") 

    start = descriptionParts[1].strip()
    stop = descriptionParts[2].strip()
    strand = descriptionParts[3].strip()
    contig = '_'.join(seq_record.id.split("_")[:-1])

    prodigalDict["id"].append(seq_record.id)
    prodigalDict["seq"].append(seq_record.seq)
    prodigalDict["contig"].append(contig)
    prodigalDict["stop"].append(stop)
    prodigalDict["start"].append(start)
    prodigalDict["strand"].append(strand)

  return pd.DataFrame.from_dict(prodigalDict)


def homology_withProdigal(homology_results_file, prodigalDF):
	homology_resultsDF = pd.read_csv(homology_results_file)

	return homology_resultsDF.merge(prodigalDF, left_on="qseqid",right_on="pephash")#, left_on = "qseqid", right_on = "id")

def componentDFs(homology_withProdigalDF):	
	microcinDF = homology_withProdigalDF[homology_withProdigalDF["component"]=="microcins.verified"]
	immunity_proteinDF = homology_withProdigalDF[homology_withProdigalDF["component"]=="immunity_proteins.verified"]
	CvaBDF = homology_withProdigalDF[homology_withProdigalDF["component"]=="CvaB.verified"]
	return microcinDF, immunity_proteinDF, CvaBDF

def bestHits(microcinDF,immunity_proteinDF,CvaBDF):
  best_microcin_idx = microcinDF.groupby(['contig'])['bitscore'].transform(max) == microcinDF['bitscore']
  best_microcinDF = microcinDF[best_microcin_idx]

  best_immunity_protein_idx = immunity_proteinDF.groupby(['contig'])['bitscore'].transform(max) == immunity_proteinDF['bitscore']
  best_immunity_proteinDF = immunity_proteinDF[best_immunity_protein_idx]

  best_CvaB_idx = CvaBDF.groupby(['contig'])['bitscore'].transform(max) == CvaBDF['bitscore']
  best_CvaBDF = CvaBDF[best_CvaB_idx]

  return pd.concat([best_microcinDF, best_immunity_proteinDF,best_CvaBDF])


def contigs_wMicrocins(best_hitsFile):
	best_hitsDF = pd.read_csv(best_hitsFile)
	needed_columns = ["cinful_id","contig","start","stop","strand"]
	renameDict_microcin = {"cinful_id":"microcin_id","start":"microcin_start","stop":"microcin_stop","strand":"microcin_strand"}
	microcin_contigs = best_hitsDF[best_hitsDF["component"] == "microcins.verified"][needed_columns].rename(columns=renameDict_microcin)
	microcin_contig_componentDF = best_hitsDF[best_hitsDF["contig"].isin(microcin_contigs["contig"])]

	renameDict_CvaB = {"cinful_id":"CvaB_id","start":"CvaB_start","stop":"CvaB_stop","strand":"CvaB_strand"}
	microcin_contig_CvaB = microcin_contig_componentDF[microcin_contig_componentDF["component"] == "CvaB.verified"][needed_columns].rename(columns=renameDict_CvaB)

	return microcin_contigs.merge(microcin_contig_CvaB, left_on="contig",right_on="contig")
	
def nearestImmunityProtein(immunityDB, bestMicrocinHits):
	candidateList = []
	for row in bestMicrocinHits.to_dict(orient="records"):
		immunitySubset = immunityDB[immunityDB["sample"] + immunityDB["contig"] == row["sample"]+row["contig"] ].sort_values("start")
		immunitySubset["microcinHit"] = row["cinful_id"]
		immunityUpstream = immunitySubset[immunitySubset["start"] < row["start"]].tail(3)
		immunityDownstream = immunitySubset[immunitySubset["start"] > row["stop"]].head(3)
		nearestCandidates = pd.concat([immunityUpstream,immunityDownstream])
		candidateList.append(nearestCandidates)
	return pd.concat(candidateList)

def tmhmmCol(df,seqCol="seq"):
  tmhmmAnnotations = []
  for seq in df["seq"]:
    tmhmmAnnotation = pyTMHMM.predict(seq.strip("*"), compute_posterior=False)
    tmhmmAnnotations.append(tmhmmAnnotation)
  # df["tmhmm"] = tmhmmAnnotations
  return tmhmmAnnotations	
	
	

	

rule best_hits:
	input:
		merged_homology_results = config["outdir"] + "/02_homology_results/all_merged.csv",
		signalSeq = config["outdir"] + "/01_orf_homology/microcins/signalSeq.hit.csv"
		
	output:
		config["outdir"] + "/03_best_hits/best_hits.csv"
	run:
		
		homologyDF = pd.read_csv(input.merged_homology_results )

		# prodigalDF =  pd.read_csv(input.nr_csv) 
		
		signalSeqDF = pd.read_csv(input.signalSeq)

		# homology_withProdigalDF = homology_withProdigal(homologyFile, prodigalDF)
		microcinDF, immunity_proteinDF, CvaBDF = componentDFs(homologyDF)
		if not microcinDF.empty:
			best_hitsDF = bestHits(microcinDF,immunity_proteinDF,CvaBDF)
			best_hitsDF["signalMatch"] = best_hitsDF["pephash"].isin(signalSeqDF["signalMatch"])
			best_hitsDF.to_csv(output[0], index = False)
			

rule bestHitsContigs:
	input:
		config["outdir"] + "/03_best_hits/best_hits.csv"
	output:
		config["outdir"] + "/03_best_hits/best_hit_contigs.csv"
	run:
		microcinContigsDF = contigs_wMicrocins(input[0])
		microcinContigsDF.to_csv(output[0],index = False)


rule candidate_immunity:
	input:
		bestHits = config["outdir"] + "/03_best_hits/best_hits.csv",
		immunityDB = config["outdir"] + "/01_orf_homology/prodigal_out.all.nr_expanded.csv",
		immunityHomologs = config["outdir"] + "/01_orf_homology/immunity_proteins/blast_v_hmmer.csv"
	output:
		config["outdir"] + "/03_best_hits/best_immunity_protein_candidates.csv"
	run:
		immunityDB = pd.read_csv(input.immunityDB)
		seqLen = immunityDB["seq"].str.len()
		immunityDB = immunityDB[(seqLen <= 250 ) & (seqLen >= 30 )]
		immunityDB = immunityDB[immunityDB["allStandardAA"]]

		bestHits = pd.read_csv(input.bestHits)
		bestMicrocinHits = bestHits[bestHits["component"] == "microcins.verified"]

		immunityHomologs = pd.read_csv(input.immunityHomologs)

		nearestImmunityDF = nearestImmunityProtein(immunityDB, bestMicrocinHits)
		nearestImmunityDF["tmhmm"] = tmhmmCol(nearestImmunityDF)
		nearestImmunityDF["homologyHit"] = nearestImmunityDF["pephash"].isin(immunityHomologs["qseqid"])

		nearestImmunityDF.to_csv(output[0], index = None)



	