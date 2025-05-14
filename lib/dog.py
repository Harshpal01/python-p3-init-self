#!/usr/bin/env python3

# lib/dog.py

class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed
if __name__ == "__main__":
    fido = Dog("Rex")  
    print(fido.name)    
    print(fido.breed)