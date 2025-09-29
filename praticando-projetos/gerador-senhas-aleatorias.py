import string
import secrets

letras_senha = string.ascii_letters + string.digits + string.ascii_uppercase + string.printable
senha = ''.join(secrets.choice(letras_senha) for i in range(12))
print(f'Aqui está sua Nova Senha: {senha}')