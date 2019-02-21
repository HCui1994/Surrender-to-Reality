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


class Solution(object):
    def is_number(self, s):
        status = "skip"
        digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        for i in range(len(s)):
            if status == "skip_prev":
                if s[i] == ' ':
                    pass
                elif s[i] in ['+', '-']:
                    status = "record_prev"
                elif s[i] in digits:
                    status = "record_prev"
                else:
                    return False
            elif status == "record_prev":
                if s[i] in digits:
                    pass
                elif s[i] in ['e', 'E']:
                    status = "record_post"
                else:
                    return False
            elif status == "record_post":
                if s[i] in digits:
                    pass
                elif s[i] == ' ':
                    status = "skip_post"
                else:
                    return False
            elif status == "skip_post":
                if s[i] == ' ':
                    pass
                else:
                    return False
        return True


    def test(self):
        s = " -90e3   "
        print(self.is_number(s))



Solution().test()