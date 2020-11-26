class Node :
    def __init__(self, data=None, next=None) :
        self.data = data
        self.next = next

class LinkedList :
    def __init__(self) :
        self.head = None

    def insert_at_beginning(self, data) :
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data) :
        if self.head is None :
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next :
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list):

        for data in data_list :
            self.insert_at_end(data)    

    def get_length(self) :
        itr = self.head
        cnt = 0
        while itr :
            cnt+=1
            itr = itr.next

        return cnt

    def remove_at(self, idx) :
        if idx < 0 or idx > self.get_length()-1 :
            raise IndexError("Invalid index")

        if idx == 0 :
            self.head = self.head.next
            return

        itr = self.head
        prev = None

        for i in range(idx) :
            prev = itr
            itr = itr.next

        prev.next = itr.next
  
            
    def insert_at(self, idx, data) :
        if idx < 0 or idx > self.get_length() - 1 :
            raise IndexError("Invalid index [" + str(idx) + "]")    

        if idx == 0 :
            self.insert_at_beginning(data)
            return

        itr = self.head
        cnt = 0
        while iter :
            if cnt == idx - 1 :
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            cnt += 1
            
    def insert_after_value(self, data_after, data_to_insert) :
        # Search for first occurance of data_after value in linked list
        # Now insert data_to_insert after data_after node

        itr = self.head

        while itr and itr.data != data_after :
            itr = itr.next

        if itr :
            node = Node(data_to_insert, itr.next)
            itr.next = node
        else :
            raise Exception("No such a data[" + str(data_after)+"]")

    def remove_by_value(self, data):
        # Remove first node that contains data   
        if self.head is None :
            raise Exception("No such a data[" + str(data)+"]")

        if  self.head.data == data :
            self.head = self.head.next
            return

        itr = self.head

        while itr.next and itr.next.data != data :
            itr = itr.next
        
        if itr.next is None :
            raise Exception("No such a data[" + str(data)+"]")

        itr.next = itr.next.next
    

    def __str__(self) :
        if self.head is None :
            return 'Empty'
        
        itr = self.head
        to_string = ''
        while itr :
            to_string = to_string + str(itr.data) + "->"
            itr = itr.next
        to_string += 'nil'

        return to_string

if __name__ == '__main__' :
   linked_list = LinkedList()

   linked_list.insert_at_beginning(5)
   linked_list.insert_at_beginning(90)
   linked_list.insert_at_end(99)
   linked_list.insert_at_end(100)
   linked_list.insert_values([45, 78, 32, 56, 97, 77, 32])
   print(linked_list)
   linked_list.remove_at(10)
   print(linked_list)
   linked_list.insert_at(4, 200)
   print(linked_list)  
   linked_list.insert_after_value(100, 150)
   print(linked_list)  
   linked_list.remove_by_value(200)
   print(linked_list)  
   print('length:', linked_list.get_length())
#    linked_list.remove_at(20)
