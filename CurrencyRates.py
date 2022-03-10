from forex_python.converter import CurrencyRates
from forex_python.bitcoin import BtcConverter
currency = CurrencyRates()

def currencyConversion():
  option = input("""Choose the conversion option \n1 --> Currency to Currency \n2 --> Bitcoin to Currency \n """).upper()
  print(option)
  if option == '1':
    from_Currrency = input("From Currency: ").upper()
    amount = int(input("Enter the amount: "))
    to_Currency = input("To Currency: ").upper()
    print(amount, from_Currrency, "to", to_Currency)
    result = currency.convert(from_Currrency, to_Currency, amount)
    print("Conversion Amount:", result)
  elif option == '2':
    b = BtcConverter()
    input_Currrency = input("Enter Currency: ").upper()
    result = b.get_latest_price(input_Currrency)
    print("1 Bitcoin = "+str(result)+ ' '+ input_Currrency)


if __name__ == '__main__':
    currencyConversion()