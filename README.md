# MAEtools

# Introduction<br />
MAEtools provides a pipeline for analysing MAE-Seq data starting at mapped paired-end sequencing reads.<br />
It can be used on Linux.<br />

MAE-seq is an experimental technique for detecting transcriptional regulatory elements down to 25 nt. This project is a tool for analyzing MAE-seq data, which has three modules: align/psamtools/quantify.<br />

This version can be called directly without installation.<br />
Prerequisite:<br />
BWA Version: (>= 0.7.5a-r405)<br />
samtools Version: (>= 0.1.19-44428cd)<br />
cutadapt Version (>= 1.8.dev0)<br />


# Usage<br />
Step 1: Mapping<br />
This step will generate 7 cmd files in output/script/.<br />
The order of execution is：<br />
*1.cutad.sh<br />
*2.cutad.sh<br />
*1.aln.sh<br />
*2.aln.sh<br />
*.sampe.sh<br />
*.grep.sh<br />
*.aligned_pair.sh<br />
Finally we will get valid.sam file in this step.<br />

Step 2: Sam files processing<br />
This step will generate 1/2 cmd files. 1 for single library/2 for multiple libraries.<br />
The order of execution is：<br />
*.merge.sh<br />
*.samtools.sh<br />
Finally we will get valid.sort.sam file in this step<br />

Step3： Quantitative analysis processing<br />
This step will generate 2 cmd files.<br />
*.filter25.sh<br />
*.nor.sh<br />
Finally we will get nor.txt file in this step<br />

We use Poisson test to have the quantitative analysis. The R script and other necessary scripts are provided in MAEtools/scripts.<br />
We will also update this function and integrate it in coming version.
