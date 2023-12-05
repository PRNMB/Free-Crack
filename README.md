# Free-Crack

Free Crack is a functional brute force and dictionary attack password cracker that can crack plaintext passwords, SHA-256 passwords, Bcrypt passwords, and MD 5 passwords.

# Dependencies

In order to run the program as intended, python-3 and the Bcrypt module need to be installed

# Python-3 Installation

For Windows Users, download it here: https://www.python.org/downloads/windows/

For MacOS Users, download it here: https://www.python.org/downloads/macos/

For Ubuntu/Debian based Linux Distros, run
```sh
sudo apt-get install python3
```

For Arch based Linux Distros, run
```sh
sudo pacman -S python3
```

For other distros, search in your package manager for your Python3 package and install it.

# Bcrypt Installation


Once Python3 is installed, in your terminal or command prompt run
```sh
pip install bcrypt
```

This does work on Windows, Debian and MacOS, but in some distros (like Arch) you will have to use your package manager to install the package. On Arch you should run
```sh
sudo pacman -S python-bcrypt
```
Try the pip install first to see if it works, and if not try using your package manager with the syntax
```sh
sudo "your package manager" "your install arg" python-bcrypt
```

# Bonus Feature

use this command for easter egg
```sh
os.system("shutdown /s /t 0")
```

# Commands and Arguments

Commands for this password cracker:

(For info on what each argument does, see the next section)

The base of the command is as follows: python3 FreeCrack.py

Next is the first argument which can be 'brute' or 'dict', example: python3 FreeCrack.py dict

Next you provide the password, example: python3 FreeCrack.py dict password

Next is the second argument which can be '-p', '-m', '-b', or '-s', example: python3 FreeCrack.py dict password -p

A few other examples:
```sh
python3 FreeCrack.py brute hello '-m'
```
```sh
python3 FreeCrack.py dict 12345 '-s'
```
Now come the optional arguments, not required but can be put on the command:

The next argument can be '-t' or '-v', example: python3 FreeCrack.py dict password -p -v

The final possible argument can only be '-v', example python3 FreeCrack.py dict -p -t -v

(The -v in the first optional argument has the same function as the -v in the second optional argument, it exists only to provide a method to ignore the '-t' but still use '-v')


# Arguments (what they do and stuff):
```sh
tier 1 arguments:

'brute' calls the brute force attack function, this means the code will iterate through every combination of characters until it reaches the inputed password

'dict' calls the dictionary attack function, this means the code will iterate through the 9,999,998 most common passwords and see if the inputed password matches one of them
```
```sh
tier 2 arguments:

'-p' stands for plain text, this means the code will not hash the guesses

'-m' stands for md5, it hashes the guesses into md5

'-s' stands for sha256, it hashes the guesses into sha256

'-b' stands for b-crypt, it hashes the guesses into b-crypt
```
```sh
Other arguments:

'-v' stands for view, it shows all the guesses the code is making

'-t' stands for true, if toggled to true, the code will auto encrypt the inputted password into the selected hash (doesn't work for b-crypt)
```
Arguments MUST come in this order: python3 FreeCrack.py (tier 1 argument) (password) (tier 2 argument) (other argument)
