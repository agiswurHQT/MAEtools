#!/bin/bash
input_lib=${1}
output_lib=${2}
cv=${3}
outdir=${4}
p1=${output_lib##*/}
prefix=${p1%.*}

export PATH=/usr/bin:$PATH

/public/agis/zhangyubo_group/huangqitong/software/bedtools/bin/bedtools intersect -a ${output_lib} -b ${input_lib} -wo | awk '{if ($9==24) print }' > ${outdir}/${prefix}_overlap.txt
/public/agis/zhangyubo_group/huangqitong/software/bedtools/bin/bedtools intersect -a ${output_lib} -b ${input_lib} -wao | awk -va=${cv} '{if ($9==0) print $1"\t"$2"\t"$3"\t"$4"\t"$5"\t"$6"\t"$7"\t"a"\t"$9}' > ${outdir}/${prefix}_no_overlap.txt
cat ${outdir}/${prefix}_overlap.txt ${outdir}/${prefix}_no_overlap.txt > ${outdir}/${prefix}_all.txt
rm ${outdir}/${prefix}_overlap.txt ${outdir}/${prefix}_no_overlap.txt

