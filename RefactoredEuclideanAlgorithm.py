
class GCDCalculator:
    """
    A utility class to calculate the GCD of two positive integers using the Euclidean Algorithm.

    This class provides reusable functionality for finding the greatest common divisor (GCD)
    """



    def calculate_gcd(a, b):
        """
        Finds the GCD of two integers using the Euclidean Algorithm.

        Parameters:
        - a, b (int): Positive integers.

        Returns:
        - int: The GCD of 'a' and 'b'.
        """
        while b != 0:
            a, b = b, a % b
        return a

def get_user_input():
    """
    Accepts and validates the users input for two positive integers and
    returns a tuple of two integers if valid, None otherwise
    """
    
    try:  
        # Prompt user for the first and second numbers
        a = int(input("Please enter the first positive integer: "))
        b = int(input("Please enter the second positive integer: "))
        
        # Validate that both numbers are positive
        if a <= 0 or b <= 0:
            print("Error: Both numbers must be positive integers.")
            return None

        return a, b
    except ValueError:
        # Handle non-integer inputs
        print("Error: Please enter valid integers.")
        return None

if __name__ == "__main__":
    """
  Finds the GCD of two integers using the Euclidean Algorithm.
    """
    user_input = None
 
    # Continue prompting until valid input is received
    while user_input is None:
        user_input = get_user_input()

   # Compute the GCD using the GCDCalculator class
    gcd = GCDCalculator.calculate_gcd(user_input[0], user_input[1])
    
    # Display the result
    print(f"The GCD of {user_input[0]} and {user_input[1]} is: {gcd}")

