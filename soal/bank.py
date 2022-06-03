from abc import ABC, abstractmethod

class Bank(ABC):

    @abstractmethod
    def do_transaction (self,total : int):
        pass