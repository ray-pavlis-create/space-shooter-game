class Character:
  def __init__(self, name, phraseOne, phraseTwo):
    self.name = name
    self.phraseOne = phraseOne
    self.phraseTwo = phraseTwo
    self.level = 0
  
  def speak(self, phraseNum):
    if phraseNum == 1:
      print(self.phraseOne)
    elif phraseNum == 2:
      print(self.phraseTwo)
    else:
      print("Invalid Entry")
    
  def setLevel(self, newLevel):
    self.level += newLevel
    print(self.level)

character1 = Character("Spiderman", "My Spidey-Senses are tingling", "Your friendly neighborhood Spiderman")

character2 = Character("Kung Fu Panda", "Skadoosh!", "You have been blinded by pure awesomeness!")

character1.speak(1)
character1.setLevel(2)
character1.speak(2)

character2.speak(1)
character2.setLevel(2)
character2.speak(2)