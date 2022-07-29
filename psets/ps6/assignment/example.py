class Dog:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.dog_tag = name

    def print_info(self):
        print(self.owner)
        print(f"{self.owner}'s dog, {self.name}")


d = Dog("Puck", "Emily")
# print(d.dog_tag)  # Puck

d.print_info()
