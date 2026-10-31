import ipaddress


def subnet_calculator(cidr):
    interface = ipaddress.ip_interface(cidr)
    network = interface.network

    total_addresses = network.num_addresses

    if network.prefixlen == 32:
        usable_hosts = 1
        first_usable = str(network.network_address)
        last_usable = str(network.network_address)

    elif network.prefixlen == 31:
        usable_hosts = 2
        first_usable = str(network.network_address)
        last_usable = str(network.broadcast_address)

    else:
        usable_hosts = max(total_addresses - 2, 0)

        if usable_hosts > 0:
            first_usable = str(network.network_address + 1)
            last_usable = str(network.broadcast_address - 1)
        else:
            first_usable = "N/A"
            last_usable = "N/A"

    return {
        "IP Address": str(interface.ip),
        "Network Address": str(network.network_address),
        "Subnet Mask": str(network.netmask),
        "Broadcast Address": str(network.broadcast_address),
        "Prefix Length": f"/{network.prefixlen}",
        "Total Addresses": total_addresses,
        "Usable Hosts": usable_hosts,
        "First Usable IP": first_usable,
        "Last Usable IP": last_usable,
    }


def ip_class_information(ip):
    address = ipaddress.ip_address(ip)

    if address.version != 4:
        raise ValueError("Only IPv4 addresses are supported.")

    first_octet = int(str(address).split(".")[0])

    if 1 <= first_octet <= 126:
        ip_class = "A"
        default_mask = "255.0.0.0"
    elif 128 <= first_octet <= 191:
        ip_class = "B"
        default_mask = "255.255.0.0"
    elif 192 <= first_octet <= 223:
        ip_class = "C"
        default_mask = "255.255.255.0"
    elif 224 <= first_octet <= 239:
        ip_class = "D (Multicast)"
        default_mask = "Not Applicable"
    else:
        ip_class = "E (Reserved)"
        default_mask = "Not Applicable"

    if address.is_loopback:
        address_type = "Loopback"
    elif address.is_link_local:
        address_type = "Link-Local"
    elif address.is_multicast:
        address_type = "Multicast"
    elif address.is_private:
        address_type = "Private"
    elif address.is_global:
        address_type = "Public"
    else:
        address_type = "Special/Reserved"

    return {
        "IP Address": str(address),
        "IP Class": ip_class,
        "Default Subnet Mask": default_mask,
        "Address Type": address_type,
    }


def address_range_calculator(cidr):
    network = ipaddress.ip_network(cidr, strict=False)

    total_addresses = network.num_addresses

    if network.prefixlen == 32:
        usable_hosts = 1
        first_usable = str(network.network_address)
        last_usable = str(network.network_address)

    elif network.prefixlen == 31:
        usable_hosts = 2
        first_usable = str(network.network_address)
        last_usable = str(network.broadcast_address)

    else:
        usable_hosts = max(total_addresses - 2, 0)

        if usable_hosts > 0:
            first_usable = str(network.network_address + 1)
            last_usable = str(network.broadcast_address - 1)
        else:
            first_usable = "N/A"
            last_usable = "N/A"

    return {
        "Network Address": str(network.network_address),
        "Broadcast Address": str(network.broadcast_address),
        "First Usable IP": first_usable,
        "Last Usable IP": last_usable,
        "Subnet Mask": str(network.netmask),
        "Prefix Length": f"/{network.prefixlen}",
        "Total Addresses": total_addresses,
        "Usable Hosts": usable_hosts,
    }