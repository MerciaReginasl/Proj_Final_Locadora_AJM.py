import os

# Função para ler o total de dinheiro ganho do arquivo dinheiro_ganho.txt
def ler_dinheiro_ganho():
    if os.path.exists("dinheiro_ganho.txt"):
        with open("dinheiro_ganho.txt", "r") as arquivo:
            dinheiro_ganho = float(arquivo.read())
    else:
        dinheiro_ganho = 0.0
    return dinheiro_ganho

# Função para atualizar o total de dinheiro ganho no arquivo dinheiro_ganho.txt
def atualizar_dinheiro_ganho(novo_valor):
    with open("dinheiro_ganho.txt", "w") as arquivo:
        arquivo.write(str(novo_valor))

# Função para ler as locações do arquivo locacoes.txt
def ler_locacoes():
    if os.path.exists("carros_locados.txt"):
        with open("carros_locados.txt", "r") as arquivo:
            locacoes = []
            for linha in arquivo:
                dados = linha.strip().split(",")
                locacoes.append({"cliente": dados[0], "carro": dados[1]})
    else:
        locacoes = []
    return locacoes

# Função para determinar o veículo mais locado
def veiculo_mais_locado():
    with open("carros.txt", "r") as arquivo:
        contadores = []
        # Leia uma linha por vez até encontrar o final do arquivo
        linha = arquivo.readline()
        while linha:
            # Processamento da linha
            dados = linha.strip().split(",")
            contadores.append(int(dados[4]))
            linha = arquivo.readline()
        valorMaior = max(contadores)

    with open("carros.txt", "r") as arquivo:
        linha = arquivo.readline()
        while linha:
            # Processamento da linha
            dados = linha.strip().split(",")
            if int(dados[4]) == valorMaior:
                nomeDoCarro = dados[0]
            # Leia a próxima linha
            linha = arquivo.readline()
    
        print(nomeDoCarro)
    
    return nomeDoCarro

# Função para verificar se um carro está locado para um cliente
def verificar_locacao(placa, cpf):
    locacoes = ler_locacoes()
    for locacao in locacoes:
        if locacao['carro'] == placa and locacao['cliente'] == cpf:
            return True
    return False

# Função para adicionar um novo carro ao arquivo de carros disponíveis
def adicionar_carro(carro, placa, numero_veiculo, preco_locacao, contador=0):
    with open("carros.txt", "a") as arquivo:
        arquivo.write(f"{carro},{placa},{numero_veiculo},{preco_locacao},{contador}\n")
        
# Função para adicionar um carro locado ao arquivo carros_locados.txt
def adicionar_carro_locado(carro, cpf):
    with open("carros_locados.txt", "a") as arquivo:
        arquivo.write(f"{carro},{cpf}\n")
   
#esta função analise se o cliente tem conta ou nao na locadora     
def verificar_cliente(cpf):
    if os.path.exists("clientes.txt"):
        with open("clientes.txt", "r") as arquivo:
            for linha in arquivo:
                if cpf in linha:
                    return True
    return False

# Função para remover um carro locado do arquivo carros_locados.txt
def remover_carro_locado(placa):
    locacoes = ler_locacoes()
    locacoes = [locacao for locacao in locacoes if locacao['carro'] != placa]
    with open("carros_locados.txt", "w") as arquivo:
        for locacao in locacoes:
            arquivo.write(f"{locacao['cliente']},{locacao['carro']}\n")

# Função para ler os carros disponíveis para locação do arquivo carros.txt
def ler_carros_disponiveis():
    carros = []
    with open("carros.txt", "r") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(",")
            carros.append({"carro": dados[0], "placa": dados[1], "numero_veiculo": dados[2], "preco_locacao": float(dados[3])})
    carros_locados = ler_carros_locados()
    carros_disponiveis = [carro for carro in carros if carro['placa'] not in carros_locados]
    return carros_disponiveis

# Função para ler os carros locados do arquivo carros_locados.txt
def ler_carros_locados():
    carros_locados = []
    if os.path.exists("carros_locados.txt"):
        with open("carros_locados.txt", "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(",")
                if len(dados) == 2:  # Verifica se a linha tem os dados esperados
                    carros_locados.append({"carro": dados[0], "cpf": dados[1]})
    return carros_locados
 
#funcao para adicionar o dinheiro do carro locado   
def dinheiro_ganho():
    if os.path.exists("dinheiro_ganho.txt"):
        with open("dinheiro_ganho.txt", "r") as arquivo:
            total = float(arquivo.read())
            print(f"Total de dinheiro ganho: R$ {total:.2f}")
    else:
        print("Nenhum dinheiro foi ganho ainda.")
        
# Função para listar os clientes cadastrados
def listar_clientes():
    if os.path.exists("clientes.txt"):
        with open("clientes.txt", "r") as arquivo:
            clientes = arquivo.readlines()
            if clientes:
                print("Lista de clientes cadastrados:")
                for cliente in clientes:
                    print(cliente.strip())
            else:
                print("Nenhum cliente cadastrado.")
    else:
        print("Nenhum cliente cadastrado.")

# Função para cadastrar um novo cliente
def cadastrar_cliente(nome, email, cpf):
    if not verificar_cliente(cpf):  # Verifica se o cliente já está cadastrado pelo CPF
        with open("clientes.txt", "a") as arquivo:
            arquivo.write(f"{nome},{email},{cpf}\n")
        print("Cliente cadastrado com sucesso!")
    else:
        print("CPF já cadastrado.")


