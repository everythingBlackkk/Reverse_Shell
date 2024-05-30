# Remote Attacker Tool

!

This is a remote attacker tool developed in Python that allows you to establish a connection with a victim machine over a network and execute various commands remotely.

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
git clone https://github.com/your_username/remote-attacker-tool.git


## Options


-ip, --victim_ip: IP address of the victim machine.
-s, --victim_port: Port number of the victim machine.


## Commands
upload <file_path>: Uploads a file from your machine to the victim machine.
download <file_path>: Downloads a file from the victim machine to your machine.
delete <file_path>: Deletes a file on the victim machine.
exit: Closes the connection and exits the tool.
## Warning!!
Note: This tool is for educational purposes only. Use it responsibly and only on systems you are authorized to access.

Example
