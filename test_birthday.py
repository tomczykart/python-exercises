import birthday
from io import StringIO

def get_name():
    name = input('Podaj swoje imie: ')
    return name

def test_get_name(monkeypatch):
    user_input = StringIO('Artur\n')
    monkeypatch.setattr('sys.stdin', user_input)
    assert get_name() == 'Artur'

def test_get_name_v2(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'Artur')
    assert birthday.get_name() == 'Artur'

#def test_1_birthday():
#    assert calculate_when(22) == 2100

#def test_2_birthday():
#    assert calculate_when(100) == 2022
