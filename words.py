
def print_upper_words(l, must_start_with):
    """ print list of words in UPPER CASE
    that begin with letter in a certain set
    """
    for word in l:
        for letter in must_start_with:
            if word[0] == letter or word[0] == letter.upper():
                print(word.upper())

print_upper_words(['scott', 'david', 'Ernie', 'kushnier', 'echo'], must_start_with={"e"})

print('-------')
print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})
