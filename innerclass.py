class Car:
    def __init__(self):
        self.make = 'honda'
        self.year = 1000

    class Engine:
        def __init__(self):
            self.no = '1442342'
        def start(self):
            print 'started'

Car().Engine().start()