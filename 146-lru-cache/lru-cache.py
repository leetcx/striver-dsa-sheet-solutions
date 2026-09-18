class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
class LRUCache:
    

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            p=node.prev
            p.next=node.next
            node.next.prev=p
            m = self.tail.prev
            m.next = node
            node.prev = m
            node.next = self.tail
            self.tail.prev = node

            return node.value
        else:
            return -1

        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node=self.cache[key]
            node.value=value
            p=node.prev
            p.next=node.next
            node.next.prev=p

            m=self.tail.prev
            m.next=node
            node.prev=m
            node.next=self.tail
            self.tail.prev=node
        else:
            node=Node(key,value)
            if len(self.cache) < self.capacity:
                m=self.tail.prev
                m.next=node
                node.prev=m
                node.next=self.tail
                self.tail.prev=node
            else:
                z=self.head.next
                self.head.next=z.next
                z.next.prev=self.head
                m=self.tail.prev
                m.next=node
                node.prev=m
                node.next=self.tail
                self.tail.prev=node
                del self.cache[z.key]
            
            self.cache[key]=node




        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)