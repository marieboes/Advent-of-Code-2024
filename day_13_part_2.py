import re
import numpy as np

def parse_input(input_str):
    task_pattern = r"Button A: X\+(\d+), Y\+(\d+)\s*Button B: X\+(\d+), Y\+(\d+)\s*Prize: X=(\d+), Y=(\d+)"
    matches = re.findall(task_pattern, input_str)
    tasks = [
        (
            (int(a_x), int(a_y)),
            (int(b_x), int(b_y)),
            (int(prize_x) + 10000000000000, int(prize_y) + 10000000000000)
        )
        for a_x, a_y, b_x, b_y, prize_x, prize_y in matches
    ]
    return tasks

def parse_input(input_str):
    task_pattern = r"Button A: X\+(\d+), Y\+(\d+)\s*Button B: X\+(\d+), Y\+(\d+)\s*Prize: X=(\d+), Y=(\d+)"
    matches = re.findall(task_pattern, input_str)
    tasks = [
        ((int(a_x), int(a_y)), (int(b_x), int(b_y)), (int(prize_x) + 10000000000000, int(prize_y) + 10000000000000))
        for a_x, a_y, b_x, b_y, prize_x, prize_y in matches
    ]
    return tasks

def calculate_button_presses(button_a, button_b, target):
    button_a_x, button_a_y = button_a
    button_b_x, button_b_y = button_b
    target_x, target_y = target

    max_a_presses = target_x // button_a_x
    optimal_a_presses = None
    optimal_b_presses = None

    for a_presses in range(max_a_presses + 1):
        remaining_x = target_x - a_presses * button_a_x
        remaining_y = target_y - a_presses * button_a_y

        if remaining_x % button_b_x == 0 and remaining_y % button_b_y == 0:
            b_presses_x = remaining_x / button_b_x
            b_presses_y = remaining_y / button_b_y

            if b_presses_x == b_presses_y and b_presses_x >= 0:
                if optimal_a_presses is None or a_presses < optimal_a_presses:
                    optimal_a_presses = a_presses
                    optimal_b_presses = int(b_presses_x)

    if optimal_a_presses is not None:
        return optimal_a_presses, optimal_b_presses
    else:
        return None


def process_input(input_str):
    tasks = parse_input(input_str)
    results = []
    total_weighted_sum = 0

    for button_a, button_b, prize in tasks:
        result = calculate_button_presses(button_a, button_b, prize)

        if result:
            a_presses, b_presses = result
            weighted_sum = (a_presses * 3) + (b_presses * 1)
            results.append(f"Press Button A {a_presses} times and Button B {b_presses} times. Sum: {weighted_sum}.")
            total_weighted_sum += weighted_sum
        else:
            results.append("No valid sequence of button presses found.")

    results.append(f"Total Weighted Sum: {total_weighted_sum}.")
    return results

input_string = """
Button A: X+49, Y+27
Button B: X+35, Y+65
Prize: X=4326, Y=4898

"""

results = process_input(input_string)
for result in results:
    print(result)