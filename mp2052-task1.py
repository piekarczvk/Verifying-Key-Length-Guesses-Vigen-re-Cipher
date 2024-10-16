import string
from collections import Counter

# function will return frequency of each letter in the ith column, and the number of letters 
def letter_frequencies(column):
    # dictionary initialization, each letter starts with frequency 0
    frequency_list = {chr(i): 0 for i in range(97, 123)}  # 'a' to 'z'
    
    # count the total number of letters in the column
    total_letters = len(column)

    # calculate the frequency of each letter in the column
    for l in column:
        frequency_list[l] += 1
    
    # return the frequency dictionary and the total number of letters
    return frequency_list, total_letters

#function to calculate MR value (Measure of Roughness)
def calculate_MR(frequency_list, total_letters):
    #return 0 if the column is too small to calculate MR
    if total_letters <= 1:
        return 0

    # calculation for MR value using this formula: MR = ∑fi(fi−1) / L(L−1)
    mr = (sum(f * (f - 1) for f in frequency_list.values()) / (total_letters * (total_letters - 1)))
    return mr 

# function to create a matrix, splitting the text into columns depending on key length guess
def create_matrix(ciphertext, key_length):

    # create empty matrix with number of empty lists as number of 'key_length'
    matrix = [[] for _ in range(key_length)]

    for i, letter in enumerate(ciphertext):
        if letter.isalpha():  # select letters only 
            matrix[i % key_length].append(letter.lower())  # Store in lowercase

    return matrix

# function will find the best MR value (the closest to English)
# and display all MR values for all key length guesses
def find_best(ciphertext, key_lengths):
    goal_mr = 0.0686  # MR value for English text
    best_key = None


    # difference initialized to infinity, so we can find the smallest
    best_difference = float('inf')

    print("Key Length Guess | MR Value | Difference from English MR")
    print("---------------------------------------------------------")

    # normalize ciphertext: remove non-letter characters and convert to lowercase
    ciphertext = ''.join([c.lower() for c in ciphertext if c in string.ascii_letters])

    for key_length in key_lengths:
        matrix = create_matrix(ciphertext, key_length)  # Create a matrix for the key length guess
        total_mr = 0

        #calculate MR for each column in the matrix
        for column in matrix:
            l_frequencies, total_letters = letter_frequencies(column)
            column_mr = calculate_MR(l_frequencies, total_letters)
            total_mr += column_mr  #accumulate MR values

        # average MR value for this key length guess
        average = total_mr / len(matrix) if len(matrix) > 0 else 0
        # Calculate difference from known English MR
        difference = abs(average - goal_mr)

        # display MR value for each key length guess
        print(f"      {key_length}         |  {average:.5f}  |  {difference:.5f}")

        
        if difference < best_difference:
            best_difference = difference
            best_key = key_length

    # display the most likely correct key length
    print("\nBest Key Length:  ", best_key)

    return best_key

#test case
ciphertext = "Svuwctlq iravxhoqu ywoxwiv Owmkhsdhzhf ndg xdwyhr $400 slzrlct wc hocc rbk rt srrkub jdhgfstwsxvpuwhrhbkfyy zwjh cvhb. Zks iravdbev cvwwidz oqhkuquqbkfh rdmku oroccv vaqrxhry rt MSIy wc crfq vmtfvxrbuxgrb, gzusgpzoqwtj hnh quvhrb otg qupdrhl prp ui hxdwtlbm dbj uitqwtj OO pcjhzy.."  # Replace with actual ciphertext
key_lengths = [1, 2, 3, 4, 5, 6, 7, 8]  # key length guesses
best_key_length = find_best(ciphertext, key_lengths)
