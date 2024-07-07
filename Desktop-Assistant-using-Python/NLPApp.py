import google.generativeai as genai

class NLPModel:

  def get_model(self):
    genai.configure(api_key = "AIzaSyATC2sKaSNhQCe9ArHNn7CuE-_AWlJRrj8")
    model = genai.GenerativeModel("gemini-pro")

    return model


class NLPApp(NLPModel):
  def __init__(self):
    self.__database = {}
    self.__first_menu()

  def __first_menu(self):
    first_input = input("""
    Hi! How would you like to proceed?

    1. Not a member? Register
    2. Already a member? Login
    3. I think you have entered a wrong window! Exit

    """)

    if first_input == '1':
      #register
      self.__register()

    elif first_input == '2':
      #login
      self.__login()

    else:
      exit()

  def __second_menu(self):
    second_input = input("""
    Hi! How would you like to proceed?

    1. Sentiment Analysis
    2. Language Translation
    3. Language Detection

    """)

    if second_input == '1':
      #Sentiment Analysis
      self.__sentiment_analysis()

    elif second_input == '2':
      #Language Translation
      self.__language_translation()

    elif second_input == '3':
      #Language Detection
      self.__language_detection()

    else:
      exit()


  def __register(self):
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    if email in self.__database:
      print("Your email already exists")

    else:
      self.__database[email] = [name, password]
      print("Registration successful. Now you can login!")
      print(self.__database)
      self.__first_menu()

  def __login(self):
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    if email in self.__database:
      if self.__database[email][1] == password:
        print("Login successful")
        self.__second_menu()

      else:
        print("Wrong password, Try again!")
        self.__login()

    else:
      print("This email is not registered")
      self.__first_menu()


  def __sentiment_analysis(self):
    user_text = input("Enter your text: ")
    model = super().get_model()
    response = model.generate_content(f"Give me the sentiment of this sentence: {user_text}")
    results = response.text
    print(results)
    self.__second_menu()

  def __language_translation(self):
    user_text = input("Enter your text: ")
    model = super().get_model()
    response = model.generate_content(f"Give me hindi translation of this sentence: {user_text}")
    results = response.text
    print(results)
    self.__second_menu()

  def __language_detection(self):
    user_text = input("Enter your text: ")
    model = super().get_model()
    response = model.generate_content(f"Detect the language of this sentence: {user_text}")
    results = response.text
    print(results)
    self.__second_menu()