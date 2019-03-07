def my_split(string, break_ch=' '):
    if not string:
        return []
    res = []
    start = 0
    while start < len(string):
        end = start
        while end < len(string) and string[end] != break_ch:
            end += 1
        res.append(string[start: end])
        start =  (start + 1) if start == end else end
    
    print(res)    


my_split("the   sky is     blue ! ", ' ')