a = {} # Empty Dictionary

Bittu = {
    "Name": 'Bittu Dey',
    "StudentId": 2311200001180,
    "Department": 'CSE',
    "RegistrationId": 230011809175,
    "Batch": 2027
}

print(type(Bittu)) # Type of Bittu
print(Bittu.items()) # Accessing all key-value pairs
print(Bittu.keys()) # Accessing all keys
print(Bittu.values()) # Accessing all values
print(Bittu['Name']) # Accessing value using key

Bittu.update({"Batch": 2026})   # Update existing key-value pair
Bittu.update({"Age": 19}) # Add new key-value pair
print(Bittu)