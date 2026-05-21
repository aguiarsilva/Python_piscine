from array2D import slice_me


family = [[1.80, 78.4],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]

# Subject tests
# print(slice_me(family, 0, 2))
# print(slice_me(family, 1, -2))

def print_separator():
    print("\n" + "="*60)

print("="*60)
print("Slice_me function tester")
print("="*60)

# Test case 1: Subject slice - basic positive
print_separator()
print("Test 1: Basic slice (0, 2)")
print("-" * 40)
print(slice_me(family, 0, 2))

# Test case 2: Subject slice - negative indices
print_separator()
print("Test 2: Negative indices (1, -2)")
print("-" * 40)
print(slice_me(family, 1, -2))

# Test case 3: Empty list (start == end)
print_separator()
print("Test 3: Empty slice (2, 2)")
print ("-" * 40)
print(slice_me(family, 2, 2))

# Test case 4: Start beyond length
print_separator()
print("Test 4: Start beyond length (5, 7)")
print("-" * 40)
try:
    print(slice_me(family, 5, 7))
except Exception as e:
    print(f"❌ Expected Error: {type(e).__name__}: {e}")

# Test case 5: End beyond length
print_separator()
print("Test 5: End beyond length (1, 10)")
print("-" * 40)
print(slice_me(family, 1, 10))

# Test case 6: Negative start
print_separator()
print("Test 6: Negative start (-3, -1)")
print("-" * 40)
print(slice_me(family, -3, -1))

# Test case 7: Full slice (ommiting start/end equivalent)
print_separator()
print("Test 7: Full slice (0, len)")
print("-" * 40)
print(slice_me(family, 0, len(family)))

# Error Handling tests

# Test case 8: Invalid family type
print_separator()
print("Test 8: Invalid family type (not a list)")
print("-" * 40)
try:
    print(slice_me("not a list", 0, 2))
except Exception as e:
    print(f"✅ Correct error: {type(e).__name__}: {e}")

# Test case 9: Invalid start type
print_separator()
print("Test 9: Invalid start type (string)")
print("-" * 40)
try:
    print(slice_me(family, "0", 2))
except Exception as e:
    print(f"✅ Correct error: {type(e).__name__}: {e}")

# Test case 10: Invalid end type
print_separator()
print("Test 10: Invalid end type (float)")
print("-" * 40)
try:
    print(slice_me(family, 0, 2.5))
except Exception as e:
    print(f"✅ Correct error: {type(e).__name__}: {e}")

# Test case 11: Empty family
print_separator()
print("Test 11: Empty family list")
print("-" * 40)
try:
    print(slice_me([], 0, 2))
except Exception as e:
    print(f"✅ Correct error: {type(e).__name__}: {e}")

# Test case 12: Non-matrix family (rows of diff lengths
print_separator()
print("Test 12: Invalid matrix (rows of different lengths)")
print("-" * 40)
invalid_family = [[1.80, 78.4, 75],[2.15, 102.7],[1.88, 75.2]]
try:
    print(slice_me(invalid_family, 0, 2))
except Exception as e:
    print(f"✅ Correct error: {type(e).__name__}: {e}")

# Test case 13: Single row matrix
print_separator()
print("Test 13: Single row matrix")
print("-" * 40)
single_row = [[1.80, 78.4]]
print(slice_me(single_row, 0, 1))

# Test case 14: Large numbers and edge cases
print_separator()
print("Test 14: Large numbers matrix")
print("-" * 40)
large_family = [[i, i**2] for i in range(1, 101)]
print(f"Created matrix with {len(large_family)} rows")
result = slice_me(large_family, 10, 20)
print(f"Sliced 10 rows: {len(result)} rows returned")



