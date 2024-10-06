import socket
from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad

# Same key as the server
key = b'12345678'  # Ensure that the key is 8 bytes

def des_decrypt(ciphertext, key, iv):
    cipher = DES.new(key, DES.MODE_CBC, iv)
    decrypted_padded_plaintext = cipher.decrypt(ciphertext)
    decrypted_plaintext = unpad(decrypted_padded_plaintext, DES.block_size)
    return decrypted_plaintext

def start_client():
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    server_address = ('localhost', 65432)
    client_socket.connect(server_address)

    try:
        # Receive the data from the server
        data = client_socket.recv(1024)

        # Extract the IV and the encrypted message
        iv = data[:8]  # The first 8 bytes are the IV
        encrypted_message = data[8:]  # The rest is the encrypted message

        # Decrypt the message using DES
        decrypted_message = des_decrypt(encrypted_message, key, iv)

        print(f"Decrypted message from the server: {decrypted_message.decode()}")
        
    finally:
        client_socket.close()

if __name__ == "__main__":
    start_client()
