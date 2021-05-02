# imports
import csv
import os
import hashlib as hash
import time
import math
import matplotlib.pyplot as plt

print("Program Started")

# the maximum length of a password in words, go through all possible combos
# of up to MAX_PASS_LENGTH words
MAX_PASS_LENGTH = 3

# open the file and parse it into a list
wordlist = []
wordlist.append("")
file = open('dictionary.txt', 'r')
filecontent = csv.reader(file)
for word in filecontent:
    wordlist.append(word[0])


passwordlist = []
file = open('passwords.txt', 'r')
filecontent = csv.reader(file)
for word in filecontent:
    passwordlist.append(word[0])

print(passwordlist)

guesses = []
time_passed = []

# determine hasher
hasher = input("Would you like to use (0) sha256 or (1) sha512?: ")


# take an input password and hash it
for index, plaintext_password in enumerate(passwordlist):
    password_length = len(plaintext_password)
    hash_type = 'SHA256' if hasher else 'SHA512'
    hashed_password = hash.sha3_256() if hasher else hash.sha3_512()
    hashed_password.update(str.encode(plaintext_password))

    # starts the clock
    start = time.time()

    # go through every permutation of up to MAX_PASS_LENGTH words in wordlist
    counter = 1
    worked = False
    case_counter = 0
    while counter < pow(len(wordlist), MAX_PASS_LENGTH):
        current = ""
        temp = counter
        for i in range(MAX_PASS_LENGTH):
            current += wordlist[temp % len(wordlist)]
            temp = temp // len(wordlist)

        counter += 1

        # hash the permutation
        
        if len(current) == password_length:
            case_counter += 1
            # hash the permutation
            curr_hashed = hash.sha3_256() if hasher else hash.sha3_512()
            curr_hashed.update(str.encode(current))
            # compare it to the hashed_password
            if curr_hashed.hexdigest() == hashed_password.hexdigest():
                # print the permuation if it was correct and exit the loop
                print("The hash " + curr_hashed.hexdigest() + " corresponds to " + current)
                worked = True
                break

    # if up to MAX_PASS_LENGTH was not enough (or it was not a permutation of the words)
    # print out the password and a not found statement
    if not worked:
        print("There was no combination that worked for " + plaintext_password)

    # stops the clock
    elapsed_time = time.time() - start
    time_passed.append(elapsed_time)
    guesses.append(counter)

#    # adds the count number for each point in time
#    for i in range (math.ceil(elapsed_time) * 100):
#        guesses.append((case_counter / elapsed_time) * i / 100)
#        time_passed.append(i / 100)
#        if (i / 100 > elapsed_time):
#            break
print(guesses)
print(time_passed)
plots everything
plt.plot(time_passed, guesses)
plt.xlabel('Time Elapsed (seconds)')
plt.ylabel('Hashes Compared')
plt.suptitle(str(case_counter) + ' crack attempts over ' + str(round(elapsed_time, 3)) + ' seconds', fontsize=14, fontweight='bold')
plt.title('Dictionary size: ' + str(len(wordlist)) + ' words | Hash type: ' + hash_type)
plt.show()
