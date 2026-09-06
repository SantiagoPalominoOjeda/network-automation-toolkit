from network_utils import analyze_ip, scan_network


def show_menu():
    print("\n================================")
    print("   NETWORK AUTOMATION TOOLKIT")
    print("================================")
    print("1. Analyze IP")
    print("2. Scan Network")
    print("3. Exit")


def analyze_ip_option():
    ip = input("\nEnter an IP address: ")

    try:
        information = analyze_ip(ip)
        print("\nNetwork information")
        print("-------------------")
        print(f"IP Address: {information['address']}")
        print(f"Version: IPv{information['version']}")
        print(f"Private: {information['private']}")
        print(f"Global: {information['global']}")

    except ValueError:
        print("Invalid IP address.")


def scan_network_option():
    network = input("\nEnter network (CIDR): ")

    try:
        results = scan_network(network)
        print("\nScan results")
        print("-------------------")
        for host, is_up in results.items():
            status = "UP" if is_up else "DOWN"
            print(f"{host:<16} {status}")

    except ValueError:
        print("Invalid network.")


def main():
    while True:
        show_menu()

        option = input("\nSelect an option: ")
        if option == "1":
            analyze_ip_option()
        elif option == "2":
            scan_network_option()
        elif option == "3":
            print("\nExiting...")
            break
        else:
            print("\nInvalid option.")


if __name__ == "__main__":
    main()