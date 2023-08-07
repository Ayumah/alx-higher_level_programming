#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - function that checks if a singly linked list has a cycle.
 * @list: pointer to the linked list.
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *first = list;
	listint_t *last = list;

	while (first && last && last->next)
	{
		first = first->next;
		last = last->next->next;
		if (last == first)
			return (1);
	}
	return (0);
}
