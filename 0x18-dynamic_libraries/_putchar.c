#include <unistd.h>
/**
 * -putchar - writes the character c to stdout
 *  @c: the character to write
 *
 *  Return : on success 1
 *  On Error, -1 is returned , and errno is set appropriatly.
 */
int _putchar(char c)
{
	return (write(1,&c, 1));
}
