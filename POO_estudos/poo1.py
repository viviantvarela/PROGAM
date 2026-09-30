# Aluno(a): Vivian Thaís Varela Oliveira
# Turma: TSI 2026.2

# Aplicação - Cadastro com validação
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
