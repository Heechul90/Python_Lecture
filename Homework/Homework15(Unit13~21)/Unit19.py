### Unit 19. 계단식으로 별 출력하기
## 19.6 심사문제: 산 모양으로 별 출력하기
## 표준 입력으로 삼각형의 높이가 입력됩니다. 
## 입력된 높이만큼 산 모양으로 별을 출력하는 프로그램을 만드세요
## (input에서 안내 문자열은 출력하지 않아야 합니다). 
## 이때 출력 결과는 예제와 정확히 일치해야 합니다. 
## 모양이 같더라도 공백이나 빈 줄이 더 들어가면 틀린 것으로 처리됩니다.



n = int(input('정수를 입력하시오.: '))


for i in range(1, n + 1):
    for k in range(0, n - i):
        print(' ', sep = '', end = '')
    print('*' * (i * 2 - 1))




