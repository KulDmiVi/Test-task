import re


def check_string(math_operation: str) -> str:
    if re.fullmatch(r'^([1-9]|10) [-+*/] ([1-9]|10)$', math_operation.strip()):
        return math_operation.replace(' ', '')
    else:
        raise ValueError


def main(operation: str) -> int:
    try:
        return int(eval(check_string(operation)))
    except ValueError as e:
        print('Строка не соотвествует формату. Попробуйте еще раз!')


if __name__ == '__main__':
    print('КАЛЬКУЛЯТОР')
    print('Программа для выполнения простых арифметических операций (+, -, *, /)')
    print('над целыми от 1 до 10')
    input_string = input('Введите строку содержащую выражение например "1 + 2":\n')
    result = main(input_string)
    if result is not None:
        print(result)
