import socket
import argparse

# Função para receber dados do servidor
def receive_data(sock):
    while True:
        # Get the host's response, no more than, say, 1,024 bytes
        response_data = sock.recv(1024).decode("utf-8")
        
        if not response_data:
            print("Conexão encerrada pelo servidor.")
            break

        print(f"Dado recebido: {response_data}")

# Construct the argument parser
ap = argparse.ArgumentParser()

# Add the arguments to the parser
ap.add_argument("-a", "--address", required=True,
                help="Server IP Address or URL")
ap.add_argument("-p", "--port", required=True,
                help="Server Port")
ap.add_argument("-d", "--deviceid", required=True,
                help="Device ID")

args = vars(ap.parse_args())

HOST = args['address']
PORT = int(args['port'])
device_id = args['deviceid']

# Create a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the remote host and port
sock.connect((HOST, PORT))

print("Conectado")

# Send a request to the host
sock.send("app\n".encode()[:-1])

# Get the host's response, no more than, say, 1,024 bytes
response_data = sock.recv(1024).decode("utf-8")
print(response_data)
if response_data == "fail":
    print("Falha ao se conectar ao servidor.")
    sock.close()
    exit()

# Send a request to the host
sock.send((device_id + "\n").encode()[:-1])

# Get the host's response, no more than, say, 1,024 bytes
response_data = sock.recv(1024).decode("utf-8")

if response_data == "fail":
    print("Falha ao autenticar o dispositivo.")
    sock.close()
    exit()


receive_data(sock)

