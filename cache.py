class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.order = []
        self.hits = 0
        self.misses = 0
        self.logs = []

    def get(self, key):
        if key not in self.cache:
            self.misses += 1
            self.logs.insert(0, f"MISS: Key {key} not found")
            return None

        self.order.remove(key)
        self.order.append(key)
        self.hits += 1
        self.logs.insert(0, f"HIT: Accessed key {key}")

        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.order.remove(key)

        elif len(self.cache) >= self.capacity:
            lru = self.order.pop(0)
            del self.cache[lru]
            self.logs.insert(0, f"EVICTED: Key {lru}")

        self.cache[key] = value
        self.order.append(key)
        self.logs.insert(0, f"ADDED: {key} → {value}")

    def get_cache(self):
        return list(reversed(self.order))  # MRU first

    def stats(self):
        return {
            "hits": self.hits,
            "misses": self.misses,
            "size": len(self.cache)
        }