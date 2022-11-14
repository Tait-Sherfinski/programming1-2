def main():
  eggs = int(input("Enter # of eggs purchased: "))
  dozens = eggs/12.0
  remainder = eggs % 12
  eggs = 0
  price = 0.0

  if eggs > 0 and eggs < 48:
    price = 0.50 / 12
  if eggs >= 48 and eggs < 72:
    price = 0.45
  if eggs >= 72 and eggs < 132:
    price = 0.40
  if eggs >= 132:
    price = 0.35
  pass


if __name__ == "__main__":
  main()