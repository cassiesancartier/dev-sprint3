# This is where the answers to Chapter 8 questions for the BSS Dev RampUp go
# Name: Cassie Sancartier

8.9

>>> def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False
    
    i = 0
    j = (len(word2) - 1)
    
    while j > -1:
        print i, j    #print here
        
        if word1[i] != word2[j]:
            return False
        i = i + 1
        j = j - 1
        
    return True

>>> is_reverse('pots', 'stop')
0 3
1 2
2 1
3 0
True

8.12

# These next two functions are what I was working on before looking at the answer,
# I got stuck on how to assign the new letter values to a new string given that
# strings are 'immutable' - so went to look at the answer for clues, and realized
# that rotating the individual letters first was the solution. I was getting an error 
# at the new_word[index] = chr((ord(letter)) + 10) line.


# did a specific function for 10 spaces first
def rotate_word_ten(word):
    index = 0

    for letter in word:
        print ord(letter) #print here to check   
        if ord(letter) < 112:
            new_word[index] = chr((ord(letter)) + 10)
        else:
            new_word[index] = chr((ord(letter)) - 16)
        index = index + 1
    
    return new_word[0:len(word)]

# generalized 

def rotate_word(word, places):
    forward = places
    backward = 26 - places
    turn_point = 122 - places

    for letter in word:
        print ord(letter) #print here to check   
        if ord(letter) < turn_point:
            chr((ord(letter)) + places)
        else:
            chr((ord(letter)) - backward)
    return word[0:len(word)]


# My final answer, after checking:

def rotate_letter(letter, n):
    start = ord('a')
    c = ord(letter) - start
    i = (c + n) % 26 + start
    return chr(i)

def rotate_word(word, n):
    new_word = ''
    for letter in word:
        new_word += rotate_letter(letter, n)
    return new_word


>>> rotate_word('cat', 10)
'mkd'








