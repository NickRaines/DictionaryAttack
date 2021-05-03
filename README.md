# DictionaryAttack  
Implement a dictionary attack on passwords hashed using the SHA-256 and SHA-512 hashing algorithms.  

# Writeup
***(User instructions and screenshots provided in following sections)***
* The program (the file named “source.py”) is designed to be run using the two txt files contained in the zip folder alongside it, dictionary.txt and passwords.txt. The former provides the dictionary from which the passwords can draw from, while the latter is meant to be edited by the user to contain on each new line a password. The passwords can be any combination of individual words from the passwords file, with words being combined with no spaces; passwords are at minimum one word long. In order to keep the program’s runtime low for demonstration purposes, the dictionary file is kept short and the number of individual words combined into passwords is three max, but these can be easily changed by swapping in a new dictionary file and increasing the variable “MAX_PASS_LENGTH.” In order to run the file, all one must do is extract all of the files into one folder and double click on source.py.
* When the window running the program opens, the user will be prompted to select whether they want their passwords to be hashed using SHA-256 or SHA-512; they may do this by typing either a ‘0’ or a ‘1’ into the input as explained by the prompt. If they do not type a valid input, they will again be prompted to type either a zero or a one until they correctly do so.
* After making their selection, the program will run through all of the user’s passwords and hash them. The program will then take single words, and combinations of words, off of the dictionary, check if they’re the same length as the original password, and if they are, hash them to compare the hashes to determine if that combination of words is the original password. (If the password is not cracked, the program will print out a statement telling the user this.)
* After running through all provided user passwords, a scatter plot will be generated showing the number of times a potential password was hashed and compared to the user’s password compared to the time it took to crack that password. The plot also shows information such as the total number of times hashes were compared, the total amount of time the program ran for, the dictionary size, and the hash selected by the user.

# User Instructions
1. Download and extract the folder containing the files
2. (Optional) Replace the dictionary and passwords files as desired.
3. Run source.py and type ‘0’ or ‘1’ to select a hash option.
4. From there, the passwords will be run through the program and the results displayed.

# Screenshots
***Running the program using SHA-256***
![Command window](https://drive.google.com/uc?export=view&id=1-CBSYu3pjmoaqndld5hdVBleMXhhBATX)
![Plot](https://drive.google.com/uc?export=view&id=1NryF2k-nRNBELJVBglKX2zfr9gSaEiFt)

***Running the program using SHA-512***
![Command window](https://drive.google.com/uc?export=view&id=1XEq3anXrJ9cPHu-k-WdllamvTdtpOIkq)
![Plot](https://drive.google.com/uc?export=view&id=1NUXP_t27wvvw0E7n_NdavI6VzG4s7lNH)
