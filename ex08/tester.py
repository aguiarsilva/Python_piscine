#from time import sleep
#from tqdm import tqdm
#from Loading import ft_tqdm

#for elem in ft_tqdm(range(333)):
    #sleep(0.005)

#print()
#for elem in tqdm(range(333)):
    #sleep(0.005)

#print()

from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

def test_comparison(n, sleep_time, description):
    """Properly test both functions with fresh generators"""
    print(f"\n{description}")
    print(f"Testing: {n} iterations with {sleep_time}s sleep")
    print("-" * 50)
    
    print("Custom ft_tqdm:")
    for elem in ft_tqdm(range(n)):  # Create generator here, inside the test
        sleep(sleep_time)
    
    print("\nOriginal tqdm:")
    for elem in tqdm(range(n)):     # Create generator here
        sleep(sleep_time)
    
    print()

# Run tests
test_comparison(20, 0.1, "Test 1: 20 iterations, 0.1s sleep")
test_comparison(10, 0.05, "Test 2: 10 iterations, 0.05s sleep")
test_comparison(50, 0.01, "Test 3: 50 iterations, 0.01s sleep")
test_comparison(100, 0, "Test 4: 100 iterations, no sleep")


def test_edge_cases():
    """Test edge cases and special scenarios"""
    print("\n" + "="*50)
    print("EDGE CASE TESTS")
    print("="*50)
    
    # Test 1: Empty range
    print("\nTest: Empty range (no sleep)")
    print("-" * 50)
    print("Custom ft_tqdm:")
    for elem in ft_tqdm(range(0)):
        pass
    print("\nOriginal tqdm:")
    for elem in tqdm(range(0)):
        pass
    print()
    
    # Test 2: Medium-sized fast iteration
    test_comparison(100, 0.01, "Test: 100 iterations with 0.01s sleep")
    
    # Test 3: Larger dataset
    test_comparison(200, 0.005, "Test: 200 iterations with 0.005s sleep")
    
    # Test 4: Two sequential calls (verify cleanup)
    print("\nTest: Sequential calls (verify newlines)")
    print("-" * 50)
    print("Custom ft_tqdm - Call 1:")
    for elem in ft_tqdm(range(20)):
        sleep(0.01)
    print("\nCustom ft_tqdm - Call 2:")
    for elem in ft_tqdm(range(20)):
        sleep(0.01)
    print("\nOriginal tqdm - Call 1:")
    for elem in tqdm(range(20)):
        sleep(0.01)
    print("\nOriginal tqdm - Call 2:")
    for elem in tqdm(range(20)):
        sleep(0.01)
    print("✓ Both implementations completed with proper separation")


test_edge_cases()
