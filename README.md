# LRU Cache Replacement Simulator

## Overview
This project simulates a **memory cache replacement system** using the **Least Recently Used (LRU)** policy.  
It demonstrates how real-world systems manage limited memory efficiently by evicting the least recently accessed data.

---

## Objective
To design and implement an optimized LRU Cache with:
- O(1) time complexity
- Efficient memory management
- Real-time visualization of cache operations

---

## Core Data Structures
- **HashMap (Dictionary)** → O(1) lookup
- **Doubly Linked List** → O(1) insertion & deletion

---

## Algorithm Used
### LRU (Least Recently Used)
- Most recently accessed item → moved to front
- Least recently used item → removed when capacity exceeds

---

## Time Complexity

| Operation | Complexity |
|----------|-----------|
| get()    | O(1) |
| put()    | O(1) |
| eviction | O(1) |

---

##  Features

### Core Functionalities
- Add key-value pairs to cache
- Access existing keys
- Automatic eviction of least recently used item

### Performance Tracking
- Cache Hits counter
- Cache Misses counter
- Cache Size tracking

### Visualization
- Cache blocks displayed (MRU → LRU)
- MRU highlighted in green
- LRU highlighted in red
- Activity logs showing operations

###  Simulation Mode
- Automatically performs random operations
- Helps analyze cache behavior

---