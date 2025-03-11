from random import shuffle, randint

numbers = ["0","1","2","3","4","5","6","7","8","9"]
lowercase_letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
uppercase_letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
special_symbols = ["~","!","@","#","$","%","&","*","(",")","{","}","[","]","_","-","+","=","|","\\","/",";",":","?",",",".","<",">","'",]

# Just a list to catch different ways of responding "yes" in the terminal.
accept_question = ["Y","y","YES","yes","Yes","Ye","YE","ye"]

# Asks the user what kinds of symbols should be included in the password.
chosen_symbols = []
if input("Include numbers? (Y/N): ") in accept_question:
    chosen_symbols = chosen_symbols + numbers

if input("Include lowercase letters? (Y/N): ") in accept_question:
    chosen_symbols = chosen_symbols + lowercase_letters

if input("Include uppercase letters? (Y/N): ") in accept_question:
    chosen_symbols = chosen_symbols + uppercase_letters

if input("Include special characters? (Y/N): ") in accept_question:
    chosen_symbols = chosen_symbols + special_symbols

#In case no symbols were selected, the program will throw an error and quit.
if len(chosen_symbols) == 0:
    print("No types of symbols were ever chosen, cannot continue. Please restart the program if this was a mistake.")
    exit()

# The list of chosen symbols is shuffled just to add some extra "pseudo-randomness", 
# even though it probably doesn't actually do anything.
shuffle(chosen_symbols)
chosen_symbols_length = len(chosen_symbols)

# Asks the user how long the password should be.
password_length = int(input("How long should the password be? "))

# Create the list of letters for the final list, and append n amount of randomly choses symbols to it, 
# corresponding to the inputted length.
final_password_list = []
n = password_length
while n > 0:
    final_password_list.append(chosen_symbols[randint(0,chosen_symbols_length-1)])
    n = n - 1

# The list containing the password sequence is converted to a string and printed.
final_password = str("".join(final_password_list))
print(f"\nGenerated password:\n{final_password}")

# Keep the terminal window open until the user presses Enter.
input("\nPress Enter to exit...")