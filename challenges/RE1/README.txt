The source code is encrypted with the flag, decrypting the source code is not your goal.
The python script will decrypt the source code if it is given a file with the flag in it.

AGAIN, THE SOURCE CODE IS NOT YOUR GOAL! what you have to do is extract the flag from the
binary RE1.o the methods to reach it may or may not involve:
cat
radare #db sym.main,dc,ds,pd N,?
ltrace -s
strace 
objdump -ds
file
strings
The source code is just for reference after you finish.
