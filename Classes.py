class Dog:
    # constructor
    def __init__(self, name, month, day, year, speakText):
        self.name = name
        self.month = month
        self.day = day
        self.year = year
        self.speakText = speakText
    
    # accessor method returns 'speakText'
    def speak(self):
        return self.speakText
    
    # accessor method to get name
    def getName(self):
        return self.getName

    # accessor method to get Birth Date
    def birthDate(self):
        # formatting the date, prepend 0 if day or month is single digit
        lenOfMonth = (len(str(self.month)))
        lenOfDay = (len(str(self.day)))
        if lenOfMonth == 1:
            self.month = '0'+str(self.month)
        if lenOfDay == 1:
            self.day = '0'+str(self.day)
        return str(self.month) + "/" + str(self.day) + "/" + str(self.year)

    # mutator method that changes speakText in the Dog object
    def changeBark(self, bark):
        self.speakText = bark

# initialise an object
snowy = Dog('Snowy', 1, 1, 1958, 'Light Bark')
# access object's accessor methods
print(snowy.birthDate())
print(snowy.speak())
# use object's mutator method
snowy.changeBark('Loud Bark!')
print(snowy.speak())