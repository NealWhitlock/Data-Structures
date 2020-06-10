"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    # Adds node to next
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    # Adds node to previous
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    # Gets rid of a node and reassigns pointers for 'adjacent' nodes
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        # Create new_node
        new_node = ListNode(value, None, None)

        # Check if DLL is empty
        # If empty assign head and tail for new_node
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node

        # If not empty replace head
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        # Check if head exists. If not, return None
        # if not self.head:   # This check is unneeded
        #     return None
        
        # Save current head value to return
        head_value = self.head.value
        
        # Check if head and tail are the same and set both to None if so
        # if self.head is self.tail:  # This check happens in DLL delete
        #     self.head = None
        #     self.tail = None

        # Delete current head
        self.delete(self.head)  # DLL delete

        return head_value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        # Create new_node
        new_node = ListNode(value, None, None)

        # Check if DLL is empty
        # If empty assign head and tail for new_node
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node

        # If not empty replace tail
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        # Check if tail exists. If not, return None
        # if not self.tail:
        #     return None
        
        # Save current tail value to return
        tail_value = self.tail.value
        
        # Check if head and tail are the same and set both to None if so
        # if self.head is self.tail:
        #     self.head = None
        #     self.tail = None

        # Delete current tail
        self.delete(self.tail)  # DLL delete

        return tail_value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        # Check if node already head
        # if node is self.head:
        #     return None
        
        # Save node's value
        node_value = node.value

        # Delete node
        self.delete(node)  # DLL delete

        # Move node to head position
        self.add_to_head(node_value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        # Check if node already tail
        # if node is self.tail:
        #     return None
        
        # Save node's value
        node_value = node.value

        # Delete node
        self.delete(node)  # DLL delete

        # Move node to tail position
        self.add_to_tail(node_value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        # Check if DLL is empty
        if not self.head and not self.tail:
            return
        # Check if only one element in DLL
        elif self.head is self.tail:
            self.head = None
            self.tail = None
        # Check if trying to delete head
        elif node is self.head:
            self.head = node.next
            node.delete()  # Node class delete
        # Check if trying to delete tail
        elif node is self.tail:
            self.tail = node.prev
            node.delete()  # Node class delete
        # All other instances of a node
        else:
            node.delete()  # Node class delete
        
        # Decrease length by one for the node being removed
        self.length -= 1
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        # If no head then there is no list
        if not self.head:
            return None

        # Get the head's value
        high_val = self.head.value
        # Get the head node as a whole
        current = self.head

        # Move through each node in turn
        while current:
            if current.value > high_val:  # Compare the new node's value to high
                high_val = current.value  # If new node's value higher,save it
            current = current.next  # Move to the next node

        return high_val                  

