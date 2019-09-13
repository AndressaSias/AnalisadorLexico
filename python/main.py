import re
def verificaVariavel(variavel):
    if re.match("\d+\.\d+", variavel):
        print("ACHEI FLOAT {}".format(variavel.strip()))
    else:
        if re.fullmatch("(^[a-zA-Z])+[0-9]*?[a-zA-Z0-9]*\n", variavel):
            print("ACHEI STRING {}".format(variavel.strip()))
filepath = 'file.txt'
with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       verificaVariavel(line)
       line = fp.readline()
       cnt += 1
