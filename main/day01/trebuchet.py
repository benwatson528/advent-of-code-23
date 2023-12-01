NUMBERS = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}


def solve(calibration_values, is_words) -> int:
    return sum((find_digit(c, False, is_words) * 10) + find_digit(c[::-1], True, is_words) for c in calibration_values)


def find_digit(calibration_value, is_reversed, is_words):
    lowest_idx = len(calibration_value)
    if is_words:
        for number in NUMBERS.keys():
            word_idx = calibration_value.find(number[::-1] if is_reversed else number)
            if word_idx != -1 and word_idx < lowest_idx:
                digit = NUMBERS[number]
                lowest_idx = word_idx
    try:
        digit_idx = [x.isdigit() for x in calibration_value].index(True)
        if digit_idx < lowest_idx:
            digit = calibration_value[digit_idx]
    except ValueError:
        # no number in the string, there must be words instead
        pass
    return int(digit)
