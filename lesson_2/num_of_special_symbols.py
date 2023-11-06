
word = input("введите слово: ")
spec_s = ".,?!"
res = 0
for i in range(len(word)):
    cur_sym = word[i]
    index_cur_sym = spec_s.find(cur_sym)
    if index_cur_sym >= 0:
    #if cur_sym == spec_s[0] or cur_sym == spec_s[1] or cur_sym == spec_s[2] or cur_sym == spec_s[3]:
        res += 1

print(res)
    
 