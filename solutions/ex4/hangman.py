from ex4 import hangman_helper


def update_word_pattern(word, pattern, letter):  # function to check If the player guessed right or not it will
    # update the pattern
    chars = []
    st = ""
    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:  # to check if there is a letter in the word
                chars.append(letter)
            elif pattern[i] != '_':  # so it won't replace already found chars
                chars.append(pattern[i])
            else:
                chars.append('_')
        for i in chars:
            st += i  # put all founded chars in one string
        return st
    else:
        pass


def filter_words_list(words, pattern, wrong_guess_lst):
    hint_list = []
    is_true = True
    for i in words:
        if len(i) == len(pattern):
            for j in range(len(pattern)):
                if pattern[j] == '_':  # So it won't try to check if char equals to char in i, otherwise it will break
                    continue
                else:
                    if pattern[j] == i[j]:
                        is_true = True  # To check for every character
                    else:
                        is_true = False
                        break
            if is_true:
                for h in i:
                    if h not in wrong_guess_lst:  # to see the some chars are not in the wrong guess list
                        if i not in hint_list:
                            hint_list.append(i)
                        else:
                            break
                    else:
                        break
            else:  # so it won't stay as false in the next i
                is_true = True
        else:
            continue
    return hint_list


def run_single_game(words_list, score):
    word = hangman_helper.get_random_word(words_list)  # choosing a random word from words.txt
    pattern = ""
    wrong_guess_list = []
    good_guesses = []
    for i in range(len(word)):  # create the pattern
        pattern += '_'
    while pattern != word:
        msg = ""
        input_char = hangman_helper.get_input()
        guess = input_char[1]
        if 1 in input_char:  # if he just enter a character
            if guess == "":  # Otherwise for some reason it will give him tons of points...
                msg = "You have to guess."
            elif guess.isupper():
                msg = "The guess isn't a lowercase character."
            elif not guess.isalpha():
                msg = "The guess gotta be alphabetic."
            elif len(guess) > 1:
                msg = "You typed more then one character. If you want to type a word, then use '!*'."
            elif guess in good_guesses or guess in wrong_guess_list:
                msg = "Already guessed this character."
            elif guess is int:
                msg = "Not a character."
            else:
                if guess in word:
                    msg = ""
                    good_guesses.append(guess)  # so in the fourth elif it will check if the char already guessed
                    pattern = update_word_pattern(word=word, pattern=pattern, letter=guess)
                    if str(word).count(guess) > 1:
                        n = str(word).count(guess)
                        score += (n * (n + 1) // 2) - 1  # minus 1 because that's what they say. even if he's right
                else:
                    wrong_guess_list.append(guess)
                    msg = "Nope. Letter is not in word."
                    score -= 1
            hangman_helper.display_state(pattern=pattern, points=score, wrong_guess_lst=wrong_guess_list,
                                         msg=msg)  # print current status
            if score <= 0:
                break
        elif 2 in input_char:  # if he enters '!*' (replace * with the word)
            guess = input_char[1]
            n = 0
            for i in guess:
                if i in word:
                    if i not in pattern:
                        n += 1
                    pattern = update_word_pattern(word=word, pattern=pattern, letter=i)
            if n > 1:
                score += (n * (n + 1) // 2) - 1  # minus 1 because that's what they say. even if he's right.
            else:
                score -= 1
            if pattern == word:  # so it won't print display_state twice
                break
            else:
                hangman_helper.display_state(pattern=pattern, points=score, wrong_guess_lst=wrong_guess_list,
                                             msg=msg)
            if score <= 0:
                break
        elif 3 in input_char:  # if he enter '?'
            score -= 1
            new_hint = []
            hint = filter_words_list(words=words_list, pattern=pattern, wrong_guess_lst=wrong_guess_list)
            hint_length = hangman_helper.HINT_LENGTH
            n = hint_length
            if len(hint) > hangman_helper.HINT_LENGTH:
                new_hint.append(hint[hint_length * n // hint_length])
                new_hint.append(hint[2*n//hint_length])
                new_hint.append(hint[n//hint_length])
                new_hint.append(hint[0])
            hangman_helper.show_suggestions(new_hint)
            hangman_helper.display_state(pattern=pattern, points=score, wrong_guess_lst=wrong_guess_list,
                                         msg=msg)
    if pattern == word:
        msg = "You win!\n"
        hangman_helper.display_state(pattern=pattern, points=score, wrong_guess_lst=wrong_guess_list,
                                     msg=msg)
    else:
        msg = "You lost. the word was: {0}\n".format(word)
        hangman_helper.display_state(pattern=pattern, points=score, wrong_guess_lst=wrong_guess_list,
                                     msg=msg)
    return score


def main():
    words_list = hangman_helper.load_words()
    played = 1
    score = hangman_helper.POINTS_INITIAL  # Started points given from hangman_helper
    while True:
        if score > 0:
            score = run_single_game(words_list=words_list, score=score)
            if score <= 0:
                continue
            else:
                msg_try = "You played {0} games\nYou have {1} score so far\n".format(played, score)
                cont = hangman_helper.play_again(msg=msg_try)
                if cont:
                    played += 1
                    continue
                else:
                    break
        elif score <= 0:
            msg_try = "You played {0} games till you lost\nDo you want start a new series of games?".format(played)
            cont = hangman_helper.play_again(msg=msg_try)
            if cont:
                played = 1
                score = hangman_helper.POINTS_INITIAL  # Started points given from hangman_helper
                continue
            else:
                break
