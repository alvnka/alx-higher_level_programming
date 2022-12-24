#include "lists.h"
/**
 * insert_node - function that inserts
 * a node into a sorted singly linked list
 * @head: holds the address to the head
 * @number: holds the number to be added
 * Return: address to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prev, *new, *current;

	new = malloc(sizeof(listint_t));
	new->n = number;

	current = *head;
	prev = NULL;
	while (current != NULL && current->n < number)
	{
		prev = current;
		current = current->next;
	}
	new->next = current;
	if (prev != NULL)
	{
		prev->next = new;
	}
	else
	{
		*head = new;
	}
	return (new);
}
