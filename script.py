from utils.colors import *
import tools.nmap as nmap

print(nmap.scan("192.168.1.15"))
prRed("TESTE")
print(nmap.os("192.168.1.15"))