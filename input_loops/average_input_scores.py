"""CIS 189
Alex Rickels
Mod 5 Topic 2 - while loop """

# declare a variable sum to store the scores total
# declare a variable to store the number of items in the list, use len()
# write a for loop to sum the items in the list
# declare a variable avg to calculate the average
# return  # variable avg


def average(score_list):
    total_scores = sum(score_list)
    items_in_list = len(score_list)
    average_score = total_scores/items_in_list
    return average_score


if __name__ == '__main__':
    average(list)
