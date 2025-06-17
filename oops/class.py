class Dog:
    species = "Canis familiaris"  # class variable

    def __init__(self, name):
        self.name = name

    @classmethod
    def common_species(cls):
        return f"All dogs belong to {cls.species}"
        
print(Dog.common_species())  # Output: All dogs belong to Canis familiaris
