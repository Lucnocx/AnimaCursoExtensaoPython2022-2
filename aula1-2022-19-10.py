# Meu primeiro projeto Python!!! 
#
# print() = comando de saida
print("Hello World!")

# Quando quiser guardar uma String! (frase)
nome = "Lucas Nocera"
#Quando quiser guardar um número inteiro
idade = 20

#Exibir o meu nome (que está dentro da variável nome)
print(nome)

#Quando quiser exibir a frase "Minha idade é " completando com o conteúdo da variável idade
#print("Meu nome é "+nome)
print("Minha idade é "+str(idade)+" anos")
print(f"Minha idade é {idade} anos")
print("Minha idade é {} anos".format(idade))

#Quando quiser exibir "Meu nome é ... e tenho ... 
#anos.." trocando pelas variáveis nome e idade
print("Meu nome é {} e tenho {} anos".format(nome, idade))
