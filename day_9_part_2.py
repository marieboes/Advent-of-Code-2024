def parse_to_list_of_numbers(input_text):
    return [int(char) for char in input_text if char.isdigit()]

def transform_numbers(numbers):
    transformed_list = []
    odd_index = 0

    # Convert numbers into the initial pattern
    for index, num in enumerate(numbers):
        if index % 2 == 0:
            transformed_list.append(str(odd_index) * num)
            odd_index += 1
        else:
            transformed_list.append('.' * num)

    transformed_str = ''.join(transformed_list)
    print(f"Initial transformed string: {transformed_str}")

    transformed_chars = list(transformed_str)
    length = len(transformed_chars)

    # Process numbers from 9 to 0 and move them to match with dots on the left
    for current_number in range(9, -1, -1):
        current_char = str(current_number)
        i = 0

        while i < length:
            if transformed_chars[i] == current_char:
                # Locate the end of current character sequence
                j = i
                while j < length and transformed_chars[j] == current_char:
                    j += 1

                number_length = j - i

                # Optimize dot sequence search
                k = 0
                while k < i:
                    if transformed_chars[k] == '.':
                        # Check if we have a dot sequence of the same length
                        end_k = k + number_length
                        if transformed_chars[k:end_k] == ['.'] * number_length:
                            # Move the number sequence to the left
                            transformed_chars[k:end_k] = [current_char] * number_length
                            transformed_chars[i:j] = ['.'] * number_length

                            print(
                                f"After moving '{current_char}' from [{i} to {j}) to [{k} to {end_k}): {''.join(transformed_chars)}")
                            break

                    k += 1

                i = j
            else:
                i += 1

    final_result_str = ''.join(transformed_chars)
    print(f"Final transformed sequence: {final_result_str}")

    # Calculate checksum: number multiplied by its position
    total_sum = sum(int(char) * index for index, char in enumerate(final_result_str) if char.isdigit())

    print(f"Total sum: {total_sum}")

    return total_sum

input_text = "2333133121414131402"
parsed_numbers = parse_to_list_of_numbers(input_text)
final_sum = transform_numbers(parsed_numbers)
print(final_sum)