# ARQUIVOS

# NECESSÁRIO QUE O ARQUIVO SEJA CRIADO NA RAIZ DO DIRETORIO REFERENTE AO PROJETO
my_file = open('teste.txt')
print(my_file)
#RESULTADO É O OBEJTO:
#<_io.TextIOWrapper name='teste.txt' mode='r' encoding='UTF-8'>


#MÉTODO (.read)
#RETORNA O CONTEUDO DO ARQUIVO
print(my_file.read())


#MÉTODO (.seek)
#RETORNA O INCIO DO CURSOR, POIS O PYTHON NECESSITA SABER ONDE INICIAR A LEITURA DA LINHA.
print(my_file.seek(0))

#MÉTODO (.readline)
# RETORNA O CONTEUDO DO ARQUIVO APÓS A EXECUÇÃO DO (.seek), POIS O CURSO INCIOU DO ZERO.
print(my_file.readline())