class Patient:
    def __init__(self):
        self.__name = '';
        self.__id = '';
        self.__ssn = '';

    def getName(self):
        return self.__name

    def getId(self):
        return self.__id

    def getSSN(self):
        return self.__ssn

    def setName(self, name):
       self.__name = name

    def setId(self, id):
       self.__id= id

    def setSSN(self, ssn):
        self.__ssn = ssn

patient = Patient()
patient.setId(1)
patient.setName('john')
patient.setSSN('1343242')
print(patient.getId())
print(patient.getName())
print(patient.getSSN())