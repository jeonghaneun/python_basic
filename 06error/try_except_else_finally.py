try:
    number_input_a = int(input("정수입력> "))
    print("원의 반지름 : ", number_input_a)
    print("원의 둘레: ", 2*3.14*number_input_a)
    print("원의 넓이:" , 3.14*number_input_a*number_input_a)
except:
    print("정수를 입력하라고! ")
else:
    print("예외가 발생하지 않았습니다.")
finally:
    print("일단 프로그램이 어떻게든 끝났습니다.")
#try 구문은 단독 사용불가, except,finally 와 반드시 함께사용 
#else는 except 구문뒤에 사용 
print("1. try + except")
print("2. try + except + else")
print("3. try + except + else + finally")
print("4. try + finally")


