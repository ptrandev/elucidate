#!/usr/bin/python

# Elucidate: A Python script that uses basic methods to crack passwords.
# Based off of a script created by Science Buddies. (http://www.sciencebuddies.org/Files/5549/17/crack2.py)

# This script contains cleaner, improved code and commenting.
# You could call me a script kiddie. I may be terrible  at Python but I'm sure everyone except Guido did so at one point.

# See README.md for more information.
# Availiable on Github: https://github.com/DonutDeflector/elucidate

# Go to line 368 to set the passwords you want to guess.

######################################################################################

# extra functions
import sys, time, hashlib
from array import *

#################### 
# global variables # 
####################

# password to crack from 0-6
which_password = 0

# the passwords we are trying to crack; these variables will get written in
password0 = ""
password1 = ""
password2 = ""
password3 = ""
password4 = ""
password5 = ""
password6 = ""

# total number of guesses we had to make to find it
totalguesses = 0


#--------------- extra helper functions -------------------
# These will be used by our search routines later on. We'll get these defined and out
# of the way. The actual search program is called "main" and will be the last one
# defined. Once it's defined, the last statement in the file runs it.
#
#

# Takes a number from 0 on up and the number of digits we want it to have. It uses that
# number of digits to make a string like "0000" if we wanted 4 or "00000" if we wanted
# 5, converts our input number to a character string, sticks them together and then returns
# the number we started with, with extra zeroes stuck on the beginning. 
def leading_zeroes(n, zeroes):
    t=("0"*zeroes)+str(n)
    t=t[-zeroes:]
    return t

# check_userpass
def check_userpass(which_password, password):
    global password0, password1, password2, password3
    global password4, password5, password6
    
    result = False

    if (0 == which_password):
        if password == password0:
            result = True

    if (1 == which_password):
        if password == password1:
            result = True

    if (2 == which_password):
        if password == password2:
            result = True

    if (3 == which_password):
        if password == password3:
            result = True

    if (4 == which_password):
        if password == password4:
            result = True
            
    if (5 == which_password):
        if password == password5:
            result = True
            
    if (6 == which_password):
        if password == password6:
            result = True
            
    return result

# This displays the results of a search including tests per second when possible
def report_search_time(tests, seconds):
    if (seconds > 0.000001):
        print ("The search took "+make_human_readable(seconds)+" seconds for "+make_human_readable(tests)+" tests or "+make_human_readable(tests/seconds)+" tests per second.")
    else:
        print ("The search took "+make_human_readable(seconds)+" seconds for "+make_human_readable(tests)+" tests.")
    return

##################
# search methods #
##################

# search method 1 will try using digits as the password.
def search_method_1(num_digits):
    global totalguesses
    result = False
    a=0
    #num_digits = 3    # How many digits to try. 1 = 0 to 9, 2 = 00 to 99, etc.
    starttime = time.time()
    tests = 0
    still_searching = True
    print("Using method 1 and searching for "+str(num_digits)+" digit numbers.")
    while still_searching and a<(10**num_digits):
        ourguess = leading_zeroes(a,num_digits)
        tests = tests + 1
        totalguesses = totalguesses + 1
        if (check_userpass(which_password, ourguess)):
            print ("Password Cracked:" +str(which_password)+" is " + ourguess)
            still_searching = False   # we can stop now - we found it!
            result = True
    a=a+1
    seconds = time.time()-starttime
    report_search_time(tests, seconds)
    return result

# search method 2 is a simulation of a letter-style combination lock. Each'wheel' has the
# letters A-Z, a-z and 0-9 on it as well as a blank. The idea is that we have a number of
# wheels for a user name and password and we try each possible combination.
def search_method_2(num_pass_wheels):
    global totalguesses
    result = False
    starttime = time.time()
    tests = 0
    still_searching = True
    print("Using method 2 and searching with "+str(num_pass_wheels)+" password wheels.")
    wheel = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789~!@#$%^&*()_-+={}[]:<>,./"
    # we only allow up to 8 wheels for each password for now
    if (num_pass_wheels > 8):
        print("Unable to handle the request. No more than 8 characters for a password")
        still_searching = False
    # set all of the wheels to the first position
    pass_wheel_array=array('i',[1,0,0,0,0,0,0,0,0])
        
    while still_searching:
        ourguess_pass = ""
        for i in range(0,num_pass_wheels):  # once for each wheel
            if pass_wheel_array[i] > 0:
                ourguess_pass = wheel[pass_wheel_array[i]] + ourguess_pass
        #print ("trying ["+ourguess_pass+"]")
        if (check_userpass(which_password, ourguess_pass)):
            print ("Success! Password  "+str(which_password)+" is " + ourguess_pass)
            still_searching = False   # we can stop now - we found it!
            result = True
        tests = tests + 1
        totalguesses = totalguesses + 1
# spin the rightmost wheel and if it changes, spin the next one over and so on
        carry = 1
        for i in range(0,num_pass_wheels): # once for each wheel
            pass_wheel_array[i] = pass_wheel_array[i] + carry
            carry = 0
            if pass_wheel_array[i] > 62:
                pass_wheel_array[i] = 1
                carry = 1
                if i == (num_pass_wheels-1):
                    still_searching = False

    seconds = time.time()-starttime
    report_search_time(tests, seconds)
    return result

# This function takes in numbers, rounds them to the nearest integer and puts
# commas in to make it more easily read by humans
def make_human_readable(n):
    if n>=1:
        result = ""
        temp=str(int(n+0.5))
        while temp != "":
            result = temp[-3:] + result
            temp = temp[:-3]
            if temp != "":
                result = "," + result
    else:
        temp = int(n*100)
        temp = temp /100
        result = str(temp)
    return result
        
## A little helper program to remove any weird formatting in the file
def cleanup (s):
    s = s.strip()
    return s

## A little helper program that capitalizes the first letter of a word
def Cap (s):
    s = s.upper()[0]+s[1:]
    return s


# search method 3 uses a list of dictionary words. In this case, we have a list
# of the 500 most commonly used passwords in 2005 as collected by Mark Burnett
# for his book "Perfect Passwords" (ISBN 978-1597490412). Because the list comes
# from so many people around the world, we had to remove some of the passwords.
# People like to use passwords that they think will shock other people, so
# sometimes they're not fit for polite company.
def search_method_3(file_name):
    global totalguesses
    result = False
    
    # you know what I like more than my lamborghini? knowledge
    f = open(file_name)
    words = f.readlines()
    f.close
    # We need to know how many there are
    number_of_words = len(words)
    print("Using method 3 with "+str(number_of_words)+" in the list")
    
    ## Depending on the file system, there may be extra characters before
    ## or after the words. 
    for i in range(0, number_of_words):
        words[i] = cleanup(words[i])

    # Let's try each one as the password and see what happens
    starttime = time.time()
    tests = 0
    still_searching = True
    word1count = 0           # Which word we'll try next

    while still_searching:
        ourguess_pass = words[word1count]
        #print("Guessing: "+ourguess_pass)
        # Try it the way it is in the word list
        if (check_userpass(which_password, ourguess_pass)):
            print ("Success! Password "+str(which_password)+" is " + ourguess_pass)
            still_searching = False   # we can stop now - we found it!
            result = True
        tests = tests + 1
        totalguesses = totalguesses + 1
        # Now let's try it with the first letter capitalized
        if still_searching:
            ourguess_pass = Cap(ourguess_pass)
            #print("Guessing: "+ourguess_pass)
            if (check_userpass(which_password, ourguess_pass)):
                print ("Success! Password "+str(which_password)+" is " + ourguess_pass)
                still_searching = False   # we can stop now - we found it!
                result = True
            tests = tests + 1
            totalguesses = totalguesses + 1

        word1count = word1count + 1
        if (word1count >=  number_of_words):
            still_searching = False

    seconds = time.time()-starttime
    report_search_time(tests, seconds)
    return result
            
## Search method 4 is similar to 3 in that it uses the dictionary, but it tries two
## two words separated by a punctuation character
def search_method_4(file_name):
    global totalguesses
    result = False
    
    # Start by reading the list of words into a Python list
    f = open(file_name)
    words = f.readlines()
    f.close
    # We need to know how many there are
    number_of_words = len(words)
    
    ## Depending on the file system, there may be extra characters before
    ## or after the words. 
    for i in range(0, number_of_words):
        words[i] = cleanup(words[i])

    # Let's try each one as the password and see what happens
    starttime = time.time()
    tests = 0
    still_searching = True
    word1count = 0           # Which word we'll try next
    punc_count = 0
    word2count = 0

    punctuation="~!@#$%^&*()_-+={}[]:<>,./X"  # X is a special case where we omit
                                              # the punctuation to run the words together

    number_of_puncs = len(punctuation)
    print("Using method 4 with "+str(number_of_puncs)+" punc chars and "+str(number_of_words)+" in the list")

    while still_searching:
        if ("X" == punctuation[punc_count]):
            # If we're at the end of the string and found the 'X', leave it out
            ourguess_pass = words[word1count] + words[word2count]
        else:
            ourguess_pass = words[word1count] + punctuation[punc_count] + words[word2count]
        #print("Guessing: "+ourguess_pass)
        # Try it the way they are in the word list
        if (check_userpass(which_password, ourguess_pass)):
            print ("Success! Password "+str(which_password)+" is " + ourguess_pass)
            still_searching = False   # we can stop now - we found it!
            result = True
        tests = tests + 1
        totalguesses = totalguesses + 1
        # Now let's try it with the first letter of the first word capitalized
        if still_searching:
            ourguess_pass = Cap(words[word1count]) + punctuation[punc_count] + words[word2count]
            if (check_userpass(which_password, ourguess_pass)):
                print ("Success! Passwword "+str(which_password)+" is " + ourguess_pass)
                still_searching = False   # we can stop now - we found it!
                result = True
            tests = tests + 1
            totalguesses = totalguesses + 1
        # Now let's try it with the first letter of the second word capitalized
        if still_searching:
            ourguess_pass = words[word1count] + punctuation[punc_count] + Cap(words[word2count])
            if (check_userpass(which_password, ourguess_pass)):
                print ("Success! Password "+str(which_password)+" is " + ourguess_pass)
                still_searching = False   # we can stop now - we found it!
                result = True
            tests = tests + 1
            totalguesses = totalguesses + 1
        # Now let's try it with the both words capitalized
        if still_searching:
            ourguess_pass = Cap(words[word1count]) + punctuation[punc_count] + Cap(words[word2count])
            if (check_userpass(which_password, ourguess_pass)):
                print ("Success! Password "+str(which_password)+" is " + ourguess_pass)
                still_searching = False   # we can stop now - we found it!
                result = True_
            tests = tests + 1
            totalguesses = totalguesses + 1

        word1count = word1count + 1
        if (word1count >=  number_of_words):
            word1count = 0
            punc_count = punc_count + 1
            if (punc_count >= number_of_puncs):
                punc_count = 0
                word2count = word2count + 1
                if (word2count >= number_of_words):
                    still_searching = False

    seconds = time.time()-starttime
    report_search_time(tests, seconds)
    return result


def main(argv=None):
    global password0, password1, password2, password3
    global password4, password5, password6, totalguesses
    global which_password

    # set the passwords you want to guess here
    password0="albert"
    password1="mustang"
    password2="123456"
    password3="summer"
    password4="password"
    password5="football"
    password6="2000"

    # start searching
    which_password = 1
    which_password = int(input("Password to Decrypt: (0-6) "))
    overallstart = time.time()
    foundit = False
    print("Trying to guess password "+str(which_password))
    # Look through our list of common passwords first
    if not foundit:
        foundit = search_method_3("passwords.txt")
    # Still looking? Let's combine the common passwords 2 at a time
    if not foundit:
        foundit = search_method_4("passwords.txt")
    # Still looking? See if it's a single digit
    if not foundit:
        foundit = search_method_1(1)
    # Still looking? See if it's a 2 digit number
    if not foundit:
        foundit = search_method_1(2)
    # Still looking? See if it's a 3 digit number
    if not foundit:
        foundit = search_method_1(3)
    # Still looking? See if it's a 4 digit number
    if not foundit:
        foundit = search_method_1(4)
    # Still looking? See if it's a 5 digit number
    if not foundit:
        foundit = search_method_1(5) 
    # Still looking? See if it's a 6 digit number
    if not foundit:
        foundit = search_method_1(6)
    # Still looking? See if it's a 7 digit number
    if not foundit:
        foundit = search_method_1(7)
    # Still looking? See if it's a 8 digit number
    if not foundit:
        foundit = search_method_1(8)
    # Still looking? Guess up to 8 character combinations
    if not foundit:
        foundit = search_method_2(8)
    seconds = time.time()-overallstart

    # print information about the guessing process (total seconds, total guesses, and guesses per second)
    print ("")
    print ("Total Seconds: "+make_human_readable(seconds)+"")
    print ("Total Guesses: "+make_human_readable(totalguesses)+"")
    print ("Guesses/Second: "+make_human_readable(totalguesses/seconds)+"")

print ("- Elucidate: Python Password Cracker -")
if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
