my_list = [1,5,67,45,3,34]

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self):
        #prints out itself, although i was getting an error when i used .join so i did my own way
        node = self.head
        final_string = ""
        while node is not None:
            final_string+=str(node.data) + " -> "
            node = node.next
        final_string+="None"
        
        return final_string
    
    def __iter__(self):
        #makes the object iterable
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node):
        #set the current head to the next node
        node.next = self.head
        #now the head is open so set the passed in node as the head
        self.head = node

    def add_last(self, node):
        #if there is no head set the the passed in node as the head
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        #get to the last node and set its next node to the passed in node
        current_node.next = node

    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        for node in self:
            if node.data == target_node_data:
                #set the new nodes next node = to the next node of the target node
                new_node.next = node.next
                #set the target nodes next node = to the passed in node , which places it next in the list
                node.next = new_node
                return

        raise Exception("Node with data '%s' not found" % target_node_data)
    
    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                #once the target node is found, set the passed in node = previous nodes next node, and set the passed in nodes next node = the target node
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)
    
    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                #literally just forget about the target node by setting the previous nodes next node = to the target nodes next node, which just makes everthing forget about the target node
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)
    
    def print_list(self):
        for node in self:
            print(node.data, end=" -> ")


def swap(i,j, array):
    array[i],array[j] = array[j],array[i]
    
def bubbleSort(array):
    isSorted = False
    while not isSorted:
        isSorted = True
        for num in range(len(array) - 1):
            if array[num] > array[num + 1]:
                swap(num, num + 1, array)
                isSorted = False
    return array

def sort_list(*args, **kwargs):
    def inner(func):
        #sort list
        sorted_list = bubbleSort(kwargs['passed_list'])


        #run decorated function and pass in newly created and sorted list
        func(sorted_list)
    return inner

@sort_list(passed_list = my_list)
def convert_to_linked_list(a_list):
    #print(a_list)
    #take hypothetically sorted list and turn it into linked list
    newly_linked_list = LinkedList()
    for num in a_list:
        new_node = Node(num)
        newly_linked_list.add_last(new_node)
    print(newly_linked_list)


convert_to_linked_list



