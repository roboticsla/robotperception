import socket
import random
import math

def is_prime(n, k=5):
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True
    
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_prime(bits):
    while True:
        p = random.getrandbits(bits)
        if is_prime(p):
            return p

def generate_keys(bits):
    p = generate_prime(bits)
    g = random.randint(2, p - 1)
    x = random.randint(1, p - 2)
    h = pow(g, x, p)
    return p, g, x, h

def decrypt(c1, c2, x, p):
    s = pow(c1, x, p)
    m = (c2 * pow(s, p - 2, p)) % p
    return m

def main():
    host = '127.0.0.1'
    port = 65432

    # Generate keys
    p, g, x, h = generate_keys(256)
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Server listening on {host}:{port}")
        print(f"Public key: (p={p}, g={g}, h={h})")

        
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            
            # Send public key to client
            conn.sendall(f"{p},{g},{h}".encode())
            
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                c1, c2 = map(int, data.decode().split(','))
                m = decrypt(c1, c2, x, p)
                print(f"Received encrypted message: ({c1}, {c2})")
                print(f"Decrypted message: {m}")

if __name__ == "__main__":
    main()