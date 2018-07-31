import requests


def main():
    response = requests.get('https://www.google.com.tw/')
    print(response.status_code)
    print('-----------------------------------------------------------------------------------------------------------------------')
    print(response.headers)
    print('-----------------------------------------------------------------------------------------------------------------------')
    print(response.text)
    print('-----------------------------------------------------------------------------------------------------------------------')
    print(response.content)
    print('-----------------------------------------------------------------------------------------------------------------------')


if __name__ == '__main__':
    main()