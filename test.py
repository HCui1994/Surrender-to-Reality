def compare(string1, string2):
    if len(string1) < len(string2):
        return True
    elif len(string1) == len(string2):
        return string1 <= string2
    else:
        return False


print(compare("255", "255"))