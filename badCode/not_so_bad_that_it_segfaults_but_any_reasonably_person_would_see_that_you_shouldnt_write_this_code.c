#include <string.h>
#include <stdio.h>

void alter_string(char *s)
{
        strcpy (s, "Goodbye!");//overwrite some bytes in Hello, World!
        printf ("Result: %s\n", s);
};

int main()
{
	char rw_STRING[] = "Hello, world!\n";
        alter_string (rw_STRING);
	return 0;
};
