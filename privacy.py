def print_document(pages):
    flag = False
    for i in pages:
        if "Секретно" not in i:
            print(i)
        else:
            flag = True
            break
    if not flag:
        print("Напечатано без купюр")
    else:
        print('Дальнейшие материалы засекречены')
