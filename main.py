#fuction will return frequency of each letter in the ith column, and the number of letters 
def letter_frequencies(column):
    #dictionary intialization, each letter starts with frequency 0
    frequency_list={chr(i):0 for i in range(97,123)}
    total_letters=len(column)
    for l in column:
        frequency_list[l] +=1

    return frequency_list, total_letters

#function to calculate MR value (Measure of Roughness ) 

def calculate_MR(frequency_list, total_letters):
    if total_letters <=1:
        return 0
    #calculation for MR value using this formula: MR=∑fi(fi−1) / L(L−1)
    mr=(sum(f*(f-1) for f in frequency_list.values())/(total_letters*(total_letters-1)))
    return mr 



