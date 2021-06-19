user_input_a = input("정수입력")

if user_input_a.isdigit():
    number_input_a= int(user_input_a)
    print("원의 반지름 :", number_input_a)
    print("원의둘레:", 2*3.14*number_input_a)
    print("원의 넓이 :", 3,14* number_input_a*number_input_a)
else:
    print("정수를 입력하지 않았습니다")
#isdgit:숫자로만 구성되었는지 확인 
#예외처리까지 생각하기
#구문오류 - 코드 실행전 오류//예외&런타임오류 - 실행중 오류 

