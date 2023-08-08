#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: first node
 * @number: number to be added
 * Return: address of the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current_node = *head, *prev_node = NULL;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	while (current_node != NULL && current_node->n < new_node->n)
	{
		prev_node = current_node;
		current_node = current_node->next;
	}

	if (prev_node == NULL)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		prev_node->next = new_node;
		new_node->next = current_node;
	}
	return (new_node);
}
