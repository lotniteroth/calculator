num1=input("លេខទីមួយ: ")
operation=input("ជ្រើសរើសប្រមាណវិធី+ - × ÷: ")
num2=input("លេខទីពីរ: ")
#add
if operation =="+":
	print("ចម្លើយគឺ  ")
	print (float(num1)+float(num2))
	print("Thank You")
#substract
if operation =="-":
	print("ចម្លើយគឺ  ")
	print(float(num1)-float(num2))
	print("Thank You")
#multiply
if operation =="×":
	print("ចម្លើយគឺ ")
	print(float(num1)*float(num2))
	print("Thank You")
#divide
if operation=="÷":
	print("ចម្លើយគឺ ")
	print(float(num1)/float(num2))
	print("Thank You")