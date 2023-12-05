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
(For info on what each argument, means see the next section)
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
Arguments (what they do and stuff):

Now come the optional arguments, not required but can be put on the command:
The next argument can be '-t' or '-v', example: python3 FreeCrack.py dict password -p -v
The final possible argument can only be '-v', example python3 FreeCrack.py dict -p -t -v
(The -v in the first optional argument has the same function as the -v in the second optional argument, it exists only to provide a method to ignore the '-t' but still use '-v')

