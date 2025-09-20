# Importando minhas funções
import dados
# Loop infinito
while True:
    # Lista com os tipos de dados
    tipos_dados = [4, 6, 8, 10, 12, 20, 100]
    # Recebendo a quantidade de dados que iram ser rolados.
    quant_dados = dados.menu()
    # Ser a quantidade for zero o programa para.
    if quant_dados == 0:
        break
    else:
        # Recebendo o tipo de dado e depois efetuando a rolagem.
        res_tipo = dados.tipos(tipos_dados)
        dados.rolls(quant_dados, tipos_dados[res_tipo - 1])
# Fim do programa.
print('-' * 50)
print('OBRIGADO POR USAR O MEU DICE ROLLER'.center(50))
print('-' * 50)
