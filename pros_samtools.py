#coding:utf-8

import os
import commands

def mergesam(inputpath,inputdict):
	if inputpath.endswith('/'):
		inputpath=inputpath[:-1]

	listd=os.listdir(inputpath)
	listvp=[i for i in listd if i.endswith('valid.sam')]
	
	temid=listvp[0].split('.')[0]
	temcmd='cat '	
	for i in listvp:
		temcmd=temcmd+inputpath+'/'+i+' '
	temcmd=temcmd+' > '+inputpath+'/'+temid+'.merge.sam'	
	temfile=open(inputdict['outputpath']+'/script/'+temid+'.merge.sh','w')
	temfile.write(temcmd)
	temfile.close()


def generateCMD(inputpath,inputdict,inputtype):
	listd=os.listdir(inputpath)
	for i in listd:
		if i.endswith('valid.sam'):	
			temid=i.split('.')[0]
			break

	if inputtype=='valid':
		temcmd=inputdict['samtools']+' view -T '+inputdict['reference']+' -bS '+inputpath+'/'+temid+'.valid.sam > '+inputpath+'/'+temid+'.valid.bam\n'
	elif inputtype=='merge':
		temcmd=inputdict['samtools']+' view -T '+inputdict['reference']+' -bS '+inputpath+'/'+temid+'.merge.sam > '+inputpath+'/'+temid+'.valid.bam\n'
	else:
		pass

	temfile=open(inputdict['outputpath']+'/script/'+temid+'.samtools.sh','w')
	temfile.write(temcmd)

	temcmd=inputdict['samtools']+' sort '+inputpath+'/'+temid+'.valid.bam '+inputpath+'/'+temid+'.valid.sort\n'
	temfile.write(temcmd)
	temcmd=inputdict['samtools']+'view '+inputpath+'/'+temid+'.valid.sort.bam > '+inputpath+'/'+temid+'.valid.sort.sam'
	temfile.write(temcmd)
	temfile.close()
