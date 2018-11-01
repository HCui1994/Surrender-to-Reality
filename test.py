string = ""
def pass_by_reference_test(string):
    string += "shit"

pass_by_reference_test(string)
print(string)