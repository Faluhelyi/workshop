def JKP():
    import random
    while True:
        Escolhas=["pedra","papel","tesoura"]
        comp=random.choice(Escolhas)
        jogador= None
        while jogador not in Escolhas:
            jogador=input("pedra,papel ou tesoura? ").lower()
        print("computador: ",comp)
        print("jogador: ",jogador)
        if comp==jogador:
            print("deu empate")
        elif comp=="tesoura":
            if jogador=="papel":
                print("Eu venci!")
            elif jogador=="pedra":
                print("Você venceu")
        elif comp=="papel":
            if jogador=="pedra":
                print("Eu venci!")
            elif jogador=="tesoura":
                print("Você venceu")
        elif comp=="pedra":
            if jogador=="tesoura":
                print("Eu venci!")
            elif jogador=="papel":
                print("Você venceu")
        Jogardnv=input("Jogar de novo?(sim/nao): ").lower()
        if Jogardnv != "sim":
            break
    print("Tchau")