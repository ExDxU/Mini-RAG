---
curso: "CS50's Introduction to Programming with Python (CS50P) — Harvard"
semana: 0
aula: "Lecture 0 — Functions, Variables"
titulo: "Semana 0 — Funções e Variáveis"
topicos: [python, interpretador, VS Code, terminal, print, input, funções, argumentos, parâmetros, efeitos colaterais, valores de retorno, variáveis, atribuição, comentários, pseudocódigo, strings, str, métodos de string, strip, title, f-strings, escape, int, float, conversão de tipos, round, formatação numérica, def, main, escopo, return]
fontes:
  - "Notas oficiais: https://cs50.harvard.edu/python/notes/0/"
  - "Transcrição da videoaula (David J. Malan)"
idioma: pt-BR
---

# Semana 0 — Funções e Variáveis (CS50P)

## Visão geral da aula

A Semana 0 do CS50P, o curso de introdução à programação com Python de Harvard ministrado por David J. Malan, apresenta os dois blocos de construção mais fundamentais de qualquer programa: **funções** e **variáveis**. A aula parte do programa mais clássico da computação, o `hello, world`, e o transforma pouco a pouco num programa que conversa com o usuário, guarda o que ele digitou, limpa e formata esse texto, faz contas com números inteiros e decimais e, por fim, organiza tudo em funções criadas pelo próprio programador.

A ideia que atravessa a aula inteira é simples: uma **função** é uma ação (um verbo) que o programa executa, e uma **variável** é um nome que guarda um valor para ser usado depois. Ao longo do caminho surgem conceitos que vão acompanhar o aluno pelo resto do curso: argumentos e parâmetros, valores de retorno, efeitos colaterais, tipos de dados (`str`, `int`, `float`), métodos, comentários, pseudocódigo, legibilidade, documentação e escopo.

Esta anotação acompanha a ordem da aula e incorpora tanto o conteúdo das notas oficiais quanto as explicações, analogias e dúvidas de alunos que aparecem na videoaula.

## O ambiente: editor de texto, terminal e interpretador

### Escrevendo código no VS Code

Na aula, o David usa o **Visual Studio Code (VS Code)**, um editor de texto voltado para programação. Ele tem três áreas importantes: o **explorador de arquivos**, onde aparecem os arquivos do projeto; o **editor**, onde o código é escrito; e o **terminal**, uma interface de linha de comando (CLI) onde se digitam comandos de texto para o computador.

Para criar e abrir um arquivo novo, digita-se no terminal:

```bash
code hello.py
```

A extensão `.py` indica que o arquivo contém código Python. Dentro dele, o primeiro programa da aula é:

```python
print("hello, world")
```

Para executá-lo, volta-se ao terminal e digita-se:

```bash
python hello.py
```

O resultado é a frase `hello, world` aparecendo na tela.

Um aluno perguntou se daria para escrever código no Word ou no Excel. A resposta foi que, tecnicamente, código é apenas texto puro, então qualquer editor de texto serviria; porém programas como o Word inserem formatação invisível (negrito, fontes, quebras especiais) que atrapalha. Um editor de código como o VS Code é melhor porque oferece coloração de sintaxe, terminal integrado e ferramentas de depuração.

Outro aluno perguntou se um programa pode rodar sem o terminal. Pode: programas podem ter interfaces gráficas (GUIs) com botões e janelas. A linha de comando é usada no curso porque é mais simples para aprender e dá mais controle ao programador.

### O que faz o interpretador Python

O computador só entende **binário**, isto é, sequências de zeros e uns. Ninguém escreve programas diretamente em zeros e uns; escrevemos em uma linguagem legível para humanos, como Python. Quando rodamos `python hello.py`, o programa chamado `python` funciona como um **interpretador**: ele lê o código de cima para baixo, linha por linha, e traduz cada instrução para algo que o computador sabe executar.

Por isso, o mesmo arquivo `hello.py` pode ser lido por uma pessoa e executado pela máquina: o interpretador é o tradutor entre as duas.

O comando `python` sem nome de arquivo abre o **modo interativo**, com o prompt `>>>`. Ali é possível digitar uma linha de Python e ver o resultado na hora, como numa conversa com o interpretador. O David mostra esse modo rapidamente, mas avisa que no curso quase sempre se escreve código em arquivos.

## Funções

### O que é uma função

Uma **função** é uma ação que o programa sabe realizar. O David compara funções a **verbos**: `print` é o verbo "imprimir", ou seja, mostrar algo na tela. Python já vem com muitas funções prontas (as funções embutidas, ou *built-in*), e mais tarde o aluno aprende a criar as suas.

### Argumentos

O que vai dentro dos parênteses de uma função é o seu **argumento**: um valor que influencia o que a função faz. Em `print("hello, world")`, o argumento é o texto `"hello, world"`. Se o argumento mudar, o comportamento muda: `print("oi")` mostra `oi`.

### Efeitos colaterais

Quando `print` mostra algo na tela, isso é chamado de **efeito colateral** (*side effect*): algo visível que a função faz no mundo, como escrever no terminal. Nem toda função tem efeito colateral visível; algumas apenas calculam e devolvem um valor. Essa distinção vai ser essencial na Semana 5, quando funções que só imprimem se mostram difíceis de testar.

## Bugs: os erros fazem parte do processo

Um **bug** é um erro no código. O David insiste que bugs são normais e que todo programador, inclusive os experientes, os comete o tempo todo. O exemplo da aula é esquecer o parêntese de fechamento:

```python
print("hello, world"
```

Ao rodar esse código, o Python mostra uma mensagem de erro. A analogia usada é a de um e-mail: se você esquece um parêntese numa mensagem para um amigo, ele entende mesmo assim; o computador, ao contrário, lê o código literalmente e não consegue adivinhar o que você quis dizer. A correção é simplesmente fechar o parêntese:

```python
print("hello, world")
```

As mensagens de erro do Python costumam indicar a linha e o tipo do problema, mas nem sempre apontam exatamente o ponto certo. Aprender a ler essas mensagens é uma habilidade que se desenvolve com a prática.

## Melhorando o primeiro programa: `input` e variáveis

### A função `input`

Para tornar o programa interativo, usa-se a função `input`, que mostra uma pergunta (o *prompt*) e espera o usuário digitar algo e pressionar Enter:

```python
input("What's your name? ")
print("hello, world")
```

Esse código pergunta o nome, mas não faz nada com a resposta: continua imprimindo `hello, world`. O David personifica a função `input` como um amigo a quem você pede para buscar o nome do usuário; o amigo volta e **devolve** o que ouviu. Esse valor devolvido é o **valor de retorno** da função. Se ninguém guardar o valor de retorno, ele simplesmente se perde.

Um aluno perguntou se `input` funciona para qualquer tipo de dado. A resposta importante: `input` **sempre devolve texto** (uma string), não importa o que o usuário digite. Mesmo que ele digite `42`, o resultado é o texto `"42"`. Para usar como número, é preciso converter, assunto que aparece mais adiante na aula.

### Variáveis e o operador de atribuição

Para guardar o valor devolvido por `input`, usamos uma **variável**: um nome que funciona como um recipiente para um valor. O David compara a variável a um post-it com uma etiqueta, onde se anota um valor para consultar depois.

```python
name = input("What's your name? ")
print("hello, world")
```

O sinal `=` aqui **não significa igualdade** como na matemática. Em Python, `=` é o **operador de atribuição**: ele pega o valor do lado direito e o copia para a variável do lado esquerdo. A leitura correta da linha acima é: "execute `input`, pegue o que ela devolver e guarde na variável `name`". A ordem importa: primeiro o lado direito é avaliado, depois o resultado vai para a esquerda.

### Um bug clássico: aspas em volta da variável

A tentativa seguinte é imprimir o nome:

```python
name = input("What's your name? ")
print("hello, name")
```

O resultado é sempre `hello, name`, independentemente do que o usuário digitar. O motivo: tudo que está entre aspas é texto literal. Para o Python, `"hello, name"` é só uma sequência de caracteres que por acaso contém a palavra "name"; ele não faz a ligação com a variável.

Uma primeira correção é imprimir em duas linhas, com a variável fora das aspas:

```python
name = input("What's your name? ")
print("hello,")
print(name)
```

Funciona, mas o nome aparece numa linha separada do "hello,". As próximas seções resolvem isso de maneiras cada vez mais elegantes.

## Comentários e pseudocódigo

### Comentários

Um **comentário** é uma anotação no código para humanos; o interpretador o ignora completamente. Em Python, comentários começam com `#`:

```python
# Ask the user for their name
name = input("What's your name? ")
print("hello,")
print(name)
```

Comentários servem para explicar o que o código faz, para lembrar o próprio autor de decisões tomadas e para facilitar o trabalho de outras pessoas que lerem o programa. Um aluno perguntou como fazer comentários de várias linhas: basta começar cada linha com `#`. Aspas triplas (`"""`) também funcionam, mas têm um significado especial (as *docstrings*) que aparece no fim do curso, na Semana 9.

### Pseudocódigo

**Pseudocódigo** é escrever, em linguagem natural, os passos que o programa precisa seguir, antes de saber exatamente como codificá-los. Os comentários são o lugar perfeito para isso; eles funcionam como uma lista de tarefas:

```python
# Ask the user for their name
name = input("What's your name? ")

# Print hello
print("hello,")

# Print the name inputted
print(name)
```

A técnica é útil sobretudo quando você ainda não sabe como resolver um problema: primeiro se descreve o plano em português (ou inglês), depois se substitui cada passo por código.

## Funções com vários argumentos

### Concatenação com `+`

Uma forma de juntar o "hello," e o nome numa só linha é **concatenar** (unir) as duas strings com `+`:

```python
name = input("What's your name? ")
print("hello, " + name)
```

Repare no espaço depois da vírgula dentro das aspas: sem ele, a saída seria `hello,David`. O `+`, quando aplicado a textos, cola um no outro sem acrescentar nada.

### Passando dois argumentos para `print`

Outra forma é passar dois argumentos, separados por vírgula:

```python
name = input("What's your name? ")
print("hello,", name)
```

Aqui `print` recebe dois valores e, por padrão, os separa com um espaço. Um aluno perguntou qual a diferença entre as duas versões. A resposta: com `+`, você constrói **uma** string e passa **um** argumento; com a vírgula, você passa **dois** argumentos e deixa o `print` inserir o espaço automaticamente. Encadear muitos `+` funciona, mas o código fica confuso rapidamente.

## Strings e parâmetros

### O tipo `str`

Um texto em Python é uma **string**, cujo tipo se chama `str`. Strings são sequências de caracteres escritas entre aspas duplas ou simples.

### Parâmetros e a documentação de `print`

Os **parâmetros** são os valores que uma função *aceita*, conforme descrito na sua definição ou documentação; os **argumentos** são os valores que você efetivamente *passa* ao chamá-la. A documentação oficial de Python mostra a assinatura de `print` assim:

```text
print(*objects, sep=' ', end='\n', file=None, flush=False)
```

Lendo essa assinatura, aprende-se muito:

- `*objects` indica que `print` aceita qualquer quantidade de objetos para imprimir.
- `sep=' '` diz que, entre os objetos, `print` coloca um espaço por padrão.
- `end='\n'` diz que, ao terminar, `print` coloca uma **quebra de linha** (`\n`) por padrão. É por isso que cada `print` começa numa linha nova.

Esses parâmetros com nome e valor padrão podem ser alterados. Para que o nome fique na mesma linha que o "hello,", basta trocar o final padrão por nada:

```python
name = input("What's your name? ")
print("hello,", end="")
print(name)
```

Com isso, o primeiro `print` não pula linha, e o segundo continua na mesma linha. Esses argumentos passados pelo nome (`end=""`, `sep=", "`) são chamados de **argumentos nomeados** (*keyword arguments*).

### Aspas dentro de strings e caracteres de escape

Um problema surge quando o texto precisa conter aspas:

```python
print("hello,"friend"")
```

O Python acha que a string terminou na segunda aspa e não entende o resto, gerando um erro. Há duas soluções. A primeira é usar aspas simples por fora: `print('hello, "friend"')`. A segunda, mais comum, é **escapar** as aspas internas com uma barra invertida:

```python
print("hello, \"friend\"")
```

A barra invertida `\` é um **caractere de escape**: ela diz ao Python que o próximo caractere deve ser tratado literalmente, não como parte da sintaxe. O mesmo mecanismo explica o `\n`, que significa "quebra de linha".

## f-strings: formatando strings

A forma mais elegante e mais usada no curso para misturar texto e variáveis é a **f-string** (*formatted string*):

```python
name = input("What's your name? ")
print(f"hello, {name}")
```

O `f` antes das aspas avisa o Python de que, dentro daquela string, tudo que estiver entre chaves `{}` deve ser substituído pelo valor correspondente. Sem o `f`, a saída seria literalmente `hello, {name}`. As f-strings aparecem em praticamente todas as semanas seguintes.

## Mais sobre strings: métodos

### Limpando a entrada do usuário

Usuários nem sempre digitam como esperamos: podem colocar espaços antes ou depois do nome, ou escrever tudo em minúsculas. Strings em Python têm **métodos**, que são funções embutidas no próprio tipo `str` e chamadas com um ponto depois do valor.

O método `strip` remove espaços em branco do início e do fim:

```python
name = input("What's your name? ")
name = name.strip()
print(f"hello, {name}")
```

Repare que `name.strip()` não altera `name` diretamente; ele devolve uma nova string limpa, e por isso a atribuição `name = name.strip()` é necessária. Strings em Python são imutáveis.

O método `title` coloca a primeira letra de cada palavra em maiúscula:

```python
name = input("What's your name? ")
name = name.strip()
name = name.title()
print(f"hello, {name}")
```

Um aluno perguntou se dá para remover espaços do *meio* da string. `strip` não faz isso: ele só remove espaços das pontas (e existem `lstrip` e `rstrip` para limpar só o lado esquerdo ou só o direito). Remover espaços internos exige outra técnica, como o método `replace`.

### Encadeando métodos

Como cada método devolve uma string, é possível chamar outro método em cima do resultado, em sequência:

```python
name = input("What's your name? ").strip().title()
print(f"hello, {name}")
```

Isso se chama **encadeamento de métodos**. A leitura é da esquerda para a direita: `input` devolve o texto, `.strip()` limpa as pontas desse texto e `.title()` capitaliza o resultado. Um aluno perguntou quantos métodos podem ser encadeados. Tecnicamente, quantos se quiser; na prática, cadeias longas ficam difíceis de ler e vale quebrá-las em várias linhas.

Uma dica prática da aula: no terminal, a **seta para cima** recupera os comandos anteriores, poupando digitação.

## Números inteiros: `int`

### Operadores aritméticos

Números inteiros são do tipo `int`. Python oferece os operadores matemáticos usuais: `+` (soma), `-` (subtração), `*` (multiplicação), `/` (divisão) e `%` (**módulo**, que devolve o **resto** da divisão; por exemplo, `7 % 3` é `1`). O operador `%` reaparece na Semana 1 para descobrir se um número é par ou ímpar.

Um primeiro programa de calculadora:

```python
x = 1
y = 2

z = x + y

print(z)
```

Ele imprime `3`. Os valores, porém, estão fixos no código (*hard-coded*).

### Um bug importante: `input` devolve texto

Ao trocar os valores fixos por entradas do usuário:

```python
x = input("What's x? ")
y = input("What's y? ")

z = x + y

print(z)
```

Se o usuário digita `1` e `2`, o programa imprime `12`, não `3`. O motivo é o que já se viu: `input` devolve **strings**, e `+` entre strings **concatena**. O Python juntou o texto "1" com o texto "2".

### Conversão de tipos

A solução é converter as strings em inteiros com a função `int`. Essa conversão de um tipo para outro é chamada de *casting*:

```python
x = input("What's x? ")
y = input("What's y? ")

z = int(x) + int(y)

print(z)
```

Agora o resultado é `3`. É possível ainda **aninhar** as chamadas, convertendo logo na entrada:

```python
x = int(input("What's x? "))
y = int(input("What's y? "))

print(x + y)
```

Funções aninhadas são avaliadas **de dentro para fora**, como parênteses na matemática: primeiro `input` pergunta e devolve o texto, depois `int` converte esse texto em número, e por último o resultado é atribuído a `x`.

## Legibilidade acima de tudo

Diante de várias versões do mesmo programa, todas corretas, o David pede à turma que vote: qual é melhor? A conclusão é que não existe uma única resposta certa, mas há critérios. Código deve ser **legível**: fácil de entender para você daqui a algumas semanas e para outras pessoas. Uma linha muito comprimida pode ser elegante e, ao mesmo tempo, difícil de ler e de depurar. Simplicidade, clareza e menos oportunidades de erro valem mais do que esperteza. Comentários e uma boa organização ajudam muito.

## Números de ponto flutuante: `float`

### O tipo `float`

Números com parte decimal, como `0.52` ou `3.14`, são do tipo `float` (*floating-point*, ponto flutuante). A calculadora passa a aceitar decimais trocando `int` por `float`:

```python
x = float(input("What's x? "))
y = float(input("What's y? "))

print(x + y)
```

Com `1.2` e `3.4`, o resultado é `4.6`.

### Arredondando com `round`

A documentação de `round` mostra a assinatura `round(number[, ndigits])`. Na documentação de Python, **colchetes indicam argumentos opcionais**: é possível chamar `round(x)` (arredonda para o inteiro mais próximo) ou `round(x, 2)` (arredonda para duas casas decimais).

```python
x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x + y)

print(z)
```

### Separador de milhares

Para exibir números grandes com vírgulas separando os milhares (por exemplo `1,000`), usa-se um **especificador de formato** dentro da f-string:

```python
z = round(x + y)
print(f"{z:,}")
```

### Controlando casas decimais

A divisão costuma gerar dízimas longas:

```python
x = float(input("What's x? "))
y = float(input("What's y? "))

z = x / y

print(z)
```

Com `2` e `3`, aparece `0.6666666666666666`. Há duas maneiras de mostrar apenas duas casas. Com `round`:

```python
z = round(x / y, 2)
print(z)
```

Ou com formatação na f-string, deixando o valor intacto e mudando só a exibição:

```python
z = x / y
print(f"{z:.2f}")
```

O `.2f` significa "formate como ponto flutuante com 2 casas decimais".

### Limites dos floats

Um aluno perguntou se existe limite de casas decimais. Existe: a memória do computador é finita, então floats não conseguem representar todos os números reais com precisão perfeita. Pequenas imprecisões aparecem em certos cálculos. Os inteiros de Python, por outro lado, não têm limite superior prático: podem crescer tanto quanto a memória permitir.

## Criando suas próprias funções com `def`

### Por que criar funções

Quando o mesmo problema aparece repetidamente, vale encapsular a solução numa função própria. Um aluno perguntou se uma função pode ser usada muitas vezes, e é exatamente essa a vantagem: escrever uma vez, chamar quantas vezes for preciso.

### O erro de chamar uma função inexistente

O David começa chamando uma função `hello` que ainda não existe:

```python
name = input("What's your name? ")
hello()
print(name)
```

O Python responde com um `NameError`: ele não conhece nenhum nome `hello`.

### Definindo a função

Funções são criadas com a palavra-chave `def`, seguida do nome, parênteses e dois-pontos:

```python
def hello():
    print("hello")


name = input("What's your name? ")
hello()
print(name)
```

Em Python, a **indentação** (o recuo das linhas) define o que pertence à função. Tudo que está indentado abaixo do `def` é o corpo da função; o código que volta à margem esquerda está fora dela. Outras linguagens usam chaves para isso; Python usa o recuo, e ele é obrigatório.

### Parâmetros

Para que `hello` cumprimente uma pessoa específica, ela passa a aceitar um **parâmetro**:

```python
def hello(to):
    print("hello,", to)


name = input("What's your name? ")
hello(name)
```

Ao chamar `hello(name)`, o valor de `name` é passado para o parâmetro `to`, que dentro da função se comporta como uma variável.

### Valores padrão

Um parâmetro pode ter um valor padrão, usado quando nenhum argumento é passado:

```python
def hello(to="world"):
    print("hello,", to)


name = input("What's your name? ")
hello(name)
hello()
```

A segunda chamada, sem argumento, imprime `hello, world`.

### A convenção da função `main`

É comum organizar o programa com uma função principal chamada `main` no topo do arquivo e as funções auxiliares abaixo:

```python
def main():
    name = input("What's your name? ")
    hello(name)
    hello()


def hello(to="world"):
    print("hello,", to)
```

Ao rodar essa versão, **nada acontece**. O motivo: o arquivo apenas *define* duas funções, mas nenhuma é *chamada*. A correção é chamar `main()` no final:

```python
def main():
    name = input("What's your name? ")
    hello(name)
    hello()


def hello(to="world"):
    print("hello,", to)


main()
```

Por que chamar `main` só no final? Porque o Python lê o arquivo de cima para baixo. Se `main()` fosse chamada antes de `hello` ser definida, o interpretador ainda não conheceria `hello` e lançaria um `NameError`. Chamando `main()` na última linha, todas as funções já foram lidas quando o programa começa a de fato executar. Essa estrutura permite colocar a lógica principal no topo, onde é mais fácil de ler.

## Escopo

**Escopo** é a região do código onde uma variável existe e pode ser usada. Uma variável criada dentro de uma função só existe dentro dela. Na aula, o David demonstra isso tentando usar dentro de `hello` a variável `name`, que foi criada dentro de `main`: o resultado é um `NameError`, porque `hello` não enxerga as variáveis locais de `main`. A forma correta de compartilhar o valor é passá-lo como argumento, exatamente o que `hello(name)` faz.

## Valores de retorno

### `return`

Até aqui, `hello` produz um efeito colateral (imprime). Mas muitas funções existem para **calcular algo e devolver o resultado** para quem as chamou. Para isso usa-se `return`:

```python
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n


main()
```

`main` passa `x` para `square`; `square` calcula `n * n` e **devolve** o valor com `return`; o valor devolvido aparece no lugar da chamada `square(x)` e é impresso por `main`. Essa é a diferença essencial entre imprimir e retornar: imprimir mostra algo ao usuário; retornar entrega um valor ao programa, que pode guardá-lo, usá-lo em outras contas ou passá-lo adiante.

O David menciona ainda duas alternativas para elevar ao quadrado: o operador de potência `**` (`n ** 2`) e a função embutida `pow` (`pow(n, 2)`).

## Glossário da Semana 0

- **Função**: ação nomeada que o programa executa, como `print` ou `input`. Pode ser embutida ou criada com `def`.
- **Argumento**: valor passado a uma função na chamada, entre os parênteses.
- **Parâmetro**: nome, na definição da função, que recebe um argumento.
- **Argumento nomeado (keyword argument)**: argumento passado pelo nome, como `end=""`.
- **Valor de retorno**: valor que a função devolve a quem a chamou, com `return`.
- **Efeito colateral**: algo que a função faz além de devolver um valor, como imprimir na tela.
- **Variável**: nome que guarda um valor.
- **Atribuição (`=`)**: copia o valor da direita para a variável da esquerda.
- **String (`str`)**: sequência de caracteres (texto).
- **Método**: função que pertence a um tipo e é chamada com ponto, como `name.strip()`.
- **f-string**: string com prefixo `f` que substitui `{variável}` pelo valor.
- **Caractere de escape (`\`)**: faz o caractere seguinte ser lido de forma especial ou literal, como `\"` e `\n`.
- **`int`**: tipo dos números inteiros.
- **`float`**: tipo dos números com parte decimal.
- **Casting / conversão de tipo**: transformar um valor de um tipo em outro, como `int("3")`.
- **Comentário**: texto após `#`, ignorado pelo interpretador.
- **Pseudocódigo**: descrição dos passos em linguagem natural, antes do código.
- **Escopo**: região do código onde uma variável existe.
- **Interpretador**: programa que lê e executa o código Python.
- **Bug**: erro no programa.

## Erros comuns desta semana

- Colocar o nome de uma variável entre aspas (`"hello, name"`), o que imprime o texto literal em vez do valor.
- Somar entradas de `input` sem converter: `"1" + "2"` resulta em `"12"`.
- Esquecer o `f` de uma f-string: `"hello, {name}"` imprime as chaves literalmente.
- Esquecer de reatribuir após um método: `name.strip()` sozinho não altera `name`.
- Definir `main` e esquecer de chamá-la no fim do arquivo.
- Chamar uma função antes de defini-la, gerando `NameError`.
- Tentar usar dentro de uma função uma variável que só existe em outra (problema de escopo).
- Confundir imprimir (efeito colateral) com retornar (valor entregue ao programa).

## Perguntas e respostas para revisão

**Por que `input` seguido de `+` concatena em vez de somar?** Porque `input` sempre devolve uma string, e o operador `+` aplicado a strings une os textos. É preciso converter com `int` ou `float` antes de somar.

**Qual a diferença entre `print("hello, " + name)` e `print("hello,", name)`?** A primeira monta uma única string e passa um argumento; a segunda passa dois argumentos e deixa `print` separá-los com espaço (o valor padrão de `sep`).

**Por que cada `print` começa em uma nova linha?** Porque o parâmetro `end` de `print` tem valor padrão `"\n"`, uma quebra de linha. Passar `end=""` evita isso.

**Qual a diferença entre `round(z, 2)` e `f"{z:.2f}"`?** `round` produz um novo número arredondado; o especificador `.2f` só muda a forma como o número é exibido na string.

**Por que se chama `main()` na última linha?** Porque o Python lê o arquivo de cima para baixo; chamando `main` no fim, todas as funções já estão definidas quando a execução começa.

**Qual a diferença entre uma função que imprime e uma que retorna?** A que imprime mostra algo na tela (efeito colateral) e devolve `None`; a que retorna entrega um valor que pode ser guardado, testado e reutilizado.

## Conexões com o restante do curso

As funções criadas aqui com `def` e `main` são a base de todas as semanas seguintes. A distinção entre imprimir e retornar volta com força na Semana 5 (testes unitários). Os métodos de string reaparecem na validação de entradas das Semanas 1 a 3 e nas expressões regulares da Semana 7. A conversão com `int` motiva o tratamento de exceções da Semana 3, quando o usuário digita algo que não é número. E a observação de que `str`, `int` e `float` são tipos com métodos prepara a Semana 8, onde se descobre que esses tipos são, na verdade, classes.
