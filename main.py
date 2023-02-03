# Singly linked list

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def insert_back(self, data):
        '''Inserts elements at the end of the linked list'''
        newNode = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
        else:
            self.head = newNode
        self.count += 1

    def insert_front(self, data):
        '''Inserts elements into the linked list from the front'''
        newNode = Node(data)
        if self.head:
            temp = self.head
            self.head = newNode
            newNode.next = temp
        else:
            self.head = newNode
        self.count += 1

    def insert_at(self, data, index):
        '''Inserts elements into the linked list at a specific index'''
        newNode = Node(data)
        current = self.head
        if self.count >= index:
            for i in range(0, index - 2):  # -2 to offset starting from 0 and to land on the previous node
                current = current.next

        temp = current.next
        current.next = newNode
        newNode.next = temp
        self.count += 1

    def delete_value(self, data):
        '''Deletes a specific value in the linked list'''
        if self.count >= 1:
            current = self.head
            # If the list has one element and it matches.
            if self.count == 1 and current.value == data:
                self.head = None
                self.count -= 1
            else:
                next = current.next
                while next:
                    if next.value == data:
                        current.next = next.next
                        self.count -= 1
                    current = next
                    next = next.next
        else:
            print('The list is empty. No values were deleted')

    def delete_index(self, index):
        '''Deletes the item at the given index'''
        if self.count >= 1:
            if self.count >= index:
                current = self.head
                if index == 0:
                    self.head = current.next
                    self.count -= 1
                else:
                    for i in range(0, index - 1):
                        current = current.next
                    current.next = current.next.next
                    self.count -= 1
            else:
                print(f'Index provided is outside of the boundary of the list. It contains {self.count} elements')
        else:
            print('The list is empty. No values were deleted')

    def print(self):
        '''Prints the linked list'''
        current = self.head
        while current:
            print(current.value)
            current = current.next


def reverse_list(list):
    '''Returns a copy of the given linked list but in reverse'''
    new_list = LinkedList()
    current = list.head
    if list.count > 1:
        while current:
            new_list.insert_front(current.value)
            current = current.next
    else:
        return list
    return new_list


__name__ = "__main__"

# Testing values
list = LinkedList()
list.insert_back(3)
list.insert_back(5)
list.insert_back(7)
list.insert_front(1)
list.insert_front(13)
list.insert_back(6)
list.insert_at(55, 2)
list.insert_at(10, 4)
list.delete_value(7)
list.delete_index(0)
list.print()
print()
n_list = reverse_list(list)
n_list.print()
