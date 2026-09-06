from network_utils import analyze_ip


def main():
    ip = input("Enter an IP address: ")

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


if __name__ == "__main__":
    main()