#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
"""
So the idea is this:
1. Use a doubly linked list to store the key-value pairs
2. Use a hash map to store the key-node pairs
3. When a node is accessed, move it to the head of the linked list
4. When a node is added, add it to the head of the linked list
5. When a node is removed, remove it from the tail of the linked list
Generate a solution based on the above idea
"""
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev, self.next = None, None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head

    def get(self, key: int) -> int:
        if key in self.hashmap:
            node = self.hashmap[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self._remove(self.hashmap[key])
        node = Node(key, value)
        self._add(node)
        self.hashmap[key] = node
        if len(self.hashmap) > self.capacity:
            node = self.tail.prev
            self._remove(node)
            del self.hashmap[node.key]
            
    def _remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def _add(self, node):
        head_next = self.head.next
        self.head.next, head_next.prev = node, node
        node.prev, node.next = self.head, head_next
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

