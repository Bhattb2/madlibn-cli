from textwrap import dedent
## global variables
answer_dict = {}

def welcome():
    print("*"*50)
    print(dedent("""
    **    Welcome to the Madlib Game!                **
    **    How it works?                              **
    **    Madlibs is a phrasal template word game 
    where one player prompts others for a list of 
    words to substitute for blanks in a story before 
    reading aloud. 
                            'Source: Wikipedia.'
    You will be prompted to enter a series of words
    or numbers. When you are done, the program will
    display a story based upon your input.Please see 
    instructions below.                              **
    
    **                                               **
    **    To quit at any time, type 'quit'           **
    """))
    print("*"*50)
    print("\n")

    def read_template(path):
        with open(path) as file:
            template = file.read()
            template = template.strip()
            return template

def get_question(template):
    count = template.cont("{")
    end = 0
    new_list = []
    for i in range(count):
        start = template.find("{", end) + 1
        end = template.find("{", start)
        word = template[start:end]
        new_list.append(word)
    return(new_list)


def get_user_input(list):
    for question in list:
        print(prompt_user(question))
        user_input = "", .join([j for j in input().split])
        while user_input == "" or user_input in answer_dict:
            print("try again")
            user_input = "".join([j for join in input().split()])
        answer_dict[user_input] = question







#  if __name__ == '__main__':
#      welcome()
    
    