import sys
import itertools
import string
import hashlib
import time
import bcrypt

max = 10
all = string.printable 
arg4 = ""
arg3 = ""
guess2 = ""
#python knows what an argument is, argv is just the argument at location after cmd
#inside brackets, cmd is python3 FreeCrack.py arg1 agr2 etc
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
def brute():
    startTime = time.time()
    password2=password.encode('utf-8')
    for length in range(1,max):
        for combination in itertools.product(all, repeat=length):
            guess = "".join(combination)
            
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
            if (guess2 == password):
                print("Password " + guess + " has been cracked!")
                endTime=time.time()
                finalTime=(endTime-startTime)
                print("It took " + str(finalTime) + " seconds to crack this password")
                raise SystemExit

def dict():
    numbChecked = int(0)
    lineNumb = int(0)
    with open('10-million-password-list-top-1000000.txt') as fopen:
        for line in fopen.readlines():
            lineNumb += 1
            lineB = line.strip
            if(arg2=="-p"):
                line2=lineB
            elif(arg2=="-m"):
                line2=hashlib.md5(lineB.encode('utf-8')).hexdigest()
            elif(arg2=="-s"):
                line2=hashlib.sha256(lineB.encode('UTF-8')).hexdigest()
            if(arg4=="-v"):
                print(line2())
            elif(arg3=="-v"):
                print(line2())
            if line2() == password:
                print("\nYour password kinda sucks lol")
                raise SystemExit
            else:
                numbChecked += 1
    if ((lineNumb - numbChecked) == 0):
        print("\nYour password is not common")
        raise SystemExit
        

if(arg1 == "brute"):
    brute()
if(arg1 == "dict"):
    dict()
