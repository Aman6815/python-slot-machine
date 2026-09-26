import random

# Game settings
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

# Number of each symbol available
SYMBOL_COUNT = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}




# Payout multiplier for each symbol
SYMBOL_VALUE = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}





def check_winnings(columns, lines, bet, values):
    """Check selected lines for matching symbols and calculate winnings."""
    winnings = 0
    winning_lines = []

    for line in range(lines):
        symbol = columns[0][line]

        for column in columns:
            if symbol != column[line]:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    """Generate a random slot machine result."""
    all_symbols = []

    for symbol, count in symbols.items():
        all_symbols.extend([symbol] * count)

    columns = []

    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]

        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    """Display the slot machine result."""
    print("\n+---+---+---+")
    
    for row in range(len(columns[0])):
        print("| " + " | ".join(column[row] for column in columns) + " |")
    
    print("+---+---+---+")


def deposit():
    """Get the player's starting balance."""
    while True:
        amount = input("What would you like to deposit? $")

        if amount.isdigit():
            amount = int(amount)

            if amount > 0:
                return amount

            print("Amount must be greater than 0.")
        else:
            print("Please enter a valid number.")


def get_number_of_lines():
    """Get the number of betting lines."""
    while True:
        lines = input(
            f"Enter the number of lines to bet on (1-{MAX_LINES}): "
        )

        if lines.isdigit():
            lines = int(lines)

            if 1 <= lines <= MAX_LINES:
                return lines

            print(f"Please enter a number between 1 and {MAX_LINES}.")
        else:
            print("Please enter a valid number.")


def get_bet():
    """Get the bet amount for each line."""
    while True:
        amount = input(
            f"What would you like to bet on each line (${MIN_BET}-${MAX_BET})? $"
        )

        if amount.isdigit():
            amount = int(amount)

            if MIN_BET <= amount <= MAX_BET:
                return amount

            print(f"Bet must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Please enter a valid number.")


def spin(balance):
    """Play one round of the slot machine."""
    lines = get_number_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"Insufficient balance. "
                f"Your current balance is ${balance}."
            )
        else:
            break

    print(f"\nBet: ${bet} per line")
    print(f"Lines: {lines}")
    print(f"Total bet: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, SYMBOL_COUNT)

    print_slot_machine(slots)

    winnings, winning_lines = check_winnings(
        slots, lines, bet, SYMBOL_VALUE
    )

    if winnings > 0:
        print(f"🎉 You won ${winnings}!")
        print("Winning lines:", *winning_lines)
    else:
        print("No winning combinations this round.")

    return winnings - total_bet


def main():
    """Run the slot machine game."""
    print("================================")
    print("       PYTHON SLOT MACHINE      ")
    print("================================")

    balance = deposit()

    while True:
        print(f"\nCurrent balance: ${balance}")

        answer = input("Press Enter to spin or 'q' to quit: ")

        if answer.lower() == "q":
            break

        balance += spin(balance)

        if balance <= 0:
            print("\nYou have run out of money. Game over!")
            break

    print("\n================================")
    print(f"Game over. Final balance: ${balance}")
    print("Thanks for playing!")
    print("================================")


if __name__ == "__main__":
    main()
