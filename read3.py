data = []
count = 0
with open('wiki.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 5 == 0: #求餘數
			print(len(data))
print('檔案讀取完了,總共有', len(data), '筆資料')
sum_len = 0
for d in data:
	sum_len += 1
print('每筆平均長度', sum_len/len(data))

# new = []
# for d in data:
# 	if len(d) <100:
# 		new.append(d)
# print('一共有', len(new), '筆留言小於100')
# print(new[400])
# print(new[299])		

word = []
for d in data:
	if 'data' in d:
		word.append(d)
print('一共有', len(word), '筆data在留言裡')
print(word[0])

bad = [d for d in data if 'bad' in d]
print(len(bad))

hello = ['hello' in d for d in data]
print(len(hello))


#文字計數
wc = {}
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 #新增新的key進wc字典

for word in wc:
	if wc[word] > 50:
		print(word, wc[word])			
print(len(wc))

while True:
	word = input('請問你想查什麼字: ')
	if word =='q':
		break
	if word in wc:
		print(word, '出現過的次數為', wc[word])
	else:
		print('這個字沒出現過喔')
		

print('感謝查詢')