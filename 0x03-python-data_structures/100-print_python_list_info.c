#include "lists.h"

/**
 * is_palindrome - tests if linked lists is palindrome
 * @head: address of pointer to list
 * Return: 1 is palindrome else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *node, *prev;
	int failed = 0;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
	}
	node = slow;
	prev = NULL;
	while (node)
	{
		fast = node->next;
		node->next = prev;
		prev = node;
		node = fast;
	}
	fast = *head;
	node = prev;
	while (prev)
	{
		if (fast->n != prev->n)
		{
			failed = 1;
			break;
		}
		fast = fast->next;
		prev = prev->next;
	}
	prev = NULL;
	while (node)
	{
		fast = node->next;
		node->next = prev;
		prev = node;
		node = fast;
	}
	return (!failed);
}

void switch_values(int *a, int *b)
{
	*a ^= *b;
	*b ^= *a;
	*a ^= *b;
}

int main(void)
{
	int a = 89;
	int b = 10;

	/* Insert your code here */
	switch_values(&a, &b);

	printf("a=%d - b=%d\n", a, b);

	return 0;
}