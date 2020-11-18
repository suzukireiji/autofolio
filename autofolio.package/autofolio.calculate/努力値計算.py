def f():
    a = input("性格補正を掛けますか:")
    if a == "yes":
        from math import ceil
        try:
            x = input("目標値を入力してください:")
            y = input("種族値を入力してください:")
            x = int(x)
            x = ceil(x / 1.1)
            y = int(y)
            z = (x - y - 21) * 8 + 4
            if 0 <= z <= 252:
                print(z)
                f()
            else:
                print("不正な値です。再入力して下さい。")
                f()
        except ValueError:
            print("不正な値です。再入力して下さい。")
            f()

    else:
        try:
            x = input("目標値を入力してください:")
            y = input("種族値を入力してください:")
            x = int(x)
            y = int(y)
            z = (x - y - 21) * 8 + 4
            if 0 <= z <= 252:
                print(z)
                f()
            else:
                print("不正な値です。再入力して下さい。")
                f()
        except ValueError:
            print("不正な値です。再入力して下さい。")
            f()


f()
