def check_palindrom(str):
    # продумал случай, если строка начинается с большой буквы
    str = str.lower()
    if str == str[::-1]:
        return True
    else:
        return False
print(check_palindrom('Шалаш'))