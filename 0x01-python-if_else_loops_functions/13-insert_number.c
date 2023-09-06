#include "lists.h"

/**
 * insert_node -function that inserts a number into a sorted singly linked list
 *
 * @head: pointer to singly linked list
 * @number: number to be added to the list
 *
 * Return: the address of the new node or NULL
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp;
	listint_t *ptr = *head;
	listint_t *current;

	temp = malloc(sizeof(listint_t));
	if (temp == NULL)
		return (NULL);

	if (*head == NULL)
		return (add_nodeint_end(head, number));

	temp->n = number;

	if (number <= ptr->n)
	{
		temp->next = ptr;
		*head = temp;
		return (*head);
	}
	current = (*head)->next;
	while (current)
	{
		if ((number >= ptr->n) && (number <= current->n))
		{
			temp->next = current;
			ptr->next = temp;
			return (temp);
		}
		ptr = ptr->next;
		current = current->next;
	}
	if (number > ptr->n)
	{
		ptr->next = temp;
		return (temp);
	}
	return (NULL);
}
