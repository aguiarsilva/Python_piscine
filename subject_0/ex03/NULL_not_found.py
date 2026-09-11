def NULL_not_found(object: any) -> int:
    """
    This function prints the type of null-like objects.
    Returns 0 on success, 1 on error.
    """
    if object is None:
        print(f"Nothing: {object} {type(object)}")
        return 0

    if isinstance(object, float) and object != object:
        print(f"Cheese: {object} {type(object)}")
        return 0

    if type(object) is int and not isinstance(object, bool) and object == 0:
        print(f"Zero: {object} {type(object)}")
        return 0

    if isinstance(object, str) and object == "":
        print(f"Empty: {type(object)}")
        return 0

    if type(object) is bool and object is False:
        print(f"Fake: {object} {type(object)}")
        return 0

    print("Type not found")
    return 1
