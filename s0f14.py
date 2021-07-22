#!/usr/bin/python3
#
# Script que automatiza la busqueda de informacion.
# By Blackster

#importamos los modulos necesarios para nuestro programa.
from colorama import Fore, init
import subprocess
import time
import sys
import os
init()

banner = """

                                                                                    
                                                                                    
                      000000000        ffffffffffffffff    1111111       444444444  
                    00:::::::::00     f::::::::::::::::f  1::::::1      4::::::::4  
                  00:::::::::::::00  f::::::::::::::::::f1:::::::1     4:::::::::4  
                 0:::::::000:::::::0 f::::::fffffff:::::f111:::::1    4::::44::::4  
    ssssssssss   0::::::0   0::::::0 f:::::f       ffffff   1::::1   4::::4 4::::4  
  ss::::::::::s  0:::::0     0:::::0 f:::::f                1::::1  4::::4  4::::4  
ss:::::::::::::s 0:::::0     0:::::0f:::::::ffffff          1::::1 4::::4   4::::4  
s::::::ssss:::::s0:::::0 000 0:::::0f::::::::::::f          1::::l4::::444444::::444
 s:::::s  ssssss 0:::::0 000 0:::::0f::::::::::::f          1::::l4::::::::::::::::4
   s::::::s      0:::::0     0:::::0f:::::::ffffff          1::::l4444444444:::::444
      s::::::s   0:::::0     0:::::0 f:::::f                1::::l          4::::4  
ssssss   s:::::s 0::::::0   0::::::0 f:::::f                1::::l          4::::4  
s:::::ssss::::::s0:::::::000:::::::0f:::::::f            111::::::111       4::::4  
s::::::::::::::s  00:::::::::::::00 f:::::::f            1::::::::::1     44::::::44
 s:::::::::::ss     00:::::::::00   f:::::::f            1::::::::::1     4::::::::4
  sssssssssss         000000000     fffffffff            111111111111     4444444444
                                                                                    
                                                                                    
       By Blackster                                                                             
                                                                                    
"""

what_banner = """

          _           _                _     
         | |         | |              | |    
__      _| |__   __ _| |___      _____| |__  
\ \ /\ / / '_ \ / _` | __\ \ /\ / / _ \ '_ \ 
 \ V  V /| | | | (_| | |_ \ V  V /  __/ |_) |
  \_/\_/ |_| |_|\__,_|\__| \_/\_/ \___|_.__/ 
                                             
                                             

"""


dnsrecon = """

______ _   _  _____                          
|  _  \ \ | |/  ___|                         
| | | |  \| |\ `--. _ __ ___  ___ ___  _ __  
| | | | . ` | `--. \ '__/ _ \/ __/ _ \| '_ \ 
| |/ /| |\  |/\__/ / | |  __/ (_| (_) | | | |
|___/ \_| \_/\____/|_|  \___|\___\___/|_| |_|
                                             
                                             

"""


""" clase inicial, creadad principalmente para mostrar una ayuda y las opciones disponibles """
class help:
	def __init__(self):
		pass

	def ayuda(self):
		os.system('clear')
		print(Fore.MAGENTA)
		print(banner)
		print(Fore.GREEN)
		print("Uso: python3 s0f14.py < -opciones > www.example.com")
		print("\nOpciones: \n\t-t : seleccionar objetivo.")


	def ask_again():
		os.system('clear')
		print(Fore.CYAN)
		print(banner)
		print(Fore.GREEN)
		print("falta 1 argumento")
		print("\nejemplo: python3 s0f14.py -t www.example.com")

""" Inicio de nuestra clase de ataque, la cual contiene los procesos y parametros que se ejecutaran posteriormente mediante cada ejecucion
 que se haya realizado. """
class Attack:
	def __init__(self):
		self.cls = os.system('clear')
		self.fore = print(Fore.YELLOW)
		self.bnr = print(banner)
		self.target = print("\nObjetivo: --> ", sys.argv[2])
		self.timer = time.sleep(2)
		self.s = "Cargando *.* ...."
		self.i = 0
		while self.i <= 3:
			print(Fore.RED)
			print(self.s)
			time.sleep(1)
			self.i += 1
			if self.i == 3:
				break
		print(Fore.MAGENTA)
		print(what_banner)
		subprocess.run("whatweb {}".format(sys.argv[2]), shell=True, check=False)
		time.sleep(1)
		subprocess.run("whois {}".format(sys.argv[2]), shell= True, check=False)
		time.sleep(2)
		subprocess.run("wafw00f {}".format(sys.argv[2]), shell= True, check=False)
		time.sleep(2)
		print(Fore.GREEN)
		print(dnsrecon)
		subprocess.run("dnsrecon -d {}".format(sys.argv[2]), shell= True, check=False)
		time.sleep(2)
		subprocess.run("nmap -sV -v {}".format(sys.argv[2]), shell= True, check=False)
		time.sleep(2)
		subprocess.run("wpscan --url {}".format(sys.argv[2]), shell= True, check=False)
		time.sleep(2)
		subprocess.run("theHarvester -d {} -b google".format(sys.argv[2]), shell= True, check=False)
		time.sleep(1)
		subprocess.run("joomscan -u {}".format(sys.argv[2]), shell= True, check=False)
		time.sleep(2)
		#subprocess.run("wapiti -u {} --scope page".format(sys.argv[2]), shell= True, check=False)



if __name__=="__main__":
	if len(sys.argv)==1:
		ayudar = help()
		ayudar.ayuda()

	elif len(sys.argv)==2 and sys.argv[1]=='-t':
		ayudita = help
		ayudita.ask_again()

	elif len(sys.argv)==3 and sys.argv[2]:
		atacar = Attack()