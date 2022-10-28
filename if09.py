def main(a):
    """
    The two-digit integer is given.
    Replace the digits of the number.
    True if the resulting number is less than or equal to the old number, otherwise return False.
    
    Args:
        a: integer
    Returns:
        boolean: True if the resulting number is less than or equal to the old number, otherwise return False.
    """
    b= a//10 + a%10*10
    if a > b :
        return True
    if a == b:
        return True
    else:
        return False
print(main(57))
print(main(21))
