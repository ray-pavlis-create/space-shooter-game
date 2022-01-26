class Backpack:
  #Properties
  def __init__(self, color, size):
    self.color = color
    self.size = size
    self.item = []
    self.open = False
  
  #Methods
  def openBag(self):
    self.open = True
    print("The backpack is now open")
  
  def closeBag(self):
    self.open = False
    print("The backpack is now closed")
  
  def putIn(self, item):
    if self.open == True:
      self.item.append(item)
      print(str(item) + " was added to the backpack")
    else:
      print("Please open the backpack first")
  
  def takeOut(self, item):
    if self.open == True:
      self.item.remove(item)
      print(str(item) + " was removed from the backpack")
    else:
      print("Bag is closed or item is not in bag")

bag1 = Backpack("Blue", "Small")
bag2 = Backpack("Red", "Medium")
bag3 = Backpack("Green", "Large")

bag1.openBag()
bag1.putIn("Lunch")
bag1.putIn("Jacket")
bag1.closeBag()
bag1.openBag()
bag1.takeOut("Jacket")
bag1.closeBag()