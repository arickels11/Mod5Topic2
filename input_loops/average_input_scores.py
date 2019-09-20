"""CIS 189
Alex Rickels
Mod 5 Topic 2 - while loop"""


def average(score_list):
    total_scores = sum(score_list)
    items_in_list = len(score_list)
    average_score = total_scores/items_in_list
    return average_score


if __name__ == '__main__':
    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")
    scores = []
    score = 0
    while score != -1:
        try:
            score = int(input("Please enter a score, type -1 to end: "))
            if score == -1:
                break
            scores.append(score)
        except ValueError:
            print("Please enter a numerical value")
    avg_scores = average(scores)
    print(last_name, ", ", first_name, " grade: ", str(round(avg_scores, 2)))


#  tested 0, 70, 80, 90, 100. expected: 80, output: 80
#  tested 60, alex, 70, 80. expected: 70, output: 70
#  tested 2, 2, 3. expected: 2.33, output: 2.33
