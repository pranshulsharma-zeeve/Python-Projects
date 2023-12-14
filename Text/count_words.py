def count_w(st):
    cnt = {}
    words = st.split()
    for word in words:
        if word in cnt:
            cnt[word] += 1
        else:
            cnt[word] = 1
    return cnt


st = str(input("Enter string: "))
print(count_w(st))
