import ipaddress


def analyze_ip(ip_address):
    ip = ipaddress.ip_address(ip_address)


    return {
       "address": str(ip),
        "version": ip.version,
        "private": ip.is_private,
        "global": ip.is_global 

    }