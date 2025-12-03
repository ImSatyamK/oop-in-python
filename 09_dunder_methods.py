class ShoppingCart:
    def __init__(self, items):
        """
        Called automatically when you create an object.
        Used to initialize attributes.
        """
        self.items = items

    def __str__(self):
        """
        Called by print(obj)
        Returns a user-friendly string.
        """
        return f"ShoppingCart with {len(self.items)} items"

    def __repr__(self):
        """
        Called in the interpreter or debugging.
        Should return a string that clearly represents the object.
        """
        return f"ShoppingCart({self.items!r})"

    def __len__(self):
        """
        Makes len(obj) work.
        Should return the size of your collection.
        """
        return len(self.items)

    def __getitem__(self, index):
        """
        Allows indexing like obj[index].
        Must return the item at that position.
        """
        return self.items[index]

cart = ShoppingCart(["apple", "milk", "bread"])

print(cart) # __str__ called
print(repr(cart)) # __repr__ called
print(len(cart)) # __len__ called
print(cart[1]) # __getitem__ called
# Demonstrating the use of dunder methods to customize class behavior

