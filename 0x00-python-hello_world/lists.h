#ifndef LISTS_H
#define LISTS_H
#include <stdio.h>
#include <stdlib.h>
int check_cycle(listint_t *list);
/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 * Description: singly linked list node structure
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;i
#endif
