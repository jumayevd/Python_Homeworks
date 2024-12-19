def invest(amount, rate, years):

    for year in range(1, years + 1):
        amount += amount * rate  
        print(f"Year {year}: ${amount:.2f}")

try:
    principal = float(input("Enter the initial amount: "))
    annual_rate = float(input("Enter the annual rate of return (as a decimal, e.g., 0.05 for 5%): "))
    num_years = int(input("Enter the number of years: "))

    print("\nInvestment Growth Over Time:")
    invest(principal, annual_rate, num_years)

except ValueError:
    print("Invalid input. Please enter numeric values.")
