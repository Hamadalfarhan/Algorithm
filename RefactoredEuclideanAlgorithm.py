
class GCDCalculator:
    """
    This class implements the Euclidean Algorithm to find the greatest common divisor (GCD).
    """



    def calculate_gcd(a, b):
        """
        Calculates the GCD of two positive integers using the Euclidean Algorithm.
        :param a: First positive integer
        :param b: Second positive integer
        :return: GCD of the two integers
        """
        while b != 0:
            a, b = b, a % b
        return a

def get_user_input():
    """
    Accepts and validates user input for two positive integers.
    :return: A tuple of two integers if valid, None otherwise
    """
    try:
        a = int(input("Please enter the first positive integer: "))
        b = int(input("Please enter the second positive integer: "))

        if a <= 0 or b <= 0:
            print("Error: Both numbers must be positive integers.")
            return None

        return a, b
    except ValueError:
        print("Error: Please enter valid integers.")
        return None

if __name__ == "__main__":
    user_input = None

    while user_input is None:
        user_input = get_user_input()

    gcd = GCDCalculator.calculate_gcd(user_input[0], user_input[1])
    print(f"The GCD of {user_input[0]} and {user_input[1]} is: {gcd}")

