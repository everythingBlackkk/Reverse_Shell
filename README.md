# Reverse Shell Tool 
# Alert!
# This tool is for the purpose of understanding how the ReverseShell is hacked behind the scenes and not for actual work with it
# تهدف هذه الأداة إلى فهم كيفية اختراق ReverseShell خلف الكواليس وليس للعمل الفعلي بها.
This is a remote attacker tool developed in Python that allows you to establish a connection with a victim machine over a network and execute various commands remotely.

## Victim Side Code

I added the victim-side in this repository , so users can see the entire codebase and understand how both attacker-side and victim-side components work together.

## Features

- Establishes a TCP connection with the victim machine.
- Sends commands to the victim machine.
- Uploads and downloads files to/from the victim machine.
- Executes commands on the victim machine.
- Handles secure communication using JSON encoding and base64 encoding/decoding for files.

## Prerequisites

- Python 3.x installed on your machine.
- Required Python packages: `colorama`, `argparse`.

## Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/everythingBlackkk/Reverse_Shell.git
```
## Options

```bash
-ip, --victim_ip: IP address of the victim machine.
-p, --victim_port: Port number of the victim machine.
```

## Commands

upload <file_path>: Uploads a file from your machine to the victim machine.
download <file_path>: Downloads a file from the victim machine to your machine.
delete <file_path>: Deletes a file on the victim machine.
exit: Closes the connection and exits the tool.
## Warning!!
Note: This tool is for educational purposes only. Use it responsibly and only on systems you are authorized to access.

## Example

```bash
python Backdor_Att.py -ip 192.168.1.100 -p 8080
```
This will establish a connection with the victim machine having the IP address 192.168.1.100 on port 8080.

## Author

This tool is created by Yassin Abd-elrazik. You can find more of my projects on GitHub.



