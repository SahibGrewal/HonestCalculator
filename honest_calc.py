a = ["+", "-", "*", "/"]
msg = ""


def check():
    msg = ""
    if is_one_digit(x) and is_one_digit(y) == True:
        msg = msg + " ... lazy"
    if x == 1 or y == 1 and oper == "*":
        msg = msg + " ... very lazy"
    if (x == 0 or y == 0) and (oper == "*" or oper == "+" or oper == "-"):
        msg = msg + " ... very, very lazy"
    if msg != "":
        msg = "You are" + msg
    print(msg)


def is_one_digit(v):
    try:
        if -10 < v < 10 and v == int(v):
            return True
    except Exception:
        return False


while True:
    print("Enter an equation")
    calc = input()
    x, oper, y = calc.split()

    if x == "M":
        x = M
    if y == "M":
        y = M


    try:
        float(x)
        float(y)
        if oper in a:
            x = float(x)
            y = float(y)
            check()
            if oper == "+":
                result = x + y
                print(result)
                store = input("Do you want to store the result? (y / n):")
                if store == "y" and is_one_digit(result) == True:
                    sure1 = input("Are you sure? It is only one digit! (y / n)")
                    if sure1 == "y":
                        sure2 = input("Don't be silly! It's just one number! Add to the memory? (y / n)")
                        if sure2 == "y":
                            sure3 = input("Last chance! Do you really want to embarrass yourself? (y / n)")
                            if sure3 == "y":
                                M = result
                                cont = input("Do you want to continue calculations? (y / n):")
                                if cont == "y":
                                    pass
                                else:
                                    break
                            else:
                                cont = input("Do you want to continue calculations? (y / n):")
                                if cont == "y":
                                    pass
                                else:
                                    break
                        else:
                            cont = input("Do you want to continue calculations? (y / n):")
                            if cont == "y":
                                pass
                            else:
                                break
                    else:
                        cont = input("Do you want to continue calculations? (y / n):")
                        if cont == "y":
                            pass
                        else:
                            break
                elif store == "y":
                    M = result
                    cont = input("Do you want to continue calculations? (y / n):")
                    if cont == "y":
                        pass
                    else:
                        break
                else:
                    cont = input("Do you want to continue calculations? (y / n):")
                    if cont == "y":
                        pass
                    else:
                        break
            elif oper == "-":
                result = x - y
                print(result)
                store = input("Do you want to store the result? (y / n):")
                if store == "y" and is_one_digit(result) == True:
                    sure1 = input("Are you sure? It is only one digit! (y / n)")
                    if sure1 == "y":
                        sure2 = input("Don't be silly! It's just one number! Add to the memory? (y / n)")
                        if sure2 == "y":
                            sure3 = input("Last chance! Do you really want to embarrass yourself? (y / n)")
                            if sure3 == "y":
                                M = result
                                cont = input("Do you want to continue calculations? (y / n):")
                                if cont == "y":
                                    pass
                                else:
                                    break
                            else:
                                cont = input("Do you want to continue calculations? (y / n):")
                                if cont == "y":
                                    pass
                                else:
                                    break
                        else:
                            cont = input("Do you want to continue calculations? (y / n):")
                            if cont == "y":
                                pass
                            else:
                                break
                    else:
                        cont = input("Do you want to continue calculations? (y / n):")
                        if cont == "y":
                            pass
                        else:
                            break
                elif store == "y":
                    M = result
                    cont = input("Do you want to continue calculations? (y / n):")
                    if cont == "y":
                        pass
                    else:
                        break
                else:
                    cont = input("Do you want to continue calculations? (y / n):")
                    if cont == "y":
                        pass
                    else:
                        break
            elif oper == "*":
                result = x * y
                print(result)
                store = input("Do you want to store the result? (y / n):")
                if store == "y" and is_one_digit(result) == True:
                    sure1 = input("Are you sure? It is only one digit! (y / n)")
                    if sure1 == "y":
                        sure2 = input("Don't be silly! It's just one number! Add to the memory? (y / n)")
                        if sure2 == "y":
                            sure3 = input("Last chance! Do you really want to embarrass yourself? (y / n)")
                            if sure3 == "y":
                                M = result
                                cont = input("Do you want to continue calculations? (y / n):")
                                if cont == "y":
                                    pass
                                else:
                                    break
                            else:
                                cont = input("Do you want to continue calculations? (y / n):")
                                if cont == "y":
                                    pass
                                else:
                                    break
                        else:
                            cont = input("Do you want to continue calculations? (y / n):")
                            if cont == "y":
                                pass
                            else:
                                break
                    else:
                        cont = input("Do you want to continue calculations? (y / n):")
                        if cont == "y":
                            pass
                        else:
                            break
                elif store == "y":
                    M = result
                    cont = input("Do you want to continue calculations? (y / n):")
                    if cont == "y":
                        pass
                    else:
                        break
                else:
                    cont = input("Do you want to continue calculations? (y / n):")
                    if cont == "y":
                        pass
                    else:
                        break
            elif oper == "/":
                result = x / y
                print(result)
                store = input("Do you want to store the result? (y / n):")
                if store == "y" and is_one_digit(result) == True:
                    sure1 = input("Are you sure? It is only one digit! (y / n)")
                    if sure1 == "y":
                        sure2 = input("Don't be silly! It's just one number! Add to the memory? (y / n)")
                        if sure2 == "y":
                            sure3 = input("Last chance! Do you really want to embarrass yourself? (y / n)")
                            if sure3 == "y":
                                M = result
                                cont = input("Do you want to continue calculations? (y / n):")
                                if cont == "y":
                                    pass
                                else:
                                    break
                            else:
                                cont = input("Do you want to continue calculations? (y / n):")
                                if cont == "y":
                                    pass
                                else:
                                    break
                        else:
                            cont = input("Do you want to continue calculations? (y / n):")
                            if cont == "y":
                                pass
                            else:
                                break
                    else:
                        cont = input("Do you want to continue calculations? (y / n):")
                        if cont == "y":
                            pass
                        else:
                            break
                elif store == "y":
                    M = result
                    cont = input("Do you want to continue calculations? (y / n):")
                    if cont == "y":
                        pass
                    else:
                        break
                else:
                    cont = input("Do you want to continue calculations? (y / n):")
                    if cont == "y":
                        pass
                    else:
                        break
        else:
            print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
    except ValueError:
        print("Do you even know what numbers are? Stay focused!")
    except ZeroDivisionError:
        print("Yeah... division by zero. Smart move...")
