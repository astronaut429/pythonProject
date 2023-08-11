n = int(input("enter number: "))

counter = 0
ways = 0

while counter < n/4:
    nest_counter = 0

    while nest_counter < n/5:
        if 4 * counter + 5 * nest_counter == n:
            ways += 1

        nest_counter += 1

    counter += 1
