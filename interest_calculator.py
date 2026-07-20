def calculate_simple_interest(principal, rate, time):
    """
    Calculate simple interest.

    Formula: SI = (P * R * T) / 100

    Parameters:
        principal (float): The initial amount of money (P)
        rate (float): Annual interest rate in percent (R)
        time (float): Time period in years (T)

    Returns:
        float: The simple interest amount
    """
    simple_interest = (principal * rate * time) / 100
    return simple_interest


def main():
    print("=== Simple Interest Calculator ===")

    try:
        principal = float(input("Enter principal amount: "))
        rate = float(input("Enter annual interest rate (%): "))
        time = float(input("Enter time period (years): "))

        interest = calculate_simple_interest(principal, rate, time)
        total_amount = principal + interest

        print(f"\nSimple Interest: {interest:.2f}")
        print(f"Total Amount (Principal + Interest): {total_amount:.2f}")

    except ValueError:
        print("Invalid input. Please enter numeric values only.")


if __name__ == "__main__":
    main()
