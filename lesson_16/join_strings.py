def joiner(input_list):
    ans = ''
    length = len(input_list)
    for i in range(length):
        ans += input_list[i]
        if i < length - 1:
            ans += ','


    return ans


print(joiner(['a', 'b c d', 'ef']))