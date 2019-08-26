from abc import abstractmethod
from abc import ABC
class TouchScreenLaptop(ABC):
    @abstractmethod
    def scroll(self):
        pass
    @abstractmethod
    def click(self):
        pass
class HP(TouchScreenLaptop):
    def scroll(self):
        print('hp')

    @abstractmethod
    def click(self):
        pass



class Dell(TouchScreenLaptop):
    def scroll(self):
        print('dell')

    @abstractmethod
    def click(self):
        pass

class HPNoteBook(HP):
    def click(self):
        print('hp notebook print')

class DellNoteBook(Dell):
    def click(self):
        print('dell notebook print')


hpnotebook = HPNoteBook()
hpnotebook.click()

dellnotebook = DellNoteBook()
dellnotebook.click()


