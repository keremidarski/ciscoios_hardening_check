# Cisco IOS Hardening Check

This script parses a Cisco IOS configuration file and checks if the configuration aligns with the [Cisco Guide to Harden Cisco IOS Devices](https://www.cisco.com/c/en/us/support/docs/ip/access-lists/13608-21.html).

It provides a detailed report of the aspects of the configuration that do not adhere to the guide, and assigns a score out of 10 based on the number of checks that pass.

## What It Checks
The script checks the following aspects of a Cisco IOS configuration:

- Passwords and Privileges: Checks for secret password, password encryption, and minimum password length settings.
- Router Identification: Checks for hostname, domain name, and login banner settings.
- SNMP: Checks for SNMP community strings, SNMP access restrictions, and SNMP logging.
- NTP: Checks for NTP server, NTP authentication, and timezone settings.
- TCP and UDP Servers: Checks whether TCP and UDP small servers are disabled.
- ICMP: Checks for ICMP echo ignore settings.
- CDP: Checks whether CDP is disabled if not necessary.
- Routing Protocol: Checks for routing update authentication.
- Ports: Checks whether the Auxiliary port, Console port, and VTY lines are secured.
- Packet Filtering: Checks for packet filtering settings.
- CoPP: Checks whether Control Plane Policing (CoPP) is implemented.
- IP Spoofing and Route Filtering: Checks for anti-spoofing features and route filtering settings.
- Each of these checks contributes equally to the final score. If a check passes, it means the related aspect of the configuration adheres to the hardening guide. If a check fails, the script will provide a message with details about what needs to be corrected.

## Prerequisites

- Python 3.x
- `ciscoconfparse` Python module

## Usage

1. Install the `ciscoconfparse` module using pip:

    ```bash
    pip install ciscoconfparse
    ```

2. Run the script with the `-f` option followed by the path to the configuration file:

    ```bash
    python3 script.py -f /path/to/config/file
    ```

The script will print a detailed report of the configuration aspects that do not adhere to the hardening guide, and a score out of 10.

## Scoring

The script performs a total of 28 checks on the configuration file. Each check that passes contributes equally to the final score. The score is calculated as follows:

1. The total number of checks is 28.
2. The number of failed checks is calculated by summing the lengths of all the message values.
3. The number of passed checks is then calculated by subtracting the number of failed checks from the total number of checks.
4. Finally, the score is calculated by dividing the number of passed checks by the total number of checks, multiplying by 10, and rounding to 2 decimal places.

A higher score indicates a better configuration. If all checks pass, the script will assign a score of 10/10.

## Disclaimer

This script is for educational purposes and is not intended for use in a production environment. The script is a basic structure and doesn't cover all checks or possible configurations. The regular expressions used are basic and may need to be refined to more accurately match the specific syntax used in your configuration files.
