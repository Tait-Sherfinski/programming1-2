def main():
  eggs = int(input("Enter # of eggs purchased: "))
  dozens = eggs // 12
  remainder = eggs % 12

  if eggs > 0 and eggs < 48:
    price = 0.50 * dozens
  if eggs >= 48 and eggs < 72:
    price = 0.45 * dozens
  if eggs >= 72 and eggs < 132:
    price = 0.40 * dozens
  if eggs >= 132:
    price = 0.35 * dozens
  print(price + (remainder * (1 / 12) / 2))
  pass


if __name__ == "__main__":
  main()