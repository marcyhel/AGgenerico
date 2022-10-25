# Biblioteca de Algoritimo Genetipo 
Essa é uma iniciativa para que mais pessoas possam uzar algoritimos geneticos de forma sinples e rapida, sem muitas complicações 

## Instalação
A instalação pode ser feita atravez do gerenciador de pacodes do python utilizando o comando
``` python
pip install aggenerico
```
## Importação
Para importar deve fazer a importação do pacode e chamar o codigo AG
```python
from aggenerico import AG
```
## Divisão de tarefas
Para que possa funcionar corretamente devemos separar em duas partes, uma com a interface do indviduo e a outra a classe do algoritimo gnetico
primeiro devemos implementar a interface `AG.Individuo` 
```python
class cc (AG.Individuo):
  def __init__(self):
    super().__init__()
```
Essa interface implementa funções como `mutação`e `crossover` ficando assim

```python
class Algo (AG.Individuo):
  def __init__(self):
    super().__init__()
  def inicia(self):
    pass
  def semi_reset_individuo(self):
    pass
  def reset_individuo(self):
    pass
  def update(self):
    pass
  def cross(self,a,b):
    pass
  def muta(self):
    pass
  def end(self):
    pass
```
### Lidando com Aleatoriedade
Em alguns casos teremos que lidar com aleatoridades ou inconsistencia dos dados nos individuos pra isso cada individuos podem ser executados mais de uma vez na mesma geração 
para que o impacto da inconsistencia dos dados seja disolvido por isso temos o `semi_reset_individuo` e o `reset_individuo`, o semi reset é quando vai haver mais de uma execução por geração
e assim podemos fazer o reset de apenas algumas coisas e mantendo outras ao longo da geração como a pontuação
e o reset é executado ao final de cada geração limpando ate mesmo a pontuação


## Configurações adicionais
Algumas coisas que podemos configurar por enquanto é o learning rate de nossa rede da seguinte forma `rede_neural.addLearningRate(0.01) ` isso afeta o quanto vai ser o passo de 
aprendizado da rede a cada epoc
podemos alterar a função de ativação da seginte forma `rede_neural.ativador = rede.RedeNeural.tanh`
|Ativação||
|------|-----|
|sigmoid | Utilizado para calculos não lineares |
|tanh|Utilizado para calculos não lineares|

Breve será adicionados outras funções de ativação
### Lista de funções

|Funções| entrada|retorno|
|------|-----|----|
|predict|.predict(array)|Matriz|
|treinar|.treinar(array_entradas, array_saidas, epoc)||
|save|.save(nome = "Nome_do_arquivo")||
|open|.open(nome = "Nome_do_arquivo")||
|addNeuronio|.addNeuronio(2, 5)||
|addLearningRate|.addLearningRate(0.01)||
## Exemplos
### Exemplo 1
Treinando e salvando
```python
from neuralml import rede

redeneural = rede.RedeNeural()
redeneural.ativador = rede.RedeNeural.tanh

redeneural.addNeuronio(2,5)
redeneural.addNeuronio(5,1)

entrada = [[0,0],[0,1],[1,0],[1,1]]
saida = [[0],[0],[1],[1]]

redeneural.treinar(entrada,saida,epoc=6000)

print(redeneural.predict([1,1]))

rede_neural.save(nome="teste")
```
### Exemplo 2
Abrindo arquivos salvos
```python
from neuralml import rede

rede_neural = rede.RedeNeural()

rede_neural.ativador = rede.RedeNeural.tanh

rede_neural.addNeuronio(2,5)
rede_neural.addNeuronio(5,1)
rede_neural.open()

print(rede_neural.predict([1,1]))
```
