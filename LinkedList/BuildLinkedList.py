class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def insertAtBegnning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    

    def insertAtEnd(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next 

        temp.next = new_node
    
    
    def insertAtPos(self,pos,data):

        if pos < 0:
            print("Cannot insert at -ve position")
            return
        
        new_node = Node(data)

        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        curr_pointer = self.head
        curr_pos = 0

        while curr_pointer is not None and curr_pos < pos - 1:
            curr_pointer = curr_pointer.next
            curr_pos += 1

        # If curr_pointer is None, the position is out of bounds
        if curr_pointer is None:
            print("Position out of bounds")
            return
        
        # Insert the new node at the desired position
        new_node.next = curr_pointer.next
        curr_pointer.next = new_node


    def deleteNode(self,data):

        temp = self.head
        if temp is not None:
            if temp.data == data:
                self.head = temp.next
                temp = None
                return

        while temp is not None:
            if temp.data == data:
                break
           
            prev = temp
            temp = temp.next
        
        if temp is None:
            return

        prev.next = temp.next
        temp = None

    
    def print_list(self):
        temp = self.head

        if temp is None:
            print("List is Empty")
        
        while temp:
            print(temp.data,end= " ")
            temp = temp.next


if __name__ == "__main__":
    llist = LinkedList()
    
    llist.insertAtEnd(1)
    llist.insertAtBegnning(2)
    llist.insertAtBegnning(3)
    llist.insertAtEnd(4)
    llist.insertAtPos(4,21)
    
    print("Linked list before insertion:")
    llist.print_list()  

    llist.insertAtPos(2, 9)
    print("Linked list after insertion at position 2:")
    llist.print_list() 

    llist.deleteNode(3)
    print("Linked list after deletion of 3:")
    llist.print_list()  