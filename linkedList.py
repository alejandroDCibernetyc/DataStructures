#Implemeting a Singly Linked List
#Class Node just ned the value or element and the pointer to the "Next" node
class Node:
    __slots__ = 'element', 'next'
    def __init__(self, element, next):
        self.element = element
        self.next = next

#Class LinkedList is in charge to manage the nodes (connect nodes) in a list
class LinkedList:
    
    def __init__(self):
        '''Çreate an empty Linked List'''
        self.head = None        #reference to the head node, 
        self.size = 0           #number of list elements, initialize as empty 
    
    def __len__(self):          #Method to get the len of the linked list
        return self.size
    
    def is_empty(self):
        return self.size == 0   #Return True if list is empty
    
    def is_tail(self,node):
        '''check if the current node is the tail'''
        return node.next == None                   #Return True if is the tail
    
    def push(self, element):
        '''Add element to the top (in the head) of the list'''
        self.head = Node(element, self.head)        #Declare new node as Head
        self.size += 1                              #Increase the list size
    
    def top(self):
        '''Consult the head element (not remove)'''
        if self.is_empty():
            print("The list is empty, theres no head")
        else:
            return self.head.element    #Return the head element
        
    def pop_head(self):
        ''''Remove and return the element in the head'''
        if self.is_empty():
            print("The list is empty, None nodes to remove")
        else:
            nodePoped = self.head               #Save tha node poped
            self.head = nodePoped.next          #Declare the new head of the list
            nodePoped.next = None               #Delete the pointer "next" of the nodePoped
            self.size -= 1
            return nodePoped.element            #Return the element of the node poped
    def pop_tail(self):
        pass

    def remove(self, index):
        '''Remove specific position of the node
        index will be the same as normal Array in
        python (starting from 0)
        '''
        if self.is_empty():
            print("The list is empty, no nodes to remove")
        elif index > self.size -1:
            print("Index out of range")
        else:
            if index == 0:
                self.pop_head()                 #Remove the had
            else:
                '''Traversing the list to find and remove'''
                node_to_remove  = self.head
                for i in range(0,index):
                    node_to_remove = node_to_remove.next
                    self.__remove_node(node_to_remove)


    def __remove_node(self, node_to_remove):
        pass
        



