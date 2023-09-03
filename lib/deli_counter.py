class DeliCounter:
    def __init__(self):
        self.queue = []

    def line(self):
        if not self.queue:
            return "The line is currently empty."
        else:
            return "Current Queue: " + ", ".join(f"{i + 1}. {person}" for i, person in enumerate(self.queue))

    def take_a_number(self, name):
        self.queue.append(name)
        position = len(self.queue)
        return f"Welcome, {name}. You are number {position} in line."

    def now_serving(self):
        if not self.queue:
            return "There is nobody waiting to be served!"
        else:
            serving_person = self.queue.pop(0)
            return f"Now serving {serving_person}."

    def remove(self, name):
        if name in self.queue:
            self.queue.remove(name)
            return f"{name} has been removed from the queue."
        else:
            return f"{name} is not in the queue."

    def clear(self):
        self.queue = []
        return "The queue has been cleared."

# Example usage:
deli = DeliCounter()
print(deli.line())  # The line is currently empty.
print(deli.take_a_number("Luiz Diaz"))  # Welcome, Luiz Diaz. You are number 1 in line.
print(deli.take_a_number("Dominic Szoboslai"))    # Welcome, Dominic Szoboslai. You are number 2 in line.
print(deli.line())  # Current Queue: 1. Luiz Diaz, 2. Dominic Szoboslai
print(deli.now_serving())  # Now serving Luiz Diaz.
print(deli.line())  # Current Queue: 1. Dominic Szoboslai
print(deli.remove("Bob"))  # Bob has been removed from the queue.
print(deli.line())  # The line is currently empty.
print(deli.clear())  # The queue has been cleared.
