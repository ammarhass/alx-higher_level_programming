#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - function that checks
 * if a singly linked list is a palindrome
 *
 * @head: head of the list
 * Return: 1 or 0
 */

int is_palindrome(listint_t **head)
{
	listint_t *current;
	int *ptr;
	int size = 0;
	int i = 0, j = 0;

	if (head == NULL)
		return (1);

	current = *head;
	while (current)
	{
		size++;
		current = current->next;
	}

	ptr = malloc(sizeof(int) * size);
	if (ptr == NULL)
		return (0);
	current = *head;
	for (i = 0; i < size; i++)
	{
		ptr[i] = current->n;
		current = current->next;
	}
	i = 0;
	j = size - 1;
	while (i <= j)
	{
		if (ptr[i] != ptr[j])
		{
			free(ptr);
			return (0);
		}
		i++;
		j--;
	}
	free(ptr);

	return (1);
}
