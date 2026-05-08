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
