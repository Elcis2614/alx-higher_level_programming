#include "lists.h"
/**
*check_cycle - check if there is a cycle in a link list
*@list: the list
*Return: 0 if not , 1 if yes
*/
int check_cycle(listint_t *list)
{
	listint *start, *temp;

	if (list != NULL)
	{
		start = list;
		temp = list;
		do {
			if ((*temp)->next == list)
				return (1);
			temp = (*temp)->next;
		} while (temp != NULL);
	}
	return (0);
}
