file = open(
    fr'C:\Users\aamrl\OneDrive\Desktop\2023-CodingAdvent\Challenges\Day2\Day_two_Long_String.txt', 'r')
game_data: list[str] = file.readlines()
# print(list_of_AlpaNumeric_Strings)
file.close()

total_cubes = {"red": 12, "green": 13, "blue": 14 }

Example_data = {
    1: {
        'set1': {"blue": 3, "red": 4, "green": 0},
        'set2': {"blue": 6, "red": 1, "green": 2},
        'set3': {"blue": 0, "red": 0, "green": 2},
    },
    2: {
        'set1': {"blue": 1, "red": 0, "green": 2},
        'set2': {"blue": 4, "red": 1, "green": 3},
        'set3': {"blue": 1, "red": 1, "green": 1},
    },
    3: {
        'set1': {"blue": 6, "red": 20, "green": 8},
        'set2': {"blue": 5, "red": 4, "green": 13},
        'set3': {"blue": 15, "red": 1, "green": 5},
    },
    4: {
        'set1': {"blue": 6, "red": 3, "green": 1},
        'set2': {"blue": 15, "red": 6, "green": 3},
        'set3': {"blue": 15, "red": 14, "green": 3},
    },
    5: {
        'set1': {"blue": 1, "red": 6, "green": 3},
        'set2': {"blue": 2, "red": 1, "green": 2},
        'set3': {"blue": 0, "red": 0, "green": 0},
    },
}
# def find_occurrences(s, ch):
  # return [i for i, letter in enumerate(s) if letter == ch]
# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
def parse_line_of_game_data(string:str):
    line_of_game_data:dict[str,int]={
        "blue":0, "green":0, "red":0
        }
    num_stack:list[str] = []
    color_string:str ="" 
    index = string.index(":")
    while index < len(string):
        char = string[index]
        if(char.isnumeric()):
            num_stack.append(char)
            index+=1
        while(char != "," or char != ";"):
            if(char != " "):
                color_string +=char
                index+=1


def parse_game_data(game_data:list[str])->dict:
    parsed_game_data = {}
    for index,game in enumerate(game_data):
        parsed_game_data[index]= 

