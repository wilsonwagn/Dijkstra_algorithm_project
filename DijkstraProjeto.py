import sys

#—————————————————————————————————————————— ADICIONANDO VERTICES ————————————————————————————————————————————————————————————————————————
baseDados = open("base.txt", 'r')
vertices = {}
verticesInv = {}
total = 0
for linha in baseDados:
    user = ""
    for x in range(len(linha)):
        if x == 0 and linha[x] == "@":
            user+=linha[x]
        if linha[x] == "," or (x == 0 and linha[x] == "C"):
            break
        elif linha[x] != "@":
            user+=linha[x]
    if user != "":
        vertices[user.upper()] = total
        verticesInv[total] = user.upper()
        total+=1
baseDados.close()
#———————————————————————————————————————————— ADICIONANDO ARESTAS ——————————————————————————————————————————————————————————————————————
arestas = []
for x in range(len(vertices)):
  arestas.append([0]*len(vertices))
#————————————————————————————————————————————— ADICIONANDO PESOS —————————————————————————————————————————————————————————————————————

baseDados = open("base.txt", 'r').readlines()
quantArestas = 0
for linha in range(1, len(baseDados)):
    linha = baseDados[linha].split(',')
    contaPrincipal = linha[0]
    x = 1
    while x < len(linha):
        if linha[x] == "" or linha[x] == "\n":
            break
        else:
            quantArestas+=1
            arestas[vertices[contaPrincipal.upper()]][vertices["@"+linha[x].upper()]] = int(linha[x+1])
            arestas[vertices["@"+linha[x].upper()]][vertices[contaPrincipal.upper()]] = int(linha[x+1])
            x+=2

#————————————————————————————————————————————— DIKSTRA —————————————————————————————————————————————————————————————————————

class Dijkstra:
  def __init__(self, vertices, arestas, inicio):
    self.tamanho = len(vertices)
    self.vertices = vertices
    self.grafo = arestas
    self.inicio = inicio

  def mostra_solucao(self, distancias):
    print(f'Menores distâncias de {self.vertices[self.inicio]} até todos os outros')
    for vertice in range(self.tamanho):
      print(self.vertices[vertice], distancias[vertice])

  def distancia_minima(self, distancia, visitados):
    minimo = sys.maxsize
    
    for vertice in range(self.tamanho):
      if distancia[vertice] < minimo and visitados[vertice] == False:
        minimo = distancia[vertice] 
        indice_minimo = vertice
    return indice_minimo

  def dijkstra(self):
    distancia = [sys.maxsize] * self.tamanho
    distancia[self.inicio] = 0
    visitados = [False] * self.tamanho

    for NickiMinaj in range(self.tamanho):
      indice_minimo = self.distancia_minima(distancia, visitados)
      visitados[indice_minimo] = True
      for vertice in range(self.tamanho):
        
        #Se a distância daquela posição do vertice for maior que 0 | E não foi visitado // 
        # Distancia do vertice atual foi maior que a distancia do vertice mínimo
        # +
        if self.grafo[indice_minimo][vertice] > 0 and visitados[vertice] == False \
            and distancia[vertice] > (distancia[indice_minimo] + self.grafo[indice_minimo][vertice]):
          
          #RELAXAMENTO, ou seja, atualização dos valores | Parte principal do algoritmo.
          distancia[vertice] = distancia[indice_minimo] + self.grafo[indice_minimo][vertice]
    self.mostra_solucao(distancia)

dijkstra = Dijkstra(verticesInv, arestas, vertices['@KIMKARDASHIAN'])
dijkstra.dijkstra()
print(f"O projeto tem {len(vertices)} vertices e {quantArestas} arestas")
