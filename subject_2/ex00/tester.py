from give_bmi import give_bmi, apply_limit

# Tester from subject
# height = [2.71, 1.15]
# weight = [165.3, 38.4]
#
# bmi = give_bmi(height, weight)
# print(bmi, type(bmi))
# print(apply_limit(bmi, 26))

def run_tests(name, func, *args, expect_exception=None):
    print(f"\n-- {name} --")
    try:
        result = func(*args)
        if expect_exception:
            print(f"x Expected {expect_exception} but got result: {result}")
        else:
            print(f"✅ Result: {result}")
    except Exception as e:
        if expect_exception and type(e).__name__ == expect_exception:
            print(f"✅ Correct exception: {type(e).__name__}: {e}")
        else:
            print(f"x Unexpected exception: {type(e).__name__}: {e}")

# 1. Subject tests
run_tests("Subject tests", give_bmi, [2.71, 1.15], [165.3, 38.4], expect_exception=None)
bmi = give_bmi([2.71, 1.15], [165.3, 38.4])
run_tests("Apply limit subject tests", apply_limit, bmi, 26, expect_exception=None)

# 2. Empty lists
run_tests("Empty Lists", give_bmi, [], [], expect_exception=None)

# 3. Mismatched Lenghts
run_tests("Mismatched Lenghts", give_bmi, [1.75, 1.00], [70], expect_exception="ValueError")

# 4. Non-list arguments
run_tests("Height not a list", give_bmi, "not a list", [70], expect_exception="TypeError")
run_tests("Weight not a list", give_bmi, [70], "not a list", expect_exception="TypeError")

# 5. Invalid types inside lists
run_tests("String in height", give_bmi, ["1.75", 1.00], [70, 80], expect_exception="TypeError")
run_tests("String in weight", give_bmi, [1.75, 1.00], ["70", 80], expect_exception="TypeError")
run_tests("Boolean in height", give_bmi, [1.75, True], [70, 80], expect_exception="TypeError")
run_tests("Boolean in weight", give_bmi, [1.75, 1.00], [True, 80], expect_exception="TypeError")

# 6. Zero / negative values
run_tests("Zero height", give_bmi, [1.75, 0], [70, 80], expect_exception="ValueError")
run_tests("Negative weight", give_bmi, [1.75, 1.00], [-70, 80], expect_exception="ValueError")

# 7. Very large numbers (should not overflow in Python)
run_tests("Very large numbers", give_bmi, [1e6, 1e6], [1e12, 1e12], expect_exception=None)

# 8. Mixed int/float (should be accepted)
run_tests("Mixed int/float", give_bmi, [175, 1.80], [70, 80], expect_exception=None)

# 9. apply limit extra tests
bmi_sample = [22.5, 27.3, 18.9, 32.1]
run_tests("apply_limit with limit=25", apply_limit, bmi_sample, 25, expect_exception=None)
run_tests("apply_limit with limit not int", apply_limit, bmi_sample, "25", expect_exception="TypeError")

print("\n=== All tests completed ===")


