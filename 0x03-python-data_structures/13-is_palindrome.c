#include "lists.h"

/**
 * is_palindrome - this function checks whether a given string is palindrome
 * @head: a pointer to the start of the list
 * Return: if its a palidrome it is 1, if not it is 0
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (check_pal(head, *head));
}

/**
 * check_pal - function to check if the supplied list is palidrome
 * @head: pointer to where the list begins  to the beginning of the list
 * @last: pointer to where the list ends
 * Return: if its a palidrome it is 1, if not it is 0
 */
int check_pal(listint_t **head, listint_t *last)
{
	if (last == NULL)
		return (1);
	if (check_pal(head, last->next) && (*head)->n == last->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
