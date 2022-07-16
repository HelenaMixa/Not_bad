def number_of_ways(n):
    if n in (1, 2):
        return n
    if n == 3:
        return number_of_ways(n - 1) + number_of_ways(n - 2) + 1
    return number_of_ways(n - 1) + number_of_ways(n - 2) + number_of_ways(n - 3)


if __name__ == '__main__':
    while True:
        try:
            n_steps = int(input("Please enter the number of stairs "))
            print(f"Number of ways - {number_of_ways(n_steps)}")
            calculate_again = input("Calculate again? ")
            if not calculate_again or calculate_again.lower() in ['no', 'n', 'ні']:
                break
        except ValueError:
            print("Oops! Invalid input. Are you sure you entered a number?  Try again...")
            continue
