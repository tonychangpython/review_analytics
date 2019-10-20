data = []
count = 0
with open('review.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 5 == 0: #求餘數
			print(len(data))
print(len(data))
print(data[300])
print('-----------------------')
print(data[288])