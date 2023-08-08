#import nmap package
import nmap

# define the Nmap scanner
nm = nmap.PortScanner()

# Specify the target host and ports to scan
target_host = "[THE IP ADDRESS]" #enter here the wanted IP for scanning
ports_to_scan = "1-1000"  #define the range scanning of the ports

# Perform version detection scan on specified ports
nm.scan(hosts=target_host, ports=ports_to_scan, arguments="-sV")

# Print scan results
for host in nm.all_hosts():
    print("Host:", host)
    for port, info in nm[host]['tcp'].items():
        print("Port:", port)
        print("Service:", info['name'])
        print("Version:", info['version'])
        print("State:", info['state'])
        print("=" * 40)
