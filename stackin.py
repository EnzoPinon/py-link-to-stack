class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail= None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail=new_node


    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.tail = new_node
            self.head=new_node

    def printLinkedList(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

class Stack:
    def __init__(self):
        self.top =None

    def push(self,data):
        new_node=Node(data)
        if self.top:            
            new_node.next=self.top
        self.top=new_node
    
    def pop(self):
        if self.top is None:
            return  None
        else: 
            popped_node = self.top 
            self.top = self.top.next
            popped_node.next=None
            return popped_node.data
    def peek(self):
        if self.top:
            return self.top.data 
        else:
            return None
        
    def is_empty(self):
        return self.top is None
    
    def print_stack(self):
        current_node=self.top
        while current_node:
            print(current_node.data)
            current_node=current_node.next
        # print("None")

    def size(self):
        current_node=self.top
        count=0
        while current_node:
            count+=1
            current_node=current_node.next
        return count

list_01 = LinkedList()
list_02 = LinkedList()
temporary = Stack()
final = Stack()
second_holder = Stack()

# Create List 1

list_01.insert_at_beginning(1)
list_01.insert_at_end(2)
list_01.insert_at_end(4)
list_01.printLinkedList()

# Create List 2

list_02.insert_at_beginning(1)
list_02.insert_at_end(3)
list_02.insert_at_end(4)
list_02.printLinkedList()

# Start a counter

num_counter = 0

while num_counter != 3:
    current_node_1 = list_01.head
    current_node_2 = list_02.head
    if current_node_1 == list_01.head and current_node_2 == list_02.head:

        num01 = current_node_1.data
        num02 = current_node_2.data
        
        if num01 > num02 or num01 == num02:
            final.push(num01)
            final.push(num02)
        else:
            final.push(num01)
            final.push(num02)
            
    else:

        num01 = current_node_1.data
        num02 = current_node_2.data
        print(num01)
        print(num02)
        
        if num01:
            check_size_01 = final.size()

            if check_size_01 != 0:
                while check_size_01 != 0:
                    original = final.pop()
                    if num01 > original:
                        second_holder.push(original)
                        check_size_01 -= 1
                    else:
                        temporary.push(num01)
                        break
            
            temp_size = temporary.size()
            second_temp_size = second_holder.size()

            # Second holder holds all numbers less than the number
            # Temporary holds all numbers greater than

            while second_temp_size != 0:
                number = second_holder.pop()
                final.push(number)
                second_temp_size -=1

            while temp_size != 0:
                secnum = temporary.pop()
                final.push(secnum)
                temp_size -=1
        
        if num02:
            check_size_01 = final.size()

            if check_size_01 != 0:
                while check_size_01 != 0:
                    original = final.pop()
                    if num02 > original:
                        second_holder.push(original)
                        check_size_01 -= 1
                    else:
                        temporary.push(num01)
                        break
            
            temp_size = temporary.size()
            second_temp_size = second_holder.size()

            # Second holder holds all numbers less than the number
            # Temporary holds all numbers greater than

            while second_temp_size != 0:
                number = second_holder.pop()
                final.push(number)
                second_temp_size -=1

            while temp_size != 0:
                secnum = temporary.pop()
                final.push(secnum)
                temp_size -=1

    list_01.head = current_node_1.next
    list_02.head = current_node_2.next
    current_node_1.next = None
    current_node_2.next = None
    num_counter +=1

# At the end of the Loop, we now have a stack but it is in decreasing order. We want in a NON-decreasing order.

final.print_stack()
        
# Making a final stack called OutPut

output = Stack()

final_size = final.size()

while final_size != 0:
    orig = final.pop()
    output.push(orig)
    final_size -=1

output.print_stack()

                    
                    



