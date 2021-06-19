list_number = [52.273, 32, 72 ,100]

try:
    number_input = int(input("정수입력 >"))
    print("{}번째 오쇼: {}".format(number_input,list_number[number_input]))
    예외.발생해주세요()#처리불가 예외
except ValueError as exception:
    print("정수를 입력해주세요 ")
    print(type(exception),exception)
    print("esception: ", exception)
except IndexError as exception:
    print("리스트의 인덱스를 벗어났어요")
    print(type(exception),exception)
    print("exception:" ,exception)
except Exception as exception:#Value Error, IndexError 이외의 예외처리 
    print("미리 파악하지못한 예외가 발생했습니다.")
    print(type(exception),exception)