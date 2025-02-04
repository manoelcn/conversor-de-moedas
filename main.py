from clients import CoinConversorService


client = CoinConversorService()
conversion = client.converter('USD', 'BRL')

print(conversion)