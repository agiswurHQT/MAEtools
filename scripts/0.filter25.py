#!/public/software/bin/python2.7
#coding:utf-8

import sys
import collections


samfile=open(sys.argv[1],'r')
outputfile=open(sys.argv[2],'w')

dictloc=collections.OrderedDict()
listw=[]
temnum=1
for i in samfile:
	temlst=i.split('\t')
	if len(temlst[9])==25:
		listw.append([temlst[2],temlst[3]])
		if len(listw)==2:
			if listw[0]==listw[1]:
				temnum=temnum+1	
				listw=[listw[1]]	
			else:
				temstr=listw[0][0]+'\t'+listw[0][1]+'\t'+str(int(listw[0][1])+24)+'\t'+str(temnum)+'\n'							
				outputfile.write(temstr)
				listw=[listw[1]]
				temnum=1

temstr=listw[0][0]+'\t'+listw[0][1]+'\t'+str(int(listw[0][1])+24)+'\t'+str(temnum)+'\n'
outputfile.write(temstr)
	
samfile.close()
outputfile.close()
