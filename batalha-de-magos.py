import random

def exibir_status(jogador1, jogador2, vida1, vida2):
    print(f"Status: {jogador1} - Vida: {vida1}, {jogador2} - Vida: {vida2}")

def aplicar_bola_de_fogo(alvo, jogador1, jogador2, vida1, vida2):
    dano = random.randint(15, 30)
    if alvo == 1:
        vida1 -= dano
        print(f"{jogador2} lançou Bola de Fogo em {jogador1} causando {dano} de dano.")
    else:
        vida2 -= dano
        print(f"{jogador1} lançou Bola de Fogo em {jogador2} causando {dano} de dano.")
    return vida1, vida2

def aplicar_raio_congelante(alvo, jogador1, jogador2, vida1, vida2, congelado1, congelado2):
    dano = random.randint(10, 20)
    if alvo == 1:
        vida1 -= dano
        print(f"{jogador2} lançou Raio Congelante em {jogador1} causando {dano} de dano.")
        if random.random() < 0.25:
            congelado1 = True
            print(f"{jogador1} foi congelado.")
        else:
            print(f"{jogador1} não foi congelado.")
    else:
        vida2 -= dano
        print(f"{jogador1} lançou Raio Congelante em {jogador2} causando {dano} de dano.")
        if random.random() < 0.25:
            congelado2 = True
            print(f"{jogador2} foi congelado.")
        else:
            print(f"{jogador2} não foi congelado.")
    return vida1, vida2, congelado1, congelado2

def aplicar_cura(jogador, jogador1, jogador2, vida1, vida2):
    cura = random.randint(10, 25)
    if jogador == 1:
        vida1 += cura
        if vida1 > 100:
            vida1 = 100
        print(f"{jogador1} curou {cura} pontos de vida. Vida atual: {vida1}.")
    else:
        vida2 += cura
        if vida2 > 100:
            vida2 = 100
        print(f"{jogador2} curou {cura} pontos de vida. Vida atual: {vida2}.")
    return vida1, vida2

def escolher_magia(nome):
    print(f"\n{nome}, escolha sua magia:")
    print("1 - Bola de Fogo (15-30 de dano)")
    print("2 - Raio Congelante (10-20 de dano, chance de congelar)")
    print("3 - Cura (10-25 de vida)")
    return input("Digite o número da magia: ")

def turno(jogador, jogador1, jogador2, vida1, vida2, congelado1, congelado2):
    if jogador == 1 and congelado1:
        print(f"{jogador1} está congelado e perdeu o turno.")
        congelado1 = False
        return vida1, vida2, congelado1, congelado2
    elif jogador == 2 and congelado2:
        print(f"{jogador2} está congelado e perdeu o turno.")
        congelado2 = False
        return vida1, vida2, congelado1, congelado2

    nome = jogador1 if jogador == 1 else jogador2
    magia = escolher_magia(nome)

    if magia == '1':
        vida1, vida2 = aplicar_bola_de_fogo(2 if jogador == 1 else 1, jogador1, jogador2, vida1, vida2)
    elif magia == '2':
        vida1, vida2, congelado1, congelado2 = aplicar_raio_congelante(2 if jogador == 1 else 1, jogador1, jogador2, vida1, vida2, congelado1, congelado2)
    elif magia == '3':
        vida1, vida2 = aplicar_cura(jogador, jogador1, jogador2, vida1, vida2)
    else:
        print("Opção inválida. Tente novamente.")
        return turno(jogador, jogador1, jogador2, vida1, vida2, congelado1, congelado2)

    return vida1, vida2, congelado1, congelado2

print("\n=== Batalha de Magos ===")
jogador1 = input("Digite o nome do Jogador 1: ")
jogador2 = input("Digite o nome do Jogador 2: ")
print(f"\n{jogador1} e {jogador2}, preparem-se para a batalha!\n")

vida1, vida2 = 100, 100
congelado1, congelado2 = False, False
turno_num = 1

while vida1 > 0 and vida2 > 0:
    print(f"\n===== TURNO {turno_num} =====")
    exibir_status(jogador1, jogador2, vida1, vida2)

    vida1, vida2, congelado1, congelado2 = turno(1, jogador1, jogador2, vida1, vida2, congelado1, congelado2)
    if vida2 <= 0:
        break

    vida1, vida2, congelado1, congelado2 = turno(2, jogador1, jogador2, vida1, vida2, congelado1, congelado2)
    turno_num += 1
    if vida1 <= 0:
        break

print("\n===== FIM DE JOGO =====")
exibir_status(jogador1, jogador2, vida1, vida2)
vencedor = jogador1 if vida1 > 0 else jogador2
print(f"O vencedor é {vencedor}!")