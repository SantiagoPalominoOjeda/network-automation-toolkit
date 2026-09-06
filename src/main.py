from network_utils import analyze_ip, scan_network, discover_devices
from ssh_automation import (
    get_routing_table,
    get_version,
    get_interfaces,
    execute_command

)

def show_menu():
    print("\n================================")
    print("   NETWORK AUTOMATION TOOLKIT")
    print("================================")
    print("1. Analyze IP")
    print("2. Scan Network")
    print("3. Discover Devices")
    print("4. SSH Automation")
    print("5. Exit")

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
            discover_devices_option()
        elif option == "4":
            ssh_automation_option()
        elif option == "5":
            print("\nExiting...")
            break
        else:
            print("\nInvalid option.")

def discover_devices_option():
    network = input("\nEnter network (CIDR): ")
    try:
        devices = discover_devices(network)
        print("\nDiscovered devices")
        print("-------------------")

        if not devices:
            print("No devices found.")
            return

        for device in devices:
            print(
                f"{device['ip']:<16} "
                f"{device['status']:<8} "
                f"{device['hostname']}"
            )

    except ValueError:
        print("Invalid network.")

def ssh_automation_option():
    while True:
        print("\n==============================")
        print("      SSH AUTOMATION")
        print("==============================")
        print("1. Show Routing Table")
        print("2. Show Interfaces")
        print("3. Show Version")
        print("4. Custom Command")
        print("5. Back to Main Menu")

        option = input("\nSelect an option: ")

        try:
            if option == "1":
                print("\nRouting Table")
                print("-------------------")
                print(get_routing_table())

            elif option == "2":
                print("\nNetwork Interfaces")
                print("-------------------")
                print(get_interfaces())

            elif option == "3":
                print("\nFRRouting Version")
                print("-------------------")
                print(get_version())

            elif option == "4":
                command = input("\nEnter Linux command: ")

                if not command.strip():
                    print("Command cannot be empty.")
                    continue

                print("\nCommand Output")
                print("-------------------")
                print(execute_command(command))

            elif option == "5":
                break

            else:
                print("\nInvalid option.")

        except Exception as error:
            print(f"\nSSH connection error: {error}")

if __name__ == "__main__":
    main()