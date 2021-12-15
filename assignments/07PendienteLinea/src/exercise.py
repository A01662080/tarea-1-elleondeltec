def main():

    x1 = float(input("Dame x1: "))
    y1 = float(input("Dame y1: "))
    x2 = float(input("Dame x2: "))
    y2 = float(input("Dame y2: "))
    m = oper(x1,y1,x2,y2)
    print(m)

def oper(x1,y1,x2,y2):
    numerador = y2-y1
    denominador = x2-x1
    m = numerador/denominador
    return m

if __name__ == '__main__':
    main()
