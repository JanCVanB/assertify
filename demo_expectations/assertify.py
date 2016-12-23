from my_expectations import EXPECTATIONS


def test(name, value, line_number):
    """Call this function after changing a variable's value

    Eventually this function should be called automatically every time
    a variable changes its value, rather than called manually by developers.

    :name str: Variable name, for looking up the variable's expectations
    :value: Variable value, for comparing against the variable's expectations
    :line_number int: Line number in which the variable's value changes
    :returnvalue: None
    """

    if name not in EXPECTATIONS:
        return

    if '=' in EXPECTATIONS[name]:
        comparator = EXPECTATIONS[name]['=']
        try:
            assert value == comparator
        except AssertionError:
            print_prefix(line_number)
            print_problem(name, value, '=', comparator)

    if '<' in EXPECTATIONS[name]:
        comparator = EXPECTATIONS[name]['<']
        try:
            assert value < comparator
        except AssertionError:
            print_prefix(line_number)
            print_problem(name, value, '<', comparator)

    if '>' in EXPECTATIONS[name]:
        comparator = EXPECTATIONS[name]['>']
        try:
            assert value > comparator
        except AssertionError:
            print_prefix(line_number)
            print_problem(name, value, '>', comparator)


def print_prefix(line_number):
    print('Assertify found a problem on line {}:'.format(line_number))


def print_problem(name, value, comparison, comparator):
    print('   ', name, '({})'.format(value), 'is not', comparison, comparator)
