# import os
# import platform

# def clear_console():
#     if platform.system () == "Windows":
#         os.system("cls")


print("------------------------------------------------")
print("Digite a tabuada que deseja e para sair digite 0")
print("------------------------------------------------")

numero = int(input("Digite a tabuada"))

while numero != 0:
    for i in range(11):
        print(f'{numero} X {i} = {numero*i}')
    numero = int(input("Digite a tabuada"))
   
    



