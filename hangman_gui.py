import random as rd
import sys

op = 0
a = False

# lista de palavras
lista = ('chocolate', 'computador', 'guilherme', 'samuel', 'tais', 'roberto', 'mario', 'caderno', 'celular')

# pegar um elemento aleatório da lista
index = rd.randint(0, len(lista) - 1)

# guardar na lista
palavra = lista[index]

# letras escolhidas pelo usuário e guardadas pelo programa
let_guardadas = []

# variavel para input da letra
escolhaLetra = ''

# qual posição a letra está
posicao_letra = []

# variavel auxiliar
id = False

# contar letras (usado para ver se ganhou o jogo)
letras_vitoria = 0

vida = 5 # qtd de vida

# Função para escrever as barras
def escrever_barras():
    global palavra
    global posicao_letra
    for i in range(len(palavra)): # Escrever as barras com falta de letras
        if palavra[i] == escolhaLetra: # se a letra da palavra for igual a escolhida atual
            #print(escolhaLetra, end='')
            posicao_letra[i] = escolhaLetra # guarda na posição

    #print(posicao_letra)
    jogo() # volta ao jogo

# Função para verifiar se a letra já foi selecionada
def letra_lista():
    global let_guardadas, escolhaLetra, id

    for i in range(len(let_guardadas)): # Testar caso essa letra já foi escolhida
        if let_guardadas[i] == escolhaLetra: # se for igual
            id = True # variavel auxiliar para true
            print('\nLetra já selecionada') # escreve msg
            id = False
            #print(posicao_letra)
            jogo()
            break

    if id == False: # caso o id for falso (a letra não está na lista)
        let_guardadas.append(escolhaLetra) # adiciona letra à lista

# Função para testar se a letra está na palavra
def letra_palavra():
    global escolhaLetra, palavra, vida

    p = False # quantas vezes a letra aparece na palavra

    for i in range(len(palavra)): # Testar se a letra está na palavra
        if palavra[i] == escolhaLetra: # caso a letra escolhida estiver na palavra
            p = True

    if p == False: # caso a letra não estiver, exibir msg
        print('\nA letra não está na palavra!')
        vida -= 1

# Função que verifica se o jogador ganhou o jogo
def win():
    global letras_vitoria, palavra

    letras_vitoria = 0 # variável que verifica se a soma de letras guardadas na posicao_letra é igual na palavra

    for i in range(len(palavra)):
        if posicao_letra[i] == palavra[i]: # se for igual
            letras_vitoria += 1 # some mais um

    # lógica: se o número de letras verificadas iguais a palavra (letras_vitoria) for igual a palavra, print campeão
    if letras_vitoria >= len(palavra):
        print('\nParabéns!! Você é o Einstein das palavras!\nA palavra era:',palavra)

# Função que verifica se o jogador perdeu o jogo
def lose():
    global vida

    if vida <= 0:
        print('\nPerdeu Playboy!\nA palavra certa era:',palavra)

def jogo(): # função jogo
    global escolhaLetra, a, palavra, vida, letras_vitoria

    lose()
    win()

    if vida <= 0 or letras_vitoria >= len(palavra):
        a = False
    else:
        a = True
        print('\n')
        for i in range(len(palavra)): # Escrever as barras com falta de letras
            print(posicao_letra[i], end="")
        escolhaLetra = input('\nVidas Restantes: '+str(vida)+' Escolha uma letra: ') # Input da letra

    if a == True:
        letra_lista()
        if id == False:
            letra_palavra()
            escrever_barras()
    else:
        menu()

def creditos():
    print('\nCriador: Samuel\n')
    menu()

def menu():
    global palavra, posicao_letra, op

    #print(palavra) # trapaça: saber qual palavra é

    op = 0

    for i in range(len(palavra)):  # Append número de barras
        posicao_letra.append('_')

    while op <= 0 or op > 3:
        print('\nBem-vindo ao jogo! Escolha uma opção:\n[1] Iniciar Jogo\n[2] Créditos\n[3] Sair\nResposta: ', end="")
        op = int(input())
        if op <= 0 or op > 3:
            print('\nEscolha uma opção correta!\n')
        else:
            if(op == 1):
                jogo()
            elif(op == 2):
                creditos()
            elif(op == 3):
                sys.exit()
                op = 0

if __name__ == '__main__':
    menu()
