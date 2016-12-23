from my_tests import TESTS


def test(name, value, line_number):
    """Call this function after changing a variable's value

    Eventually this function should be called automatically every time
    a variable changes its value, rather than called manually by developers.

    :name str: Variable name, for looking up the variable's expectations
    :value: Variable value, for comparing against the variable's expectations
    :line_number int: Line number in which the variable's value changes
    :returnvalue: None
    """

    if name not in TESTS:
        return

    try:
        assert TESTS[name]['test'](value)
    except AssertionError:
        print_prefix(line_number)
        print_problem(name, value, TESTS[name]['description'])


def print_prefix(line_number):
    print('Assertify found a problem on line {}:'.format(line_number))


def print_problem(name, value, test_description):
    print('   ', name, '({})'.format(value), 'is not', test_description)
