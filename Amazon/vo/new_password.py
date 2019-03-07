def new_password(password, mapping):
    res = []
    password_to_list = list(password)

    def recur(new_password, i):
        if i == len(password):
            if new_password == password:
                return
            res.append(new_password)
            return
        recur(new_password + password_to_list[i], i + 1)  # no replacement
        if password_to_list[i] in mapping.keys():
            for c in mapping[password_to_list[i]]:
                # replacement
                recur(new_password + c, i + 1)

    recur("", 0)
    return res


mapping = {'a': set(['c', 'b']), 'd': set(['s', 'g'])}
password = "abcd"

print(new_password(password, mapping))