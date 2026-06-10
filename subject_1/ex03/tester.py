from contextlib import redirect_stdout
from io import StringIO
from NULL_not_found import NULL_not_found


def check_case(label, value, expected_output, expected_return):
    buffer = StringIO()
    with redirect_stdout(buffer):
        result = NULL_not_found(value)

    output = buffer.getvalue()
    assert output == expected_output, (
        f"{label}: unexpected output\n"
        f"expected: {expected_output!r}\n"
        f"got:      {output!r}"
    )
    assert result == expected_return, (
        f"{label}: unexpected return value\n"
        f"expected: {expected_return!r}\n"
        f"got:      {result!r}"
    )
    print(f"{label}: OK")


check_case("Nothing", None, "Nothing: None <class 'NoneType'>\n", 0)
check_case("Garlic", float("NaN"), "Cheese: nan <class 'float'>\n", 0)
check_case("Zero", 0, "Zero: 0 <class 'int'>\n", 0)
check_case("Empty", "", "Empty: <class 'str'>\n", 0)
check_case("Fake", False, "Fake: False <class 'bool'>\n", 0)
check_case("True", True, "Type not found\n", 1)
check_case("Float zero", 0.0, "Type not found\n", 1)
check_case("Regular string", "Brian", "Type not found\n", 1)


# Tester from subject sheet
# Nothing = None
# Garlic = float("NaN")
# Zero = 0
# Empty = ""
# Fake = False
# NULL_not_found(Nothing)
# NULL_not_found(Garlic)
# NULL_not_found(Zero)
# NULL_not_found(Empty)
# NULL_not_found(Fake)
# print(NULL_not_found("Brian"))
