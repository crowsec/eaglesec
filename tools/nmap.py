import nmap3

nmap = nmap3.Nmap()

def scan(host):
    return nmap.scan_top_ports(host, default=100)

def os(host):
    return nmap.nmap_os_detection(host)