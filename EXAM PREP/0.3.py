string = [int(i) for i in input().split("@")]
command = input()

position = 0

while not command == "Love!":
    length_jump = command.split()[1]
    length_jump = int(length_jump)

    position = position + length_jump

    if position >= len(string):
        position = 0

    if string[position] == 0:
        print(f"Place {position} already had Valentine's day.")
    else:
        string[position] -= 2
        if string[position] == 0:
            print(f"Place {position} has Valentine's day.")

    command = input()

print(f"Cupid's last position was {position}.")

counter = 0

for num in string:
    if not num == 0:
        counter += 1

if counter == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {counter} places.")



