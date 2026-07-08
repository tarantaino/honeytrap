import socket
import paramiko
import threading
import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core.database import init_db, log_attack

HOST_K = paramiko.RSAKey.generate(2048) #gerenates a RSA "bait" to pretend to be a real server, like a usual SSH server

class SSHServer(paramiko.ServerInterface): #using a server interface
    def __init__(self, client_ip):
        self.event=threading.Event() #threading to receive different attacks
        self.client_ip = client_ip

        #intercept username and pswd
        def check_auth_password(self, username, password):
            print(f"Login attempt: User:{username} | Password: {password}")
            log_attack()
            #always return fail authentication so that the user never access
            return paramiko.AUTH_FAILED
        
        #deny access via public key, we need clear pswd
        def check_auth_publickey(self, username, key):
            return paramiko.AUTH_FAILED
        #we only accept pswd as way to access
        def get_allowed_auth(self, username):
            return "password"
        
        def check_chann_request(self, kind, chaind):
            return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED
        
def handle_conn(client_sock, addr):
    print(f"New connection detected from: {addr[0]}:{addr[1]}")
    try:
        transport = paramiko.Transport(client_sock) #normal socket in the SSH paramiko protocol
        transport.add_server_key(HOST_K)

        server = SSHServer(client_ip = addr[0])
        try:
            transport.start_server(server=server)
        except paramiko.SSHException:
            print("Failed SSH negotiation.")
            return
        
        chann = transport.accept(20) #we wait for the attacker to do something, 20 secs max
        if chann is None:
            pass

    except Exception as e:
        print(f"Connection management error: {str(e)}")
    finally:
        try:
            transport.close()
        except:
            pass

def start_hp(host = "0.0.0.0", port = 2222):
    init_db() #inizialize db before opening ports
    try:
        #socket listening
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((host, port))

        #we accept 100 connection queue max
        sock.listen(100)
        print(f"HoneyTrap Active")
        print(f"Listening to SSH attacks on {host}:{port}...")

        while True: #server on
            client_socket, addr = sock.accept()
            #open a separate thread for every attacker
            client_thread = threading.Thread(target=handle_conn, args=(client_socket, addr))
            client_thread.start()

    except Exception as e:
        print(f"Critical server error: {str(e)}")

if __name__ == "__main__":
    start_hp()