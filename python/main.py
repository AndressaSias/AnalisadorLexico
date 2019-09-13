import re
def verificaVariavel(variavel,cnt):
    if re.fullmatch("\d+\n", variavel):
        return "inteiro"
    elif re.fullmatch("\d+\.\d+\n", variavel):
            return "real"
    elif re.fullmatch("(^[a-zA-Z])+[0-9]*?[a-zA-Z0-9]*\n", variavel):
            if variavel == "int\n":
                print("[{}] INT".format(cnt))
            elif variavel == "double\n":
                print("[{}] DOUBLE".format(cnt))
            elif variavel == "float\n":
                print("[{}] FLOAT".format(cnt))
            elif variavel == "real\n":
                print("[{}] REAL".format(cnt))
            elif variavel == "break\n":
                print("[{}] BREAK".format(cnt))
            elif variavel == "case\n":
                print("[{}] CASE".format(cnt))
            elif variavel == "char\n":
                print("[{}] CHAR".format(cnt))
            elif variavel == "const\n":
                print("[{}] CONST".format(cnt))
            elif variavel == "continue\n":
                print("[{}] CONTINUE".format(cnt))
            else:
                return("identificador")
    elif re.fullmatch("[/]{2}[ ]*[a-zA-Z0-9\s]*\n", variavel):
             print("[{}] COMENTARIO".format(cnt))
    else:
         return("erro")
filepath = 'file.txt'
with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   ident = 1
   d = {}
   erros = []
   while line:
       retorno = verificaVariavel(line, cnt)
       if retorno == "identificador":
           if line.strip() not in d.keys():
               d[line.strip()] = ident
               ident = ident + 1
           print("[{}] IDENTIFICADOR {}".format(cnt, d[line.strip()]))
       elif retorno == "inteiro":
           if line.strip() not in d.keys(): 
               d[line.strip()] = ident
               ident = ident + 1
           print("[{}] NUMERO INTEIRO {}".format(cnt, d[line.strip()]))
       elif retorno == "real":
           if line.strip() not in d.keys():
               d[line.strip()] = ident
               ident = ident + 1
           print("[{}] NUMERO REAL {}".format(cnt, d[line.strip()]))
       elif retorno == "erro":
            erros.append(cnt)
       line = fp.readline()
       cnt += 1

print("Tabela de Símbolos: {}".format(d.keys()))
print("O programa possui erros nas linhas {}".format(erros))