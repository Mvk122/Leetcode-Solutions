import requests
from decimal import Decimal

def format_string(number_string):
    parts = number_string.split(".")
    current = ""
    for index, char in enumerate(reversed(parts[0])):
        if index % 3 == 0 and index != 0:
            current += ","
        current += char
    current = current[::-1]
    if len(parts) > 1:
        return f"${current}.{parts[1]}"
    else:
        return f"${current}.00"

def main(name, city):
    request_url = "https://jsonmock.hackerrank.com/api/transactions/"
    result = requests.get(f"{request_url}?page=1")
    pages = result.json()['total_pages']

    credit_amount = Decimal(0)
    debit_amount = Decimal(0)
    for page in range(1, pages):
        page_data = requests.get(f"{request_url}?page={page}").json()
        
        for response in page_data["data"]:
            if response['userName'] == name and response['location']['city'] == city:
                amount_string = response['amount'][1:].replace(",", "")
                amount_decimal = Decimal(amount_string)
                if response['txnType'] == "debit":
                    debit_amount = max(amount_decimal, debit_amount)
                else:
                    credit_amount = max(credit_amount, amount_decimal)

    return [format_string(str(credit_amount)), format_string(str(debit_amount))] 



if __name__ == "__main__":
    print(main("Bob Martin", "Brownlee"))