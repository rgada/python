class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class linked_list():
    def __init__(self):
        self.start = None
        self.end = None
        self.count = 0

    def insert_at_beigging(self,data):
        node = Node(data)
        if self.start is None:
            self.start = node
            self.end = node
        else:
            node.next = self.start
            self.start.prev = node
            self.start = node
        self.count += 1

    def push(self,data):
        node = Node(data)
        if self.start is None:
            self.start = node
            self.end = node
        else:
            node.prev = self.end
            self.end.next = node
            self.end = node
        self.count += 1

    def pop(self):
        try:
            data = self.end.data
            self.end = self.end.prev
            self.end.next = None
            self.count -= 1
            return data
        except:
            print("Linked list is empty")

    def get_node_at_index(self,index=None):
        if index is None or index < 0 or index > self.count-1:
            raise IndexError("linked list index out of range")

        i = 0
        head = self.start
        while i != index:
            head = head.next
            i += 1
        return head

    def insert(self,data,index):
        if index > self.count:
            self.push(data)
        elif index <= 0:
            self.insert_at_beigging(data)
        else:
            node = Node(data)
            try:
                head = self.get_node_at_index(index)
                head.prev.next = node
                node.prev = head.prev
                node.next = head
                head.prev = node
            except IndexError as e:
                print(e)

    def delete(self,index):
        try:
            head = self.get_node_at_index(index)
            head.prev.next = head.next
            head.next.prev = head.prev
        except IndexError as e:
            print(e)

    def __len__(self):
        return self.count

    def reverse(self):
        if self.start is None:
            print("Empty linked list")
        head = self.end
        while head is not None:
            print(f"{head.data} ", end="")
            head = head.prev
        print()

    def print(self):
        if self.start is None:
            print("Empty linked list")
        head = self.start
        while head is not None:
            print(f"{head.data} ", end="")
            head = head.next
        print()

    """
    def append(self,data):
        node = Node(data,self.start,self.end)
        if self.start is None:
            self.start = node
        self.end = node
    """

if __name__ == "__main__":
    ll = linked_list()

    #for i in range(10):
    #    ll.push(i)

    ll.print()
    ll.insert(100,2)
    ll.print()
    ll.reverse()

    ll.delete(2)
    ll.print()
    ll.reverse()