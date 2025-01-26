
class GCDCalculator:
    
    # A utility class to calculate the GCD of two positive integers using the Euclidean Algorithm.
    # This class provides reusable functionality for finding the greatest common divisor (GCD) and the least common multiple (LCM)
    
    @staticmethod
    def calculate_gcd(a, b):
        """
        Finds the GCD of two integers using the Euclidean Algorithm.
        """
        while b != 0:
            a, b = b, a % b
        return a

   
    @staticmethod
    def calculate_lcm(a, b):
        """Calculate the Least Common Multiple (LCM) using the GCD."""
        return abs(a * b) // GCDCalculator.calculate_gcd(a, b)
    

def get_user_input():
    """
    Accepts and validates the users input for two positive integers and
    returns a tuple of two integers if valid, None otherwise
    """
    while True:
       try:  
           # Prompt user for the first and second numbers
           a = int(input("Please enter the first positive integer: "))
           b = int(input("Please enter the second positive integer: "))
        
           # Validate that both numbers are positive
           if a <= 0 or b <= 0:
               print("Invalid input: Both numbers must be positive integers.")
           elif a > 1_000_000_000 or b > 1_000_000_000:
               print("Error: Numbers are too large. Please enter values below 1,000,000,000.")   
           else:
                return a, b    
       except ValueError:
           print("Invalid input: Please enter valid integers.")
        


if __name__ == "__main__":
    print("Welcome to the GCD Calculator!")
    
  # Finds the GCD of two integers using the Euclidean Algorithm.
    
    user_input = None
 
    # Continue prompting until valid input is received
    while user_input is None:
        user_input = get_user_input()

   # Compute the GCD using the GCDCalculator class
    gcd = GCDCalculator.calculate_gcd(user_input[0], user_input[1])
    lcm = GCDCalculator.calculate_lcm(user_input[0], user_input[1])

    # Display the results
    print(f"The greatest common divisor (GCD) of {user_input[0]} and {user_input[1]} is: {gcd}.")
    print(f"The least common multiple (LCM) of {user_input[0]} and {user_input[1]} is: {lcm}.")
