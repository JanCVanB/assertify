# Assertify

Assert the values of certain variables whenever you use or change them.


## Why

Do you like type checking? Well, this is one step further - "value checking".

It's like injecting your code with a lot of assertions -
you feel good knowing your important variables are always in a good state.

### The value of "value checking"

Type checking is, loosely, the process of testing a variable's type
whenever it is used or updated.
It can also be summarized as the process of checking that
a function's parameters and return values are of the proper variable types.

In some programming languages/stacks, type checking occurs at compile time,
and in others it occurs at runtime.
In some programming languages/stacks, type checking is mandatory,
and in others it is optional - introduced by the developer for
testing, security, documentation, and/or program confidence.

Type checking can remove the need for many explicit tests of variable types,
but these implicit "auto-tests" only confirm
that a variable has the correct type.
Even within the boundaries of one variable type,
a variable can still end up with an unexpected or unintended value,
such as a negative integer or an empty array.

Therefore, if type checking is the process of testing
a variable's _type_ whenever it is used or updated,
then I see a logical extension in "value checking" - the process of testing
a variable's _**value**_ whenever it is used or updated.

Ideally, this would occur before and after every instruction at runtime,
like many auto-injected assertions.
However, depending on the programming language and implementation,
this may introduce unacceptable delays in a program's execution
if enough variable values are tested against enough tests.


## Work in progress

I have no idea how to implement Assertify in a way that's sane for me or you.

### Desirable properties

- Zero impact on the user's source code
    - Source code that is covered by Assertify should
      look no different from source code that isn't
    - Additional configuration file(s) are acceptable
- Minimal impact on the user
    - Tests/expectations/constraints should be easy to
      define, maintain, and read
- Minimal impact on the program execution time
    - Only run in development
    - Be fast
    - Skip unnecessary tests, if any
    - Encourage user to only test important variables?
- Useful output
    - Don't interrupt program execution?
        - Warn/error toggles for each test and one global toggle for all tests
    - Emulate quality test runner output

### Stack ideas

- Javascript
    - ES6 already transpiles, so inject assertions during transpilation??
    - ESLint plugin to catch a subset of operations in static code analysis
      that clearly violate expectations (like direct assignment to bad value)
    - Redux/Vuex plugin to test state after every update (easiest to start)
- Python
    - Inject assertions in compilation??
