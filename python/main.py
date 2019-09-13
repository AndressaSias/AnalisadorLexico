import re
def verificaVariavel(variavel,cnt):
    if re.fullmatch("\d+\n", variavel):
        print("[{}] INT".format(cnt, variavel.strip()))
    else:
        if re.fullmatch("\d+\.\d+\n", variavel):
            print("[{}] FLOAT {}".format(cnt, variavel.strip()))
        else:
            if re.fullmatch("(^[a-zA-Z])+[0-9]*?[a-zA-Z0-9]*\n", variavel):
                if variavel == "int\n":
                    print("[{}] INT {}".format(cnt, variavel.strip()))
                elif variavel == "double\n":
                    print("[{}] DOUBLE {}".format(cnt, variavel.strip()))
                elif variavel == "float\n":
                    print("[{}] FLOAT {}".format(cnt, variavel.strip()))
                elif variavel == "real\n":
                    print("[{}] REAL {}".format(cnt, variavel.strip()))
                elif variavel == "break\n":
                    print("[{}] BREAK {}".format(cnt, variavel.strip()))
                elif variavel == "case\n":
                    print("[{}] CASE {}".format(cnt, variavel.strip()))
                elif variavel == "char\n":
                    print("[{}] CHAR {}".format(cnt, variavel.strip()))
                elif variavel == "const\n":
                    print("[{}] CONST {}".format(cnt, variavel.strip()))
                elif variavel == "continue\n":
                    print("[{}] CONTINUE {}".format(cnt, variavel.strip()))
                else:
                    return("identificador")
            else:
                if re.fullmatch("[/]{2}[ ]*[a-zA-Z0-9\s]*\n", variavel):
                     print("[{}] COMENTARIO {}".format(cnt, variavel.strip()))
filepath = 'file.txt'
with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   ident = 1
   d = {}
   while line:
       retorno = verificaVariavel(line, cnt)
       if retorno == "identificador":
           if line.strip() not in d.keys():
               d[line.strip()] = ident
               ident = ident + 1
           print("[{}] IDENTIFICADOR {} {}".format(cnt, line.strip(), d[line.strip()]))
       line = fp.readline()
       cnt += 1

