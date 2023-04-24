#Parte A
import math
x = int(input("Informe o valor de x na origem: "))
y = int(input("Informe o valor de y na origem: "))
n = int(input("Informe a quantidade de pontos a serem lidos: "))

#Váriáveis de quantos pontos há em cada quadrante
cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0

#Variáveis de calculo para distância de mais proximo e mais distante
distante = 0
pontoXMaisDistante = 0
pontoYMaisDistante = 0

proximo = float('inf')
pontoXMaisProximo = 0
pontoYMaisProximo = 0

#Iniciando o looping
for i in range(n):

    #Pedindo o valor de x e y de cada ponto
    vx = int(input("Digite o valor de x na coordenada: "))
    vy = int(input("Digite o valor de y na coordenada: "))

    #Calculando a distância
    distancia = math.sqrt((vx - x)**2 + (vy - y)**2)

    #Verificando qual é o ponto mais proximo e o mais distante
    if distancia < proximo:
        proximo = distancia
        pontoXMaisProximo = vx
        pontoYMaisProximo = vy

    if distancia > distante:
        distante = distancia
        pontoXMaisDistante = vx
        pontoYMaisDistante = vy

    #Verificando o quadrante do ponto e adicionando +1 na variável correspondente (iniciadas em cima)
    if vy == y or vx == x:
        print(f"Ponto {vx} , {vy} estão sobre o eixo de coordenadas: ")
    elif vx > 0 and vy > 0:
        print(f"Ponto {vx} , {vy} está no 1º Quadrante")
        cont1 = cont1 + 1
    elif vx < 0 and vy > 0:
        print(f"Ponto {vx} , {vy} está no 2º Quadrante")
        cont2 = cont2 + 1
    elif vx < 0 and vy < 0:
        print(f"Ponto {vx} , {vy} está no 3º Quadrante")
        cont3 = cont3 + 1
    elif vx > 0 and vy < 0:
        print(f"Ponto {vx} , {vy} está no 4º Quadrante")
        cont4 = cont4 + 1


print(f"Ponto {pontoXMaisDistante} , {pontoYMaisDistante} é o mais distante do ponto de origem, e o valor da distância é de {distante:.2f}")
print(f"Ponto {pontoXMaisProximo} , {pontoYMaisProximo} é o mais próximo do ponto de origem, e o valor da distância é de {proximo:.2f}")
print(f"Existem {cont1} pontos no 1º Quadrante, {cont2} pontos no 2º Quadrante, {cont3} pontos no 3º Quadrante e {cont4} pontos no 4º Quadrante")
        
#Iniciando Parte B

#Solicitando os valores para o usuário
x = int(input("Digite a coordenada x do ponto de origem A do robô: "))
y = int(input("Digite a coordenada y do ponto de origem A do robô: "))
segundos = int(input("Digite por quantos segundos o robô irá caminhar: "))

#Cálculo
for i in range(segundos):
  if (i % 3 == 0):
    y += 1
  elif (i % 2 == 0):
    x += 2

#Resultado da coordenada final
print(f"Ao final da caminhada o robô estará no ponto ({x}, {y}) do plano cartesiano")