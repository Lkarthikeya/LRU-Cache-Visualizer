from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def _add(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1

    def put(self, key, value):
        if key in self.cache:
            self._remove(self.cache[key])

        node = Node(key, value)
        self._add(node)
        self.cache[key] = node

        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]

    def get_cache_state(self):
        result = []
        curr = self.head.next
        while curr != self.tail:
            result.append((curr.key, curr.value))
            curr = curr.next
        return result

cache = LRUCache(3)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/put', methods=['POST'])
def put():
    data = request.json
    cache.put(int(data['key']), int(data['value']))
    return jsonify(cache.get_cache_state())

@app.route('/get', methods=['POST'])
def get():
    data = request.json
    value = cache.get(int(data['key']))
    return jsonify({
        "value": value,
        "cache": cache.get_cache_state()
    })

if __name__ == '__main__':
    app.run(debug=True)