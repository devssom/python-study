"""
<대본 다듬기 문제>
모자장수는 곧 진행되는 연극에서 주인공을 맡게 되었습니다. 완벽히 연습했지만 유독 한 문장이 발음하기 어려워 문장 중간에 특수문자를 넣어 읽기 편하게 하려고 합니다.
지시사항을 참고하여 코드를 작성하세요.

<지시사항>
변수 sentence에는 모자장수가 읽을 짝수 길이의 문장이 무작위로 생성되어 저장됩니다.
사용자로부터 문장 중간에 넣을 특수문자를 입력받으세요. 그리고 입력받은 특수문자를 문자열 sentence의 가운데에 삽입한 뒤에 저장하세요.
문장의 길이가 홀수인 경우는 고려하지 않습니다.

<입력 예시>
,

<출력 예시>
# sentence가 "모자장수는 최고야!"라고 가정합니다.
모자장수는, 최고야!
"""

from elice_func import elice_random_string
sentence = elice_random_string()

special = input()
listsentence = list(sentence)
half = len(sentence)//2
listsentence.insert(half, special)
sentence = "".join(listsentence)

print(sentence)

