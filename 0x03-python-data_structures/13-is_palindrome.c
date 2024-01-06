#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head; /* pointer to the middle node of the list */
	listint_t *fast = *head;/* pointer to the last node of the list */
	listint_t *second_half = NULL; /* pointer to the head of the second half */
	listint_t *mid = NULL; /* pointer to middle node of list if has odd length */
	bool res = false;/* boolean variable to store the result */

	/* Check if the list is empty or has only one node */
	if (*head == NULL || (*head)->next == NULL)
		return (1);/* return 1 as an empty list or a single node is a palindrome */

	/* Use a slow and a fast pointer to find the middle of the list */
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next; /* move the fast pointer two nodes ahead */
		slow = slow->next; /* move the slow pointer one node ahead */
	}

	if (fast != NULL) /* Check if the list has odd length */
	{
		mid = slow; /* save the middle node */
		slow = slow->next;/* move the slow pointer to the next node */
	}

	second_half = slow;/* Save the head of the second half of the list */
	reverse_listint(&second_half);/* Rev 2nd half of list using other function */
	/* Compare 1st and 2nd half of list using other function */
	res = compare_lists(*head, second_half);
	/* Restore the original list by reversing the second half again */
	reverse_listint(&second_half);

	/* Reattach the middle node if the list has odd length */
	if (mid != NULL)
	{
		mid->next = second_half;
	}
	else /* Otherwise, update the head pointer to the second half */
	{
		*head = second_half;
	}
	return (res); /* Return the result as an int */
}

/**
 * reverse_listint - reverses a linked list and returns the new head
 * @head: pointer to the head of the linked list
 * Return: pointer to the new head of the reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *prev = NULL; /* pointer to the previous node */
	listint_t *curr = *head; /* pointer to the current node */
	listint_t *next = NULL; /* pointer to the next node */

	while (curr != NULL) /* loop until the end of the list */
	{
		next = curr->next; /* save the next node */
		curr->next = prev; /* make the current node point to the previous node */
		prev = curr; /* move the previous node to the current node */
		curr = next; /* move the current node to the next node */
	}
	*head = prev; /* update the head pointer to the last node */
	return (*head); /* return the new head */
}

/**
 * compare_lists - compares two linked lists and returns true if they are equal
 * @head1: pointer to the head of the first linked list
 * @head2: pointer to the head of the second linked list
 * Return: true if the lists are equal, false otherwise
 */
bool compare_lists(listint_t *head1, listint_t *head2)
{
	while (head1 != NULL && head2 != NULL) /* loop until one of the lists ends */
	{
	if (head1->n != head2->n) /* compare the data of the nodes */
		return (false); /* return false if they are different */
		head1 = head1->next; /* move to the next node in the first list */
		head2 = head2->next; /* move to the next node in the second list */
	}
	/* check if both lists have reached the end */
	if (head1 == NULL && head2 == NULL)
		return (true); /* return true if they are equal */
	return (false); /* return false if one list is longer than the other */
}
