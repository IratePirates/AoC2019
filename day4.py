in_min=136818
in_max=685979

def includes_duplicates(num):
	str_num = str(num)
	for n in range(len(str_num) - 1):
		if str_num[n] == str_num[n + 1]:
			return True
	return False

def monotonic_increase(num):
	str_num = str(num)
	for n in range(len(str_num) - 1):
		if str_num[n + 1] < str_num[n]:
			return False
	return True

def includes_exactly_a_pair(num):
	str_num = str(num)
	digits = []
	for i in range(10):
		tmp = str_num.count(str(i))
		if tmp > 1:
			digits.append(tmp)
	for i in range(len(digits)):
		if digits[i] == 2:
			return True
	return False

#print(len(filter(includes_duplicates, filter(monotonic_increase, range(in_min, in_max)))))
print(len(filter(includes_exactly_a_pair,filter(monotonic_increase, range(in_min, in_max)))))