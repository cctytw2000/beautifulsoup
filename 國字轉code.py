import urllib.parse as UP

def main():
 while 1 :   #讓他 可以不中斷程式
    val = input("請輸入國字:")
    quote_val = UP.quote(val)    #把  VAL 裡面的中文用quote轉成電腦語言
    print(quote_val)
    val = UP.unquote(quote_val)  #把   電腦語言用unquote轉成中文
    print(val)


if __name__ == '__main__':
    main()