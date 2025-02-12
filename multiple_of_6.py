def get_multiple_6() :
    """
    resturns a multiple of 6 that was entered by the user.
    :return: int a number
    """
    while True:
        try:
            n = input("Please give me a multiple of 6:")
            n = int(n)
            if n % 6 == 0:
                return n
            elif n / 6 == n // 6:
                return n
            else:
                print("thats not a multiple of 6")
        except ValueError:
            print("you have not entered a number")





print(get_multiple_6())
