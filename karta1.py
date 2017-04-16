import random
class Game(object):
  def __init__(self,nob): # Initial position at the middle bottom of the area. numberofopponents=nob. Fetches size, area, and starts play.
    self.size()
    self.opponentspawn(nob)
    self.area()
    self.play()

  def play(self): # Moving aspect.
    cmd = "nnnn"
    while cmd != "exit":
      cmd = raw_input("\n\nDirection? ")
      if cmd != "exit":
        self.move(cmd)
        self.area()

  def move(self, direction): # Direction, moving.
    self.direction=direction
    if direction == "s":
      self.position[1] = self.position[1]+1
    elif direction == "d":
      self.position[0] = self.position[0]+1
    elif direction == "w":
      self.position[1] = self.position[1]-1
    elif direction == "a":
      self.position[0] = self.position[0]-1
    self.encounter()

  def outofboundary(self): # Warning for stepping out of boundary (OBS, not working at the moment)
    if self.position[0]<0 or self.position[0]>10 or self.position[1]<0 or self.position[1]>10:
      raise Exception("Out of boundary")
      
      
  def opponentspawn(self, nob): #determines position of opponents. nob = numberofopponents
    self.nob=nob
    self.A=[]
    for i in range(0,self.nob):
      self.A.append([random.randint(0,self.sizex-1), random.randint(0,self.sizey-1)]) # Random numbers determines opponents position
  
  
  def encounter(self): # Checks if player and opponents are in the same coordinates
    for i in range(0,self.nob):
      if self.position[0]==self.A[i][0] and self.position[1]==self.A[i][1]:
        raise Exception("Encounter")
        


  def area(self): # Plots room/area
    for y in range(0,self.sizey):
      print ""
      for x in range(0,self.sizex):
	printed = False
        for i in range(0,self.nob):
          if self.A[i][0]==x and self.A[i][1]==y:
            print "X",
            printed = True
        if not printed:
          if self.position[0]==x and self.position[1]==y:
            print "P",
          else:
            print "O",

  def size(self): # Randomizes room size
    self.sizex=random.randint(4,10)
    self.sizey=random.randint(4,10)
    self.startposx=int(self.sizex/2)
    self.position=[self.startposx, self.sizey-1]

player1 = Game(5) # 5 opponents



# Example start position
# O - nothing, X - opponent, P -player 
# O O O O O O O O O O O
# O O O O O O O X O O O
# O O O O O O O O O O O
# O O O X O O O O O O O
# O O O O O O O O O X O
# O O O O O O O O O O O
# O O O O O O O O O O O
# O O O O O P O O O O O


