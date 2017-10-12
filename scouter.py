#Finds strongest openents
def scouter(power)
	A = power
	if A <= 9000:
		if A < 2000:
			return print("Not even worth my time")
		return print("Pretty decent power level")
	else:
		return print("Its over NINE THOUSAND!!!!!!!")

print(scouter(2400))
print(scouter(100))
print(scouter(12000))