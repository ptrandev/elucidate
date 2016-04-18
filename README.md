# Elucidate
A Python script that uses basic methods to crack passwords.

Based off a script created by [Science Buddies](http://www.sciencebuddies.org/Files/5549/17/crack2.py).

This script contains cleaner, improved code and commenting.

You could call me a script kiddie. I may suck at Python but I'm sure everyone except Guido did so at one point.
___

## Table of Contents -
1. Methods of Cracking Passwords
2. Useage
3. Modification and Redistribution

___

## 1. Methods of Cracking Passwords

Elucidate uses 4 methods to crack passwords:

#### 1. Dictionary of Common Passwords
  
Elucidate will use the "password.txt" file to guess the password. It contains only safe-for-work (and school) common passwords from a book called *Perfect Passwords: Selection, Protection, Authenication* by Mark Burnett (__ISBN 978-1597490412__). 

#### 2. Dictionary of Common Passwords (Plus Plus)

This builds upon the the first method. It combines two common passwords together, does the same with punctuation seperating the two, and capitalizes the first letters of each word.

#### 3. Numbers Only
  
The script will guess the password only using numbers. It will first guess 1 number, then 2 number combinations, then 3 number combinations, etc. It will guess up combinations up to 8 characters.

#### 4. Combination of Characters
  
Elucidate will combine all characters and punctiation sequentially. It will first guess 1 character, then 2 character combinations , then 3 character combinations, etc. It will guess combinations up to 8 characters.

___

## 2. Useage (For Linux)

#### Package Requirements:
1. Python 2/3

#### Obtaining and Executing:
1. Open the terminal and type:

    <strong>$ git clone https://github.com/DonutDeflector/elucidate.git</strong>

2. Naviate to the directory:

    <strong>$ cd elucidate/elucidate/</strong>

3. Execute the script:

    <strong>$ python elucidate.py</strong>

#### Edit Passwords to Crack:
1. Open the <em>elucidate.py</em> file in your favorite text editor:

	<strong>$ nvim elucidate.py</strong>

2. Navigate to <em>line 371</em> and change <em>password0 - password9</em>:

    # set the passwords you want to guess here
    password0="123456"

    password1="albert"

    password2="03694816"

    password3="mistress!maxwell"

    password4="phantomscorpion"

    password5="armor"

    password6="frBSD173"

    password7="m0n2t3r2"

    password8="correcthorsebatterystaple"

    password9="Gkgmyf8jNYB2UbVf"


#### Operation:
1. After executing the script, it will prompt you: 

    <strong>- Elucidate: Python Password Cracker -</strong>

    <strong>Password to Decrypt (0-9):</strong>

2. 

___

## 3. Modification and Redistribution



