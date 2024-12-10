def parse_to_list_of_numbers(input_text):
    return [int(char) for char in input_text if char.isdigit()]


def transform_numbers(numbers):
    transformed_chars = []
    location_list = []
    odd_index = 0

    # Convert numbers into the initial pattern and track location numbers
    for index, num in enumerate(numbers):
        if index % 2 == 0:
            transformed_chars.extend([odd_index] * num)
            location_list.append((odd_index, num))
            odd_index += 1
        else:
            transformed_chars.extend([-1] * num)  # Use -1 to represent '.'

    length = len(transformed_chars)

    # Create a list to keep track of dot sequences (start, length)
    dot_sequences = []
    i = 0
    while i < length:
        if transformed_chars[i] == -1:
            start = i
            while i < length and transformed_chars[i] == -1:
                i += 1
            dot_sequences.append((start, i - start))
        else:
            i += 1

    # Process based on highest location number
    location_list.sort(reverse=True)
    for loc_num, char_count in location_list:
        i = 0
        while i < length:
            if transformed_chars[i] == loc_num:
                # Find the end of the current number sequence
                j = i
                while j < length and transformed_chars[j] == loc_num:
                    j += 1
                number_length = j - i

                # Find a suitable dot sequence
                for k, (dot_start, dot_length) in enumerate(dot_sequences):
                    if dot_length >= number_length:
                        # Move the number sequence to the dot start
                        transformed_chars[dot_start:dot_start + number_length] = [loc_num] * number_length
                        transformed_chars[i:j] = [-1] * number_length

                        # Update the dot_sequences
                        if dot_length == number_length:
                            dot_sequences.pop(k)
                        else:
                            dot_sequences[k] = (dot_start + number_length, dot_length - number_length)
                        break

                i = j
            else:
                i += 1

    # Convert integers back to characters
    final_result_str = ''.join(
        '.' if x == -1 else str(x) for x in transformed_chars
    )

    # Calculate checksum: number multiplied by its position
    total_sum = sum(
        int(char) * index for index, char in enumerate(final_result_str) if char.isdigit()
    )

    return total_sum


input_text = "234567874874903342482349"
parsed_numbers = parse_to_list_of_numbers(input_text)
final_sum = transform_numbers(parsed_numbers)
print(final_sum)