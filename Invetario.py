#########################################
#	         Invetário Eletrônico		      #
#					                              #
#    Autor: Renar Freitas dos Santos	  #
#     e-mail: renarfreitas@gmail.com	  #
#       Data: 16/07/2016 | 23:25        #
# Ultima modificação: 10/07/2018|14:48  #
#########################################

import platform
import ctypes
import subprocess
import cpuinfo
import os, sys
import glob
import re
import time
import multiprocessing
import pickle
import base64
import uuid
import xlrd
import xlwt
from tkinter import*

#Funções
def bt1():
    #print('ATUALIZADO!')
    status['text']="Atualizado!"
    a=open("bd.xls", "w")
    a.write(host)
    a.write("\t")
    a.write(s5)
    a.write("\t")
    a.write(matricula)
    a.write("\t")
    a.write(local)
    a.write("\t")
    a.write(platform.platform)
    a.close()
 def bt2():
    #print('CADASTRADO!')
    status['text']="Cadastrado!"

    
#Janela Principal    
myjan=Tk()
#Lebel supoerior
mlb=Label(text='==| ATUALIZAÇÃO DE MICROCOMPUTADORES NO INVENTÁRIO |==\n', fg='blue',bd=1,relief=SUNKEN,anchor=W)
mlb.pack()

#Foto de fundo
photo = PhotoImage(file='Metrô-Salvador.png')
label = Label(myjan,image=photo)
label.pack()

#Leitura do SO e Hardware

###Identifica se é Windows, Linux e outros SO
##so = platform.system() 

#Identifica a arquitetura do processador"
info = cpuinfo.get_cpu_info()
processor = info['vendor_id']
brand = info['brand']
bits = info ['bits']
str(brand)
#Nome do Computador
host = platform.node()

#Em caso de Linux exibe informações da distribuição e no caso de Windows exibe algumas informações sobre o Windows
so_version = platform.platform()
so_complit_version = platform.version()

#Número de serie
s = subprocess.check_output(['cmd.exe', '/c','wmic bios get serialnumber'])
s0 = str(s)
s1 = s0.replace(" ","")
s2 = s1.replace("\\r","")
s3 = s2.replace("\\n","")
s4 = s3.replace("b'SerialNumber","")
s5 = s4.replace("'","")

#Quantidade de memória
memo = subprocess.check_output(['cmd.exe', '/c','wmic ComputerSystem get TotalPhysicalMemory/value'])
memo0 = str(memo)
memo1 = memo0.replace(" ","")
memo2 = memo1.replace("\\r","")
memo3 = memo2.replace("\\n","")
memo4 = memo3.replace("b'SerialNumber","")
memo5 = memo4.replace("'","")

#Entrada de dados
##entrd=Entry(myjan)
##entrd.place(x=10, y=370)

entrd1=Entry(myjan)
entrd1.place(x=10, y=400)

entrd2=Entry(myjan)
entrd2.place(x=10, y=430)

entrd3=Entry(myjan)
entrd3.place(x=10, y=460)

#Label
lb=Label(myjan, text="Host: "+str(platform.node()), fg='yellow', bg='grey')
lb.place(x=10, y=100)
lb=Label(myjan, text="S O: "+str(platform.platform()), fg='yellow', bg='grey')
lb.place(x=10, y=120)
lb=Label(myjan, text="Processador: "+str(brand), fg='yellow', bg='grey')
lb.place(x=10, y=140)
lb=Label(myjan, text="Número de serie: "+s5, fg='yellow', bg='grey')
lb.place(x=10, y=160)
lb=Label(myjan, text="Memória fisica: "+memo5, fg='yellow', bg='grey')
lb.place(x=10, y=180)
#lb=Label(myjan, text=matricula, fg='yellow', bg='grey')
#lb.place(x=10, y=180)

##lb0=Label(myjan, text='PATRIMÔNIO MICROCOMPUTADOR', fg='black', bg='grey')
##lb0.place(x=115, y=370)

lb1=Label(myjan, text='PATRIMÔNIO MONITOR', fg='black', bg='grey')
lb1.place(x=115, y=400)

lb2=Label(myjan, text='LOCALIZAÇÃO, (Ex: Estação ACN, Sala de Descompressão)', fg='black', bg='grey')
lb2.place(x=115, y=430)

lb3=Label(myjan, text='MATRICLUCA DO RESPONSÁVEL', fg='black', bg='grey')
lb3.place(x=115, y=460)

status=Label(myjan, text='Funcionando.',fg='blue',bd=1,relief=SUNKEN,anchor=W)
status.pack(side=BOTTOM, fill=X)

myjan.title("VeriMetrô")
myjan.resizable(width=False,height=False)
myjan.geometry('510x540')

myjan["bg"] = "grey"

#Botões
bt1=Button(myjan, width=20, text="ATUALIZAR",command=bt1)
bt1.place(x=350, y=490)

#bt2=Button(myjan, width=20, text="NOVO",command=bt2)
#bt2.place(x=10, y=490)

myjan.mainloop()
