'''Test app start functionality'''
import pytest
from app import App

def test_app_start_exit_command(monkeypatch):
    '''Test exit command after program start'''
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    assert e.type == SystemExit

def test_app_start_unknown_command(capfd, monkeypatch):
    '''Test unknown command after program start'''
    inputs = iter(['random 2 2', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit):
        app.start()
    res = capfd.readouterr()
    assert "No such command random\n" in res.out
