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

    def __init__(self, capacity= MIN_CAPACITY):
      self.capacity= capacity
      self.nodeCount= 0
      self.storage= [None] * self.capacity
      self.resizeCeil= 0.7
      self.resizeFloor= 0.2


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.nodeCount / self.capacity


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
        # check load factor and resize as needed
        if self.get_load_factor() >= self.resizeCeil:
          self.resize(self.capacity * 2)

        # get index from hash
        ind= self.hash_index(key)

        # insert at index
          # cases: 
            # is key already there?
              # if so, overwtite the value
              # else: add to tail
            # if index is empty (NONE)?
              # add to head like  normal
        # add next pointer to new node pointing at the old 'first node'
        # increment the nodeCounter

        # if that index is None
        if self.storage[ind] == None:
          self.storage[ind]= HashTableEntry(key, value)
          self.nodeCount+= 1
          # return self.storage[ind].key
        
        # if there are already nodes at this index, check if key exists
        else:
          cur= self.storage[ind]
          while cur != None:
            # if key exists, overwrite it's value
            if cur.key == key:
              cur.value= value
              break
            # if we're on the last node
            elif cur.next != None:
              cur= cur.next
            else:
              break
          # if key doesn't exist, add it to tail
          cur.next= HashTableEntry(key, value)
          self.nodeCount+= 1



    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # check resize before delete
        if self.get_load_factor() <= self.resizeFloor:
          self.resize(MIN_CAPACITY)
        else:
          self.resize(self.capacity // 2)

        # get index
        ind= self.hash_index(key)
        cur= self.storage[ind]
        prev= self.storage[ind]

        # if only one node?
        if cur.next == None:
          # set index slot to None
          self.storage[ind]= None
          # decrement nodeCounter
          self.nodeCount-= 1
          return

        # if 1st node but not the ONLY node
        elif cur.key == key:
          self.storage[ind]= cur.next
          self.nodeCount-= 1
          return
        else:
          cur= cur.next
        
        # if more than one node:
        while cur != None:
        # if key matches any other node
          if cur.key == key:
            # set prev.next= cur.next
            prev.next= cur.next
            self.nodeCount-= 1
            return
          elif cur.next != None:
            cur= cur.next
            prev= prev.next
          else: break
        
        # if key not found:
        print('Warning, key not found')


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # what if ind is empty(NONE)? return None
        # search linked list for key
          # if no key, return None
          # else: return value

        # get index
        ind= self.hash_index(key)

        cur= self.storage[ind]
        while cur != None:
          # if key exists
          if cur.key == key:
            return cur.value
          cur= cur.next
        return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """


        # copy old list
        oldArr= self.storage
        # make new list of new_capacity size
        newArr= [None] * new_capacity
        # set self.storage to the new list
        self.storage= newArr
        self.capacity= len(newArr)

        #loop through old list
        for slot in oldArr:
          if slot != None:
            cur= slot
            while cur:
              self.put(cur.key, cur.value)
              cur= cur.next

        # then self.put each item into the new storage
        # print('new cap: ', self.capacity)
        # set new capacity


if __name__ == "__main__":
    # ht = HashTable(8)

    # ht.put("line_1", "'Twas brillig, and the slithy toves")
    # ht.put("line_2", "Did gyre and gimble in the wabe:")
    # ht.put("line_2", "All mimsy were the borogoves,")
    # ht.put("line_4", "And the mome raths outgrabe.")
    # ht.put("line_5", '"Beware the Jabberwock, my son!')
    # ht.put("line_6", "The jaws that bite, the claws that catch!")
    # ht.put("line_7", "Beware the Jubjub bird, and shun")
    # ht.put("line_8", 'The frumious Bandersnatch!"')
    # ht.put("line_9", "He took his vorpal sword in hand;")
    # ht.put("line_10", "Long time the manxome foe he sought--")
    # ht.put("line_11", "So rested he by the Tumtum tree")
    # ht.put("line_12", "And stood awhile in thought.")

    print("")
    # print(ht.get("line_1"))

    # for i in range(1, MIN_CAPACITY+ 1):
    #     print(ht.get(f"line_{i}"))
    
    print("")
    # ht.delete("line_2")
    # ht.delete("line_2")
    # ht.delete("line_3")
    print("")
    print("")

    # for i in range(1, MIN_CAPACITY+ 1):
    #     print(ht.get(f"line_{i}"))

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
