#Implementing a Stack with a  linked list
#Class Node just need the value or element and the pointer to the "Next" node
class Node:
    __slots__ = 'element', 'next'
    def __init__(self, element, next):
        self.element = element
        self.next = next

#Class LinkedList is in charge to manage the nodes (connect nodes) in a list
class Stack:
    
    def __init__(self):
        '''Çreate an empty Linked List'''
        self.head = None        #reference to the head node
        self.size = 0           #number of list elements, initialize as empty 
    
    def _len(self):
        '''Get th len of the list'''          
        return self.size
    
    def is_empty(self):
        '''Çheck if the list is empty'''
        return self.size == 0   #Return True if list is empty
    
    
    def push(self, element):
        '''Add element to the top (in the head) of the list'''
        self.head = Node(element, self.head)        #Declare new node as Head
        self.size += 1                              #Increase the list size
        return


    def top(self):
        '''Consult the head element (not remove)'''
        if self.is_empty():
            print("The list is empty, theres no head")
        else:
            return self.head.element    #Return the head element
    
    
    def pop(self):
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
    
    def __pop_unique_node(self):
        '''If want to remove the unique node of the list'''

        self.head =None                 #There is no head
        self.size = 0                   #No elements in th elist
        return
    

    def show_list(self):
        '''Method to show the hole linked list,
        consider that we just can se the output if the node.element == float, int , bolean or str
        if its node.element ==  object the output maybe doesn't look great, you may have to make some adjusment to this method
        '''
        current_node = self.head
        print(f"\n[Head]\n   ↓")
        if self.size > 0:
            print(f"[{current_node.element}]\n   ↓", )
            for i in range(0, self.size-1):
                current_node = current_node.next
                print(f"[{current_node.element}]\n   ↓")
        
        print(f"[None]\n  ↑\n[Tail]")
        return

if __name__ == "__main__":
    pass