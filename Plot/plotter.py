import matplotlib.pyplot as plt

dates = [i for i in range(2000, 2023)]


def plot_exchange_rate(exchange_rates):
    plt.figure(figsize=(10, 6))
    plt.plot(dates, exchange_rates, marker='o', linestyle='-')
    plt.title('UAH/USD Exchange Rate Since 2000')
    plt.xlabel('Year')
    plt.ylabel('Exchange Rate')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
