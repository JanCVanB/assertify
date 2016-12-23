from assertify import test

# Eventually automatic tests - for now manual after every variable modification
small = 2      ; test(name='small', value=small, line_number=4)
large = 20     ; test(name='large', value=large, line_number=5)
neggy = -2     ; test(name='neggy', value=neggy, line_number=6)
zilch = 0      ; test(name='zilch', value=zilch, line_number=7)

small *= 3     ; test(name='small', value=small, line_number=9)
large *= 3     ; test(name='large', value=large, line_number=10)
neggy -= small ; test(name='neggy', value=neggy, line_number=11)
zilch *= 3     ; test(name='zilch', value=zilch, line_number=12)

small *= 3     ; test(name='small', value=small, line_number=14)
large *= 3     ; test(name='large', value=large, line_number=15)
neggy -= small ; test(name='neggy', value=neggy, line_number=16)
extra = 1      ; test(name='extra', value=extra, line_number=17)
zilch += extra ; test(name='zilch', value=zilch, line_number=18)
