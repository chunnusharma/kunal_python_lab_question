def hammingDist(str1, str2):
	i = 0
	count = 0

	while(i < len(str1)):
		if(str1[i] != str2[i]):
			count += 1
		i += 1
	return count

# Driver code
str1 = input()
str2 = input()

# function call
print(hammingDist(str1, str2))
