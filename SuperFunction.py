__metaclass_ = type # super only works with new style classes

class Bird:
     def  __init__(self):
          self.hungry = True
     def eat(self):
          if self.hungry:
               print 'Aaah...'
               self.hungry = False
          else:
                print 'No Thanks'

class SongBird(Bird):
     def  __init__(self):
#          Bird.__init__(self)
          super().__init__(self)
          self.sound = 'Squaak'
     def sing(self):
          print self.sound
