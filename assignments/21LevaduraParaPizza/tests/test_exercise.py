def main():

    gramos = int(input("Dame la harina en gramos: "))
    harina  = gramos  *  .050
    harina = round(harina,1)
    print("Necesitas estos gramos de levadura:",harina)


if __name__ == '__main__':
    main()
