def reverse_words_in_a_string(string):

    def reverse(string, start, end):
        """ reverse string[start: end] """
        i = start
        for i in range((end - start) // 2):
            string[start + i], string[end - i - 1] = string[end - i - 1], string[start + i]

    string = list(string)
    # preprocess
    left = 0  # index where the next word should start
    start = 0  # index where the next word starts in original string
    useful_length = 0
    words_cnt = 0  # counting words
    while start < len(string):
        while start < len(string) and string[start] == ' ':
            # jump [space]
            start += 1
        end = start
        while end < len(string) and string[end] != ' ':
            end += 1
        string[left: left + (end - start)] = string[start: end]  # copy words from original space to new space
        reverse(string, left, left + (end - start))  # reverse word in place
        useful_length += end - start  # words are useful
        if left + end - start < len(string):  # only add additional space when there is a new word
            string[left + end - start] = ' '
        if end != start:
            words_cnt += 1
        left += end - start + 1
        start = end
    useful_length += words_cnt - (words_cnt != 0)  # if no words, no additional space to pop
    while len(string) > useful_length:
        string.pop()

    reverse(string, 0, len(string))
    return string


reverse_words_in_a_string("   hello world!   ")
