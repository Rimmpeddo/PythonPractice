count = 0

for red in range(0,4):
    for yellow in range(0,4):
        for green in range(2,7):
            if red + yellow + green == 8:
                count += 1
                print("red: ", red)
                print("yellow: ", yellow)
                print("green: ", green)
                print(count)
                print()