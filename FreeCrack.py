#imports and stuff for stuff, don't worry about it
import sys
import itertools
import string
import hashlib
import time
import bcrypt

#uuuuhhhh like setting variables for like varying and stuff
max = 10
all = string.printable 
arg4 = ""
arg3 = ""
guess2 = ""
arg1 = sys.argv[1]     
password = sys.argv[2]
arg2 = sys.argv[3]
if len(sys.argv) == 6:
    arg4 = sys.argv[5]
if len(sys.argv)>=5:
    arg3 = sys.argv[4]
    if(arg3 == "-t"):
        if(arg2=="-m"):
            password=password=hashlib.md5(password.encode('utf-8')).hexdigest()
        elif(arg2=="-s"):
             password=hashlib.sha256(password.encode('UTF-8')).hexdigest()
if len(sys.argv) > 6:
    print("You aren't the brightest tool in the shed if you put in more arguments than acceptable")
#defining the brute force program, super cool and stuff
def brute():
    startTime = time.time()
    password2=password.encode('utf-8')
    for length in range(1,max):
        for combination in itertools.product(all, repeat=length):
            guess = "".join(combination)
            #arguments and stuff for brute forcing
            if(arg2=="-p"):
                guess2=guess
            elif(arg2=="-m"):
                guess2=hashlib.md5(guess.encode('utf-8')).hexdigest()
            elif(arg2=="-s"):
                guess2=hashlib.sha256(guess.encode('UTF-8')).hexdigest()
            elif(arg2=="-b"):
                guess2=guess.encode('utf-8')
                if bcrypt.checkpw(guess2,password2)==True:
                    print("Password " + guess + " has been cracked!")
                    endTime=time.time()
                    finalTime=(endTime-startTime)
                    print("It took " + str(finalTime) + " seconds to crack this password")
                    raise SystemExit
            if(arg4=="-v"):
                print(guess2)
            elif(arg3=="-v"):
                print(guess2)
            #checking if the guess equals the password, very cool
            if (guess2 == password):
                print("Password " + guess + " has been cracked!")
                endTime=time.time()
                finalTime=(endTime-startTime)
                print("It took " + str(finalTime) + " seconds to crack this password")
                raise SystemExit

#defining the dictionary attack, not very cool
def dict():
    #more variable defining
    password2=password.encode('utf-8')
    numbChecked = int(0)
    lineNumb = int(0)
    #itterating through the most common 9,999,998 passwords
    with open('10-million-password-list-top-1000000.txt') as fopen:
        for line in fopen.readlines():
            lineNumb += 1
            #arguments for dictionary attack
            if(arg2=="-p"):
                lineB = line.replace('\n','')
            elif(arg2=="-m"):
                lineB = line.replace('\n','')
                lineB=hashlib.md5(lineB.encode('utf-8')).hexdigest()
            elif(arg2=="-s"):
                lineB = line.replace('\n','')
                lineB=hashlib.sha256(lineB.encode('UTF-8')).hexdigest()
            if arg2 == '-b':
                lineB = line.replace('\n','')
                lineB = lineB.encode('utf-8')
                lineB = lineB.lower()
                if bcrypt.checkpw(lineB, password2) == True:
                    print("\nYour password kinda sucks lol")
                    raise SystemExit
            if(arg4=="-v"):
                print(lineB)
            elif(arg3=="-v"):
                print(lineB)
            #checking if the current password in the list of 9,999,998 matches the inputed password
            if lineB == password:
                print("\nYour password kinda sucks lol")
                raise SystemExit
            else:
                numbChecked += 1
    if ((lineNumb - numbChecked) == 0):
        print("\nYour password is not common")
        raise SystemExit

check = 0
if((arg1 != "brute")and(arg1 != "dict")):
    print("Why are you stupid?")
    check = check + 1
#defining some arguments
if(arg1 == "brute"):
    if(arg2 != "-p") and (arg2 != "-m") and (arg2 != "-s") and (arg2 != "-b"):
        print("Were you dropped on your head as a child?")
        check = check + 1
    if(len(sys.argv)>=5) and (arg3 != "-v") and (arg3 != "-t") and (arg3 != " "):
        print("You should consider reading the README")
        check = check + 1
    if(len(sys.argv)==6) and (arg4 != "-v") and (arg4 != " "):
        print("Just quit trying, this stopped being funny")
        check = check + 1
    if(check > 0):
        raise SystemExit
    elif(check == 0):
        brute()
if(arg1 == "dict"):
    if(arg2 != "-p") and (arg2 != "-m") and (arg2 != "-s") and (arg2 != "-b"):
        print("Were you dropped on your head as a child?")
        check = check + 1
    if(len(sys.argv)>=5) and (arg3 != "-v") and (arg3 != "-t") and (arg3 != " "):
        print("You should consider reading the README")
        check = check + 1
    if(len(sys.argv)==6) and (arg4 != "-v") and (arg4 != " "):
        print("Just quit trying, this stopped being funny")
        check = check + 1
    if(check > 0):
        raise SystemExit
    elif(check == 0):
        dict()

    

