from typing import Literal


class MyHashMap:
    def __init__(self):
        self.load_factor = 0.7
        self.downsize_factor = 0.25  # When the load factor falls below this threshold, we downsize
        self.bucket = [list() for _ in range(10)]  # Create a list of 10 empty lists (buckets)
        self.current_load = 0  # Track the current number of elements in the map
        self.bucket_length = len(self.bucket)  # Initial bucket size

    def put(self, key: int, value: int) -> None:
        # If the current load exceeds the load factor, resize the hash map
        if self.current_load / self.bucket_length > self.load_factor:
            self._resize()
        self._put(key, value)

    def _put(self, key: int, value: int, change_load=True):
        # Find the appropriate bucket for the key using the hash function
        array = self.bucket[self._hash(key)]
        # Check if the key already exists in the bucket
        for i, (k, v) in enumerate(array):
            if k == key:
                # If the key is found, update its value
                array[i] = (key, value)
                return
        # If the key is not found, append a new key-value pair to the bucket
        array.append((key, value))
        # Increase the current load if a new element is added
        if change_load:
            self.current_load += 1

    def get(self, key: int) -> int:
        # Retrieve the value associated with the given key
        array = self.bucket[self._hash(key)]
        # Search for the key in the bucket
        result = self._find_by_key(array, key)
        if result == -1:
            # If the key is not found, return -1
            return -1
        return result[1]  # Return the value of the found key-value pair

    def _find_by_key(self, array: list, key) -> tuple | Literal[-1]:
        # Search for a key in the bucket
        for k, v in array:
            if k == key:
                return (k, v)
        return -1  # Return -1 if the key is not found

    def remove(self, key: int) -> None:
        # Find the appropriate bucket for the key
        array = self.bucket[self._hash(key)]
        # Search for the key in the bucket
        tuple_ = self._find_by_key(array, key)
        if tuple_ != -1:
            # If the key is found, remove the key-value pair
            array.remove(tuple_)
            # Decrease the current load after removal
            self.current_load -= 1
            # If the load factor is too low, downsize the bucket array
            if self.current_load / self.bucket_length < self.downsize_factor:
                self._downsize()

    def _hash(self, key):
        # Hash function that computes an index for the key in the bucket array
        return abs(hash(key)) % self.bucket_length

    def _resize(self):
        # Double the size of the bucket array to maintain efficient performance
        old_bucket = self.bucket
        self.bucket = [[] for _ in range(2 * self.bucket_length)]  # Create new larger bucket array
        self.bucket_length = len(self.bucket)  # Update the bucket length
        # Rehash all key-value pairs from the old bucket array into the new one
        for old_array in old_bucket:
            for k, v in old_array:
                self._put(k, v, change_load=False)

    def _downsize(self):
        # Halve the size of the bucket array to save memory
        old_bucket = self.bucket
        self.bucket = [[] for _ in range(self.bucket_length // 2)]  # Create a new smaller bucket array
        self.bucket_length = len(self.bucket)  # Update the bucket length
        # Rehash all key-value pairs from the old bucket array into the new one
        for old_array in old_bucket:
            for k, v in old_array:
                self._put(k, v, change_load=False)


# Initialize the hash map
hash_map = MyHashMap()

# Perform the operations
hash_map.remove(27)  # Remove key 27
hash_map.put(65, 65)  # Insert key 65 with value 65
hash_map.remove(19)  # Remove key 19
hash_map.remove(0)  # Remove key 0
print(hash_map.get(18))  # Get value for key 18, should return -1 as key is not present
hash_map.remove(3)  # Remove key 3
hash_map.put(42, 0)  # Insert key 42 with value 0
print(hash_map.get(19))  # Get value for key 19, should return -1
hash_map.put(17, 90)  # Insert key 17 with value 90
hash_map.put(31, 76)  # Insert key 31 with value 76
hash_map.put(48, 71)  # Insert key 48 with value 71
hash_map.put(5, 50)  # Insert key 5 with value 50
hash_map.put(7, 68)  # Insert key 7 with value 68
hash_map.put(73, 74)  # Insert key 73 with value 74
hash_map.put(85, 18)  # Insert key 85 with value 18
hash_map.put(74, 95)  # Insert key 74 with value 95
hash_map.put(84, 82)  # Insert key 84 with value 82
hash_map.put(59, 29)  # Insert key 59 with value 29
hash_map.put(71, 71)  # Insert key 71 with value 71
hash_map.remove(42)  # Remove key 42
hash_map.put(51, 40)  # Insert key 51 with value 40
print(hash_map.get(33))  # Get value for key 33, should return -1
hash_map.remove(17)  # Remove key 17
hash_map.put(89, 95)  # Insert key 89 with value 95
hash_map.put(95, 35)  # Insert key 95 with value 35
hash_map.put(65, 81)  # Insert key 65 with value 81
hash_map.put(61, 46)  # Insert key 61 with value 46
hash_map.put(50, 33)  # Insert key 50 with value 33
print(hash_map.get(59))  # Get value for key 59, should return 29
hash_map.remove(5)  # Remove key 5
hash_map.put(75, 89)  # Insert key 75 with value 89
hash_map.put(80, 17)  # Insert key 80 with value 17
hash_map.put(35, 94)  # Insert key 35 with value 94
hash_map.put(80, 19)  # Update key 80 with value 19
hash_map.put(13, 17)  # Insert key 13 with value 17
hash_map.put(70, 28)  # Insert key 70 with value 28
hash_map.put(99, 37)  # Insert key 99 with value 37
hash_map.remove(13)  # Remove key 13
print(hash_map.get(90))  # Get value for key 90, should return -1
hash_map.put(41, 50)  # Insert key 41 with value 50
hash_map.remove(29)  # Remove key 29
hash_map.put(98, 54)  # Insert key 98 with value 54
hash_map.put(72, 6)  # Insert key 72 with value 6
hash_map.put(51, 88)  # Insert key 51 with value 88
print(hash_map.get(13))  # Get value for key 13, should return -1 as it was removed
hash_map.put(8, 22)  # Insert key 8 with value 22
hash_map.put(85, 31)  # Insert key 85 with value 31
hash_map.put(22, 60)  # Insert key 22 with value 60
print(hash_map.get(96))  # Get value for key 96, should return -1 as key is not present
hash_map.remove(6)  # Remove key 6
hash_map.remove(54)  # Remove key 54
hash_map.put(51, 90)  # Insert key 51 with value 90
print(hash_map.get(28))  # Get value for key 28, should return -1
hash_map.put(51, 80)  # Update key 51 with value 80
hash_map.put(69, 58)  # Insert key 69 with value 58
hash_map.put(92, 13)  # Insert key 92 with value 13
hash_map.remove(12)  # Remove key 12
print(hash_map.get(91))  # Get value for key 91, should return -1 as key is not present
hash_map.put(52, 83)  # Insert key 52 with value 83
hash_map.put(72, 54)  # Insert key 72 with value 54
hash_map.put(48, 36)  # Insert key 48 with value 36
hash_map.remove(85)  # Remove key 85
hash_map.put(25, 47)  # Insert key 25 with value 47
hash_map.put(68, 33)  # Insert key 68 with value 33
hash_map.remove(36)  # Remove key 36
hash_map.put(67, 68)  # Insert key 67 with value 68
hash_map.put(83, 36)  # Insert key 83 with value 36
hash_map.put(58, 79)  # Insert key 58 with value 79
print(hash_map.get(95))  # Get value for key 95, should return 35
hash_map.put(36, 89)  # Insert key 36 with value 89
hash_map.put(30, 85)  # Insert key 30 with value 85
hash_map.remove(33)  # Remove key 33
hash_map.put(87, 42)  # Insert key 87 with value 42
print(hash_map.get(68))  # Get value for key 68, should return 33
