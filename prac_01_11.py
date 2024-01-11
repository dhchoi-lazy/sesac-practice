from collections import Counter



char_count=Counter('Samsung')
print(char_count)

word_count=Counter(['삼성', '애플', '삼성', '아마존', '애플', '삼성'])
print(word_count)

print(word_count.most_common(1))

print(word_count['애플'])

print(sum(word_count.values()))