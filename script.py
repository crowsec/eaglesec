from utils.colors import *
import tools.nmap as nmap
import tools.wfuzz as wfuzz
from utils.banner import *

import sys
import time


def port_scan(host):
	prGreen('[!] Scan iniciado para o host: ' + host)

	result = nmap.scan(host)
	prYellow('[+] Progresso: ' + result['summary'])
	prGreen('[!] Status do Scan: ' + result['status'])

	if(len(result['ports'])>0):
		for port,data in result['ports'].items():
			prGreen('[+] ' + str(port) + '/' + str(data['protocol']) + ' - ' + data['service'])
			if(str(port) == "80"):
				wfuzz.fuzz80(host)
			elif(str(port) == "443"):
				wfuzz.fuzz443(host)
	else:
		prRed('[X] Nenhuma porta aberta encontrada :(')


def detect_os(host):
	 result = nmap.os(host)
	 return result



def main(host):
	# começa com um scan de portas
	port_scan(host)
	# depois detecta o S.O
	#detect_os(host)
	#wfuzz.fuzz443(host)


if __name__ == "__main__":
	banner()
	if(len(sys.argv) <= 1):
		prYellow('[!] Use: python script.py IP')
		prGreen('[>] Exemplo: python script.py 192.168.1.15')
	else:
		main(sys.argv[1])
