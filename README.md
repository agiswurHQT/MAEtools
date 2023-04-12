# MAEtools

Introduction
MAEtools provides a pipeline for analysing MAE-Seq data starting at mapped paired-end sequencing reads.
It can be used on Linux.

MAE-seq is an experimental technique for detecting transcriptional regulatory elements down to 25 nt. This project is a tool for analyzing MAE-seq data, which has three modules: align/psamtools/quantify.

This version can be called directly without installation.
Prerequisite:
BWA Version: (>= 0.7.5a-r405)
samtools Version: (>= 0.1.19-44428cd)
cutadapt Version (>= 1.8.dev0)


Usage
Step 1: Mapping
This step will generate 7 cmd files in output/script/.
The order of execution is：
*1.cutad.sh
*2.cutad.sh
*1.aln.sh
*2.aln.sh
*.sampe.sh
*.grep.sh
*.aligned_pair.sh
Finally we will get valid.sam file in this step.

Step 2: Sam files processing
This step will generate 1/2 cmd files. 1 for single library/2 for multiple libraries.
The order of execution is：
*.merge.sh
*.samtools.sh
Finally we will get valid.sort.sam file in this step

Step3： Quantitative analysis processing
This step will generate 2 cmd files.
*.filter25.sh
*.nor.sh
Finally we will get nor.txt file in this step
