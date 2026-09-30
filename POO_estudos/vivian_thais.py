# Aluno(a): Vivian Thaís Varela Oliveira
# Turma: TSI 2026.2

# (Nível 2) Aplicação - Cadastro com validação
# Criação da Classe "Funcionario" e "Email", e execução de testes

class SalarioInvalidoError(Exception):
    pass

class EmailInvalidoError(Exception):
    pass

class Funcionario:
    salario_minimo = 1621.00

    def __init__(self, nome: str, salario: float):
        self.nome = nome
        self.salario = salario

    @property
    def salario(self) -> float:
        return self.__salario

    @salario.setter
    def salario(self, valor: float) -> None:
        if valor < self.salario_minimo:
            raise SalarioInvalidoError(
                f"O sálario de {valor:.2f} inserido é inválido\n"
                f"O valor mínimo deve ser maior ou igual a: {self.salario_minimo}"
            )
        self.__salario = valor

    def aumentar(self, percentual: float) -> None:
        if not (0 < percentual <= 30):
            raise ValueError(
                f"O valor percentual igual a {percentual}% está inválido\n" 
                f"Deve ser maior do que 0, e menor ou igual a 30!"
            )
        self.salario += self.salario * (percentual / 100)

class Email:
    def __init__(self, endereco: str):
        self.endereco = endereco

    @property
    def endereco(self) -> str:
        return self.__endereco

    @endereco.setter
    def endereco(self, valor: str) -> None:
        if "@" not in valor or "." not in valor: 
            raise EmailInvalidoError(
                f"O email '{valor}' é inválido. Deve conter '@' e '.'."
            )
        self.__endereco = valor

print("---TESTES DA CLASSE FUNCIONÁRIO---\n")

try:
    funcionario1 = Funcionario("Pedro Júnior", 1200 )
    print(f"Funcionário: {funcionario1.nome} | Salário: {funcionario1.salario}")
except SalarioInvalidoError as e:
    print(f"[Erro 1 - Salário Inválido]: {e}\n") 

try:
    funcionario2 = Funcionario("João Paulo", 1800)
    funcionario2.aumentar(50)
except ValueError as e:
    print(f"[Erro 2 - Aumento Inválido]: {e}\n")

print("---TESTES DA CLASSE EMAIL---\n")

try:
    email1 = Email("juliana.dantas")
except EmailInvalidoError as e:
    print(f"[Erro 1 - Email Inválido]: {e}\n")

try:
    email2 = Email("gomespedro@gmailcom")
except EmailInvalidoError as e:
    print(f"[Erro 2 - Email Inválido]: {e}\n")

# (Nível 3) Criação de Classe ContaBancaria e Menu Caixa Eletrônico

class ErroDeConta(Exception):
    pass

class ValorInvalidoError(ErroDeConta):
    pass

class SaldoInsuficienteError(ErroDeConta):
    pass

class LimiteExcedidoError(ErroDeConta):
    pass


class ContaBancaria:
    def __init__(self, saldo: float = 0):
        if saldo < 0:
            raise ValorInvalidoError("[Erro - Valor Inválido] O saldo inicial não pode ser negativo.")
        self._saldo = saldo

    @property
    def saldo(self) -> float:
        return self._saldo

    def sacar(self, valor: float) -> None:
        if valor <= 0:
            raise ValorInvalidoError(
                f"[Erro - Valor Inválido] O valor de saque $({valor:.2f}) reais deve ser maior que zero!"
            )
        if valor > 1000:
            raise LimiteExcedidoError(
                "[Erro - Limite Excedido] O valor máximo por operação é de $1.000 reais"
            )
        if valor > self._saldo:
            raise SaldoInsuficienteError(
                f"[Erro - Saldo insuficiente] O valor ${valor} reais é superior ao valor em conta!"
            )
        self._saldo -= valor

    def depositar(self, valor: float) -> None:
        if valor <= 0:
            raise ValorInvalidoError(
                f"[Erro - Valor Inválido] O valor de depósito $({valor:.2f}) reais deve ser maior que zero!"
            )
        self._saldo += valor

# (Nível 3) Criação do Menu CaixaEletronico

def exibir_menu() -> None:
    print("=" * 30)
    print("     CAIXA ELETRÔNICO     ")
    print("=" * 30)
    print("1 - Ver Saldo")
    print("2 - Sacar")
    print("3 - Depositar")
    print("4 - Sair")
    print("=" * 30)

def main(): 
    conta = ContaBancaria()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        try:
            if opcao == "1":
                print(f"O saldo da conta é ${conta.saldo:.2f}")

            elif opcao == "2":
                valor = float(input("Defina o valor do saque: $  "))
                conta.sacar(valor)
                print(f"Saque de ${valor:.2f} reais realizado com sucesso!")

            elif opcao == "3":
                valor = float(input("Defina o valor do depósito: $  "))
                conta.depositar(valor)
                print(f"Depósito de ${valor:.2f} reais realizado com sucesso!")

            elif opcao == "4":
                print("Encerrando o Sistema de Caixa Eletrônico...")
                break

            else:
                print("Opção Inválida - Selecione uma outra opção (1-4)")

        except ErroDeConta as e:
            print(f"[Erro de Operação]: {e}")

        except ValueError as e:
            print("[Erro de Operação]: Entrada Inválida - Digite apenas valores númericos.")

        except Exception as e:
            print(f"Erro Inesperado: {e}")

if __name__ == "__main__":
    main()

