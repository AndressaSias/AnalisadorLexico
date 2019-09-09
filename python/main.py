import re
def verificaVariavel(variavel):
    if re.match("\d+\.\d+", variavel):
        print("ACHEI FLOAT {}".format(variavel.strip()))
    else:
        #if re.findall("\w+", variavel)
        if re.findall("([A-Z]+[a-z]+)", variavel):
            a = re.findall("([A-Z][a-z]+)", variavel)
            print("ACHEI STRING {}".format(a))
filepath = 'file.txt'
with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       #print("Line {}: {}".format(cnt, line.strip()))
       verificaVariavel(line)
       line = fp.readline()
       cnt += 1
