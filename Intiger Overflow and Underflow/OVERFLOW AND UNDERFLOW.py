import sys

def demonstrate_overflow():
    max_int = sys.maxsize  # Maximum size of an integer on this system
    overflow_value = max_int + 1
    print(f"Overflowed value: {overflow_value}")

def demonstrate_underflow():
    min_int = -sys.maxsize - 1  # Minimum size of an integer on this system
    underflow_value = min_int - 1
    print(f"Underflowed value: {underflow_value}")

# Demonstrate overflow
print("=== Overflow Example ===")
demonstrate_overflow()

# Demonstrate underflow
print("\n=== Underflow Example ===")
demonstrate_underflow()
