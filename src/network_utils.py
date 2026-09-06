import ipaddress
import subprocess

def analyze_ip(ip_address):
    ip = ipaddress.ip_address(ip_address)


    return {
        "address": str(ip),
        "version": ip.version,
        "private": ip.is_private,
        "global": ip.is_global 

    }

def get_network_hosts(network):
    net = ipaddress.ip_network(network, strict=False)
    return [str(host) for host in net.hosts()]


def ping_host(ip_address):
    result = subprocess.run(
        ["ping", "-n", "1","-w", "1000", ip_address],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return result.returncode == 0

def scan_network(network):
    hosts = get_network_hosts(network)
    results = {}
    for host in hosts:
        results[host] = ping_host(host)
    return results
