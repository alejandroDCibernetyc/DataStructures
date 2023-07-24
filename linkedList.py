#Implemeting a Singly Linked List
#Class Node just need the value or element and the pointer to the "Next" node
class Node:
    __slots__ = 'element', 'next'
    def __init__(self, element, next):
        self.element = element
        self.next = next

#Class LinkedList is in charge to manage the nodes (connect nodes) in a list
class LinkedList:
    
    def __init__(self):
        '''Çreate an empty Linked List'''
        self.head = None        #reference to the head node
        self.size = 0           #number of list elements, initialize as empty 
    
    def __len__(self):
        '''Get th len of the list'''          
        return self.size
    
    def is_empty(self):
        '''Çheck if the list is empty'''
        return self.size == 0   #Return True if list is empty
    
    def __is_tail(self,node):
        '''check if the current node is the tail'''
        return node.next == None                   #Return True if it's the tail
    
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
        
    def __pop_unique_node(self):
        '''If want to remove the unique node of the list'''

        self.head =None                 #There is no head
        self.size = 0                   #No elements in th elist
        return
    
    def pop_head(self):
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
        
    def pop_tail(self):
        '''Remove the node tail of the list'''
        if self.is_empty():
            print("The list is empty, None nodes to remove")
        else:
            node_to_remove = self.head
            if self.size == 1:
                self.__pop_unique_node()
            else:
                ''''Traversing the list from hea to tail'''
                previous_node= self.head
                while(self.__is_tail(node_to_remove) == False):         #Searching the tail of the list
                    previous_node = node_to_remove                      #Previous node is the new Tail
                    node_to_remove = node_to_remove.next                #Pass to next node
                
                previous_node.next = None
                self.size -= 1

            return node_to_remove.element                               #Return the element removed from the list




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
            elif index == self.size-1:
                self.pop_tail()                 #Remove the tail
            else:
                '''Traversing the list to find and remove'''
                node_to_remove  = self.head                 #Point to the header
                previous_node = self.head
            
                for i in range(0,index):
                    previous_node = node_to_remove
                    node_to_remove = node_to_remove.next    #Point to next node

                self.__remove_node(previous_node, node_to_remove)
                return node_to_remove.element


    def __remove_node(self, previous_node, node_to_remove):
        '''Remove a node between 2 nodes'''
        previous_node.next = node_to_remove.next            #Previous node point to the next node of thenode that it is going to be removed
        self.size -= 1        
        return 

if __name__ == "__main__":
    myList = LinkedList()
    myList.push(5)
    myList.push(6)
    myList.push(7)
    myList.push(8)
    myList.pop_head()
    print(myList.top())
