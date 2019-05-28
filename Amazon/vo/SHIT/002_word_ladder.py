import collections


class WordLadder(object):
    def ladder_length(self, begin_word, end_word, word_list):
        word_list = set(word_list)
        if end_word not in word_list:
            return 0

        queue1, queue2 = set([begin_word]), set([end_word])
        visited = set([begin_word, end_word])
        path_len, word_len = 2, len(begin_word)
        while queue1 and queue2:
            # print(begin_set, end_set, visited)
            if len(queue1) > len(queue2):
                queue1, queue2 = queue2, queue1
            temp_queue1 = set()
            for word in queue1:
                word_to_list = list(word)
                for i in range(word_len):
                    backup = word_to_list[i]
                    for replace in "qwertyuiopasdfghjklzxcvbnm":
                        word_to_list[i] = replace
                        new_word = "".join(word_to_list)
                        if new_word in queue2:
                            return path_len
                        if new_word not in word_list or new_word in visited:
                            continue
                        temp_queue1.add(new_word)
                    word_to_list[i] = backup
            visited |= temp_queue1
            queue1 = temp_queue1
            path_len += 1
        return 0


if __name__ == "__main__":
    word_ladder = WordLadder()
    ans = word_ladder.ladder_length("a", "c", ["a", "b", "c"])
    print(ans)
