print("""
===Welcome to Simple Atm===
      Available Options to select:
      1)Pin Change
      2)Balance Check
      3)Withdraw
      4)Deposit
      5)Exit
""")

menu= input("Enter your option: ")

if menu =="1":
    print("PIN CHANGEE")
elif menu=="2":
    print("Balance Check")
elif menu=="3":
    print("Withdraw")
elif menu=="4":
    print("Deposit")
else:
    print("Exit")

menu2=input ("Anything else?")
