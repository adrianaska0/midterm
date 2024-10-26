#pylint: disable=redefined-outer-name,consider-using-f-string,invalid-name,unused-variable, no-value-for-parameter
'''Test csv commands'''
import os
from decimal import Decimal
from io import StringIO
from unittest.mock import MagicMock, patch
import pytest
import pandas as pd
from app.plugins.load_csv import LoadCsvCommand
from app.plugins.save_csv import SaveCsvCommand
from calculator.calculations import Calculations
from calculator.calculation import Calculation
from calculator.operations import add

SAMPLE_DATA = '''operation, op_a, op_b
add, 3, 4
subtract, 10, 7
multiply, 2, 9
'''

@pytest.fixture
def mock_app():
    '''sample app for testing'''
    app = MagicMock()
    app.settings = {'DATA_PATH': './data'}
    app.command_handler.commands = {
        'add': MagicMock(),
        'subtract': MagicMock(), 
        'multiply': MagicMock()
    }
    yield app

def test_load_csv_command(mocker, mock_app):
    '''Test load csv command'''
    mocker.patch('pandas.read_csv', return_value=pd.read_csv(StringIO(SAMPLE_DATA)))
    Calculations.clear_history()
    LoadCsvCommand().execute(mock_app,'test.csv')
    history = Calculations.get_history()
    assert len(history) == 3

def test_load_csv_command_file_not_found(mocker, mock_app):
    '''Test error handling file not found'''
    mocker.patch('pandas.read_csv', side_effect=FileNotFoundError)
    with patch('logging.error') as mock_logging_error:
        LoadCsvCommand().execute(mock_app,'non_existent_file.csv')
    expected_log_message = "File not found %s" % os.path.join(os.path.abspath('./data'), 'non_existent_file.csv')
    mock_logging_error.assert_called_once_with(expected_log_message)

def test_load_csv_command_invalid_operation(mocker, mock_app, capfd):
    '''Test error handling for invalid op in csv'''
    SAMPLE_INVALID = '''operation, op_a, op_b
add, 3, 4
subtract, 10, 7
pain, 2, 9
'''
    mocker.patch('pandas.read_csv', return_value=pd.read_csv(StringIO(SAMPLE_INVALID)))
    Calculations.clear_history()
    LoadCsvCommand().execute(mock_app, 'test.csv')
    out, err = capfd.readouterr()
    assert "No such command: pain\n" in out

def test_load_csv_command_invalid_file_type(capfd, mock_app):
    '''Test error handlig for invalid file type'''
    LoadCsvCommand().execute(mock_app,'test.py')
    out, err = capfd.readouterr()
    assert "Invalid file type: test.py. Only CSV files allowed." in out

def test_save_csv_command_success(mock_app, capfd):
    '''Test saving csv'''
    Calculations.add_calculation(Calculation(Decimal('3'), Decimal('3'), add))
    SaveCsvCommand().execute(mock_app, 'test.csv')
    out, err = capfd.readouterr()
    assert "Calculations saved successfully in" in out

def test_save_csv_command_invalid_file_type(mock_app, capfd):
    '''Test invalid file type handling'''
    SaveCsvCommand().execute(mock_app, 'test.txt')
    out, err = capfd.readouterr()
    assert "Invalid file type: test.txt. Only CSV files allowed." in out

def test_save_csv_command_no_history(mock_app, capfd):
    '''Test error handiling with no history'''
    Calculations.clear_history()
    SaveCsvCommand().execute(mock_app, 'test.csv')
    out, err = capfd.readouterr()
    assert "No data in history to save" in out

def test_save_csv_command_invalid_arguments():
    '''Test handling with missing args'''
    with pytest.raises(TypeError):
        SaveCsvCommand().execute(mock_app)  # Missing required argument
