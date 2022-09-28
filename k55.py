from stanfordkarel import *


class ktools:
  def m(self):
    """Shorthand for move"""
    move()

    def tl(self):
      """Shorthand for turn_left"""
      turn_left()

    def tr(self):
      """Turn right"""
      self.tl()
      self.tl()
      self.tl()

    def ta(self):
      """Turn Around"""
      self.tl()
      self.tl()

    def pick(self):
      """Pick Beeper"""
      pick_beeper()

    def put(self):
      """Put Beeper"""
      put_beeper()

    def put2(self):
      """Put 2 beepers in a line"""
      self.put()
      self.m()
      self.put()

    def put5(self):
      """Put 5 beepers in a line"""
      self.put2()
      self.m()
      self.put2()
      self.m()
      self.put2()

    def fic(self):
      """Front is Clear"""
      return front_is_clear()

    def fib(self):
      """Front Is Blocked"""
      return not self.fic()

    def ric(self):
      """Right is clear"""
    self.tr()
    if self.fic():
      self.tl()
      return True
      self.tl()
      return False
    
    
    def rib(self):
      """Right is Blocked"""
      return not self.ric()

    def mazemove(self):
      """Maze move"""
      if self.fib():
        self.tl()
      else:
        self.m()
        if self.ric():
          self.tr()
          self.m()
          if self.ric():
            self.tr()
            self.m()
      pass

    def mm(self, num):
      """Move multiple"""
      for number in range(num):
        self.m()

    def pickm(self, num):
      """Pick multiple"""
      for i in range(num-1):
        self.pick()
        self.m()
      self.pick()

    def putm(self, num):
      """Put multiple"""
      for _ in range(num-1):
        self.put()
        self.m()
      self.put()

  def SOB(self) -> bool:
    """Standing on beeper"""
    return beepers_present()

  def jump(self):
    """Jump for 510"""
    while self.fic():
      self.m()
    self.tl()
    while self.rib():
      self.m()
    self.tr()
    self.m()
    self.tr()
    while self.fic():
      self.m()
    self.tl()

  def find(self):
    """Find for 515"""
    while not facing_north():
      self.tl()
    self.m()
    if not self.SOB():
      self.tl()
      self.m()
      self.tl()
      self.m()
    for _ in range(2):
      if not self.SOB():
        self.m()
        self.tl()
        self.m()
    pass

  def find2(self):
    """Find for 55"""
    while self.SOB():
      self.pick()
    self.m()
    if not self.SOB():
      self.tl()
      self.m()
      self.tl()
      self.m()
      self.tr()
      


def main():
    """ Karel code goes here! """
    kt = ktools()
    kt.find2()
    pass


if __name__ == "__main__":
    run_karel_program()