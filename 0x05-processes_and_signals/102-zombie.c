#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - creates an infinite loop to make the program freeze
 * Return: Always 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - creates 5 zombie processes
 * Return: Always 0
 */
int main(void)
{
	int n;
	pid_t z;

	for (n = 0; n < 5; n++)
	{
		z = fork();
		if (!z)
			return (0);
		printf("Zombie process created, PID: %d\n", z);
	}

	infinite_while();
	return (0);
}
