from socket import *
import random
from math import gcd

# Funções auxiliares para o RSA

def is_prime(n, k=10):
    """ Teste de primalidade usando Miller-Rabin. """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    def check(a):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return True
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                return True
        return False

    for _ in range(k):
        a = random.randint(2, n - 2)
        if not check(a):
            return False
    return True

def generate_prime(bits):
    """ Gera um número primo com o número de bits especificado. """
    while True:
        num = random.getrandbits(bits)
        if is_prime(num):
            return num

def generate_keys():
    p = generate_prime(16)
    q = generate_prime(16)
    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randrange(2, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)

    d = pow(e, -1, phi)

    return (n, e), (n, d)

def encrypt(message, e, n):
    return [pow(ord(char), e, n) for char in message]

def decrypt(cipher, d, n):
    return ''.join([chr(pow(char, d, n)) for char in cipher])

# Gera par de chaves do cliente
public_key_client, private_key_client = generate_keys()

# Conecta ao servidor
serverName = "10.1.70.37"
serverPort = 1300
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

# Envia chave pública do cliente para o servidor
clientSocket.send(f"{public_key_client[0]} {public_key_client[1]}".encode())

# Recebe chave pública do servidor
server_key_data = clientSocket.recv(1024).decode()
n_server, e_server = map(int, server_key_data.split())

# Lê e criptografa mensagem
sentence = input("🔹 Digite uma frase: ")
encrypted_message = encrypt(sentence, e_server, n_server)

# Envia mensagem criptografada
clientSocket.send(str(encrypted_message).encode())

print(f"🔹 Mensagem original: {sentence}")
print(f"🔹 Mensagem criptografada enviada: {encrypted_message}")

# Recebe mensagem criptografada do servidor
encrypted_response = eval(clientSocket.recv(65000).decode())

# Descriptografa resposta usando chave privada do cliente
decrypted_response = decrypt(encrypted_response, private_key_client[1], private_key_client[0])

print(f"🔹 Mensagem criptografada recebida do servidor: {encrypted_response}")
print(f"🔹 Mensagem descriptografada: {decrypted_response}")

# Fecha conexão
clientSocket.close()