#!/public/software/bin/python2.7
#coding:utf-8

import sys

samfile=open(sys.argv[1],'r')
outputfile=open(sys.argv[2],'w')
#unpairfile=open(sys.argv[3],'w')

listw=[]
count=0
sumSingle=0
sumMISpair=0
sumUnpair=0
unpair25M=0
for i in samfile:
	count+=1
	listw.append(i)
	if len(listw)==2:
		seq1=listw[0].split('\t')
		seq2=listw[1].split('\t')
		if seq1[0]==seq2[0]:
			d1=[seq1[2],seq1[3]]
			d2=[seq2[2],seq2[3]]
			if d1==d2:
				temstr='\t'.join(seq1)
				outputfile.write(temstr)
				sumSingle+=1
			else:
				#print listw[0]
				#print listw[1]
				v1=seq1[5]
				v2=seq2[6]
				if v1=='25M':
					temstr='\t'.join(seq1)
					outputfile.write(temstr)
					unpair25M+=1
				if v2=='25M':
					temstr='\t'.join(seq2)
					outputfile.write(temstr)
					unpair25M+=1

				sumMISpair=sumMISpair+1

			listw=[]
		else:
			listw=[listw[1]]
			temstr='\t'.join(seq1)
			outputfile.write(temstr)	
			sumUnpair+=1

print 'total:',count
print 'Valid:',sumSingle
print 'diff:',sumMISpair
print 'unpair:',sumUnpair
print 'unpair25M:',unpair25M

samfile.close()
outputfile.close()
#unpairfile.close()
