# import random

# numbers = list(range(0,10))
# print(numbers)

# three_numbers = random.sample(numbers,3)

# print("맟춰야할 숫자: ",three_numbers)

# 0부터 9까지 숫자를 담은 리스트를 생성 후
# 리스트에서 세 개의 숫자를 랜덤하게 추출합니다.



# import random

# numbers = list(range(0,10))
# print(numbers)

# three_numbers = random.sample(numbers, 3)
# print("맞춰야할 숫자:", three_numbers)

# num1,num2,num3 = map(int,input("0~9 사이의 숫자 세 개 입력(중복 불가능).ex) 3 6 9 >>").split())


# strike = 0
# ball = 0

# if three_numbers[0] == num1:
#     strike +=1
# if three_numbers[1] == num2:
#     strike +=1
# if three_numbers[2] == num3:
#     strike +=1
    
# if three_numbers[1] == num1 or three_numbers[2] ==num1:
#     ball +=1
# if three_numbers[0] == num2 or three_numbers[2] ==num2:
#     ball +=1
    
# if three_numbers[0] == num3 or three_numbers[1] ==num3:
#     ball +=1
    
    
# print(strike, "strike",ball, "ball")


# 숫자 세 개를 입력받아서 각각 num1, num2, num3, 변수에 담아준다
# map 함수를 사용하면 입력 받은 것을 int 타입으로 변환해 줄 수 있습니다.
# 우선 스트라이크 개스와 볼 개수를 0으로 설정합니다.
# num1이 three_numbers 리스트의 첫 번째 숫자와 같다면 스트라이크 개수를 하나 높여줍니다.
# 마찬가지로 num2,num3 스트라이크인지 확인합니다.
# num1이 three_numbers 리스트의 두 번째 또는 세 번째 숫자와 같다면 볼 개수를 하나 높여줍니다.
# 마찬가지로 num2, num3이 볼인지 확인합니다.

# 맞출 때까지 확인하는 방법


import random

numbers = list(range(0,10))
print(numbers)

three_numbers = random.sample(numbers, 3)
print("맞춰야할 숫자:", three_numbers)

round = 1
while True:
    

    num1,num2,num3 = map(int,input("0~9 사이의 숫자 세 개 입력(중복 불가능).ex) 3 6 9 >>").split())


    strike = 0
    ball = 0

    if three_numbers[0] == num1:
        strike +=1
    if three_numbers[1] == num2:
        strike +=1
    if three_numbers[2] == num3:
        strike +=1
        
    if three_numbers[1] == num1 or three_numbers[2] ==num1:
        ball +=1
    if three_numbers[0] == num2 or three_numbers[2] ==num2:
        ball +=1
        
    if three_numbers[0] == num3 or three_numbers[1] ==num3:
        ball +=1
        
        
    print(strike, "strike",ball, "ball")
    
    if strike ==3:
        print("[게임 끝]",round,"라운드만에 맞추셨습니다.")
        break
    
    round+=1