import re

def main():
    txt = 'Each month, over 50 million developers come to Stack Overflow ' \
    'to learn, share their knowledge, and build their careers.'
    match = re.search(r'\w+n\w+', txt)
    print(match.group(0))  #依照條件式 找到第一個就停止
    finds = re.findall(r'\w+n\w+', txt)
    print(finds[1])  #依照條件  找到所有
    parts = re.split(r'\w+n\w+', txt)
    print(parts)   #依照條件分割字串
    parts = re.sub(r'\w+n\w+', '-----', txt)
    print(parts)  #依照條件   把條件變成'-----'


if __name__ == '__main__':
    main()