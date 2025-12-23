print("""=======Welcome to Simple ATM=======
Available Options:
1) Pin Change
2) Balance Check
3) Withdraw
4) Deposit
5) Exit
""")

menu=input ("Enter your option: ")

if menu=="1":
    print("Pin Change")
elif menu=="2":
    print("Balance Chack")
elif menu=="3":
    print("withdraw")
elif menu=="4":
    print("Deposit")
elif menu=='5':
    print("Exit")
else:
    print("Invalid option. Please enter 1-5.")

# print("""======= Welcome to Simple ATM =======
# Available Options:
# 1) Pin Change
# 2) Balance Check
# 3) Withdraw
# 4) Deposit
# 5) Exit
# """)

# menu = input("Enter your option (1-5): ").strip()

# options = {
#     "1": "Pin Change",
#     "2": "Balance Check",
#     "3": "Withdraw",
#     "4": "Deposit",
#     "5": "Exit"
# }

# print(options.get(menu, "Invalid option. Please enter 1-5."))