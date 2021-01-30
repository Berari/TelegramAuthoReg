import requests

api_key = 'b720Af9f1b59bf58ebbc91f8b5404A77'

#a = requests.get(f'https://sms-activate.ru/stubs/handler_api.php?api_key={api_key}&action=getBalance').text
service = 'tg'

a = requests.get(f'https://sms-activate.ru/stubs/handler_api.php?api_key={api_key}&action=getNumber&service={service}').text

print(a)
