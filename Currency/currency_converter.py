exchange_rates = {
    'USD': 1.0,
    'EUR': 0.85,
    'GBP': 0.73,
    'JPY': 113.94,
    'CAD': 1.27,
}


def convert_currency(amount, from_currency, to_currency):

    if from_currency not in exchange_rates:
        raise ValueError("Can't convert this currency!")
    if to_currency not in exchange_rates:
        raise ValueError("Can't convert this currency!")
    
    source_rate = exchange_rates[from_currency]
    target_rate = exchange_rates[to_currency]

    converted_amount = amount * (target_rate / source_rate)
    return converted_amount
    
