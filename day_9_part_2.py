def parse_to_list_of_numbers(input_text):
    return [int(char) for char in input_text if char.isdigit()]

def transform_numbers(numbers):
    transformed_list = []
    location_list = []  # To store (location number, character count)
    odd_index = 0

    # Convert numbers into the initial pattern and track location numbers
    for index, num in enumerate(numbers):
        if index % 2 == 0:
            transformed_list.append(str(odd_index) * num)
            location_list.append((odd_index, num))
            odd_index += 1
        else:
            transformed_list.append('.' * num)

    transformed_str = ''.join(transformed_list)
    print(f"Initial transformed string: {transformed_str}")
    print(f"Location list: {location_list}")

    # Split the initial transformed string into characters for further manipulation
    transformed_chars = list(transformed_str)
    length = len(transformed_chars)

    # Prepare to track dot sequences
    dot_sequences = []

    # Preprocess: Find all dot sequences
    i = 0
    while i < length:
        if transformed_chars[i] == '.':
            start = i
            while i < length and transformed_chars[i] == '.':
                i += 1
            dot_sequences.append((start, i - start))
        else:
            i += 1

    # Debug: Print initial dot sequences
    print(f"Initial dot sequences: {dot_sequences}")

    # Process based on highest location number
    for loc_num, char_count in sorted(location_list, key=lambda x: x[0], reverse=True):
        current_char = str(loc_num)
        i = 0
        while i < length:
            if transformed_chars[i] == current_char:
                # Locate the end of the current character sequence
                j = i
                while j < length and transformed_chars[j] == current_char:
                    j += 1
                number_length = j - i

                # Debug: Attempting to move block
                print(f"Attempting to move block '{current_char}' from {i}-{j-1}")

                # Try to find a suitable dot sequence
                moved = False
                for index, (dot_start, dot_length) in enumerate(dot_sequences):
                    if dot_length >= number_length and dot_start < i:
                        # Move the number sequence to the dot start
                        end_k = dot_start + number_length
                        transformed_chars[dot_start:end_k] = [current_char] * number_length
                        transformed_chars[i:j] = ['.'] * number_length

                        # Update the dot_sequences list
                        new_start = dot_start + number_length
                        new_length = dot_length - number_length
                        if new_length > 0:
                            dot_sequences[index] = (new_start, new_length)
                        else:
                            del dot_sequences[index]
                        print(f"Moved block '{current_char}' to {dot_start}-{end_k-1}")
                        moved = True
                        break

                if not moved:
                    print(f"Block '{current_char}' couldn't be moved due to insufficient or invalid space")
                i = j
            else:
                i += 1

    final_result_str = ''.join(transformed_chars)
    print(f"Final transformed sequence: {final_result_str}")

    # Calculate checksum: number multiplied by its original position in the location list
    total_sum = 0
    for loc_num, _ in location_list:
        for index, char in enumerate(final_result_str):
            if char.isdigit() and int(char) == loc_num:
                total_sum += loc_num * index

    print(f"Total sum: {total_sum}")
    return total_sum

input_text = "234567874874903342482349"
parsed_numbers = parse_to_list_of_numbers(input_text)
final_sum = transform_numbers(parsed_numbers)
print(final_sum)