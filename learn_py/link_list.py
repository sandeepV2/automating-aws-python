class Node:
    def __init__(self, item):
        self.data = item
        self.next = None


class Ll:
    def __init__(self):
        self.head = None
        self.count = 0

    def add_s(self, item):
        temp = Node(item)
        if self.head == None:
            self.head = temp
        else:
            temp.next = self.head
            self.head = temp

    def add_e(self, item):
        temp = Node(item)
        if self.head == None:
            self.head = temp
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = temp


    def show(self):
        cur = self.head
        self.count = 0
        while cur:
            print cur.data
            cur = cur.next
            self.count += 1


    def insert_pos(self, pos, item):
        temp = Node(item)

        idx = 0
        prev = self.head
        cur = self.head
        
        while cur:
            if pos == idx:
                prev.next = temp
                temp.next = cur
                return
            
            prev = cur
            cur = cur.next
            idx += 1



    

if __name__ == '__main__':
    llObj = Ll()
    llObj.add_e(1)
    llObj.add_e(2)
    llObj.add_e(3)
    llObj.add_e(4)
    llObj.show()
    print 'count %s'%llObj.count
    llObj.insert_pos(1, 'sfs')
    llObj.show()


