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
      self.m()

    def put5(self):
      """Put 5 beepers in a line"""
      self.put2()
      self.m()
      self.put2()
      self.m()
      self.put2()

    def square(self):
      """Makes a square for 315"""
      self.put2()
      self.put2()
      self.put2()
      self.put()
      self.m()
      self.put()
      self.tl()
      self.m()
      self.put2()
      self.put2()
      self.put2()
      self.put()
      self.tl()
      self.m()
      self.put2()
      self.put2()
      self.put2()
      self.tl()
      self.m()
      self.put2()
      self.put2()
      self.put2()
      self.tl()
      


def main():
    """ Karel code goes here! """
    kt = ktools()
    kt.square()
    pass


if __name__ == "__main__":
    run_karel_program()