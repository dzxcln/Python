print("Enter marks obtained in 4 subjects:")

math = int(input("maths: "))
eng = int(input("english: "))
sci = int(input("science: "))
hindi = int(input("hindi: "))

sum = math+eng+sci+hindi
print("sum of hindi math eng and sci")

perc = (sum/400)*100


print(end=("Percentage mark = "))
print(perc)