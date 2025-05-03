# Solicita ao usuário que digite a idade e converte a entrada para inteiro
idade = int(input("Digite a sua idade: "))

# Verifica se a idade é menor que 0, o que indica uma entrada inválida
if idade < 0:
    print("Idade inválida!")
    
# Verifica se a idade está entre 0 e 17 (menor de idade)
elif idade < 18:
    print("Você é menor de idade.")

# Verifica se a idade está entre 18 e 59 (maior de idade)
elif idade >= 18 and idade < 60:
    print("Você é maior de idade.")
    
# Caso nenhuma das condições anteriores seja verdadeira, a pessoa é idosa (60 anos ou mais)
else:
    print("Você é idoso!")