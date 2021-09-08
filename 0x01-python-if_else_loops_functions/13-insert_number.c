#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: Pointer to a pointer that points to a singly linked list
 * @number: Integer in a node
 *
 * Return: Address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current_node = *head;
	listint_t *previous_node = *head;
	listint_t *new_node = (listint_t *)malloc(sizeof(listint_t));

	if (new_node == NULL)
	{
		free(new_node);
		return (NULL);
	}
	new_node->n = number;
	if (head == NULL)
	{
		*head = new_node;
		new_node->next = NULL;
		return (new_node);
	}
	if (number < current_node->n)
	{
		new_node->next = current_node;
		*head = new_node;
		return (new_node);
	}
	while (current_node->n <= number && current_node->next != NULL)
	{
		previous_node = current_node;
		current_node = previous_node->next;
	}
	if (current_node->next == NULL)
	{
		current_node->next = new_node;
		new_node->next = NULL;
		return (new_node);
	}
	new_node->next = previous_node->next;
	previous_node->next = new_node;
	current_node = NULL;
	previous_node = NULL;
	return (new_node);
}
