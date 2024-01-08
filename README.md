# Cisco IOS Hardening Check

This Python script, `cisco_ios_hardening_check.py`, parses a Cisco IOS configuration file and checks if the configuration aligns with the [Cisco Guide to Harden Cisco IOS Devices](https://www.cisco.com/c/en/us/support/docs/ip/access-lists/13608-21.html).

## Dependencies

- Python 3.x
- `ciscoconfparse` Python library

You can install the ciscoconfparse library using pip:
```
pip install ciscoconfparse
```

## Usage

Run the script in your terminal/command line with the path to the configuration file as an argument:

```
python cisco_ios_hardening_check.py path_to_your_config_file
```

## What it Checks

At its current state, the script checks the following:

1. Router Passwords and Privileges:
    - If secret password is set
    - If password encryption is enabled
    - If minimum password length is set

2. Router Identification:
    - If hostname is set
    - If domain name is set
    - If login banner is set

3. Simple Network Management Protocol (SNMP):
    - If SNMP community strings are set
    - If SNMP access is restricted
    - If SNMP logging is enabled

4. Network Time Protocol (NTP):
    - If NTP server is set
    - If NTP authenticate is enabled
    - If timezone is set

5. TCP and UDP Small Servers:
    - If TCP small servers are disabled
    - If UDP small servers are disabled

6. Internet Control Message Protocol (ICMP):
    - If ICMP echo ignore is set

## Disclaimer

This script is for educational purposes and is not intended for use in a production environment. The script is a basic structure and doesn't cover all checks or possible configurations. The regular expressions used are basic and may need to be refined to more accurately match the specific syntax used in your configuration files.
