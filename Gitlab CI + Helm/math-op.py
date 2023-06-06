def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

# Exemplo de teste para a função de soma
def test_soma():
    assert soma(2, 3) == 5
    assert soma(-1, 5) == 4

# Exemplo de teste para a função de subtração
def test_subtracao():
    assert subtracao(5, 3) == 2
    assert subtracao(10, 7) == 3

# Exemplo de teste para a função de multiplicação
def test_multiplicacao():
    assert multiplicacao(2, 3) == 6
    assert multiplicacao(-2, 4) == -8

# Exemplo de teste para a função de divisão
def test_divisao():
    assert divisao(10, 2) == 5
    assert divisao(15, 3) == 5

# Execução dos testes
test_soma()
test_subtracao()
test_multiplicacao()
test_divisao()

print("Todos os testes foram executados com sucesso!")
