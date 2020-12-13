from madlibn_cli import __version__
from madlibn_cli.madlibn import read_template, get_question, create_string, prompt_user


def test_version():
    assert __version__ == '0.1.0'
