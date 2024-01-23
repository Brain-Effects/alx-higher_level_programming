#!/usr/bin/python3


class Node:
    """
    This is the Node class.

    The purpose of this class is to define a node for a singly linked list.
    """

    def __init__(self, data, next_node=None):
        """
        This is the constructor method for the Node class.

        It initializes a Node instance with a given data and next_node.
        The data must be an integer. The next_node can be None or a Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        This is the getter method for the data attribute.

        It returns the data of the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        This is the setter method for the data attribute.

        It sets the data of the node to a given value.
        The value must be an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        This is the getter method for the next_node attribute.

        It returns the next_node of the node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        This is the setter method for the next_node attribute.

        It sets the next_node of the node to a given value.
        The value can be None or a Node.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    This is the SinglyLinkedList class.

    The purpose of this class is to define a singly linked list.
    """

    def __init__(self):
        """
        This is the constructor method for the SinglyLinkedList class.

        It initializes a SinglyLinkedList instance with a head set to None.
        """
        self.__head = None

    def __str__(self):
        """
        This method returns a string representation of the singly linked list.

        It prints the entire list in stdout, one node number by line.
        """
        node = self.__head
        result = []
        while node is not None:
            result.append(str(node.data))
            node = node.next_node
        return "\n".join(result)

    def sorted_insert(self, value):
        """
        This method inserts a new Node into the correct sorted position in
        the list (increasing order).
        """
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            node = self.__head
            while node.next_node is not None and node.next_node.data < value:
                node = node.next_node
            new_node.next_node = node.next_node
            node.next_node = new_node
