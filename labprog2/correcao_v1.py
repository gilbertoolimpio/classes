from datetime import datetime as dt

class  Cliente():
    def __init__(self, nome, cpf, sexo):
        self._nome = nome
        self._cpf = cpf
        self._sexo = sexo
        self._ativo = True

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome
    
    @property
    def cpf(self):
        return self._cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf
    
    @property
    def sexo(self):
        return self._sexo
    
    @sexo.setter
    def sexo(self, sexo):
        self._sexo = sexo
    
    @property
    def ativo(self):
        return self._ativo
    
    @ativo.setter
    def ativo(self, ativo):
        self._ativo = ativo
    
    def __str__(self):
        print(f'Nome: {self._nome}')
        print(f'CPF: {self._cpf}')
        print(f'Sexo: {self._sexo}')
        print(f'Ativo? {self._ativo}')

class Historico():
    
    def __init__(self):
        self.transacoes = list()
    
    def set_transacao(self, data, transacao, tipo_trasacao, saldo):
        transacao = f'Transacao {tipo_trasacao}: {data} -> {transacao} -> {saldo}'
        self.transacoes.append(transacao)
    
    def __str__(self):
        for transacao in self.transacoes:
            print(transacao)

class Conta():
    def __init__(self, nro_conta: int, cliente: Cliente, saldo: float,
                 limite: float, historico: Historico):
        self._nro_conta = nro_conta
        self._cliente = cliente
        self._saldo = int(saldo) if int(saldo) else 0.
        self._limite = int(limite)
        self._historico = historico if historico else Historico()
        self._ativo = True

    def __str__(self):
        print(f'Nro Conta: {self._nro_conta}')
        print(f'Dados do Cliente: {self._cliente.__str__()}')
        print(f'Saldo: {self._saldo}')
        print(f'Limite: {self._limite}')

    @property
    def ativo(self):
        return self._ativo
    
    @ativo.setter
    def ativo(self, ativo):
        self._ativo = ativo

    @property
    def nro_conta(self):
        return self._nro_conta
    
    @nro_conta.setter
    def nro_conta(self, nro_conta):
        self._nro_conta = nro_conta
    
    @property
    def cliente(self):
        return self._cliente

    @cliente.setter
    def cliente(self, cliente):
        self._cliente = cliente

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        if isinstance(saldo, str):
            saldo = float(saldo)
        self._saldo = saldo

    @property
    def limite(self):
        return self._limite
    
    @limite.setter
    def limite(self, limite):
        if isinstance(limite, str):
            limite = float(limite)

        self._limite = limite

    @property
    def historico(self):
        return self._historico

    @historico.setter
    def historico(self, historico):
        if not isinstance(historico, Historico):
            historico = Historico()
        self._historico = historico
    
    def deposito(self, valor: float):
        self._saldo += valor
        self._historico.set_transacao(dt.now(), valor, 'deposito', self._saldo )

    def saque(self, valor: float):
        if int(valor) <= (int(self._saldo) + int(self._limite)):
            self._saldo -= valor
            self._historico.set_transacao(dt.now(), valor, 'saque', self._saldo )
            
        else:
            print('Não há o valor disponível para saque')
    
    def transferir(self, conta_destino, valor):
        if int(valor) <= (int(self._saldo) + int(self._limite)):
            conta_destino.saldo += int(valor)
            self._saldo -= int(valor)
            self._historico.set_transacao(dt.now(), valor, 'transferencia', self._saldo )

        else:        
            print('Não há o valor disponível para saque')
        
        return conta_destino

class Menu():
    
    def __init__(self):
        self.contas = list()
        self.clientes = list()
        self.menu_principal()
    # Menu Principal
    def menu_principal(self):
        nro_conta = 0
        while True:
            print('*' * 60)
            print('Selecione uma opção:')
            print('1 - Cliente')
            print('2 - Conta')
            print('3 - Sair')
            opcao = input('Digite sua opção: ')
            if isinstance(opcao, str):
                try:
                    opcao = int(opcao)
                except Exception:
                    print('Digite uma opção válida')
        
            if opcao == 1:
                while True:
                    print('Menu Cliente: ')
                    print('Opções: ')
                    print('1 - Criar Cliente')
                    print('2 - Consultar Cliente')
                    print('3 - Alterar Cliente')
                    print('4 - Deletar Cliente')
                    print('5 - Voltar')
                    opcao_cliente = input('Digite sua Opcão: ')
                    if isinstance(opcao_cliente, str):
                        try:
                            opcao_cliente = int(opcao_cliente)
                        except Exception:
                            print('Digite uma opção válida')
                    if opcao_cliente == 1:
                        nome = input('Nome: ')
                        cpf = input('CPF: ')
                        sexo = input('Sexo: ')
                        cliente = Cliente(nome, cpf, sexo)
                        self.clientes.append(cliente)
                    elif opcao_cliente == 2:
                        consulta_cliente = input('Digite o nome para buscar: ')
                        encontrou = False
                        for c in self.clientes:
                            if c.nome == consulta_cliente and c.ativo:
                                c.__str__()
                                encontrou = True
                        
                        if not encontrou:
                            print('Cliente não encontrado ou Inativo!')
                            break
                    elif opcao_cliente == 3:
                        consulta_cliente = input('Digite o nome para buscar: ')
                        encontrou = False
                        for c in self.clientes:
                            if c.nome == consulta_cliente:
                                c.nome = input('Digite o Nome: ')
                                c.cpf = input('Digite o CPF: ')
                                encontrou = True
                            if not encontrou:
                                print('Cliente não encontrado!')
                                break
                    elif opcao_cliente == 4:
                        consulta_cliente = input('Digite o nome para buscar: ')
                        encontrou = False
                        for c in self.clientes:
                            if c.nome == consulta_cliente:
                                c.ativo = False
                                print('Cliente Desativado!')
                                encontrou = True
                            if not encontrou:
                                print('Cliente não encontrado!') 
                                break
                    elif opcao_cliente == 5:
                        break
                    else:
                        print('Opção selecionada não existe!')                               
            elif opcao == 2:
                while True:
                    print('Menu Conta: ')
                    print('Opções: ')
                    print('1 - Criar Conta')
                    print('2 - Consultar Conta')
                    print('3 - Alterar Limite')
                    print('4 - Deletar Conta')
                    print('5 - Depósito')
                    print('6 - Saque')
                    print('7 - Extrato')
                    print('8 - Transferência')
                    print('9 - Voltar')
                    opcao_conta = input('Digite sua Opcão: ')
                    if isinstance(opcao_conta, str):
                        try:
                            opcao_conta = int(opcao_conta)
                        except Exception:
                            print('Digite uma opção válida')
                    if opcao_conta == 1:
                        nro_conta += 1
                        print(f'Nro Conta: {nro_conta}')
                        cliente_conta = input('Nome Cliente: ')
                        limite = input('Limite: ')
                        encontrou = False
                        for c in self.clientes:
                            if c.nome == cliente_conta  and c.ativo:
                                nova_conta = Conta(nro_conta, c, 0, limite, Historico())                                        
                                self.contas.append(nova_conta)
                                encontrou = True
                        if not encontrou:
                            print('Cliente não encontrado ou Inativo!')
                            break

                    elif opcao_conta == 2:
                        consulta_conta = input('Digite o nro da conta para buscar: ')
                        encontrou = False
                        for c in self.contas:
                            if c.nro_conta == int(consulta_conta):
                                c.__str__()
                                encontrou = True
                        if not encontrou:
                            print('Conta não encontrada!')
                            break
                    elif opcao_conta == 3:
                        consulta_conta = input('Digite a conta para alteração: ')
                        encontrou = False
                        for c in self.contas:
                            if c.nro_conta == int(consulta_conta):
                                c.limite = input('Digite o Novo Limite: ')
                                encontrou = True
                            if not encontrou:
                                print('Conta não encontrado!')
                                break
                    elif opcao_conta == 4:
                        consulta_conta = input('Digite a conta para busca: ')
                        encontrou = False
                        for c in self.contas:
                            if c.nro_conta == int(consulta_conta):
                                c.ativo = False
                                print('Conta Desativado!')
                                encontrou = True
                            if not encontrou:
                                print('Conta não encontrada!')
                                break
                    elif opcao_conta == 5:
                        consulta_conta = input('Digite a conta para busca: ')
                        valor_deposito = input('Digite o valor: ')
                        encontrou = False
                        for c in self.contas:
                            if c.nro_conta == int(consulta_conta):  
                                c.deposito(float(valor_deposito))
                                encontrou = True
                            if not encontrou:
                                print('Conta não encontrada!') 
                                break
                    elif opcao_conta == 6:
                        consulta_conta = input('Digite a conta para busca: ')
                        valor_saque = input('Digite valor do saque: ')
                        encontrou = False
                        for c in self.contas:
                            if c.nro_conta == int(consulta_conta):  
                                c.saque(float(valor_saque))
                                encontrou = True
                            if not encontrou:
                                print('Conta não encontrada!') 
                                break
                    elif opcao_conta == 7:
                        consulta_conta = input('Digite a conta para busca: ')
                        encontrou = False
                        for c in self.contas:
                            if c.nro_conta == int(consulta_conta):  
                                c.historico.__str__()
                                encontrou = True
                            if not encontrou:
                                print('Conta não encontrada!') 
                                break                                   
                    elif opcao_conta == 8:
                        consulta_conta = input('Digite a conta de origem: ')
                        consulta_destino = input('Digite a conta de destino: ')
                        valor_transferencia = input('Digita o valor da Transferencia: ')

                        encontrou = False
                        for c in self.contas:
                            if c.nro_conta == int(consulta_conta):  
                                conta_origem = c
                                encontrou = True
                            if not encontrou:
                                print('Conta de origem não encontrada!') 
                                break                               
                        for c in self.contas:
                            if c.nro_conta == int(consulta_destino):  
                                conta_destino = c
                                encontrou = True
                            if not encontrou:
                                print('Conta destino não encontrada!') 
                                break                               
                        if conta_origem and conta_destino:
                            conta_origem.transferir(conta_destino, valor_transferencia)

                    elif opcao_conta == 9:
                        break
                    else:
                        print('Opção selecionada não existe!')                               

if __name__ == "__main__":
    Menu()

    






 
