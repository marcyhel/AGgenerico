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
class Algo (AG.Individuo):
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

|Funções|Resumo|
|------|-----|
|inicia|É chamado toda vez que o individuo for instanciado.|
|update|Responsavel por fazer a exução ou processamento das tarefas do individuo.|
|cross|Ressebe dois individuos como parametro e é responsavel por criar novos individuos com genes misturados com os dois recebidos.|
|muta|Faz a mutação nos genes dos individuos.|
|end|É sempre executado ao final de cada geração apenas do melhor individuo.|
|semi_reset_individuo|É executado sempre que o individuo terminar uma volta dentro da geração.|
|reset_individuo|Executado ao final da geração.|


## Classe Genetico
Ele é o núcleo do processo genetico, ele quem vai criar todos os individos e fazer todas as chamadas de funções. tendo esses parametros
`Genetico (individuo, geracao, indiv, indiv_selec, mutacao, cross, voltas, call_inicio, ordena, show_v, show_g, thread)`

|Parametro|Tipo de dado|Resumo|
|---------|------------|------|
|individuo|Classe com a interface de Individuo.|Individuo que vai ser evoluido.|
|geracao|Int|Número maximo de gerações.|
|indiv|Int|Quantidade de individuos por geração.|
|indiv_selec|Int|Quantidade de melhores individuos que será passado pra geração seguinte.|
|mutacao|Float|Taxa de mutação por geração.|
|cross|Float|Taxa d CrossOver por geração.|
|voltas|Int|Quantidade de vezes que cada indivuduo vai ser executado por geração.|
|call_inicio|Bool|Para a função inicio não ser excutado apenas na primeira geração.|
|ordena|"d" ou "c"|"d" para decrecente e "c" para crecente.|
|show_v|Bool|Printar no console os resultados de cada volta em cada geração.|
|show_g|Bool|Printar no console os resultados de cada geração.|
|thread|Int|Quantidade de thread destinadas para o processamento, se não ouver para,etro ele irá pegar a quantidade maxima de thread da maquina.|

## Exemplo
É de extrema importancia que a a classe Genetico e a chamada de iniciar estejam dentro da função main `if __name__ == "__main__":`.
```python
from aggenerico import AG
import random

class Max_Num (AG.Individuo):
  def __init__(self):
    super().__init__()
  def inicia(self):
    self.gene_a = random.random()
    self.gene_b = random.random()
  def semi_reset_individuo(self):
    self.pontos=0
  def reset_individuo(self):
    self.pontos=0
    self.pontos_t=0
  def update(self):
    self.pontos = self.gene_a + self.gene_b
  def cross(self,a,b):
    self.gene_a = b.gene_b
    self.gene_b = a.gene_a
  def muta(self):
    self.gene_a = random.random()/100
    self.gene_b = random.random()/100
  def end(self):
    print(f"melhor pontuação {self.pontos_t}")

if __name__ == "__main__":
  ag = AG.Genetico( Max_Num(),
                    geracao = 5000,
                    indiv = 400,
                    indiv_selec = 3,
                    ordena = 'd',
                    mutacao = 0.3,
                    cross = 0.7,
                    voltas = 1,
                    call_inicio = True,
                    show_g = True,
                    show_v = False,
                    thread = 8
)
  ag.iniciar()

```
