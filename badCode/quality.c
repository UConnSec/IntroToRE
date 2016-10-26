#include <string.h>
#include <stdio.h>

void alter_string(char *s)
{
        strcpy (s, "Goodbye!");//overwrites part of string s
        printf ("Result: %s\n", s);
};

int main()
{
        alter_string ("Hello, world!\n");//passes const string argument to alter_string
	return 0;
};
