from ft_filter import ft_filter


def main():
    # Test 1: filter even numbers
    result = list(ft_filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]))
    print("Even numbers:", result)
    assert result == [2, 4, 6]

    # Test 2: function is None → keep truthy values
    result = list(ft_filter(None, [0, 1, "", "hello", None, 42]))
    print("Truthy values:", result)
    assert result == [1, "hello", 42]

    # Test 3: empty iterable
    result = list(ft_filter(lambda x: x > 0, []))
    print("Empty:", result)
    assert result == []

    # Test 4: compare with built-in filter
    data = [1, 2, 3, 4, 5]
    result = list(ft_filter(lambda x: x > 2, data))
    print("Greater than 2:", result)
    assert result == list(filter(lambda x: x > 2, data))

    print("\nAll tests passed!")


if __name__ == "__main__":
    main()