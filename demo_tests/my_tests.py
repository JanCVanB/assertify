TESTS = {
    'small': {
        'description': 'between 0 and 10',
        'test': lambda x: 0 < x < 10
    },
    'large': {
        'description': 'between 10 and 100',
        'test': lambda x: 10 < x < 100
    },
    'neggy': {
        'description': 'between -10 and 0',
        'test': lambda x: -10 < x < 0
    },
    'zilch': {
        'description': 'equal to 0',
        'test': lambda x: x == 0
    }
}
