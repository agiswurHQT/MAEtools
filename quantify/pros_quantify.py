#coding:utf-8

import os
import commands

def generateCMD(inputpath,inputdict,inputds,inputcn,inputzf):
	if inputpath.endswith('/'):
                inputpath=inputpath[:-1]

	if not os.path.exists(inputdict['outputpath']+'/quant'):
		temcmd='mkdir '+inputdict['outputpath']+'/quant'	
		commands.getoutput(temcmd)

	listd=os.listdir(inputpath)
	listSortSam=[i for i in listd if i.endswith('valid.sort.sam')]
	temid=listSortSam[0].split('.')[0]
		
	temcmd=inputdict['filter25_tools']+' '+inputpath+'/'+listSortSam[0]+' '+inputdict['outputpath']+'/quant/'+temid+'.25.txt'
	temfile=open(inputdict['outputpath']+'/script/'+temid+'.filter25.sh','w')
	temfile.write(temcmd)
	temfile.close()

	temcmd=inputdict['normalization_tools']+' '+inputdict['outputpath']+'/quant'+temid+'.25.txt '+inputds+' '+inputcn+' '+inputzf+' '+inputdict['outputpath']+'/quant/'+temid+'.nor.txt'
	temfile=open(inputdict['outputpath']+'/script/'+temid+'.nor.sh','w')
	temfile.write(temcmd)
	temfile.close()
		
