"""
표준 입력으로 국어, 영어, 수학, 과학 점수가 입력됩니다. 평균 점수를 출력하는 프로그램을 만드세요(input에서 안내 문자열은 출력하지 않아야 합니다). 단, 평균 점수를 출력할 때는 소수점 이하 자리는 버립니다(정수로 출력).

참고 | 심사문제에서 안내 문자열은?
input에 문자열을 지정하면 입력을 받기 전에 안내 문자열을 출력할 수 있습니다. 하지만 심사문제에서는 입력을 받을 때 안내 문자열을 출력하면 안 됩니다.

a = int(input('숫자를 입력하세요: '))  # X 심사문제를 통과할 수 없음
a = int(input())                     # O 올바른 코드
 
a, b = map(int, input('숫자 두 개를 입력하세요: ').split()) # X 심사문제를 통과할 수 없음
a, b = map(int, input().split())                          # O 올바른 코드
따라서 input()과 같이 안내 문자열이 없는 형태로 사용해주세요.

예)

입력
83 92 87 90

결과
88

입력
32 53 22 95

결과
50

"""

korean, english, math, science = map(int, input().split())
print((korean + english + math + science) // 4)