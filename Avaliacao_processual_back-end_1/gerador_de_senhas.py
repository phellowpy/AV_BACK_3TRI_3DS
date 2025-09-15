import random
import string

caracteres = string.ascii_letters + string.digits + string.punctuation
meio = "emanuelly"

tamanho_total = 20
tamanho_lados = (tamanho_total - len(meio)) // 2

lado_esquerdo = ''.join(random.choice(caracteres) for _ in range(tamanho_lados))
lado_direito = ''.join(random.choice(caracteres) for _ in range(tamanho_total - len(meio) - tamanho_lados))

senha = lado_esquerdo + meio + lado_direito
print(f"senha: {senha}")