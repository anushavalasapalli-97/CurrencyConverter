from forex_python.bitcoin import BtcConverter


def currencyConversion():

  print("Converting 1 Bitcoin price to Currency")
  b = BtcConverter()
  input_Currrency = input("Enter Currency: ").upper()
  result = b.get_latest_price(input_Currrency)
  print("1 Bitcoin = "+str(result)+ ' '+ input_Currrency)


if __name__ == '__main__':
    currencyConversion()