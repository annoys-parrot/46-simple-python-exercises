# Exercise 12: http://www.ling.gu.se/~lager/python_exercises.html

def generate_n_chars(n, c):
    '''A function that takes an integer n and a character c and
       returns a string, n characters long, consisting only of c.'''
    new_string = ''
    for _ in range(n):
        new_string = new_string + c
    return new_string

def histogram(dataset):
    '''A function that takes a list of integers and
       prints a histogram to the screen.'''
    for n in dataset:
        print generate_n_chars(n, '*')