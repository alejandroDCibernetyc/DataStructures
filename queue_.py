#Implemeting a Queue
#Class Node just need the value or element and the pointer to the "Next" node
class Node:
    __slots__ = 'element', 'next'
    def __init__(self, element, next):
        self.element = element
        self.next = next

#Class Queuet is in charge to manage the nodes (connect nodes) in a list as FIFO
class Queue:
    
    def __init__(self):
        '''Çreate an empty Linked List'''
        self.head = None        #reference to the head node
        self.tail = None
        self.size = 0           #number of list elements, initialize as empty 
    
    def _len(self):
        '''Get th len of the list'''          
        return self.size
    
    def is_empty(self):
        '''Çheck if the list is empty'''
        return self.size == 0   #Return True if list is empty
        

    def top(self):
        '''Consult the head element (not remove), the forn of the line'''
        if self.is_empty():
            print("The Queue is empty, theres no head")
        else:
            return self.head.element    #Return the head element
        
    def back(self):
        '''Consult the last element of the Queue'''
        if self.is_empty():
            print("The Queue is empty")
        else:
            return self.tail.element
        
    def __pop_unique_node(self):
        '''If want to remove the unique node of the list'''

        self.head =None                 #There is no head
        self.size = 0                   #No elements in th elist
        return
    
    def dequeue(self):
        ''''Remove and return the element in the head'''
        if self.is_empty():
            print("The list is empty, None nodes to remove")
        else:
            nodePoped = self.head                   #Save tha node poped
            if self.size == 1:
                
                self.__pop_unique_node()
            else:
           
                self.head = nodePoped.next          #Declare the new head of the list
                nodePoped.next = None               #Delete the pointer "next" of the nodePoped
                self.size -= 1
            return nodePoped.element            #Return the element of the node poped
        
    def enqueue(self, element):
        '''Add node in the tail'''
        if self.is_empty():
            self.head = Node(element, self.head)        #Declare new node as Head
            self.tail = self.head
            self.size += 1                              #Increase the list size
        else:
            old_tail = self.tail                            #Save the old tail
            new_tail = Node(element, None)                 #Instance of new tail node
            old_tail.next = new_tail                       #Connecting old tail to new tail
            self.tail = new_tail                                #Declaring he new_tail as tail
            self.size += 1


    def show_queue(self):
        '''Method to show the hole linked list,
        consider that we just can se the output if the node.element == float, int , bolean or str
        if its node.element ==  object the output maybe doesn't look great, you may have to make some adjusment to this method
        '''
        current_node = self.head
        print(f"\n[First position]→", end=' ')
        if self.size > 0:
            print(f"[{current_node.element}]", end='')
            for i in range(0, self.size-1):
                current_node = current_node.next
                print(f"---[{current_node.element}]", end='')
        
        print(f"← [Last element]", end=' ')
        return
if __name__ == "__main__":
    myQueue = Queue()
    myQueue.show_queue()
    #Adding elements to the queue
    for i in range(0,5):
        myQueue.enqueue(i)
        myQueue.show_queue()
        print(f"Queue size: {myQueue._len()}")
    #Removing element of the Queue
    for i in range(0,5):
        myQueue.dequeue()
        myQueue.show_queue()
        print(f"Queue size: {myQueue._len()}")
