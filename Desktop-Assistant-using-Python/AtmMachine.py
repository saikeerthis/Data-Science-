class Atm:
  # constructor (special function ) - superpower
  def __init__(self):
    self.pin = ""
    self.balance = 0
    self.menu()

#class Atm2:
  # constructor (special function ) - superpower
  #def __init__(self):
    #self.pin = ""
    #self.balance = 0
    

  def menu(self):
      user_input = input(
          """
      Hi how can I help you?

      1. Press 1 to create pin
      2. Press 2 to change pin 
      3. Press 3 to check balance
      4. Press 4 to withdraw
      5. Anything to exit
      """
  )
      if user_input == '1':
        # create pin
        self.create_pin()

      elif user_input == '2':
        # change pin
        self.change_pin()

      elif user_input == '3':
        # check baalnce
        self.check_balance()

      elif user_input == '4':
        # withdraw
        self.withdraw()

      else:
        exit()

  def create_pin(self):
    user_pin = input("Please create a Pin Number: ")
    self.pin = user_pin

    user_balance = int(input("Enter Balance: "))
    self.balance = user_balance

    print("Pin created successfully")
    self.menu()

  def change_pin(self):
    old_pin = input("Enter old pin: ")

    if old_pin == self.pin:
      # Let change the pin
      new_pin = input("Enter the new pin: ")
      self.pin = new_pin
      print("Pin changed successfully!")
      self.menu()

    else:
        print("Sorry you entered wrong pin!")
        self.menu()

  def check_balance(self):
    user_pin = input("Enter your pin: ")
    if user_pin == self.pin:
      print(f"Your balance is: {self.balance}")
      self.menu()
    else:
      print("Your Pin is not correct!")
      self.menu()

  def withdraw(self):
    user_pin = input("Enter your Pin: ")
    if user_pin == self.pin:
      # allow to withdraw
      amount = int(input("Enter the amount you want to withdraw: "))
      if amount <= self.balance:
        self.balance = self.balance - amount
        print(f"Withdraw successful and the current balance is: {self.balance}")

      else:
        print("You have insufficient balance!")

    else:
      print("Your Pin is wrong")
    self.menu()

  def exit(self):
    pass


      


obj = Atm()
#obj.menu()
#obj.pin
#obj.balance