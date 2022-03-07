#open("caminho","r")

#Mode
# r = leitura
# a = append/incrementar
# w = escrita
# x = criar arquivo
# r+ = leitura + escrita

#arquivo = open("c:/Users/aniba/OneDrive/Desktop/cursopython/aula01/test3.txt","x")

# print(arquivo.readable())
# print(arquivo.read())
# print(arquivo.readline())
# print(arquivo.readline())
# print(arquivo.readline()) 
# print(arquivo.readline())

# list = arquivo.readlines()

# print(list)

# print(list[3])

#arquivo.write("\npython")


#arquivo.close()

import os

# if os.path.exists("c:/Users/aniba/OneDrive/Desktop/cursopython/aula01/test3.txt"):
#     os.remove("c:/Users/aniba/OneDrive/Desktop/cursopython/aula01/test3.txt")
# else:
#     print("arquivo não existe")

os.rmdir("c:/Users/aniba/OneDrive/Desktop/cursopython/aula01/novapasta")
