from forex_python.converter import CurrencyRates
from forex_python.bitcoin import BtcConverter
currency = CurrencyRates()

def currencyConversion():
  option = input("""Choose the conversion option \n1 --> Currency to currency \n2 --> Bitcoin to currency \n """).upper()
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






  #{"date":"2022-03-09","base":"EUR","rates":{"USD":1.0993,"JPY":127.31,"BGN":1.9558,"CZK":25.364,"DKK":7.444,"GBP":0.8357,"HUF":379.66,"PLN":4.8196,"RON":4.9485,"SEK":10.734,"CHF":1.0198,"ISK":145.3,"NOK":9.798,"HRK":7.5625,"TRY":16.1323,"AUD":1.4991,"BRL":5.5201,"CAD":1.4108,"CNY":6.9454,"HKD":8.5974,"IDR":15710.06,"INR":84.2025,"KRW":1357.08,"MXN":23.2145,"MYR":4.6028,"NZD":1.6055,"PHP":57.259,"SGD":1.4966,"THB":36.326,"ZAR":16.656}}

if __name__ == '__main__':
    currencyConversion()