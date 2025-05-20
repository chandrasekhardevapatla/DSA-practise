## Linked List

A **Linked List** is linear data structure where elements(called nodes) are stored
in non-contiguous memory locations. Each node contains
  1. Data (Value)
  2. Pointer (or Reference) to the next node
Thhink of it link chain where each link points to the next one.

# What is the use of Linked List

✅ Advantages:

🔹 **Dynamic Size** unlike arrays they can grow and shrink as needed
🔹 **Efficient Insert/Delete** at the beginning or at the midddle (no need to shif elements)

❌ Disadvantages:

🔹 **No Direct Access** No direct access to elements you must travel from the head.
🔹 **More Memory** Due to extra pointer storage
🔹 **Not cache friendly** Nodes are scattered in memory

# Types of Linked List

🔹 **Singly Linked List**
    Each node points to the next node and last node points to the null
    *Use cases*
        1. Simple dynamic list
        2. Stack implementation (Push/pop at the head)
🔹 **Doubly Linked List**
    Each node has two pointers one points to the next node and one points to the previous node
    *Use cases*
        1. Browser history (forward/backward)
        2. Undo/Redo systems
        3. Efficient bi-directional traversal
🔹 **Circular Linked List**
    The last node of linked list ponints to the first node making it a circular linked list
    *Use cases*
        1. Round-robin scheduling
        2. Circular buffers(audio/video)
        3. Mutiplayer turn-based games
🔹 **Skip List**
    A probabilistic data structure built on top of sorted linked list, where elements are spread
    accross mutiple levels for faster search.
    *Use cases*
        1. Efficient search in O(log n)
        2. Used in redis, in-memory databases


