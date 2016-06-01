# Elucidate
A nonmalicious Python script that uses basic methods to crack passwords. 

**NOTE: THIS SCRIPT IS NON MALICIOUS. ELUCIDATE ONLY CRACKS PASSWORDS THAT ARE SPECIFIED WITHIN THE SCRIPT AS VARIABLES.**

Based off a script created by [Science Buddies](http://www.sciencebuddies.org/Files/5549/17/crack2.py).

This script contains cleaner, improved code and commenting as well as additional functionality.

___

## Table of Contents -
1. Modifications Made to the Original Script
2. Methods of Cracking Passwords
3. Usage
4. Modification and Redistribution

___

## 1. Modifications Made to the Original Script
 1. Clearer commenting
 2. More readable output to the terminal
 3. Removed need for password variables in MD5 Hashes
 3. Support for up to 10 passwords (from original 7)
 4. Support for up to 8 digit passwords (from original 7)
 5. Support for up to 25 character passwords (from original 8)

___

## 2. Methods of Cracking Passwords

Elucidate uses 4 methods to crack passwords:

#### 1. Dictionary of Common Passwords
  
Elucidate will use the *"password.txt"* file to guess the password. It contains only safe-for-work (and school) common passwords from a book called *Perfect Passwords: Selection, Protection, Authenication* by Mark Burnett (___ISBN 978-1597490412___). 

#### 2. Dictionary of Common Passwords (Plus Plus)

This builds upon the the first method. It combines two common passwords together, does the same with punctuation seperating the two, and capitalizes the first letters of each word.

#### 3. Numbers Only
  
The script will guess the password only using numbers. It will first guess 1 number, then 2 number combinations, then 3 number combinations, etc. It will guess up to 8 digit numbers.

#### 4. Combination of Characters
  
Elucidate will combine all characters and punctiation sequentially. It will first guess 1 character, then 2 character combinations , then 3 character combinations, etc. It will guess combinations up to 25 characters.

___

## 3. Usage (For Linux)

#### Package Requirements:
1. Python 2.7
2. git (optional)

#### Obtaining and Executing:
1. Open the terminal and type:

    ```$ git clone https://github.com/DonutDeflector/elucidate.git```

2. Naviate to the directory:

    ```$ cd elucidate/elucidate/```

3. Execute the script:

    ```$ python elucidate.py```

#### Edit Passwords to Crack:
1. Open the <em>elucidate.py</em> file in your favorite text editor:

    ```$ nvim elucidate.py```

2. Navigate to *line 377* and change *password0 - password9*:

```
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
```

#### Operation:
1. After executing the script, it will prompt you: 

```
	- Elucidate: Python Password Cracker -

    Password to Decrypt (0-9):
```

2. Select the number that corresponds to the password you want to crack:

    ```Password to Decrypt (0-9): 3```

3. The script will now run! Here is a sample of the script's output:

```
Password to Guess (0-9): 3
Guessing: Password 3


Method 3 -- 435 passwords in list
Seconds: 0.0 | Tests: 870 | Tests/Seconds: 599,679


Method 4 -- 26 punctuation characters | 435 passwords in list
Success! Password 3 = mistress!maxwell
Seconds: 47 | Tests: 19,139,981 | Tests/Seconds: 409,128


Total Seconds: 47 seconds
Total Guesses: 19,140,851 guesses
Guesses/Second: 409,119 guesses/second
```
___

## 4. Modification and Redistribution

Do as you please with the script the only restriction is you must give credit to both [Science Buddies](http://www.sciencebuddies.org/science-fair-projects/project_ideas/CompSci_p046.shtml#procedure) and myself. The requirement is noted as so on the linked page:

```
A Note About Plagiarism: The programming examples below are available for you to download and run 
on your own computer and even to use, if your teacher agrees, for your science project. When things 
are open-source like this, it can be confusing as to what is plagiarism and what is not, so Science 
Buddies has created this clear set of definitions to guide you. If you:

   - Use the programs as they are and give Science Buddies credit— this is not plagiarism.
   - Modify the programs and say that they were adapted from Science Buddies— this is not plagiarism.
   - Write your own programs from scratch— this is not plagiarism.
   - If you use the programs as they are (or modify them) without mentioning Science Buddies— this is plagiarism.
```

**From LICENSE.md:**

```
The MIT License (MIT)

Copyright (c) 2016 Phillip T.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and 
associated documentation files (the "Software"), to deal in the Software without restriction, including 
without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the 
following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial 
portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT 
LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO 
EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER 
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR 
THE USE OR OTHER DEALINGS IN THE SOFTWARE.

```
