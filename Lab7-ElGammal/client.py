import socket
import random

def encrypt(m, p, g, h):
    y = random.randint(1, p - 2)
    c1 = pow(g, y, p)
    s = pow(h, y, p)
    c2 = (m * s) % p
    return c1, c2

def main():
    host = '127.0.0.1'
    port = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print(f"Connected to server at {host}:{port}")
        
        # Receive public key from server
        data = s.recv(1024).decode()
        p, g, h = map(int, data.split(','))
        print(f"Received public key: (p={p}, g={g}, h={h})")
        
        while True:
            m = int(input("Enter a message (integer) to encrypt (or 0 to quit): "))
            
            if m == 0:
                break
            
            c1, c2 = encrypt(m, p, g, h)
            print(f"Encrypted message: ({c1}, {c2})")

            s.sendall(f"{c1},{c2}".encode())

if __name__ == "__main__":
    main()