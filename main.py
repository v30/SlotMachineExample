import random as rnd

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_win(columns, lines, bet, values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winnings_lines.append(line + 1)
            
    return winnings, winnings_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
            
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = rnd.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
            
        columns.append(column)
        
    return columns


def deposit():
    while True:
        amount = input("Deposit amount: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount not greater than 0")
        else:
            print("Enter a number")
            
    return amount


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row])
                

def get_num_lines():
    while True:
        lines = input("Number of lines to play (1 -" + str(MAX_LINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if 0 <= lines <= MAX_LINES:
                break
            else:
                print("Enter valid number of lines")
        else:
            print("Enter a number")
            
    return lines


def get_bet():
    while True:
        amount = input("Bet amount per line: ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between. {MIN_BET} - {MAX_BET}")
        else:
            print("Enter a number")
            
    return amount


def spin(balance):
    lines = get_num_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough to bet that much, your balance is: {balance}")
        else:
            break
        
    print(f"You are betting {bet} euros on {lines} lines. Total bet is equal to: {total_bet} Euros")    
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_win(slots, lines, bet, symbol_value)
    print(f"You won {winnings} euros")
    print(f"You won on lines: ", *winning_lines)
    
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is: {balance}")
        answer = input("Press enter to play (q to quit)")
        if answer == "q":
            break
        balance += spin(balance)
        
    print(f"You left with: {balance}")


main()