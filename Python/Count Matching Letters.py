def count_correct_characters(correct, guess):
    if len(correct) != len(guess):
        raise Exception("");
    return sum([correct[i] == guess[i] for i in range(len(correct))]);