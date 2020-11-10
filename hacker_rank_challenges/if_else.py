n = int(input().strip())

if 1 <= n <= 100:
	if n % 2 != 0:
		print("Weird")
	else:
		if 2 <= n <= 5:
			print("Not Weird")
		elif 6 <= n <= 20:
			print("Weird")
		elif n > 20:
			print("Not Weird")
else:
	print("Invalid input! The number has to be between 1 and 100")
