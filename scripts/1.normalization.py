#!/public/software/bin/python2.7
#coding:utf-8

import sys
import math

inputfile=open(sys.argv[1],'r')
datasize=float(sys.argv[2])
pcrc=float(sys.argv[3])
omega=float(sys.argv[4])

norfile=open(sys.argv[5],'w')

for i in inputfile:
	temlst=i.split('\t')
	pcre=math.log10(2**pcrc)
	norval=int(temlst[-1])*omega/(datasize*pcre)
	temstr="\t".join(temlst[:-1])+'\t'+str(norval)+'\n'
	norfile.write(temstr)

inputfile.close()
norfile.close()
