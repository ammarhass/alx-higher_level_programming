#include "lists.h"

/**
 * check_cycle - function that checks if a singly linked list has a cycle in it
 *
 * @list: pointer to a linked_list
 * Return: 0 or 1
 */

int check_cycle(listint_t *list)
{
	listint_t *current = list;
	listint_t *temp = list;

	if (!list)
		return (0);

	while (current && current->next)
	{
		temp = temp->next;
		current = current->next->next;
		if (current == temp)
			return (1);
	}
	return (0);
}
