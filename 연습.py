import string

src_str = string.ascii_uppercase
dst_str = src_str[3:] + src_str[:3]

def hmm(a):
    idx = scr_str.index(a)
    return dst_str[idx]

scr = input("문장을 입력")
print('암호화된 문장: ', end='')

for ch in scr:
    if ch in src_str:
        print(hmm(ch), end='')
    else:
        print(ch, end='')

print()
