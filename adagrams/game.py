from random import randint 

def create_letter_pool():
    letter_pool = []
    letter_pool.extend(["A"] * 9)
    letter_pool.extend(["B"] * 2)
    letter_pool.extend(["C"] * 2)
    letter_pool.extend(["D"] * 4)
    letter_pool.extend(["E"] * 12)
    letter_pool.extend(["F"] * 2)
    letter_pool.extend(["G"] * 3)
    letter_pool.extend(["H"] * 2)
    letter_pool.extend(["I"] * 9)
    letter_pool.extend(["J"] * 1)
    letter_pool.extend(["K"] * 1)
    letter_pool.extend(["L"] * 4)
    letter_pool.extend(["M"] * 2)
    letter_pool.extend(["N"] * 6)
    letter_pool.extend(["O"] * 8)
    letter_pool.extend(["P"] * 2)
    letter_pool.extend(["Q"] * 1)
    letter_pool.extend(["R"] * 6)
    letter_pool.extend(["S"] * 4)
    letter_pool.extend(["T"] * 6)
    letter_pool.extend(["U"] * 4)
    letter_pool.extend(["V"] * 2)
    letter_pool.extend(["W"] * 2)
    letter_pool.extend(["X"] * 1)
    letter_pool.extend(["Y"] * 2)
    letter_pool.extend(["Z"] * 1)
    return letter_pool


def draw_letters():
    #Create the data structure containing the letters and letter distribution.
    letter_pool = create_letter_pool()

    #Randomly select 10 characters from the data structure
    counter = 0
    letter_hand = []
    for i in range(10):
        random_index = randint(0,len(letter_pool)-1)
        random_letter = letter_pool[random_index]
        letter_hand.append(random_letter)

    #Return a list of 10 strings
    return letter_hand

result = draw_letters()
print(result)

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass