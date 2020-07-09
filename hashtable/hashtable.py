class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

class LinkedList:
    def __init__(self):
        self.head = None

class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.storage = [LinkedList()] * capacity
        self.elements = 0
        # self.capacity = [None] * MIN_CAPACITY


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.storage)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.elements / self.get_num_slots()


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        seed = 0
        FNV_prime = 1099511628211
        offset_basis = 14695981039346656037

        # Your code here

        hash = offset_basis + seed
        for char in key:
            hash = hash * FNV_prime
            hash = hash ^ ord(char)
        return hash
       


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for x in key:
            hash = ((hash << 5) + hash) + ord(x)
        return hash & 0xFFFFFFFF

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % len(self.capacity)
        # return self.fnv1(key) & self.get_num_slots()

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        # self.capacity[self.hash_index(key)] = value
        index = self.hash_index(key)
        
        if self.storage[index].head == None:
            self.storage[index].head = HashTableEntry(key, value)
            self.elements += 1
            return
        else:
            cur = self.storage[index].head
            while cur.next:
                if cur.key == key:
                    cur.value = value
                cur = cur.next
            # if list doesn't have a key, add a new node
            cur.next = HashTableEntry(key, value)
            self.elements += 1
            
                

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        # self.capacity[self.hash_index(key)] = None
        index = self.hash_index(key)
        cur = self.storage[index].head
        
        if cur.key == key:
            self.storage[index].head = self.storage[index].head.next
            self.elements -= 1
            return
        
        while cur.next:
            prev = cur
            cur = cur.next
            if cur.key == key:
                prev.next = cur.next
                self.elements -= 1
                return None


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        # return self.capacity[self.hash_index(key)]

        index = self.hash_index(key)
        cur = self.storage[index].head
        
        if cur == None:
            return None
        if cur.key == key:
            return cur.value
        
        while cur.next:
            cur = cur.next
            if cur.key == key:
                return cur.value
        return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        self.capacity = new_capacity
        new_array = [LinkedList()] * new_capacity
        
        for slot in self.storage:
            cur = slot.head
            
            while cur:
                index = self.hash_index(cur.key)

                if new_array[index].head == None:
                    new_array[index].head = HashTableEntry(cur.key, cur.value)
                else:
                    node = HashTableEntry(cur.key, cur.value)
                    node.next = new_array[index].head
                    new_array[index].head = node
                cur = cur.next
            self.storage = new_array

if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
