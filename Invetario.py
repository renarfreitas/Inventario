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
from tkinter import ttk

"""Variáveis"""
patrimonioh = str
patrimoniom = str
local = str
matricula = str

#Funções
def bt1():
    #print('ATUALIZADO!')
    status['text']="Atualizado!"
    patrimonioh = str(entrd0.get())
    patrimoniom = str(entrd1.get())
    local = str(entrd2.get())
    matricula = str(entrd3.get())
    a = open("BD.xls", "w")
    a.write("\n")
    a.write(host)
    a.write("\t")
    a.write(so_version)
    a.write("\t")
    a.write(s5)
    a.write("\t")
    a.write(memo6)
    a.write("\t")
    a.write(patrimonioh)
    a.write("\t")
    a.write(patrimoniom)
    a.write("\t")
    a.write(local)
    a.write("\t")
    a.write(matricula)
    a.close()
        
"""Janela Principal"""    
myjan=Tk()
"""Lebel supoerior"""
mlb=Label(text='==| ATUALIZAÇÃO DE MICROCOMPUTADORES NO INVENTÁRIO |==\n', fg='blue',bd=1,relief=SUNKEN,anchor=W)
mlb.pack()

"""Foto de fundo"""
photo=PhotoImage(file='Metrô-Salvador.png')
label=Label(myjan,image=photo)
label.pack()

"""Leitura do SO e Hardware"""

"""Identifica se é Windows, Linux e outros SO"""
##so = platform.system() 

"""Identifica a arquitetura do processador"""
info = cpuinfo.get_cpu_info()
processor = info['vendor_id']
brand = info['brand']
bits = info ['bits']
str(brand)
"""Nome do Computador"""
host = platform.node()

"""Em caso de Linux exibe informações da distribuição e no caso de Windows exibe algumas informações sobre o Windows"""
so_version = platform.platform()
so_complit_version = platform.version()

"""Número de serie"""
s = subprocess.check_output(['cmd.exe', '/c','wmic bios get serialnumber'])
s0 = str(s)
s1 = s0.replace(" ","")
s2 = s1.replace("\\r","")
s3 = s2.replace("\\n","")
s4 = s3.replace("b'SerialNumber","")
s5 = s4.replace("'","")

"""Quantidade de memória"""
memo = subprocess.check_output(['cmd.exe', '/c','wmic ComputerSystem get TotalPhysicalMemory/value'])
memo0 = str(memo)
memo1 = memo0.replace(" ","")
memo2 = memo1.replace("\\r","")
memo3 = memo2.replace("\\n","")
memo4 = memo3.replace("b'TotalPhysicalMemory","")
memo5 = memo4.replace("'","")
memo6 = memo5.replace("=","")

"""Entrada de dados"""

"""Patrimônio Host"""
entrd0=Entry(myjan,textvariable = patrimonioh)
entrd0.place(x=10, y=378)
"""Patrimônio Monitor"""
entrd1=Entry(myjan,textvariable = patrimoniom)
entrd1.place(x=10, y=420)
"""Localização"""
entrd2=Entry(myjan, width = 55, textvariable = local)
entrd2.place(x=10, y=458)
"""Matricula"""
entrd3=Entry(myjan, textvariable = matricula)
entrd3.place(x=10, y=498)

"""Label"""
lb=Label(myjan, text="Host: "+str(platform.node()), fg='yellow', bg='grey')
lb.place(x=10, y=50)
lb=Label(myjan, text="S O: "+str(platform.platform()), fg='yellow', bg='grey')
lb.place(x=10, y=70)
lb=Label(myjan, text="Processador: "+str(brand), fg='yellow', bg='grey')
lb.place(x=10, y=90)
lb=Label(myjan, text="Número de serie: "+str(s5), fg='yellow', bg='grey')
lb.place(x=10, y=110)
lb=Label(myjan, text="Capacidade memória: " +memo6, fg='yellow', bg='grey')
lb.place(x=10, y=130)
"""cliente=PhotoImage(file='cliente.png')
lb=Label(myjan,image=cliente)
lb.place(x=10, y=150)"""

lb0=Label(myjan, text='PATRIMÔNIO DO HOST', fg='black', bg='grey')
lb0.place(x=10, y=358)

lb1=Label(myjan, text='PATRIMÔNIO DO MONITOR', fg='black', bg='grey')
lb1.place(x=10, y=399)

lb2=Label(myjan, text='LOCALIZAÇÃO, (Ex: Estação ACN, Sala de Descompressão)', fg='black', bg='grey')
lb2.place(x=10, y=438)

lb3=Label(myjan, text='MATRICULA DO USUÁRIO', fg='black', bg='grey')
lb3.place(x=10, y=478)

"""Botões"""
bt1=Button(myjan, width=20, text="ATUALIZAR",command=bt1)
bt1.place(x=350, y=490)

"""Barra de status"""
status=Label(myjan, text='Funcionando.',fg='blue',bd=1,relief=SUNKEN,anchor=W)
status.pack(side=BOTTOM, fill=X)

myjan.title("VeriMetrô")
myjan.resizable(width=False,height=False)
myjan.geometry('510x540')

myjan["bg"] = "grey"
myjan.mainloop()
