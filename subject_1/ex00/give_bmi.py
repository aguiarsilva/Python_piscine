def give_bmi(height: list[int | float],
             weight: list[int | float]
             ) -> list[int | float]:
    '''
    Calculate the BMI (Body Mass Index) for each pair of height (m)
    and weight (kg)

    Takes 2 args:
        height: list of heights in meters
        weight: list of weights in kilograms

    Returns a list of BMI values (weight/height^2)
    '''
    if not isinstance(height, list) or not isinstance(weight, list):
        raise TypeError("Height and Weight must be lists")

    if len(height) != len(weight):
        raise ValueError("Height and Weight lists must have the same range!")

    for h, w in zip(height, weight):
        if not isinstance(h, (int, float)) or isinstance(h, bool):
            raise TypeError("All values must be int or float")
        if not isinstance(w, (int, float)) or isinstance(w, bool):
            raise TypeError("All values must be int or float")
        if h <= 0 or w <= 0:
            raise ValueError("All values must be positive numbers")

    return [w / (h ** 2) for h, w in zip(height, weight)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    '''
    This function checks if the BMI value exceeds the given limit.

    Takes 2 args:
        bmi: list of bmi values
        limit: Threshold to compare against.

    Returns a list of booleans (True if the BMI is above)
    '''
    if not isinstance(limit, int) or isinstance(limit, bool):
        raise TypeError("The limit must be an int")

    return [b > limit for b in bmi]
