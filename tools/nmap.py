import nmap3
import json
nmap = nmap3.Nmap()

def scan(host):
	result_filtered = {}
	opened_ports = {}
	result_raw = nmap.scan_top_ports(host, default=100)
	result_filtered.update({'summary': result_raw['runtime']['summary']})
	result_filtered.update({'status': result_raw['runtime']['exit']})
	result_filtered.update({'host': list(result_raw.keys())[0]})
	for ports in result_raw[list(result_raw.keys())[0]]:
		if('state' in ports):
			if(ports['state'] == 'open'):
				opened_ports[ports['portid']] = {'portid' : ports['portid'], 'state': ports['state'], 'protocol': ports['protocol'], 'service': ports['service']['name']}
	result_filtered.update({'ports': opened_ports})
	if(result_filtered['status'] == 'success'):
		return result_filtered
	else:
		return False
def os(host):
    return nmap.nmap_os_detection(host)
