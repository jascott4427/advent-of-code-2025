combo = 50
safeMin = 0
safeMax = 99
count = 0
try:
    with open('input.txt', 'r') as file:
        for line in file:
            line = line.strip()
            dir = line[0]
            num = int(line[1:])
            print(dir, num)
            if dir == "R":
                combo += num
            else:
                combo -= num

            combo %= (safeMax + 1)
            
            if combo == 0:
                count += 1
            print(combo, count)
            
except FileNotFoundError:
    print("Error: The file 'input.txt' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

print(count)