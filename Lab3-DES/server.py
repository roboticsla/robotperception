import socket
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

# Use the same key for both server and client
key = b'12345678'  # Fixed 8-byte key
iv = get_random_bytes(8)   # Initialization Vector

def des_encrypt(plaintext, key, iv):
    cipher = DES.new(key, DES.MODE_CBC, iv)
    padded_plaintext = pad(plaintext, DES.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext

def start_server():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the address and port
    server_address = ('localhost', 65432)
    server_socket.bind(server_address)
    
    # Listen for incoming connections
    server_socket.listen(1)
    print("Server is listening on port 65432...")
    
    # Wait for a connection
    connection, client_address = server_socket.accept()
    try:
        print(f"Connection from {client_address}")

        # The message to be encrypted and sent to the client
        message = b"Hello, Client! This is a secret message."

        # Encrypt the message using DES
        encrypted_message = des_encrypt(message, key, iv)

        # Send the encrypted message and the IV to the client
        connection.sendall(iv + encrypted_message)  # Send IV + encrypted message

        print(f"Encrypted message sent to the client: {encrypted_message}")
        
    finally:
        connection.close()

if __name__ == "__main__":
    start_server()
