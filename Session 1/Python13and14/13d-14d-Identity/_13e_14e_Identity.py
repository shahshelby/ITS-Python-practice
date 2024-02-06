a = 3
b = a  # If a changes, then b will also (their IDs are same)

northItems = ["Rain gear", "Snow shoes"]
eastItems = ["Rain gear", "Snow shoes"]

# This is Identity Operators (is, is not)
# determine if two vars have same ID
print(a == b)  # True same value
print(a is b)  # True same ID
print(northItems == eastItems)  # True same item values
print(northItems is eastItems)  # False different ID

# northItems is eastItems: This checks whether northItems and eastItems refer to the exact same object in memory.
# Since they are separate objects (even though they contain the same items), this evaluates to False.
