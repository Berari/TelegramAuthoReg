import requests


class SmsActive:

    def __init__(self, API_KEY): 
        
        self.api_key = API_KEY

    def balance(self, mode = 2):
        
        balance = requests.get(f'https://sms-activate.ru/stubs/handler_api.php?api_key={self.api_key}&action=getBalance').text
        

        if mode == 1:
            return balance

        if mode == 2:

             balance = balance.split(':')[1]
             return float(balance)
    
    def get_phone_number(self, service, mode = 'all'):

        data = requests.get(f'https://sms-activate.ru/stubs/handler_api.php?api_key={self.api_key}&action=getNumber&service={service}').text
        #data = 'ACCESS_NUMBER:387759514:79038446907'

        phone_and_ip = data.split(':')
        id = phone_and_ip[1]
        phone = phone_and_ip[2]

        if mode == 'all':
            data_list = []

            data_list.append(id)
            data_list.append(phone)

            return data_list

        if mode == 'id':
            return id

        if mode == 'phone':
            return phone

    def changing_activation_status(self, id, status):
        data = requests.get(f'https://sms-activate.ru/stubs/handler_api.php?api_key={self.api_key}&action=setStatus&status={status}&id={id}')                           

        return data.text

    def get_activation_status(self, id):

        data = requests.get(f'https://sms-activate.ru/stubs/handler_api.php?api_key={self.api_key}&action=getStatus&id={id}')

        return data.txt

    def get_full_sms(self, id):
        status = SmsActive.get_activation_status(self, id)

        if status == 'STATUS_OK':

            sms = requests.get(f'https://sms-activate.ru/stubs/handler_api.php?api_key={self.api_key}&action=getFullSms&id={id}').text

            return sms

        else:
            a = 'EROR: sms not received'

            return a


def main():
    api_key = 'b720Af9f1b59bf58ebbc91f8b5404A77'

    sms = SmsActive(API_KEY = api_key)  #не работает с переадрисацией

    #print(sms.balance(mode = 2))
    #print(sms.get_phone_number(service = 'tg'))

if __name__ == '__main__':
    main()