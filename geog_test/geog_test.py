"""Main module."""

import random
import string

def get_random_string(length=8):
    # choose from all lowercase letter, uppercase, numbers. (optional: punctuation)
    letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", result_str)

while True:
    try:
     ps_length = input("enter the length of password you want: (enter 'quit' to quit)")
    except ValueError:
        print('please enter a vaild number.')
    if ps_length == 'quit':
        break
    else:
     get_random_string(int(ps_length))