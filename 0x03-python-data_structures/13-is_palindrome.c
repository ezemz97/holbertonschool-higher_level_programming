#include "lists.h"
/**
 * is_palindrome - Check if linked list is palindrome or not
 * @head: head pointer
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	int x = 0, y = 0, z = 0, *array;
	listint_t *tmp = *head;

	if (!head)
		return (1);
	x = counter(*head);
	array = malloc(sizeof(int) * x);
	while (tmp)
	{
		array[y] = tmp->n;
		y++;
		tmp = tmp->next;
	}
	y -= 1;
	for (z = 0; z < x / 2; z++, y--)
	{
		if (array[z] != array[y])
		{
			free(array);
			return (0);
		}
	}
	free(array);
	return (1);
}
int counter(listint_t *head)
{
	int x = 0;

	while (head)
	{
		x++;
		head = head->next;
	}
	return (x);
}
