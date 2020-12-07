#include "lists.h"

/**
  * check_cycle - CHECK IF LOOP EXIST
  * @list: list head
  * Return: 0 if no loop, 1 if cycle exist
  **/

int check_cycle(listint_t *list)
{
	listint_t *var1 = list;
	listint_t *var2 = list;

	while (var2->next != NULL)
	{
		var1 = var1->next;
		var2 = var2->next;
		if (var2->next == NULL)
			return (0);
		var2 = var2->next;
		if (var2 == var1)
			return (1);
	}
	return (0);
}
