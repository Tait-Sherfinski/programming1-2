def main():
  kilograms = int(input("Enter package weight in kilograms: "))
  centilength = int(input("Enter package length in centimeters: "))
  centiwidth = int(input("Enter package width in centimeters: "))
  centiheight = int(input("Enter package height in centimeters: "))
  if centiheight * centiwidth * centilength > 100000:
    print("Too Large")
  if kilograms > 27:
    print("Too Heavy")
  if centiheight * centiwidth * centilength > 100000 and kilograms > 27:
    print("Too heavy and Too large")
  pass


if __name__ == "__main__":
  main()