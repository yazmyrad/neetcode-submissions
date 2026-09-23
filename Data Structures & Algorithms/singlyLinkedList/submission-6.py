class Node:
    def __init__(self, val = 0):
        self.next = None
        self.val = val

class LinkedList:
    
    def __init__(self):
        self.node = Node()
        self.length = 0
    
    def get(self, index: int) -> int:
        if self.length == 0:
            return -1 
        temp = self.node
        while temp and index > 0:
            temp = temp.next
            index -= 1

        if index == 0 and temp != None:
            return temp.val
        return -1

    def insertHead(self, val: int) -> None:
        if self.length != 0:
            newnode = Node(val)
            newnode.next = self.node
            self.node = newnode      
            self.length += 1
        else:
            self.node = Node(val)  
            self.length += 1

    def insertTail(self, val: int) -> None:
        if self.length == 0:
            self.insertHead(val)
            self.length += 1
            return
        temp = self.node
        while self.node.next:
            self.node = self.node.next
        self.node.next = Node(val)
        self.node = temp
        self.length += 1

    def remove(self, index: int) -> bool:
        print(self.getValues())
        if index == 0:
            if self.length:
                self.node = self.node.next
                self.length -= 1
                return True
            return False
        else:
            prev = self.node
            next = self.node.next
            index -= 1
            while next and index > 0:
                prev = next
                next = next.next
                index -= 1
            if next == None and index >= 0:
                return False
            prev.next = next.next
            self.length -= 1
            return True

    def getValues(self) -> List[int]:
        temp = self.node
        arr = []
        while temp:
            arr.append(temp.val)
            temp = temp.next
        return arr if self.length else []
