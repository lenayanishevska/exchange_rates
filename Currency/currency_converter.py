exchange_rates = {
    ('USD',  'EUR'): 0.94,
    ('USD', 'UAH'): 38.0,
    ('USD', 'PLN'): 4.22,
    ('EUR', 'USD'): 1 / 0.94,
    ('EUR', 'UAH'): 38.0 / 0.94,
    ('EUR', 'PLN'): 4.22 / 0.94,
    ('UAH', 'USD'): 1 / 38.0,
    ('UAH', 'EUR'): 0.94 / 38.0,
    ('UAH', 'PLN'): 4.22 / 38.0,
    ('PLN', 'USD'): 1 / 4.22,
    ('PLN', 'EUR'): 0.94 / 4.22,
    ('PLN', 'UAH'): 38.0 / 4.22
}


def convert_currency(amount, from_currency, to_currency):

    if from_currency == to_currency:
        return amount

    if (from_currency, to_currency) in exchange_rates:
        rate = exchange_rates[(from_currency, to_currency)]
    else:
        raise ValueError("Can't convert this currency!")

    converted_amount = amount * rate
    return converted_amount
