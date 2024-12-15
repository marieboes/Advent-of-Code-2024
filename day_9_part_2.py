def parse_to_list_of_numbers(input_text):
    return [int(char) for char in input_text if char.isdigit()]


def transform_numbers(numbers):
    transformed_str = []

    # Convert numbers into the initial pattern
    for index, num in enumerate(numbers):
        if index % 2 == 0:
            transformed_str.extend([str(index // 2)] * num)
        else:
            transformed_str.extend(['.'] * num)

    print(f"Initial transformed string: {''.join(transformed_str)}")

    length = len(transformed_str)

    # Collect starting indices of dot sequences and their lengths
    dot_sequences = []
    i = 0
    while i < length:
        if transformed_str[i] == '.':
            start = i
            while i < length and transformed_str[i] == '.':
                i += 1
            dot_sequences.append((start, i - start))
        else:
            i += 1

    print(f"Initial dot sequences: {dot_sequences}")

    # Start processing from right to left
    i = length - 1
    while i >= 0:
        if transformed_str[i].isdigit():
            current_char = transformed_str[i]
            j = i

            # Determine the boundaries of the current block
            while j >= 0 and transformed_str[j] == current_char:
                j -= 1

            number_start = j + 1
            number_length = i - j

            print(f"Found block '{current_char}' from {number_start} to {i}")

            # Try to move this block to the earliest possible dot sequence
            for dot_start, dot_length in dot_sequences:
                if dot_length >= number_length and dot_start < number_start:
                    # Move block to this dot sequence
                    transformed_str[dot_start:dot_start + number_length] = [current_char] * number_length
                    transformed_str[number_start:number_start + number_length] = ['.'] * number_length

                    # Update the dot sequences tracking
                    dot_sequences.remove((dot_start, dot_length))
                    if dot_length > number_length:
                        dot_sequences.append((dot_start + number_length, dot_length - number_length))

                    print(f"Moved block '{current_char}' to {dot_start}-{dot_start + number_length - 1}")
                    break

            i = j
        else:
            i -= 1

    final_result_str = ''.join(transformed_str)
    print(f"Final transformed sequence: {final_result_str}")

    total_sum = 0
    for i, char in enumerate(final_result_str):
        if char.isdigit():
            # Multiply each digit by its position
            total_sum += int(char) * i

    print(f"Total sum: {total_sum}")
    return total_sum

input_text = "2333133121414131499992323232321111642"
parsed_numbers = parse_to_list_of_numbers(input_text)
final_sum = transform_numbers(parsed_numbers)
print(final_sum)