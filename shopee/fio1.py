#!/usr/bin/python2.7
# coding: utf-8
import time
import os
import sys
import platform
import shlex
import subprocess
import json
from prettytable import PrettyTable

#rwResult = {}
rwResult2 = {}


def bash(cmd):
    """
    run a bash shell command
    执行bash命令
    """
    return shlex.os.system(cmd)


def color_print(msg, color='red', exits=False):
    """
    Print colorful string.
    颜色打印字符或者退出
    """
    color_msg = {'blue': '\033[1;36m%s\033[0m',
                 'green': '\033[1;32m%s\033[0m',
                 'yellow': '\033[1;33m%s\033[0m',
                 'red': '\033[1;31m%s\033[0m',
                 'title': '\033[30;42m%s\033[0m',
                 'info': '\033[32m%s\033[0m'}
    msg = color_msg.get(color, 'red') % msg
    print(msg)
    if exits:
        time.sleep(2)
        sys.exit()
    return msg





def Usage():
    print('''
用法： ./fio size_4k size_128k /path/to/test_file"
参数:
      size_4k      进行4k读写测试的文件大小。
      size_128k    进行128k读写测试的文件大小。
      /path/to/test_file    测试文件读写的路径，这里是一个文件的完整路径。
    ''')



class FioTest(object):
    def __init__(self,name,filename,rw,bs,size,direct=1,iodepth=1,ioengine="libaio",runtime=60):
        print("lest start")
        self.name=name
        self.filename=filename
        self.direct=direct
        self.rw=rw
        self.bs=bs
        self.size=size
        self.iodepth=iodepth
        self.ioengine=ioengine
        self.runtime=runtime

    def execCmd(self):
       cmd ="fio --name="+self.name+" --rw="+self.rw+" --iodepth="+str(self.iodepth)+" --ioengine="+self.ioengine+" --thread --direct="+str(self.direct)+" --norandommap --bs="+self.bs+" --size="+self.size+" --runtime="+str(self.runtime)+" --filename="+self.filename+  " --minimal --output-format=json"
       #--output="+self.name+ "-iodepth-" +str(self.iodepth)+ "-" + self.rw
       print(cmd)
       return cmd

    def runCmd(self, cmd):
        result_str = ''
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out = process.stdout
        errors = process.stderr
        err = errors.read()
        if err:
            color_print("执行错误")
            color_print(err)
            os._exit(1)
        result_str = out.read().strip()
        if out:
            out.close()
        if errors:
            errors.close()
        return str(result_str)

    def explain(self, result):
        if self.rw == "read" or self.rw == "randread":
            r = json.loads(result)
            iops = r["jobs"][0]["read"]["iops"]
            bw = r["jobs"][0]["read"]["bw"]
            return iops,bw
        else:
            if self.rw == "write" or self.rw == "randwrite":
                r = json.loads(result)
                iops = r["jobs"][0]["write"]["iops"]
                bw = r["jobs"][0]["write"]["bw"]
                return iops, bw

    def explain2(self, result):
            r = json.loads(result)
            read_iops = r["jobs"][0]["read"]["iops"]
            print("===read_iops==",self.rw, read_iops)
            read_bw = r["jobs"][0]["read"]["bw"]
            print("===read_bw==", self.rw, read_bw)
            write_iops = r["jobs"][0]["write"]["iops"]
            print("===write_iops==", self.rw, write_iops)
            write_bw = r["jobs"][0]["write"]["bw"]
            print("===write_bw==", self.rw, write_bw)
            return read_iops,read_bw,write_iops,write_bw





    def printResult():
        table = PrettyTable(["项目", "写IOPS", "写带宽", "读IOPS", "读带宽"])
        for k, v in rwResult.items():
            list = [k, v["write_iops"], v["write_bw"], v["read_iops"], v["read_bw"]]
            table.add_row(list)
        color_print(table)




    def expResult2(self, read_iops,read_bw,write_iops,write_bw):
        name = ""
        read_iops = ""
        read_bw = ""
        write_iops = ""
        write_bw = ""
        rw = self.rw
        if rw == "write" or rw == "read":
            name = "seq-"+self.rw+"-bs-"+self.bs+"-iodepth-"+str(self.iodepth)
            read_iops = read_iops
            read_bw = read_bw
            write_iops = write_iops
            write_bw =write_bw



        elif rw == "randwrite" or rw == "randread":
            name = "rand-"+self.rw+"-bs-"+self.bs+"-iodepth-"+str(self.iodepth)
            read_iops = read_iops
            read_bw = read_bw
            write_iops = write_iops
            write_bw = write_bw
        elif rw == "randrw":
            name =  self.rw + "-bs-" + self.bs + "-iodepth-" + str(self.iodepth)
            read_iops = read_iops
            read_bw = read_bw
            write_iops = write_iops
            write_bw = write_bw

        if name in rwResult2.keys():
            print("===rwResult2==========",name)
            rwResult2[name][read_iops] = read_iops
            rwResult2[name][read_bw] = read_bw
            rwResult2[name][write_iops] = write_iops
            rwResult2[name][write_bw] = write_bw
        else:
            rwResult2[name] = {}
            rwResult2[name][read_iops] = read_iops
            rwResult2[name][read_bw] = read_bw
            rwResult2[name][write_iops] = write_iops
            rwResult2[name][write_bw] = write_bw




    def saveResult(self):
        cmd = self.execCmd()
        result = self.runCmd(cmd)
        read_iops,read_bw,write_iops,write_bw = self.explain2(result)
        self.expResult2(read_iops,read_bw,write_iops,write_bw)


def printResult2():
    table = PrettyTable(["项目", "写IOPS", "写带宽", "读IOPS", "读带宽"])
    for k, v in rwResult2.items():
        print(type(rwResult2))
        print("========",)
        list = [k, v["read_iops"], v["read_bw"], v["write_iops"], v["write_bw"]]
        table.add_row(list)
    color_print(table)


if __name__ == '__main__':
    #if len(sys.argv) != 4:
       #Usage()
       #exit(1)
 #   bs = sys.argv[1]
 #   size = sys.argv[2]
 #   filename = sys.argv[3]

    bslist = ["4k","8k"]
    sizelist = ["1m","10m"]
    filename = "testfile"
    for bs in bslist:
        for size in sizelist:
            cmd1 = FioTest(name="randread-", rw="randread", iodepth=1, ioengine="libaio", direct=1, bs=bs, size=size, runtime=60, filename=filename)
            cmd1.saveResult()


            cmd1 = FioTest(name="randwrite-"+bs, rw="randwrite", iodepth=1, ioengine="libaio", direct=1, bs=bs, size=size,
                   runtime=60, filename=filename)
            cmd1.saveResult()
            cmd1 = FioTest(name="read-" + bs, rw="read", iodepth=1, ioengine="libaio", direct=1, bs=bs, size=size,
                   runtime=60, filename=filename)
            cmd1.saveResult()
            cmd1 = FioTest(name="write-" + bs, rw="write", iodepth=1, ioengine="libaio", direct=1, bs=bs, size=size,
                   runtime=60, filename=filename)
            cmd1.saveResult()
            printResult2()



