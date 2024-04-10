from dataclasses import dataclass

"""
    Dataclasses are a sort of 'helper' to write 
    data oriented classes in python.

    Data Oriented Classes are Python way' to structure classes focused primarily on storing and managing data, 
    rather than on providing complex behaviors or algorithms. """


@dataclass
class Book:
    title: str
    author: str
    pages: int
    weight: int

    def say_hello(self, hello):
        return print(f"Hi friend, just say {hello}")

    def say_sum(self, pages, weight):
        return print(str(pages + weight))
