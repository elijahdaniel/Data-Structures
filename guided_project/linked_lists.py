class Node:
    def __init__(self, value=None, text_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


# ll = Node(1)
# ll_2 = Node(2)
# ll_3 = Node(2)
# ll_4 = Node(2)
# ll.set_next(11_2
# ll_2.set_next(ll_3)
# ll_3.set_next(ll_4)

class LinkedList:
    def __init__(self):
        # first node in the list
        self.head = None

    def add_to_end(self, value):
        # regardless of if the list is empty or not, we need to wrap the value in a Node
        new_node = Node(value)

        # what if the list is empty?
        if not self.head:
            # set head to new_node
            self.head = new_node

        # what if the list isn't empty?
        else:
            # what node do we want to add the new node to?
            # the last node in the list
            # we can get to last node in list by traversing it
            current = self.head
            while current.get_next() is not None:
                current = current.get_next()

            # we're at the end of the linked list
            current.set_next(new_node)

    def remove_from_head(self):
        # what if list is empty?
        if not self.head:
            return None

        # what if it isn't empty?
        else:
            # we want to return the value at the current head
            value = self.head.get_value()
            # remove the value at the head
            # update self.head
            self.head = self.head.get_next()
            return value
