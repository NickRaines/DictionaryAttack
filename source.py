# imports
import csv
import os
import hashlib as hash

print("Program Started")

# the maximum length of a password in words, go through all possible combos
# of up to MAX_PASS_LENGTH words
MAX_PASS_LENGTH = 3

# open the file and parse it into a list
wordlist = []
wordlist.append("")
file = open('dictionary.txt', 'r')
filecontent=csv.reader(file)
for word in filecontent:
    wordlist.append(word[0])

# take an input password and hash it
plaintext_password = input("input your password: ")
hasher = input("would you like to use (0) sha256 or (1) sha512")
hashed_password = hash.sha3_256() if hasher else hash.sha3_512()
hashed_password.update(str.encode(plaintext_password))

# go through every permutation of up to MAX_PASS_LENGTH words in wordlist
counter = 1
worked = False
while counter < pow(len(wordlist), MAX_PASS_LENGTH):
    current = ""
    temp = counter
    for i in range(MAX_PASS_LENGTH):
        current += wordlist[temp%len(wordlist)]
        temp = temp // len(wordlist)

    counter += 1

    # hash the permutation
    curr_hashed = hash.sha3_256() if hasher else hash.sha3_512()
    curr_hashed.update(str.encode(current))
    # compare it to the hashed_password
    if curr_hashed.hexdigest() == hashed_password.hexdigest():
        # print the permuation if it was correct and exit the loop
        print("The has " + curr_hashed.hexdigest() + " corresponds to " + current)
        worked = True
        break

# if up to MAX_PASS_LENGTH was not enough (or it was not a permutation of the words)
# print out the password and a not found statement
if not worked:
    print("there was no combination that worked for " + plaintext_password)
