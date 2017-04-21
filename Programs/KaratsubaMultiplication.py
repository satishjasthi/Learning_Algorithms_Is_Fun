def karatsubaMultiplication(n1,n2):
	'''Function to compute the multiplication of 2 integers using karatsuba multiplication algorithm 
	n1 & n2 are integers with even number of digits
	Currently its working only for 2 numbers with even and same number of digits '''

	number_of_digits = (len(str(n1)),len(str(n2)))
	numbers = (n1,n2)
	a,b = [0,0],[0,0]#a[0] = a,a[1] = c,b[0] = b, b[1] = d 

#splitting numbers into equal parts if number of digits is even and uneven parts if number of digits is odd
	for i in range(2):
		if i % 2 == 0:
			(a[i],b[i]) = divmod(numbers[i],10**(number_of_digits[i]/2))
			print a[i],b[i]
		else:
			(a[i],b[i]) = divmod(numbers[i],10**(number_of_digits[i]/2))
			print a[i],b[i]
	#step1:compute ac
	ac = a[0] * a[1]

	print "ac:",ac,'\n'

	#step2: compute bd
	bd = b[0] * b[i]

	print "bd:",bd,'\n'

	#step3: (a + b)(c + d)
	g = (a[0] + b[0]) * (a[1] + b[1]) 

	print "Step3:",g,'\n'
	
	#step4:	3 - 2 - 1
	temp = g - bd - ac

	print "Step4:",temp,'\n'
	
	#step5: padding and adding
	answer = ac*10**(number_of_digits[0]) + temp*10**(number_of_digits[0]/2) + bd

	return answer
 
print karatsubaMultiplication(5678,1234)
