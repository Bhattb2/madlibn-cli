import pytest

from madlibn_cli.madlibn_cli import read_template, get_questions, create_string, prompt_user

#checks new_list for the missing components
def test_get_question():
    actual = get_questions("This is a noun {noun} and a verb {verb} with adjective {adjective} noun {noun}")
    expected = ['noun', 'verb', 'adjective', 'noun']
    assert actual == expected

# check the prompt for user
# def test_prompt_user():
#     actual = prompt_user("noun")
#     excepted = "*** Please enter a noun ***"
#     assert actual == excepted

# check the final string created
# def test_create_string():
#     actual = create_string("This is a noun {noun} and a verb {verb} with adjective {adjective} noun {noun}", {'monkey': 'noun', 'eating': 'verb', 'graceful': 'adjective', 'jam': 'noun'})
#     expected = "This is a noun monkey and a verb eating with adjective graceful noun jam"
#     assert actual == expected

# def test_read_template():
#     with open('./asserts/spam.txt') as f:
#         actual = f.read().strip()
#         expected = "This is a noun {noun} and a verb {verb} with adjective {adjective} noun {noun}"
#         assert actual == expected

