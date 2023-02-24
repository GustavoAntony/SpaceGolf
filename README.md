# SPACE GOLF  

## Descrição do jogo:

O jogo simula uma partida de Golf no espaço.

## Regras do Jogo:

**Objetivo**: Acertar a bola de golf na bandeira.

**Lançamento**: O lançamento é resultado de um vetor que é criado a partir da distância entre o ponto do clique e o ponto onde o clique é solto. Esse vetor é invertido e representado como uma reta dentro do jogo.

**Vidas**: Cada fase é iniciada com 3 vidas e cada vez que a bola é lançada ou recebe um toque uma vida é decrementada.

**Bola**: Cada vez que a bola colide com a borda da tela ou com algum planeta, ela é voltada para o lugar de origem.

**Vitória**: Caso o jogador complete todas as fases o jogo é finalizado.

**Derrota**: Caso as vidas sejam zeradas o jogo é finalizado.


## Modo de execução:

1. Clone o repositório.
2. Execute 'pip install -r requirements.txt' para instalar as dependências.
3. Execute o arquivo nomeado 'main.py'

## Gif:

![SpaceGolf (1)](https://user-images.githubusercontent.com/105286051/221239305-2d98632d-d831-4ca3-8a60-be569099dd14.gif)

## Video com Som do jogo:

https://youtu.be/TkB5JTftxwM



## Modelo Físico:
Para o modelo físico do game utilizamos como base a lei da gravitação universal : 

$$ F = G \frac{m_1 m_2}{r^2} $$

onde:
- F é a força de atração entre os dois corpos;
- G é a constante gravitacional universal;
- m1 e m2 são as massas dos dois corpos;
- r é a distância entre os dois corpos.

No código ela está na classe Planet no método atract() que recebe um objeto como argumeto : 

``` 

    def atract(self, other):

        C = other.mass*self.mass*0.01

        direction = (self.pos - other.pos)
        
        distance = np.linalg.norm(direction)


        norm = direction/distance

        if distance == 0 :
            magnitute = C/1
        else :
            magnitute = C/distance**2

        force = norm * magnitute
        

        return force 
```


Vamos por partes :

- Em C guardamos a multiplicação massa dos dois corpos em questão e também a constante 0.01 que funciona como gravidade nesse caso.

- Em direction calculamos o vertor que aponta no sentido que vai do objeto ao planeta em questão. 

- Em distance calculamos o módulo do vetor direction 

- Em norm calculamos o vetor normalizado. 

- Em magnitude quardamos a operação C/distance**2 que representa a magnitude da força que será aplicada.

- Por fim, a váriavel force guarda o vetor resultante da multiplicação do norm pela magnitude.

