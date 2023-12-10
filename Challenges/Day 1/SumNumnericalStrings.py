import re
# https://hackernoon.com/how-to-read-text-file-in-python


file = open(
    fr'C:\Users\aamrl\OneDrive\Desktop\2023-CodingAdvent\Challenges\Day 1\day_One_String.txt', 'r')
list_of_AlpaNumeric_Strings: list[str] = file.readlines()
# print(list_of_AlpaNumeric_Strings)
file.close()


class SpelledNumberConverter:
    def __init__(self):
        self.spelled_to_digit = {
            'zero': "0",
            'one':  "1",
            'two': "2",
            'three': "3",
            'four': "4",
            'five': "5",
            'six': "6",
            'seven': "7",
            'eight': "8",
            'nine': "9",
            'ten': "10",
            'eleven': "11",
            'twelve': "12",
            'thirteen': "13",
            'fourteen': "14",
            'fifteen': "15",
            'sixteen': "16",
            'seventeen': "17",
            'eighteen': "18",
            'nineteen': "19",
            'twenty': "20",
            'thirty': "30",
            'forty': "40",
            'fifty': "50",
            'sixty': "60",
            'seventy': "70",
            'eighty': "80",
            'ninety': "90"
        }


def parse_spelled_out_num_to_int(input_string: str, spelled_number: str, replacement_number_digit) -> str:
    pattern = re.compile(re.escape(spelled_number), re.IGNORECASE)
    result = pattern.sub(spelled_number[0]+replacement_number_digit+spelled_number[-1], input_string)
    return result

def parse_all_spelled_nums_in_string_to_digits(unparsed_string, spelledNumberConverter: SpelledNumberConverter) -> str:
    for spelled_Number, digit in spelledNumberConverter.spelled_to_digit.items():
        unparsed_string = parse_spelled_out_num_to_int(
            unparsed_string, spelled_Number, digit)
    return unparsed_string

def get_numerical_values_only(input_string: str) -> str:
    return re.sub(r'[^0-9]', '', input_string)

def getStringSum(long_List: list[str], Spelled_Number_converter: SpelledNumberConverter) -> int:
    numbers_list: list[int] = []
    for unparsed_string in long_List:
        unparsed_string = parse_all_spelled_nums_in_string_to_digits(unparsed_string, Spelled_Number_converter)
        filtered_string = get_numerical_values_only(unparsed_string)
        numbers_list.append(int(filtered_string[0]+filtered_string[-1]))
    return sum(numbers_list)

spelledNumberConverter = SpelledNumberConverter()

example = [
"two1nine",
"eightwothree",
"abcone2threexyz",
"xtwone3four",
"4nineeightseven2",
"zoneight234",
"7pqrstsixteen"
]
total = getStringSum(list_of_AlpaNumeric_Strings, spelledNumberConverter)
print(total)
Example_total = getStringSum(example, spelledNumberConverter)
print(Example_total)
