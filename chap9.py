# This is where the answers to Chapter 9 questions for the BSS Dev RampUp go
# Name: Cassie Sancartier

9.1

fin = open('/users/cms/Desktop/RampUp/dev-sprint3/words.txt')

for line in fin:
    word = line.strip()
    if len(word) > 20:
        print word


counterdemonstrations
hyperaggressivenesses
microminiaturizations



9.2


fin = open('/users/cms/Desktop/RampUp/dev-sprint3/words.txt')

def has_no_e(word):
    if 'e' not in word:
        return True
    return False
    
def percentage_no_e(fin):
    
    count_total = 0.0
    count_without_e = 0.0
    
    for line in fin:
        word = line.strip()
        if has_no_e(word) is True:
            count_without_e += 1
        count_total += 1 
    
    percent = (count_without_e/count_total) * 100.0
    print percent



Result:
>>> percentage_no_e(fin)
33.073834231 

9.3

fin = open('/users/cms/Desktop/RampUp/dev-sprint3/words.txt')


def avoids(word, forbidden):
    for letter in word:
        if letter in forbidden:
            return False
        return True

def input_avoids():
    forbidden = raw_input("Enter five different letters:")
    fin = open('/users/cms/Desktop/RampUp/dev-sprint3/words.txt')
    count = 0
    for line in fin:
        word = line.strip()
        if avoids(word, forbidden) is True:
            print word
            count += 1
    print count

    return None

## Having an issue here - it seems to be only checking the first letter of each line?


9.4

def uses_only(word, required_letters):
    for letter in word:
        if letter not in required_letters:
            return False
    return True        





















