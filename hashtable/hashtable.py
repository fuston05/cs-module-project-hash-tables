class HashTableEntry:
    # Linked List hash table key/value pair

    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity=MIN_CAPACITY):
        # Your code here
        self.capacity = capacity
        self.storage = [None] * self.capacity
        self.nodeCount = 0

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
        load = self.nodeCount/self.capacity
        return load

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381

        for b in key:
            hash = (hash * 33) + ord(b)
            hash &= 0xffffffff  # add this for a 32-bit hashing function
            # total &= 0xffffffffffffffff  # add this for a 64-bit hashing function
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        # check loadFactor
        if self.get_load_factor() >= 0.7:
            self.resize(self.capacity * 2)

        # get index
        i = self.hash_index(key)
        cur = self.storage[i]
        if cur == None:
            self.storage[i] = HashTableEntry(key, value)
            self.nodeCount +=1
            return

        while cur is not None:
            if cur.key == key:
                cur.value = value
                return
            elif cur.next is not None:
                cur = cur.next
            else:
                cur.next = HashTableEntry(key, value)
                self.nodeCount +=1

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here

        # get the key index
        i = self.hash_index(key)

        # search through linked list and find key
        cur = self.storage[i]
        prev = self.storage[i]
        # if key is the head
        if cur is not None and cur.key == key:
            # if it's the only value in slot
            # set array slot to None
            if cur.next is None:
                data = cur.value
                self.storage[i] = None
                self.nodeCount -=1
                return data
            else:
              # if there is a next node
                data = cur.value
                self.storage[i] = cur.next
                self.nodeCount -=1
                cur.next = None
                return data
        elif cur is not None and cur.next is not None:
            cur = cur.next

            while cur is not None:
                if cur.key == key:
                    prev.next = cur.next
                    cur.next = None
                    self.nodeCount -=1
                    return cur.value
                else:
                    prev = prev.next
                    cur = cur.next
        print('could not find that item.')
        return None

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        i = self.hash_index(key)

        cur = self.storage[i]
        while cur is not None:
            # check for a matching key
            if cur.key == key:
                return cur.value
            else:
                cur = cur.next
        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here

        # create a new array at *2 capacity
        newArr = [None] * new_capacity
        # store ref to old array
        oldArr = self.storage
        # point HashTable to use the new array
        self.storage = newArr
        self.capacity= len(newArr)
        # loop through old array and 'put' each one back onto new array
        for ele in oldArr:
            # if empty, skip
            if ele is not None:
                # check if there's moren than 1 node
                cur = ele
                while cur is not None:
                    self.put(cur.key, cur.value)
                    cur = cur.next


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_2", "All mimsy were the borogoves,")
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
    print(ht.get("line_1"))

    # for i in range(1, 9):
    #     print(ht.get(f"line_{i}"))
    # ht.delete("line_1")
    # ht.delete("line_2")
    # ht.delete("line_3")

    print("")

    # # Test storing beyond capacity
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    # # Test resizing
    # old_capacity = ht.get_num_slots()
    # ht.resize(ht.capacity * 2)
    # new_capacity = ht.get_num_slots()

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    print("")
