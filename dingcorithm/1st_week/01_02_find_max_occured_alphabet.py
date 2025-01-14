def find_max_occurred_alphabet(string):
    alphabet_occurence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - 97
        alphabet_occurence_array[arr_index] += 1

    max = 0
    max_occurred_alphabet = []

    for a in alphabet_occurence_array:
        if a > max:
            max = a

    for i in range(len(alphabet_occurence_array)):
        if alphabet_occurence_array[i] == max:
            max_occurred_alphabet.append(chr(i+97))

    return max_occurred_alphabet

result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))

