from os import system


## TODO: trocar esse sistema de autenticação por dicionários
usuarios = {'Carlos': '456','Ana': '300','Pedro': '400'}
nome= input('informe o usuario')
if nome not in usuarios:
    print("Usuario incorreto")
else:
    print("Usuario logado com sucesso")

#usuario1 = "vini"
#usuario2 = "jonas"
#senha1 = "123"
#senha2 = "qwe"

## TODO: trocar por dicionários também
usuarioLogado = ""
senhaLogado = ""
dinheiro = 0
bloqueado = False


def limpar():
    system("cls")

limpar()

while True:

    if bloqueado == True:
        print("### 🔐 Seu caixa está bloqueado ####")
        senha = input("digite a senha do usuário para desbloquear")
        if senha == senhaLogado:
            bloqueado = False

    else:
        print('✅1 - Inicializar caixa')
        print("🍎 2 - Gerenciar Produtos")
        print("💰 3 - Passar Compras")
        print("❌ 4 - Bloqueio de Caixa")
        print("🔐 5 - Fechar Caixa")
        print("🔴 6 - Sair do Sistema")

        opcaoSelecionada = int(input("Qual é sua escolha:"))

        if opcaoSelecionada == 1:
 	    ## TODO: fazer uso de funções para isolar essa funcionalidade em um bloco de código separado
	    ## TODO: refatorar esse código para que ele valide usuario e senha com base no dicionário criado

            print("------- inicialização de caixa -------")
            usuario = input("Digite o seu usuário:")
            senha = input("Digite a sua senha:")

            if (usuario1 == usuario and senha1 == senha) or (usuario2 == usuario and senha2 == senha):
                usuarioLogado = usuario
                senhaLogado = senha
                dinheiro = float(input("Digite a quantidade de dinheiro disponivel:"))
                print(" -------- Caixa inicializado -------- ")
            else:
                print("⚠ Seu usuário ou senha estão errados")

            opcao = input("Digite (V) para voltar")
            if opcao == "v" or opcao == "V":
                limpar()
                continue

        elif opcaoSelecionada == 2:
            print("------- Gerenciar Produtos -------")
	    ## TODO: criar uma forma de adicionar, alterar, excluir, visualizar e pesquisar produtos do mercado (use listas ou dicionarios)

        elif opcaoSelecionada == 3:
            print("------- Passar Compras -------")
	    ## TODO: criar uma forma de "passar as compras" dos clientes e registrar essas compras. Lembre-se que ao final você precisará exibir um relatório do dia.
	    ## TODO: aqui é importante validar, se não houver produtos, não é possível passar compras.
            ## TODO: encontrar outras validações que fazem sentido!


        elif opcaoSelecionada == 4:
	    ## TODO: eu acho que aqui temos um problema de segurança, verificar
            print("------- Bloqueio do caixa -------")
            resposta = input("Tem certeza que deseja bloquear o caixa? (S/N)")
            if resposta == "S" or resposta == "s":
                bloqueado = True
                limpar()

        elif opcaoSelecionada == 5:
            print("------- Fechar caixa ------")
	    ## TODO: criar essa lógica: ao acionar o fechar caixa, deve-se exibir um relatório completo contendo
	    ###      - O total de vendas do dia; total de dinheiro arrecadado; 
	    ###      - O débito e o crédito devem devem se anular.

        elif opcaoSelecionada == 6:
            print("------- Saindo do sistema de mercado ------")
            exit()
        else:
            print("Atenção❗: você digitou uma opção inválida ")