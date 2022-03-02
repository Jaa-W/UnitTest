def power_num(number: float, power: int) -> float:
    """Raise the number to the power if number >=0 """
    
    # number can be int or float
    if not isinstance(number, int) and not isinstance(number, float):
        raise TypeError("The number can only be int or float")
    
    # power can be only be int
    if not isinstance(power, int):
        raise TypeError("The power can only be of int type")
    
    # only if number >= 0
    if number >= 0:
        return round(number ** power, 2)
    raise TypeError("The number canonly be >= 0")