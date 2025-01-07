conversion_rates = {
    'USD': {'EUR': 0.94, 'GBP': 0.82, 'INR': 83.2, 'AUD': 1.51, 'JPY': 150.3, 'CAD': 1.34},
    'EUR': {'USD': 1.06, 'GBP': 0.87, 'INR': 88.3, 'AUD': 1.61, 'JPY': 159.7, 'CAD': 1.42},
    'GBP': {'USD': 1.22, 'EUR': 1.15, 'INR': 101.6, 'AUD': 1.85, 'JPY': 182.1, 'CAD': 1.63},
    'INR': {'USD': 0.012, 'EUR': 0.011, 'GBP': 0.0098, 'AUD': 0.018, 'JPY': 1.79, 'CAD': 0.016},
    'AUD': {'USD': 0.66, 'EUR': 0.62, 'GBP': 0.54, 'INR': 55.5, 'JPY': 98.5, 'CAD': 0.89},
    'JPY': {'USD': 0.0067, 'EUR': 0.0063, 'GBP': 0.0055, 'INR': 0.56, 'AUD': 0.010, 'CAD': 0.009},
    'CAD': {'USD': 0.75, 'EUR': 0.71, 'GBP': 0.61, 'INR': 61.8, 'AUD': 1.12, 'JPY': 110.4}
}

def convert_currency(amount, from_currency, to_currency):
    """Converts amount from one currency to another."""
    if from_currency == to_currency:
        return amount
    try:
        conversion_rate = conversion_rates[from_currency][to_currency]
        return amount * conversion_rate
    except KeyError:
        return "Invalid currency code or conversion not available."

def main():
    # Input from the user
    amount = float(input("Enter amount: "))
    from_currency = input("Enter from currency (USD, EUR, GBP, INR, AUD, JPY, CAD): ").upper()
    to_currency = input("Enter to currency (USD, EUR, GBP, INR, AUD, JPY, CAD): ").upper()

    # Perform conversion
    result = convert_currency(amount, from_currency, to_currency)
    
    # Display result
    if isinstance(result, str):
        print(result)
    else:
        print(f"{amount} {from_currency} is equal to {result:.2f} {to_currency}.")

# Run the main function
if __name__ == "__main__":
    main()
