what you have to do is extract the flag from the
binary RE1.o the methods to reach it may or may not involve:
cat
radare #db sym.main,dc,ds,pd N,?
ltrace -s
strace 
objdump -ds
file
strings

The source code is encrypted with the flag, decrypting the source code is not your goal.
The python script will decrypt the source code if it is given a file with the flag in it,
a file that is encrypted, and a destination file for the decrypted plaintext.

AGAIN, THE SOURCE CODE IS NOT YOUR GOAL! 
The source code is just for reference on a poor way of checking passwords, that you can read
after you're done. Later problems will use the same format, but I'll use actually decent
encryption as opposed to a modified vignere cypher.
