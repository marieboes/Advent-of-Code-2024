def parse_to_list_of_numbers(input_text):
    return [int(char) for char in input_text if char.isdigit()]

def transform_numbers(numbers):
    transformed_list = []
    odd_index = 0

    for index, num in enumerate(numbers):
        if index % 2 == 0:
            transformed_list.append(str(odd_index) * num)
            odd_index += 1
        else:
            transformed_list.append('.' * num)

    transformed_str = ''.join(transformed_list)
    print(f"Initial transformed string: {transformed_str}")

    transformed_chars = list(transformed_str)

    for current_number in range(9, -1, -1):
        current_char = str(current_number)
        i = 0

        while i < len(transformed_chars):
            if transformed_chars[i] == current_char:
                j = i
                while j < len(transformed_chars) and transformed_chars[j] == current_char:
                    j += 1

                number_length = j - i

                for k in range(len(transformed_chars)):
                    if transformed_chars[k] == '.':
                        l = k
                        while l < len(transformed_chars) and transformed_chars[l] == '.':
                            l += 1

                        dot_length = l - k

                        if number_length == dot_length:
                            transformed_chars[k:k+number_length] = [current_char] * number_length
                            transformed_chars[i:j] = ['.'] * number_length
                            break

                i = j
            else:
                i += 1

    final_result_str = ''.join(transformed_chars)
    print(f"Final transformed sequence: {final_result_str}")

    final_numbers_list = [int(char) for char in final_result_str if char.isdigit()]
    total_sum = sum(num * index for index, num in enumerate(final_numbers_list))
    print(f"Total sum: {total_sum}")

    return total_sum

input_text = "2333133121414131402"
parsed_numbers = parse_to_list_of_numbers(input_text)
final_sum = transform_numbers(parsed_numbers)
print(final_sum)