class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self):
        data = int(input("Enter data you want to insert: "))
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head == None:
            print("Linked List is empty.")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '--->'
            itr = itr.next
        print(llstr)

    def insert_at_end(self, data = None):
        if data == None:
            data = int(input("Enter data you want to insert: "))
            if self.head==None:
                self.head = Node(data, None)
                return
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = Node(data, None)
        else:
            if self.head==None:
                self.head = Node(data, None)
                return
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = Node(data, None)
    
    def insert_values(self):
        data_list = input("Enter data (in list form) you want to insert: ").split()
        data_list = list(map(lambda x: int(x), data_list))
        self.head=None
        for data in data_list:
            self.insert_at_end(data)

    def get_count(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        return count
    
    def remove_at(self):
        index = int(input("Enter the index of the object to remove: "))
        if index<0 or index>=self.get_count():
            raise Exception("Invalid index")
        
        if index==0:
            self.head = self.head.next
            return
        
        itr = self.head
        count = 0
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                return
            count+=1
            itr = itr.next

    def insert_at(self):
        index = int(input("Enter the index you want to add data to: "))
        data = int(input("Enter the data you want to insert: "))
        if index<0 or index>self.get_count():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

if __name__ == '__main__':
    ll = LinkedList()
    while True:
        print("\nChoose option:")
        option = int(input("\n 1. Print linked list \n 2. Add object at the beginning \n 3. Add Object at the end \n 4.Add object at a specific index \n 5. Make a list linked list \n 6. Remove object at a specific index \n 7. Exit \n -> "))
        if option == 7:
            break
        option_dict = {1: ll.print, 2: ll.insert_at_beginning, 3: ll.insert_at_end, 4: ll.insert_at, 5: ll.insert_values, 6: ll.remove_at}
        option_dict[option]()