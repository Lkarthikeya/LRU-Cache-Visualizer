class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}

        # Dummy head and tail
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.hits = 0
        self.misses = 0
        self.logs = []

    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key not in self.map:
            self.misses += 1
            self.logs.insert(0, f"MISS: Key {key}")
            return None

        node = self.map[key]
        self.remove(node)
        self.insert(node)

        self.hits += 1
        self.logs.insert(0, f"HIT: Key {key}")

        return node.value

    def put(self, key, value):
        if key in self.map:
            self.remove(self.map[key])

        node = Node(key, value)
        self.insert(node)
        self.map[key] = node

        if len(self.map) > self.capacity:
            lru = self.tail.prev
            self.remove(lru)
            del self.map[lru.key]
            self.logs.insert(0, f"EVICTED: Key {lru.key}")

        self.logs.insert(0, f"ADDED: {key} → {value}")

    def get_cache(self):
        result = []
        curr = self.head.next
        while curr != self.tail:
            result.append(curr.key)
            curr = curr.next
        return result

    def stats(self):
        return {
            "hits": self.hits,
            "misses": self.misses,
            "size": len(self.map)
        }