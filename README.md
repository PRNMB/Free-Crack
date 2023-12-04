# Free-Crack
Free Crack password cracker

Commands for this password cracker:
(For info on what each argument, means see the next section)
The base of the command is as follows: python3 FreeCrack.py
Next is the first argument which can be 'brute' or 'dict', example: python3 FreeCrack.py dict
Next you provide the password, example: python3 FreeCrack.py dict password
Next is the second argument which can be '-p', '-m', '-b', or '-s', example: python3 FreeCrack.py dict password -p
A few other examples:
python3 FreeCrack.py brute hello '-m'
python3 FreeCrack.py dict 12345 '-s'

Now come the optional arguments, not required but can be put on the command:
The next argument can be '-t' or '-v', example: python3 FreeCrack.py dict password -p -v
The final possible argument can only be '-v', example python3 FreeCrack.py dict -p -t -v
(The -v in the first optional argument has the same function as the -v in the second optional argument, it exists only to provide a method to ignore the '-t' but still use '-v')

Arguments (what they do and stuff):
