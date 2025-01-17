#이 코드는 주어진 시작 숫자에서 각 자리 수를 제곱하고 합한 값을 사용하여 원하는 길이의 수열을 생성합니다. 
#예시로, 시작 숫자를 4로 하고 수열의 길이를 10으로 설정하였습니다.

#이 코드를 실행하면 다음과 같은 결과를 얻을 수 있습니다:

#\[ 4, 16, 37, 58, 89, 145, 42, 20, 4, 16 \]

def sum_of_squares(n):
    return sum(int(digit)**2 for digit in str(n))

# 수열을 생성하는 함수
def generate_sequence(start, length):
    sequence = [start]
    for _ in range(length - 1):
        next_number = sum_of_squares(sequence[-1])
        sequence.append(next_number)
    return sequence

# 시작 숫자와 길이를 설정합니다.
start_number = 4
sequence_length = 10

# 수열을 생성하고 출력합니다.
sequence = generate_sequence(start_number, sequence_length)
print(sequence)
