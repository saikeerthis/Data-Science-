def odd_even(number):
    """This function returns value based on odd or even"""
    if type(number) == int:
        if number%2 == 0:
            print("even")
        else:
            print("odd")
        
    else:
        print("are you mad?")

odd_even(22)