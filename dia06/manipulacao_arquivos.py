# Abrindo (ou criando) um arquivo no modo escrita ('w')
# Isso irá sobrescrever o conteúdo se o arquivo já existir
with open('dados.txt', 'w') as arquivo:
    arquivo.write("Nome: Igor\n")
    arquivo.write("Idade: 27\n")
    arquivo.write("Profissao: Desenvolvedor\n")

# Abrindo o mesmo arquivo no modo leitura ('r') para exibir o conteúdo
with open('dados.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print("Conteúdo do Arquivo")
    print(conteudo)
    
# Abrindo o arquivo no modo de adição ('a') para adicionar novas informações sem apagar o conteúdo existente
with open('dados.txt', 'a') as arquivo:
    arquivo.write("Cidade: Sao Paulo\n")