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
