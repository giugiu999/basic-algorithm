class HashTable:
    def __init__(self, size=10):
        """Initialize the hash table with a given size."""
        self.size = size  # Size of the hash table
        self.table = [[] for _ in range(size)]  # Use separate chaining to handle collisions

    def hash_function(self, key):
        """A simple hash function that maps keys to an index in the table."""
        return hash(key) % self.size

    def insert(self, key, value):
        """Insert a key-value pair into the hash table."""
        index = self.hash_function(key)
        # Check if the key already exists and update its value
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        # If the key doesn't exist, append the new key-value pair
        self.table[index].append([key, value])

    def search(self, key):
        """Search for a value by its key."""
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]  # Return the associated value
        return None  # Return None if the key is not found

    def delete(self, key):
        """Delete a key-value pair from the hash table."""
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                self.table[index].remove(pair)
                return True  # Return True if deletion was successful
        return False  # Return False if the key is not found

    def display(self):
        """Display the contents of the hash table."""
        for i, bucket in enumerate(self.table):
            print(f"Index {i}: {bucket}")

# Testing the hash table
hash_table = HashTable(size=5)

# Insert key-value pairs
hash_table.insert("name", "Alice")
hash_table.insert("age", 25)
hash_table.insert("city", "New York")

# Display the hash table
print("Hash Table Contents:")
hash_table.display()

# Search for keys
print("\nSearch for key 'name':", hash_table.search("name"))
print("Search for key 'city':", hash_table.search("city"))
print("Search for key 'country':", hash_table.search("country"))  # Key does not exist

# Update a key-value pair
hash_table.insert("age", 26)  # Update the value for 'age'
print("\nHash Table Contents After Update:")
hash_table.display()

# Delete a key-value pair
hash_table.delete("city")
print("\nHash Table Contents After Deleting 'city':")
hash_table.display()
