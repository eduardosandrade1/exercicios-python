print('Boa noite, colega!')
nome = input("Please, put your name: ")
# forma errada de concatenar
print("Legal te conhecer, " + nome)

# forma recomendada n°1
print("Legal te conhecer, {}".format(nome))
#forma recomendada °2
print(f"legal te conhecer, {nome}")