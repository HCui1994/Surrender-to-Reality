"""
Validate if a given string can be interpreted as a decimal number.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false

Note: It is intended for the problem statement to be ambiguous. 
You should gather all requirements up front before implementing one. However, here is a list of characters that can be in a valid decimal number:

Numbers 0-9
Exponent - "e"
Positive/negative sign - "+"/"-"
Decimal point - "."
Of course, the context of these characters also matters in the input.

Update (2015-02-10):
The signature of the C++ function had been updated. 
If you still see your function signature accepts a const char * argument, please click the reload button to reset your code definition.

"""

from enum import Enum

State = Enum("State", ("start", "sign", "digit1", "dot", "digit2", "e", "digit3", "blank2", "true", "false"))

class Solution(object):
    def is_number(self, s):
        state = State.start
        for c in s:
            if state == State.start:
                if c == ' ':
                    continue
                elif c in "+-":
                    state = State.sign
                elif c in "1234567890":
                    state = State.digit1
                elif c == '.':
                    state = State.dot
                else:
                    state = "false"
            elif state == State.sign:
                if c in "1234567890":
                    state = State.digit2
                elif c == 'e':
                    state = State.e
                else:
                    break
            elif state == State.digit2:
                if c in "1234567890":
                    state = State.digit2
                elif c == 'e':
                    state = State.e
                
                
                


    def test(self):
        s = " -90e3   "
        print(self.is_number(s))



Solution().test()