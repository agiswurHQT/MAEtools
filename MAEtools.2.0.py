#!/public/software/bin/python2.7
#coding:utf-8

import getopt
import sys
import os
import commands
from align import pros_align
from psamtools import pros_samtools
from quantify import pros_quantify

def usage():
        print "#----------------------------------------------------------#"
        print "Program: MAEtool"
        print "Version 2.0" 
        print "#----------------------------------------------------------#"
        print "Usage: MAEtool <command> [options]"
        print "command:"
        print " -h --help       help information"
        print " -v --version    show the version"
        print " --align run the alignment process"
	print " --samproc run the samtools process"
        print " --quantify      run the quantitative process"
        print " -i --input      the path of fastq.gz files/vaild.sam/valid.sort.bam"
        print " -st --SeqType   the sequencing type:SE/PE"
        print " -c --config     the config file for softwares and reference"
        print " -d --datasize   the reads count"
	print " -m --multilibs	(merge/valid) there are multiple libraries"
	print " -C --CycleNum 	the PCR cycle number"
	print " -z --Zoom	the zoom factor"


        note="  \n for align process:    e.g. MAEtools.2.0.py --align --SeqType PE -c config_test.txt -i [INPUTPATH]\n for samtools process: e.g. MAEtools.2.0.py --samproc -m merge -c config_test.txt -i [OUTPUTPATH]/bwa_hg19\n for quantitative process: e.g. MAEtools.2.0.py --quantify -c config_test.txt -d 11753674 -C 15 -z 100000000 -i [OUTPUTPATH]/bwa_hg19"
        print
        print "note:"+note

def readconfig(inputfile):
        cfile=open(inputfile,'r')
        argdict={}
        for i in cfile:
                temlst=i.split('=')	
                temk=temlst[0]
                temv=temlst[1].strip('\n')	
                argdict[temk]=temv
        cfile.close()
        return argdict

def get_option():
        opts,args=getopt.getopt(sys.argv[1:], "hvi:st:c:d:mC:z:", ["help","version","input=","SeqType=","config=","datasize=","align","samproc","quantify","multilibs","CycleNum","Zoom"])
        global inputpath,stype,dictConfig,process,libtype,datasize,cyclenum,zoom
        for opt,arg in opts:
                if opt in ("-h", "--help"):
                        usage()
                        sys.exit()

                if opt in ("-v", "--version"):
                        print "Version 2.0"
                        sys.exit()

		if opt in ("-c", "--config"):
                        dictConfig=readconfig(arg)

		if opt in ("-st", "--SeqType"):
			stype=arg


                if opt in ("-i", "--input"):
                        if arg.endswith('/'):
                                inputpath=arg[:-1]
                        else:
                                inputpath=arg
		
		if opt in ("-m","--multilibs"):
			libtype=arg

		if opt in ("-d","--datasize"):
			datasize=arg

		if opt in ("-C","--CycleNum"):
			cyclenum=arg

		if opt in ("-z","--Zoom"):
			zoom=arg

                if opt in ("--align"):
                        process='align'

		elif opt in ("--samproc"):
			process='samproc'

                elif opt in ("--quantify"):
                        process='quantify'



if __name__=='__main__':
	get_option()
	if process=='align':
		pros_align.generateCMD(dictConfig,stype,inputpath)
	
	elif process=='samproc':
		if libtype=='merge':
			pros_samtools.mergesam(inputpath,dictConfig)	
		pros_samtools.generateCMD(inputpath,dictConfig,libtype)				
		
	elif process=='quantify':
		pros_quantify.generateCMD(inputpath,dictConfig,datasize,cyclenum,zoom)
	



