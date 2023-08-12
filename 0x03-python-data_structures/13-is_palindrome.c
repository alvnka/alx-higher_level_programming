#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - checks if a list reads the same forward as backwards
 * @head: beginning of the list
 * Return: 1 if palindrome 0 if not palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *current_node = *head;
	int count = 0, index = 0, check = 0;

	if (current_node == NULL)
	{
		return (1);
	}
	else
	{
		while (current_node->next != NULL)
		{
			count++;
			current_node = current_node->next;
		}

		int list_numbers[count];

		current_node = *head;

		while (current_node != NULL)
		{
			list_numbers[index] = current_node->n;
			index++;
			current_node = current_node->next;
		}


		while (check < count / 2)
		{
			if (list_numbers[check] != list_numbers[count - check])
			{
				return (0);
			}
			check++;
		}
		return (1);
	}
}
