from tkinter import *
import os
import subprocess
import platform

import Banco

pastasoftw = os.path.dirname(__file__)
nomeArquivo = pastasoftw + "\\inventario.txt"

#===========================Criando*a*Janela===================================#
verify = Tk()
verify.title("Verify - to establish the truth in TI.")
verify.geometry("500x300")
verify.configure(bg = "#dde")

#===========================Capiturar*Dados*Hardware===========================#
"""Identifica a arquitetura do processador"""
#info = cpuinfo.get_cpu_info()
#processor = info['vendor_id']
#brand = info['brand']
#bits = info ['bits']
#str(brand)
"""Nome do Computador"""
hostname = str(platform.node())

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
serialnumber = s5

"""Quantidade de memória"""
memo = subprocess.check_output(['cmd.exe', '/c','wmic ComputerSystem get TotalPhysicalMemory/value'])
memo0 = str(memo)
memo1 = memo0.replace(" ","")
memo2 = memo1.replace("\\r","")
memo3 = memo2.replace("\\n","")
memo4 = memo3.replace("b'TotalPhysicalMemory","")
memo5 = memo4.replace("'","")
memo6 = memo5.replace("=","")
memoria = memo6

#=============================Criando*funçõe===================================#
def gravarDados():
  nomeArquivo = "\inventario.txt"
  arquivo = open(nomeArquivo, "a")
  arquivo.write("\nHostname.............................:%s" % hostname)
  arquivo.write("\nSerial Number....................:%s" % serialnumber)
  arquivo.write("\nSistema Operacional..:%s" % str(platform.platform()))
  arquivo.write("\nMemória instalada.....................:%s" % memoria)
  arquivo.write("\nPatrimonio.....................:%s" % vpathost.get())
  arquivo.write("\nPatrimonio do monitor.......:%s" % vpatmonitor.get())
  arquivo.write("\nMatricula do cliente.........:%s" % vmatricula.get())
  arquivo.write("\nLocalização do ativo..........:%s" % vlocaliza.get())
  arquivo.write("\nObs......................:%s" % vobs.get("1.0", END))
  arquivo.write("\n")
  arquivo.close()

#=====================Criando*elementos*na*Janela==============================#
vbg = "#dde"
vfg = "#009"

#anchor => N = Norte, S = Sul, E = Leste, W - Oeste
#NE = Nordeste, SE = Sudeste, SO = Sudoeste, NO = Noroeste

Label(verify, text = "Patrimônio do Host", bg =vbg, fg = vfg, anchor = W).place(x = 10, y = 10, width = 200, height = 20)
vpathost = Entry(verify)
vpathost.place( x = 10, y = 30, width = 120, height = 20)

Label(verify, text = "Patrimônio do Monitor", bg =vbg, fg = vfg, anchor = W).place(x = 10, y = 60, width = 200, height = 20)
vpatmonitor = Entry(verify)
vpatmonitor.place( x = 10, y = 80, width = 120, height = 20)

Label(verify, text = "Matricula", bg =vbg, fg = vfg, anchor = W).place(x = 10, y = 110, width = 100, height = 20)
vmatricula = Entry(verify)
vmatricula.place( x = 10, y = 130, width = 120, height = 20)

Label(verify, text = "Localização", bg =vbg, fg = vfg, anchor = W).place(x = 10, y = 160, width = 100, height = 20)
vlocaliza = Entry(verify)
vlocaliza.place( x = 10, y = 180, width = 300, height = 20)

Label(verify, text = "Obs*", bg =vbg, fg = vfg, anchor = W).place(x = 10, y = 210, width = 100, height = 20)
vobs = Text(verify)
vobs.place( x = 10, y = 230, width = 300, height = 40)

btn = Button(verify, text = "Gravar", command = gravarDados)
btn.place( x = 10, y = 275, width = 100, height = 20)


imgLogo1 = PhotoImage(file = pastasoftw+"\\logo.png")
l_later =Label(verify, image = imgLogo1)
l_later.place(x = 375, y = 0)

imgLogo = PhotoImage(file = pastasoftw+"\\p_CCR_Metrô_Bahia.png")
l_logo = Label(verify, image = imgLogo)
l_logo.place(x = 270, y = 0)

#==========================Encerrando*a*Janela=================================#
verify.resizable(width=False,height=False)
verify.mainloop()