#include "lists.h"

/**
 * check_cycle - checks fi a linked list has a cycle in it
 * @list: list to be checked
 * Return: 1 if list has a cycle and 0 if it doesn't
 */

int check_cycle(listint_t *list)
{
  listint_t *move_once = list;
  listint_t *move_twice = list;

  if (!list)
  {
    return (0);
  }
  while (move_once && move_twice && move_twice->next)
  {
    move_once = move_once->next;
    move_twice = move_twice->next->next;
    if (move_once == move_twice)
    {
      return (1);
    }
  }
  return (0);
}