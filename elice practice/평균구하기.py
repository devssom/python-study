"""
평균 구하기!
평균을 쉽게 구할 수 있도록 평균을 구하는 프로그램을 작성해봅시다.

예를 들어, 다음과 같이 입력을 주면
50
40
30
20
10
0

다음과 같이 출력해주는 프로그램이 되어야합니다.
30.0

이렇게 해봐요!
while문을 이용해서, 0을 입력할 때 까지 입력을 받습니다. 0을 입력받았으면, 0을 입력한 바로 이전까지의 수들의 평균을 구합니다.

Tip!

평균은 (자료의 합) / (자료의 크기) 입니다.
"""

i = 0
sum = 0
num = -1


while num != 0:
    num = int(input())
    sum += num
    
    if num == 0:
        break
    i += 1

print(sum/i)