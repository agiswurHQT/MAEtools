#coding:utf-8

import os
import commands

def generateAdapt(inputST):
        if inputST=='SE':
                gseq='CTAACTGGCCGGTACCTGAGCTCGCTAGCCTCGAGTCGTCGGCAGCGTCAGATGTGTATAAGAGACAG'
                aseq='CTGTCTCTTATACACATCTCCGAGCCCACGAGACAAGCTTAGACACTAGAGGGTATATAATGGAAGCTCG'
        elif inputST=='PE':                                   #gseq and aseq are reverse complementary series, so we didnt set different -a -g paramenters. If they are not reverse complementary series, we need to correct these parameter  manually
                gseq='AGATGTGTATAAGAGACAG'
                aseq='CTGTCTCTTATACACATCT'
                #default foramt:5’-AATGATACGGCGACCACCGAGATCTACACIIIIIIIITCGTCGGCAGCGTCAGATGTGTATAAGAGACAG-NNNNNN-CTGTCTCTTATACACATCTCCGAGCCCACGAGACIIIIIIIIATCTCGTATGCCGTCTTCTGCTTG-3’
        return gseq,aseq


def generateCMD(inputdict,inputST,inpath):
	ref=(inputdict['reference'].split('/')[-1]).split('.')[0]

        if not os.path.exists(inputdict['outputpath']+'/cutad'):
                temcmd='mkdir '+inputdict['outputpath']+'/cutad'
                commands.getoutput(temcmd)
        if not os.path.exists(inputdict['outputpath']+'/bwa_'+ref):
                temcmd='mkdir '+inputdict['outputpath']+'/bwa_'+ref
                commands.getoutput(temcmd)
        if not os.path.exists(inputdict['outputpath']+'/script'):
                temcmd='mkdir '+inputdict['outputpath']+'/script'
                commands.getoutput(temcmd)

        if inputdict['outputpath'].endswith('/'):
                inputdict['outputpath']=inputdict['outputpath'][:-1]

        listd=os.listdir(inpath)
        seq1,seq2=generateAdapt(inputST)
        if inputST=='PE':
                lstpair=[]
                for i in listd:
                        if i.endswith('.gz'):
                                lstpair.append(i)
                                temid=i.split('.')[0]
                                temcmd=inputdict['cutadapt']+' -g '+seq1+' -a '+seq2+' -o '+inputdict['outputpath']+'/cutad/'+i+' '+inpath+'/'+i
                                temfile=open(inputdict['outputpath']+'/script/'+temid+'.cutad.sh','w')
                                temfile.write(temcmd)
                                temfile.close()

                                lstpair.append(inputdict['outputpath']+'/bwa_'+ref+'/'+temid+'.sai')
                                temcmd=inputdict['bwa']+' aln '+inputdict['reference']+' '+inputdict['outputpath']+'/cutad/'+i+' > '+inputdict['outputpath']+'/bwa_'+ref+'/'+temid+'.sai'
                                temfile=open(inputdict['outputpath']+'/script/'+temid+'.aln.sh','w')
                                temfile.write(temcmd)
                                temfile.close()


                temcmd=inputdict['bwa']+' sampe '+inputdict['reference']+' '+lstpair[1]+' '+lstpair[3]+' '+inputdict['outputpath']+'/cutad/'+lstpair[0]+' '+inputdict['outputpath']+'/cutad/'+lstpair[2]+' > '+inputdict['outputpath']+'/bwa_'+ref+'/'+temid+'.sam'
                temfile=open(inputdict['outputpath']+'/script/'+temid+'.sampe.sh','w')
                temfile.write(temcmd)
                temfile.close()

                temfile=open(inputdict['outputpath']+'/script/'+temid+'.grep.sh','w')
                temcmd='grep "XT:A:U" '+inputdict['outputpath']+'/bwa_'+ref+'/'+temid+'.sam > '+inputdict['outputpath']+'/bwa_'+ref+'/'+temid+'.unique.sam'
                temfile.write(temcmd)
                temfile.close()

                temcmd=inputdict['aligned_pair']+' '+inputdict['outputpath']+'/bwa_'+ref+'/'+temid+'.unique.sam '+inputdict['outputpath']+'/bwa_'+ref+'/'+temid+'.valid.sam'
                temfile=open(inputdict['outputpath']+'/script/'+temid+'.aligned_pair.sh','w')
                temfile.write(temcmd)
                temfile.close()

        elif inputST=='SE':
                for i in listd:
                        if i.endswith('.gz'):
                                temid=i.split('.')[0]
                                temcmd=inputdict['cutadapt']+' -g '+seq1+' -a '+seq2+' -o '+inputdict['outputpath']+'/cutad/'+i+' '+inpath+'/'+i
                                temfile=open(inputdict['outputpath']+'/script/'+temid+'.cutad.sh','w')
                                temfile.write(temcmd)
                                temfile.close()
				
				temfile=open(inputdict['outputpath']+'/script/'+temid+'.sh','w')
                                temcmd=inputdict['bwa']+' aln '+inputdict['reference']+' '+inputdict['outputpath']+'/cutad/'+i+' > '+inputdict['outputpath']+'/bwa_'+ref+'/'+temid+'.sai\n'
                                temfile.write(temcmd)
				temcmd=inputdict['bwa']+' samse '+inputdict['reference']+' '+inputdict['outputpath']+'/bwa_'+ref+'/'+temid+'.sai '+inputdict['outputpath']+'/cutad/'+i+' > '+inputdict['outputpath']+'/bwa_'+ref+'/'+temid+'.sam'
                                temfile.write(temcmd)
                                temfile.close()

                                temfile=open(inputdict['outputpath']+'/script/'+temid+'.grep.sh','w')
                                temcmd='grep "XT:A:U" '+inputdict['outputpath']+'/bwa_'+ref+'/'+temid+'.sam > '+inputdict['outputpath']+'/bwa_'+ref+'/'+temid+'.valid.sam'
                                temfile.write(temcmd)
                                temfile.close()














