from codigo.bytebank import Funcionario
import pytest
from pytest import mark

class TestClass:
    def test_quando_idade_recebe_12_07_2001_deve_retornar_23(self):
        entrada = '12/07/2001' # Given-Contexto
        esperado = 23

        funcionario_teste = Funcionario('Teste', entrada, 1200)
        resultado = funcionario_teste.idade() # When-ação

        assert resultado == esperado # Then-desfecho

    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):
        entrada = ' Lucas Carvalho' # Given
        esperado = 'Carvalho'

        lucas = Funcionario(entrada, '11/11/1991', 1450)
        resultado = lucas.sobrenome() # When

        assert resultado == esperado # Then

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000 # Given
        entrada_nome = 'Paulo Bragança'
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, '23/04/1989', entrada_salario)
        funcionario_teste.decrescimo_salario() # When
        resultado = funcionario_teste.salario

        assert resultado == esperado # Then

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000 # Given
        esperado = 100

        funcionario_teste = Funcionario('Teste', '23/04/1989', entrada)
        resultado = funcionario_teste.calcular_bonus() # When

        assert resultado == esperado # Then

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 1000000 # Given

            funcionario_teste = Funcionario('Teste', '23/04/2998', entrada)
            resultado = funcionario_teste.calcular_bonus() # When

            assert resultado # Then