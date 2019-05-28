def my_split(string, break_pattern):
    if not string:
        return []
    res = []
    start = 0
    while start < len(string):
        end = start
        while end < len(string) and end - start < len(break_pattern) and string[end] != break_pattern[end - start]:
            end += 1
        res.append(string[start: end])
        start =  (start + 1) if start == end else end
    
    print(res)    


my_split("the  aaa sky is  aaa   blue ! ", 'aaa')