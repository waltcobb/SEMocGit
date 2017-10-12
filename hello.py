
#!/usr/bin/python

print('Hello world')

def merge(A, B):
	# 1. What are the "smallest" or "irreducible" inputs?
	# Solve those cases directly.
	if A==[]:
		return B
	if B==[]:
		return A

	# 2. Compare the first items of A and B.
	if A[0] < B[0]:
		first = A.pop(0)
		# Now A is reduced by 1 element.
		# We return A[0] + the merge of rest_A and B
		return [first] + merge(A, B)
	else:
		first = B.pop(0)
		return [first] + merge(A, B)


//random comment
# Derico Walker's added comment

#YZ's comment