class Reverser(object):
    def reverse_words(self, string):
        # preprocess
        string = list(string)
        compact = 0
        # remove tailing [space]
        while string and string[-1] == ' ':
            string.pop()
        # remove other redundant [space]
        for i in range(len(string)):
            if string[i] != ' ':
                string[compact] = string[i]
                compact += 1
            else:
                if i > 0 and string[i - 1] == ' ':
                    # string[i] is a redundant [space]
                    continue
                elif i > 0 and string[i - 1] != ' ':
                    # string[i] is a useful spaec
                    string[compact] = string[i]
                    compact += 1

        string = string[:compact] + [' ']  # add a sentinal

        start = 0
        for end in range(len(string)):
            if string[end] == ' ':
                self.reverse_helper(string, start, end)
                start = end + 1

        string.pop()  # remove sentinal

        self.reverse_helper(string, 0, len(string))
        print("".join(string))
        return "".join(string)



    def reverse_helper(self, string, start, end):
        for offset in range((end - start) // 2):
            string[start + offset], string[end - offset - 1] = string[end - offset - 1], string[start + offset]


string = " the sky     is blue!! 123  "
r = Reverser()
r.reverse_words(string)
