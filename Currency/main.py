from currency_converter import convert_currency

while True:
    try:
        amount = float(input("Enter the amount: "))
        from_currency = input("Enter the source currency: ").upper()
        to_currency = input("Enter the currency to convert to: ").upper()

        result = convert_currency(amount, from_currency, to_currency)
        print(f"{amount} {from_currency} = {result:.2f} {to_currency}")
        break
    except ValueError as e:
        print(f"Error: {e}.Try again!")
