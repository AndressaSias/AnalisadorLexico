# AnalisadorLexico

### Andressa Sias, Cristhian Bicca, Felipe Klatte

Interpretador léxico, sintático e semântico 

Trabalho realizado na cadeira de Compiladores, Ulbra Canoas, Ciência da Computação
Profa. Maria Adelina Raupp Sganzerla 

Aula 3 – Análise Léxica (Implementação de um Autômato)

Observações:
- A atividade deve ser realizada em duplas ou trios (individuais não serão aceitas);
- A linguagem escolhida para a implementação fica a critério da dupla/trio;
- O trabalho será apresentado no dia 13 de setembro de 2019 durante o período de aula diretamente
para a professora, enquanto os demais colegas executam exercícios de fixação;
- Deverá ser entregue os códigos-fontes devidamente comentados, na mesma data da apresentação.
Crie um autômato para reconhecer linguagens cujos tokens podem ser:
- Identificadores iniciados por uma letra, podendo possuir na sequência zero e/ou mais
números e/ou letras;
- Constantes numéricas formadas por um ou mais números inteiros na casa da dezena,
ou seja, até o valor 99;
- Constantes numéricas formadas por números reais, também na casa da dezena, ou
seja, valor máximo de 99.99;
- Identificadores no formato de comentários de linha, padrão da Linguagem C (//);
- As palavras reservadas da linguagem C: int, double, float, real, break, case,
char, const, continue.
O analisador deverá carregar um arquivo-texto contendo um padrão por linha e reconhecer o
token especificado. Sendo que esse deverá ser especificado pelo usuário no momento da
execução do programa.
Ao final da análise, o autômato deverá exibir:
- Os tokens de entrada (e a linha onde eles aparecem);
- A tabela de símbolos;
- A lista das linhas onde os erros aparecem (caso tenham erros no arquivo)
Por exemplo, se o usuário entrar com o arquivo contendo os dados abaixo:
a
a
int
asd
as123
99
99.
99.99
float

Compiladores

real a
real
double _c
double
as_asd
asd
// Joao da Silva
-- Teste
Joao da Silva --
char
O programa deverá emitir o seguinte arquivo de saída:
[1] IDENTIFICADOR 1
[2] IDENTIFICADOR 1
[3] INT
[4] IDENTIFICADOR 2
[5] IDENTIFICADOR 3
[6] NÚMERO INTEIRO 4
[8] NÚMERO REAL 5
[9] FLOAT
[11] REAL
[13] DOUBLE
[15] IDENTIFICADOR 2
[16] COMENTÁRIO
[19] CHAR
Tabela de Símbolos
1 - a
2 - asd
3 - as123
4 - 99
5 - 99.99
O programa possui erros nas linhas: 7, 10, 12, 14, 17 e 18
