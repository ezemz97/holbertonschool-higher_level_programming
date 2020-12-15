#include "lists.h"
/**
 * is_palindrome - Check if linked list is palindrome or not
 * @head: head pointer
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	int x = 0, y = 0, z = 0, *array;
	listint_t *tmp = *head/*, *count = *head*/;

	if (!head)
		return (1);
	/*while (count)
	{
		x++;
		count = count->next;
	}*/
	array = malloc(sizeof(int) * 20);
	while (tmp)
	{
		x++;
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
