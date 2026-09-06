from netmiko import ConnectHandler


DEVICE = {
    "device_type": "linux",
    "host": "127.0.0.1",
    "port": 2222,
    "username": "root",
    "password": "netlab123",
}


def connect_to_device():
    """Establish an SSH connection to the network device."""
    return ConnectHandler(**DEVICE)


def execute_command(command):
    """Execute a Linux command through SSH."""
    connection = connect_to_device()

    try:
        return connection.send_command(command)
    finally:
        connection.disconnect()


def get_routing_table():
    """Get the FRR routing table."""
    return execute_command(
        "vtysh -c 'show ip route'"
    )


def get_version():
    """Get FRRouting version information."""
    return execute_command(
        "vtysh -c 'show version'"
    )


def get_interfaces():
    """Get network interface information."""
    return execute_command(
        "ip addr"
    )