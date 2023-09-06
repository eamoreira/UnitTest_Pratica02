import pytest

from src.phonebook import Phonebook


class TestPhonebook:

    @pytest.fixture
    def setup(self):
        # Setup
        phonebook = Phonebook()
        phonebook.__init__()
        yield phonebook

    @pytest.mark.parametrize('name, number, result',
                             [
                                 ('Luana', '10000000', 'Numero adicionado'),
                                 ('#', '11111111', 'Nome invalido'),
                                 ('@', '11111111', 'Nome invalido'),
                                 ('!', '11111111', 'Nome invalido'),
                                 ('$', '11111111', 'Nome invalido'),
                                 ('%', '11111111', 'Nome invalido'),
                                 ('POLICIA', '190', 'Nome invalido'),
                                 ('Larisa', '', 'Numero invalido'),
                                 ('', '11111111', 'Nome invalido')
                             ])
    def test_add(self, setup, name, number, result):
        # Setup
        phonebook = setup
        resultado_esperado = result

        # Chamada
        resultado = phonebook.add(name, number)

        # Avaliação
        assert resultado == resultado_esperado

    @pytest.mark.parametrize('name, result',
                             [
                                 ('POLICIA', '190'),
                                 ('#', 'Nome invalido'),
                                 ('@', 'Nome invalido'),
                                 ('!', 'Nome invalido'),
                                 ('$', 'Nome invalido'),
                                 ('%', 'Nome invalido'),
                                 ('', 'Nome invalido')
                             ])
    def test_lookup(self, setup, name, result):
        # Setup
        phonebook = setup
        resultado_esperado = result

        # Chamada
        resultado = phonebook.lookup(name)

        # Avaliação
        assert resultado == resultado_esperado

    @pytest.mark.parametrize('result',
                             [
                                 ['POLICIA']
                             ])
    def test_get_names(self, setup, result):
        # Setup
        phonebook = setup
        resultado_esperado = result

        # Chamada
        resultado = phonebook.get_names()

        # Avaliação
        assert resultado == resultado_esperado

    @pytest.mark.parametrize('result',
                             [
                                 ['190']
                             ])
    def test_get_numbers(self, setup, result):
        # Setup
        phonebook = setup
        resultado_esperado = result

        # Chamada
        resultado = phonebook.get_numbers()

        # Avaliação
        assert resultado == resultado_esperado

    @pytest.mark.parametrize('result',
                             [
                                 'phonebook limpado'
                             ])
    def test_clear(self, setup, result):
        # Setup
        phonebook = setup
        resultado_esperado = result

        # Chamada
        resultado = phonebook.clear()

        # Avaliação
        assert resultado == resultado_esperado

    @pytest.mark.parametrize('name, result',
                             [
                                 ('POLICIA', [{'POLICIA', '190'}]),
                                 ('POLI', [{'POLICIA', '190'}]),
                                 ('Laris', [{'Larissa', '130'}, {'130', 'Larissa2'}]),
                                 ('', [])
                             ])
    def test_search(self, setup, name, result):
        # Setup
        phonebook = setup
        phonebook.add('Larissa', '130')
        phonebook.add('Larissa2', '130')
        resultado_esperado = result

        # Chamada
        resultado = phonebook.search(name)

        # Avaliação
        assert resultado == resultado_esperado

    @pytest.mark.parametrize('result',
                             [
                                 [('Clarissa', '160'), ('Larissa', '130'), ('POLICIA', '190')]
                             ])
    def test_get_phonebook_sorted(self, setup, result):
        # Setup
        phonebook = setup
        phonebook.add('Larissa', '130')
        phonebook.add('Clarissa', '160')
        resultado_esperado = result

        # Chamada
        resultado = phonebook.get_phonebook_sorted()

        # Avaliação
        assert resultado == resultado_esperado

    @pytest.mark.parametrize('result',
                             [
                                 [('POLICIA', '190'), ('Larissa', '130'), ('Clarissa', '160')]
                             ])
    def test_get_phonebook_reverse(self, setup, result):
        # Setup
        phonebook = setup
        phonebook.add('Clarissa', '160')
        phonebook.add('Larissa', '130')
        resultado_esperado = result

        # Chamada
        resultado = phonebook.get_phonebook_reverse()

        # Avaliação
        assert resultado == resultado_esperado

    @pytest.mark.parametrize('name, result',
                             [
                                 ('POLICIA', 'Numero deletado'),
                                 ('Larisa', 'Nome nao existe no Phonebook')
                             ])
    def test_delete(self, setup, name, result):
        # Setup
        phonebook = setup
        resultado_esperado = result

        # Chamada
        resultado = phonebook.delete(name)

        # Avaliação
        assert resultado == resultado_esperado

    @pytest.mark.parametrize('name, number, result',
                             [
                                 ('POLICIA', '190', 'Numero nao alterado'),
                                 ('POLICIA', '19', 'Numero alterado'),
                                 ('POLIIA', '19', 'Nome nao existe no Phonebook')
                             ])
    def test_change_number(self, setup, name, number, result):
        # Setup
        phonebook = setup
        resultado_esperado = result

        # Chamada
        resultado = phonebook.change_number(name, number)

        # Avaliação
        assert resultado == resultado_esperado

    @pytest.mark.parametrize('number, result',
                             [
                                 ('190', [{'POLICIA', '190'}, {'POLICIA1', '190'}])
                             ])
    def test_get_name_by_number(self, setup, number, result):
        # Setup
        phonebook = setup
        phonebook.add('POLICIA1', '190')
        phonebook.add('POLICIA2', '191')
        resultado_esperado = result

        # Chamada
        resultado = phonebook.get_name_by_number(number)

        # Avaliação
        assert resultado == resultado_esperado
