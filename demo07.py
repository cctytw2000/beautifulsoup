import xml.etree.ElementTree as ET


def main():
    tree = ET.parse('demo07.xml')
    # 取得demo07.XMl
    root = tree.getroot()
    # 找跟節點
    print(root)
    for node in root:
        # 找ROOT的跟節點
        print(node)
        print('-------------------------')
        for a in node:
            print(a)


if __name__ == '__main__':
    main()
