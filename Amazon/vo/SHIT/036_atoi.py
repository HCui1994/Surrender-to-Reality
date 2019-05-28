class String(object):
    def atoi(self, string):
        res = 0
        sign = True
        activate = False
        for char in string:
            if not activate:
                if char in "1234567890-+":
                    activate = True
                    if char == '+':
                        sign = True
                    elif char == '-':
                        sign = False
                    else:
                        res = res * 10 + int(char)
                    overflow, ret = self._check(res, sign)
                    if overflow:
                        return ret
                else:
                    return res
            else:
                if char in "1234567890":
                    res = res * 10 + int(char)
                    overflow, ret = self._check(res, sign)
                    if overflow:
                        return ret
                else:
                    break
            print(activate, res)
        print(res if sign else -res)
        return res if sign else -res
                

    def _check(self, res, sign):
        INT_MAX = 2 ** 32 - 1
        INT_MIN = -2 ** 32
        if not sign:
            res = -res
        if res >= INT_MAX:
            return True, INT_MAX
        elif res <= INT_MIN:
            return True, INT_MIN
        else:
            return False, res


String().atoi("words and 987")