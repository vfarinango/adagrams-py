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
    letter_hand = []
    for i in range(10):
        #Generates a random integer between 0 and the last element in letter_pool list.
        random_index = randint(0,len(letter_pool)-1)
        #Access an element within letter_pool list, determined by random_index.
        random_letter = letter_pool[random_index]
        #Add the newly generated random letter to letter_hand list.
        letter_hand.append(random_letter)
        #Remove the random_letter from letter_pool
        letter_pool.remove(random_letter)

    #Return letter_hand list of 10 letters.
    return letter_hand


def uses_available_letters(word, letter_bank):
    word = word.upper()
    #Create a dictionary for word to store the word and its frequency.
    word_count = {}
    #Iterate through each element in word and add it to word_count dictionary.
    for char in word:
        if char in word_count:
            word_count[char] += 1
        else:
            word_count[char] = 1
    

    #Create a dictionary for letter_bank to store each word and its frequency.
    letter_bank_count = {}
    #Iterate through each element in letter_bank list and add it to letter_bank_count dictionary.
    for i in letter_bank:
        if i in letter_bank_count:
            letter_bank_count[i] += 1
        else:
            letter_bank_count[i] = 1

    
    #For every letter in word_count, the letter in letter_bank_count is greater than or equal to it.
    #Iterate through word_count dictionary
    for char in word_count.keys():
        if char not in letter_bank_count or word_count[char] > letter_bank_count[char]:
            return False
    return True
        


def score_word(word):
    pass



def get_highest_word_score(word_list):
    pass


