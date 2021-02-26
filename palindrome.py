def is_palindrome(given_str: str) -> bool:
    """
        Принимает строки из заглавных и строчных букв с пробелами.
        Убирает из строки все пробелы.
        Конвертирует все буквы в строчные.
        Возвращает True, если полученная строка читается слева направо и справа налево одинаково.
        Возвращает True, если строка пустая.
    """
    lowercase_str = given_str.lower()
    lowercase_no_space_str = lowercase_str.replace(" ", "")
    return lowercase_no_space_str == lowercase_no_space_str[::-1]


is_palindrome("Вернет False от этой строки")


assert is_palindrome("топор") == False, "это не палиндром – функция должна вернуть False"
assert is_palindrome("А роза упала на лапу Азора") == True, "это палиндром – функция должна вернуть True"
assert is_palindrome("") == True, "это пустая строка – функция должна вернуть True"
