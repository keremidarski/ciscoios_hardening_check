#!/usr/bin/env python3

import argparse
from collections import defaultdict

from ciscoconfparse import CiscoConfParse


def parse_args():
    parser = argparse.ArgumentParser(
        description="Python script that parses a Cisco IOS configuration file and checks if the configuration aligns with the Cisco Guide to Harden Cisco IOS Devices."
    )

    parser.add_argument(
        "-f", "--file", help="Path to the configuration file.", required=True
    )

    return parser.parse_args()


def check_passwords_privileges(parse, messages):
    if not parse.find_objects(r"^enable secret"):
        messages["Passwords and Privileges"].append("Missing secret password")
    if not parse.find_objects(r"^service password-encryption"):
        messages["Passwords and Privileges"].append("Password encryption not set")
    if not parse.find_objects(r"^security passwords min-length"):
        messages["Passwords and Privileges"].append("Minimum password length not set")


def check_router_identification(parse, messages):
    if not parse.find_objects(r"^hostname"):
        messages["Router Identification"].append("Hostname not set")
    if not parse.find_objects(r"^ip domain-name"):
        messages["Router Identification"].append("Domain name not set")
    if not parse.find_objects(r"^banner login"):
        messages["Router Identification"].append("Login banner not set")


def check_snmp(parse, messages):
    if not parse.find_objects(r"^snmp-server community"):
        messages["SNMP"].append("SNMP community strings not set or secure")
    if not parse.find_objects(r"^snmp-server host"):
        messages["SNMP"].append("SNMP access not restricted")
    if not parse.find_objects(r"^snmp-server enable traps"):
        messages["SNMP"].append("SNMP logging not enabled")


def check_ntp(parse, messages):
    if not parse.find_objects(r"^ntp server"):
        messages["NTP"].append("NTP server not set")
    if not parse.find_objects(r"^ntp authenticate"):
        messages["NTP"].append("NTP authenticate not enabled")
    if not parse.find_objects(r"^clock timezone"):
        messages["NTP"].append("Timezone not set")


def check_tcp_udp_servers(parse, messages):
    if parse.find_objects(r"^service tcp-small-servers"):
        messages["TCP and UDP Servers"].append("TCP small servers should be disabled")
    if parse.find_objects(r"^service udp-small-servers"):
        messages["TCP and UDP Servers"].append("UDP small servers should be disabled")


def check_icmp(parse, messages):
    if not parse.find_objects(r"^no ip icmp echo-ignore"):
        messages["ICMP"].append("ICMP echo ignore not set")


def check_cdp(parse, messages):
    if parse.find_objects(r"^cdp run"):
        messages["CDP"].append("CDP should be disabled if not necessary")


def check_routing_protocol(parse, messages):
    if not parse.find_objects(r"^router rip"):
        messages["Routing Protocol"].append("Routing updates not authenticated")


def check_ports(parse, messages):
    if not parse.find_objects(r"^line aux 0"):
        messages["Ports"].append("Auxiliary port not secured")
    if not parse.find_objects(r"^line console 0"):
        messages["Ports"].append("Console port not secured")
    if not parse.find_objects(r"^line vty"):
        messages["Ports"].append("VTY lines not secured")


def check_packet_filtering(parse, messages):
    if not parse.find_objects(r"^access-list"):
        messages["Packet Filtering"].append("Packet filtering not implemented")


def check_copp(parse, messages):
    if not parse.find_objects(r"^control-plane"):
        messages["CoPP"].append("Control Plane Policing (CoPP) not implemented")


def check_spoofing_route_filtering(parse, messages):
    if not parse.find_objects(r"^ip verify"):
        messages["IP Spoofing and Route Filtering"].append(
            "Anti-spoofing features not implemented"
        )
    if not parse.find_objects(r"^ip route"):
        messages["IP Spoofing and Route Filtering"].append(
            "Route filtering not implemented"
        )


def check_config(file, messages):
    parse = CiscoConfParse(file, factory=True)

    check_passwords_privileges(parse, messages)
    check_router_identification(parse, messages)
    check_snmp(parse, messages)
    check_ntp(parse, messages)
    check_tcp_udp_servers(parse, messages)
    check_icmp(parse, messages)
    check_cdp(parse, messages)
    check_routing_protocol(parse, messages)
    check_ports(parse, messages)
    check_packet_filtering(parse, messages)
    check_copp(parse, messages)
    check_spoofing_route_filtering(parse, messages)


def print_messages(messages):
    print("-------------------------")
    print("Cisco IOS Hardening Check")
    print("-------------------------")

    if any(messages.values()):
        print("\nThe configuration file does not fully adhere to the hardening guide.")
        print("Here are some aspects of the configuration that are not hardened:")
    else:
        print(
            "\nThe configuration file fully adheres to the hardening guide. Good job!"
        )

    for category, msgs in messages.items():
        if msgs:
            print(f"\n{category}:")
            for msg in msgs:
                print(f"- {msg}")


def print_score(messages):
    total_checks = 28
    failed_checks = sum(len(v) for v in messages.values())
    passed_checks = total_checks - failed_checks
    score = round((passed_checks / total_checks) * 10, 2)

    print("\n-------")
    print(f"Configuration score: {score}/10")


def main():
    config_file = parse_args().file
    messages = defaultdict(list)
    check_config(config_file, messages)
    print_messages(messages)
    print_score(messages)


if __name__ == "__main__":
    main()
