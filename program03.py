urinishlar = 0

while urinishlar < 3:
    javob = input("O'zbekiston poytaxti qayer? ")
    if javob.lower() == "toshkent":
        print("To'g'ri.✔️")
        break
    else:
        print("Noto'g'ri.")
        urinishlar += 1

if urinishlar == 3:
    print("Bloklandiz.")
