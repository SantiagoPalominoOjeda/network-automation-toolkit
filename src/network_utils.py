import ipaddress
import subprocess
import socket


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

def get_hostname(ip_address):
    try:
        hostname = socket.gethostbyaddr(ip_address)[0]
        return hostname
    except socket.herror:
        return None

def discover_devices(network):
    hosts = get_network_hosts(network)
    devices = []
    for host in hosts:
        if ping_host(host):
            devices.append({
                "ip": host,
                "status": "UP",
                "hostname": get_hostname(host)
            })
    return devices 