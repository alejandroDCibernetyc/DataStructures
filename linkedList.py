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
    
    def _len(self):
        '''Get th len of the list'''          
        return self.size
    
    def is_empty(self):
        '''Çheck if the list is empty'''
        return self.size == 0   #Return True if list is empty
    
    def __is_tail(self,node):
        '''check if the current node is the tail'''
        return node.next == None                   #Return True if it's the tail
    
    def push_head(self, element):
        '''Add element to the top (in the head) of the list'''
        self.head = Node(element, self.head)        #Declare new node as Head
        self.size += 1                              #Increase the list size
        return

    def push_tail(self, element):
        '''Add node in the tail'''
        if self.is_empty():
            self.push_head(element)
        else:
            old_tail = self.head                            #Start our pointer
            new_tail = Node(element, None)                        #Instance of new node
            while (self.__is_tail(old_tail) == False):       #Traversing the list fromo head to tail
                old_tail = old_tail.next                    #Next node
            old_tail.next = new_tail                        #Adding next node to the old tail
            new_tail.next = None                            #Declaring he new_tail as tail
            self.size += 1
        
    def add_node(self, element, index):
        '''Adding a node in the index specifies
        this methos no overwrite the node with the same index,
        it add a node between nodes if its necesary 
        '''
        if index == 0:
            self.push_head(element)
        elif index == self.size -1:
            self.push_tail(element)
        elif index < 0 or index > self.size-1 :
            print(f"Index out of range, try with vailable index\nThe actua list have {self.size} nodes")
        else:
            previous_node= None                         #Initialice thevariable to save previous node
            node_to_move = self.head                    #Start out pointer in the head
                                                        #Instance of new node
            for i in range(0 , index):                  #Trversing the listo from head to index
                previous_node = node_to_move            #Saving the previous node
                node_to_move = node_to_move.next        #moving to the next node    
            
            new_node = Node(element, node_to_move)      #Thenew node points to the node that have mo ve to make to add itself
            previous_node.next = new_node               #previous node point to the new node
            self.size += 1

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
    

    def show_list(self):
        '''Method to show the hole linked list,
        consider that we just can se the output if the node.element == float, int , bolean or str
        if its node.element ==  object the output maybe doesn't look great, you may have to make some adjusment to this method
        '''
        current_node = self.head
        print(f"\n[Head]→", end=' ')
        if self.size > 0:
            print(f"[{current_node.element}]--->", end=' ')
            for i in range(0, self.size-1):
                current_node = current_node.next
                print(f"[{current_node.element}]--->", end=' ')
        
        print(f"[None]  [Tail]", end=' ')
        return



if __name__ == "__main__":

    #Execution example
    myList = LinkedList()
    #Trying adding- push methods
    myList.push_head(5)
    myList.push_head(6)
    myList.push_head(7)
    myList.push_head(8)
    myList.show_list()

    myList.push_tail(4)
    myList.push_tail(3)
    myList.show_list()
    
    myList.push_tail(3)
    myList.push_tail(3)
    myList.show_list()
    
    myList.add_node(2,6)
    myList.add_node(1,7)
    myList.show_list()
    print(f"\nList Size: {myList._len()}")
    #Trying pop methods
    myList.pop_head()
    myList.show_list()
    print(f"\nList Size: {myList._len()}")
    myList.remove(7)        #Removing node in index 7
    myList.show_list()
    print(f"\nList Size: {myList._len()}")
    myList.pop_tail()
    myList.show_list()
    print(f"\nList Size: {myList._len()}")
    for i in range(0, myList._len()):               #Removin all elements
        myList.pop_head()
        myList.show_list()
        print(f"\nList Size: {myList._len()}")

    #Trying to remove
    myList.pop_head()       #Removing from the head
    myList.pop_tail()       #Removing from the tail, but the list is empty
    print(f"\nList Size: {myList._len()}")