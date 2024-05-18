def contador_vogais():
    palavra = input('Digite a palavra que deseja contar quantas vogais ele contém: ').lower()
    vogais = 'aeiou'
    contador = 0

    for char in palavra:
        if char in vogais:
            contador += 1

    print(f'Sua palavra contém {contador} vogais')

if __name__ == "__main__":
    contador_vogais()