data = []
count = 0
with open('review.txt', 'r') as f:
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