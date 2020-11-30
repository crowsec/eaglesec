import nmap3
from colors import *

nmap = nmap3.Nmap()
results = nmap.scan_top_ports("192.168.1.11")
print(results)
prRed("TESTE")
os_results = nmap.nmap_os_detection("192.168.1.11")
print(os_results)