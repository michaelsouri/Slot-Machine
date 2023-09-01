import random

MAX_LINES = 3
MAX_BET = 10000
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

"""
Check if symbols match horizontally and pay out 
based on bet size of lines.
"""
def check_winnings(columns, lines, bet, values):
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

"""
Generate columns of symbols
"""
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:] # copy symbols list
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

"""
Print generated columns of symbols
"""
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()               

"""
User input for deposit amount
"""
def deposit(): 
    while True:
        amount = input("INSERT DEPOSIT AMOUNT: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("AMOUNT MUST BE GREATER AND 0.")
        else:
            print("PLEASE ENTER A NUMBER.")

    return amount        

"""
User input for number of lines to bet on
"""
def get_number_of_lines():
    while True:
        lines = input("ENTER THE NUMBER OF LINES TO BET ON (1-" + str(MAX_LINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("ENTER A VALID NUMBER OF LINES.")
        else:
            print("PLEASE ENTER A NUMBER.")

    return lines

"""
User input for amount bet on each line
"""
def get_bet():
    while True:
        amount = input("WHAT WOULD YOU LIKE TO BET ON EACH LINE? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"AMOUNT MUST BE BETWEEN ${MIN_BET} - ${MAX_BET}.")
        else:
            print("PLEASE ENTER A NUMBER.")

    return amount        

"""

"""
def spin(balance):      
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines  

        if total_bet > balance:
            print(f"YOU DO NO HAVE ENOUGH TO BET THAT AMOUNT, YOUR CURRENT BALANCE IS: ${balance}")
        else:
            break

    print(f"YOU ARE BETTING ${bet} on {lines} LINES. TOTAL BET IS: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"YOU WON ${winnings}!")
    print(f"YOU WON ON LINES:", *winning_lines)

    return winnings - total_bet

"""
User input to redeposit funds
"""
def re_deposit():
    re_deposit_answer = input("WOULD YOU LIKE TO DEPOSIT MORE? (Y/N): ").lower()
    if re_deposit_answer == "y":
        main()
    elif re_deposit_answer == "n":
        print("SEE YOU NEXT TIME.")    
        exit()
    else:
        print("PLEASE ENTER [Y] OR [N]")
        re_deposit()
               

def main():
    balance = deposit()
    while True:
        print(f"CURRENT BALANCE IS: ${balance}")
        
        if balance == 0:
            re_deposit()

        answer = input("PRESS [ENTER] TO PLAY / [Q] TO QUIT. ").lower()
        if answer == "q":
            print(f"YOU LEFT WITH: ${balance}")
            exit()
            
        balance += spin(balance)   
    

main()