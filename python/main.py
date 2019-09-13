import re
def verificaVariavel(variavel,cnt):
    if re.fullmatch("\d+\n", variavel):
        print("[{}] INT".format(cnt, variavel.strip()))
    else:
        if re.fullmatch("\d+\.\d+\n", variavel):
            print("[{}] FLOAT {}".format(cnt, variavel.strip()))
        else:
            if re.fullmatch("(^[a-zA-Z])+[0-9]*?[a-zA-Z0-9]*\n", variavel):
                print("[{}] IDENTIFICADOR {}".format(cnt, variavel.strip()))
            else:
                if re.fullmatch("[/]{2}[ ]*[a-zA-Z0-9\s]*\n", variavel):
                     print("[{}] COMENTARIO {}".format(cnt, variavel.strip()))
filepath = 'file.txt'
with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       a = verificaVariavel(line, cnt)
       
       line = fp.readline()
       cnt += 1
