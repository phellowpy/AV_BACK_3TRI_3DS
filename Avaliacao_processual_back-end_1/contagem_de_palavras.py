from collections import Counter

texto = input("digite um texto: ")
palavras = texto.split()
quantidade = len(palavras)
mais_longa = max(palavras, key=len)
contador = Counter(palavras)
mais_frequente = contador.most_common(1)[0][0]

print(f"quantidade de palavras: {quantidade}")
print(f"palavra mais longa: {mais_longa}")
print(f"palavra que mais aparece: {mais_frequente}")
