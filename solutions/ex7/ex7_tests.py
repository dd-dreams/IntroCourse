import io
from contextlib import redirect_stdout
import ex7
import sys

_colorama_enabled = False
try:
    import colorama

    colorama.init()
    _colorama_enabled = True
except ModuleNotFoundError:
    pass
color_red = (lambda text: f"\033[31m{text}\033[0m") if _colorama_enabled else (lambda text: text)
color_red_bold = (lambda text: f"\033[31;1m{text}\033[0m") if _colorama_enabled else (lambda text: text)

color_green = (lambda text: f"\033[92m{text}\033[0m") if _colorama_enabled else (lambda text: text)
color_green_bold = (lambda text: f"\033[92;1m{text}\033[0m") if _colorama_enabled else (lambda text: text)
italics_green = (lambda text: f"\033[92;3m{text}\033[0m") if _colorama_enabled else (lambda text: text)

color_blue = (lambda text: f"\033[34m{text}\033[0m") if _colorama_enabled else (lambda text: text)
italics_blue = (lambda text: f"\033[34;3m{text}\033[0m") if _colorama_enabled else (lambda text: text)

color_yellow = (lambda text: f"\033[93m{text}\033[0m") if _colorama_enabled else (lambda text: text)
color_yellow_bold = (lambda text: f"\033[93;1m{text}\033[0m") if _colorama_enabled else (lambda text: text)
TEST_FEEDBACK_RIGHT = {
    "print_to_n": color_green_bold("=== Passed test \" print_to_n \" \n"),
    "dig_sum": color_green_bold("=== Passed test \" digit_sum \" \n"),
    "is_prime": color_green_bold("=== Passed test \" is_prime \"\n"),
    "hanoi": color_green_bold("=== Passed test \" hanoi time \"\n"),
    "print_seq": color_green_bold("=== Passed test \" print_sequences \"\n"),
    "print_seq_no": color_green_bold("=== Passed test \" print_no_repetition_sequences \"\n"),
    "parentheses": color_green_bold("=== Passed test \" parentheses \"\n"),
    "flood_fill": color_green_bold("=== Passed test \" flood_fill \"\n")
}
WRONG_FEEDBACKS = {
    "print_to_n": color_red("\twhen n = 10\n"),
    "print_to_n<1": color_red("\twhen n<1\n"),
    "dig_sum1": color_red("\twhen n = 3\n"),
    "dig_sum2": color_red("\twhen n = 2684\n"),
    "dig_sum3": color_red("\twhen n = 100\n"),
    "is_primeT": color_red("\twhen n is prime\n"),
    "is_primeF": color_red("\twhen n isn't a prime\n"),
    "is_prime0": color_red("\twhen n < 1\n"),
    "is_prime1": color_red("\twhen n = 1\n"),
    "hanoi": color_red("\tthe run time was too long \n"),
    "print_seq0": color_red("\twhen n = 0 \n") + color_blue("(it should print an empty string \"\" \n)"),
    "print_seq1": color_red(" \twhen n = 1\n"),
    "print_seq2": color_red("\twhen input is [a,b,c,d],n = 2\n"),
    "print_seq3": color_red("\twhen input is [a,b,c,d],n = 4\n"),
    "print_seq_no0": color_red("\twhen n = 0 \n") + color_blue("(it should print an empty string \"\" \n)"),
    "print_seq_no1": color_red("\twhen n = 1\n"),
    "print_seq_no2": color_red("\twhen input is [a,b,c,d],n = 2\n"),
    "print_seq_no3": color_red("\twhen input is [a,b,c,d],n = 4\n"),
    "parentheses0": color_red("\twhen n = 0") + color_blue("it should be [\"\"]\n"),
    "parentheses4": color_red("\twhen n = 4\n"),
    "parentheses_too_many": color_red("\t\ttoo many elements\n"),
    "parentheses_too_little": color_red("\t\tnot enough elements\n"),
    "parentheses_duplicates": color_red("\t\tthere were duplicates\n")
}
TEST_FEEDBACK_WRONG = {
    "print_to_n": color_red_bold("=== Failed test \" print_to_n \" \n"),
    "dig_sum": color_red_bold("=== Failed test \" digit_sum \" \n"),
    "is_prime": color_red_bold("=== Failed test \" is_prime \"\n"),
    "hanoi": color_red_bold("=== Failed test \" hanoi time \"\n"),
    "print_seq": color_red_bold("=== Failed test \" print_sequences \"\n"),
    "print_seq_no": color_red_bold("=== Failed test \" print_no_repetition_sequences \"\n"),
    "parentheses": color_red_bold("=== Failed test \" parentheses \"\n"),
    "flood_fill": color_red_bold("=== Failed test \" flood_fill \"\n")
}


def print_result(bool, test, msgs=[]):
    if bool:
        sys.stderr.write(TEST_FEEDBACK_RIGHT[test])
    else:
        sys.stderr.write(TEST_FEEDBACK_WRONG[test])
        for st in msgs:
            sys.stderr.write(WRONG_FEEDBACKS[st])


def compare_lists(tst, real):
    if not len(tst) == len(real):
        return False
    for s in tst:
        if not s in real:
            return False
    for s in real:
        if not s in tst:
            return False
    return True


def no_duplicates(st):
    for i in range(len(st) - 1):
        if st[i] in st[i + 1:]:
            return False
    return True


def test_print_to_n():
    with io.StringIO() as buf, redirect_stdout(buf):
        bool = True
        msgs = []
        test = "print_to_n"
        ex7.print_to_n(-1)
        output = buf.getvalue()
        if output != "":
            bool = False
            msgs += [test + "<1"]
        ex7.print_to_n(10)
        output = buf.getvalue()
        if output != "1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n":
            bool = False
            msgs += [test]
        print_result(bool, test, msgs)


def test_dig_sum():
    bool = True
    test = "dig_sum"
    msgs = []
    output = ex7.digit_sum(3)
    if output != 3:
        bool = False
        msgs += [test + "1"]
    output = ex7.digit_sum(2684)
    if output != 20:
        bool = False
        msgs += [test + "2"]
    output = ex7.digit_sum(100)
    if output != 1:
        bool = False
        msgs += [test + "3"]
    print_result(bool, test, msgs)


def test_is_prime():
    bool = True
    test = "is_prime"
    msgs = []
    p = ex7.is_prime(31)
    if not p:
        bool = False
        msgs += [test + "T"]
    p = ex7.is_prime(32) or ex7.is_prime(121)
    if p:
        bool = False
        msgs += [test + "F"]
    try:
        assert ex7.is_prime(-1) == False
        assert ex7.is_prime(0) == False
    except:
        bool = 0
        msgs += [test + "0"]
    try:
        assert ex7.is_prime(1) == False
    except:
        bool = 0
        msgs += [test + "1"]
    print_result(bool, test, msgs)


def test_print_seq():
    test = "print_seq"
    msgs = []
    bool = True
    arr = ["a", "b", "c", "d"]
    with io.StringIO() as buf, redirect_stdout(buf):
        ex7.print_sequences(["h"], 0)
        tst = buf.getvalue()
    if not tst == "\n":
        bool = False
        msgs += [test + "0"]
    with io.StringIO() as buf, redirect_stdout(buf):
        ex7.print_sequences(["c", "v"], 1)
        tst = buf.getvalue()
    if tst != "c\nv\n" and tst != "v\nc\n":
        bool = False
        msgs += [test + "1"]
    with io.StringIO() as buf, redirect_stdout(buf):
        ex7.print_sequences(arr, 2)
        tst = buf.getvalue()
    tst = tst.split("\n")
    real = "aa\nab\nac\nad\nba\nbb\nbc\nbd\nca\ncb\ncc\ncd\nda\ndb\ndc\ndd\n"
    real = real.split("\n")
    if not compare_lists(tst, real):
        bool = False
        msgs += [test + "2"]
    with io.StringIO() as buf, redirect_stdout(buf):
        ex7.print_sequences(arr, 4)
        tst = buf.getvalue()
    tst = tst.split("\n")
    real = "aaaa\naaab\naaac\naaad\naaba\naabb\naabc\naabd\naaca\naacb\naacc\naacd\naada\naadb\naadc\naadd\nabaa" \
           "\nabab\nabac\nabad\nabba\nabbb\nabbc\nabbd\nabca\nabcb\nabcc\nabcd\nabda\nabdb\nabdc\nabdd\nacaa\nacab" \
           "\nacac\nacad\nacba\nacbb\nacbc\nacbd\nacca\naccb\naccc\naccd\nacda\nacdb\nacdc\nacdd\nadaa\nadab\nadac" \
           "\nadad\nadba\nadbb\nadbc\nadbd\nadca\nadcb\nadcc\nadcd\nadda\naddb\naddc\naddd\nbaaa\nbaab\nbaac\nbaad" \
           "\nbaba\nbabb\nbabc\nbabd\nbaca\nbacb\nbacc\nbacd\nbada\nbadb\nbadc\nbadd\nbbaa\nbbab\nbbac\nbbad\nbbba" \
           "\nbbbb\nbbbc\nbbbd\nbbca\nbbcb\nbbcc\nbbcd\nbbda\nbbdb\nbbdc\nbbdd\nbcaa\nbcab\nbcac\nbcad\nbcba\nbcbb" \
           "\nbcbc\nbcbd\nbcca\nbccb\nbccc\nbccd\nbcda\nbcdb\nbcdc\nbcdd\nbdaa\nbdab\nbdac\nbdad\nbdba\nbdbb\nbdbc" \
           "\nbdbd\nbdca\nbdcb\nbdcc\nbdcd\nbdda\nbddb\nbddc\nbddd\ncaaa\ncaab\ncaac\ncaad\ncaba\ncabb\ncabc\ncabd" \
           "\ncaca\ncacb\ncacc\ncacd\ncada\ncadb\ncadc\ncadd\ncbaa\ncbab\ncbac\ncbad\ncbba\ncbbb\ncbbc\ncbbd\ncbca" \
           "\ncbcb\ncbcc\ncbcd\ncbda\ncbdb\ncbdc\ncbdd\nccaa\nccab\nccac\nccad\nccba\nccbb\nccbc\nccbd\nccca\ncccb" \
           "\ncccc\ncccd\nccda\nccdb\nccdc\nccdd\ncdaa\ncdab\ncdac\ncdad\ncdba\ncdbb\ncdbc\ncdbd\ncdca\ncdcb\ncdcc" \
           "\ncdcd\ncdda\ncddb\ncddc\ncddd\ndaaa\ndaab\ndaac\ndaad\ndaba\ndabb\ndabc\ndabd\ndaca\ndacb\ndacc\ndacd" \
           "\ndada\ndadb\ndadc\ndadd\ndbaa\ndbab\ndbac\ndbad\ndbba\ndbbb\ndbbc\ndbbd\ndbca\ndbcb\ndbcc\ndbcd\ndbda" \
           "\ndbdb\ndbdc\ndbdd\ndcaa\ndcab\ndcac\ndcad\ndcba\ndcbb\ndcbc\ndcbd\ndcca\ndccb\ndccc\ndccd\ndcda\ndcdb" \
           "\ndcdc\ndcdd\nddaa\nddab\nddac\nddad\nddba\nddbb\nddbc\nddbd\nddca\nddcb\nddcc\nddcd\nddda\ndddb\ndddc" \
           "\ndddd\n "
    real = real.split("\n")
    if not compare_lists(tst, real):
        bool = False
        msgs += [test + "3"]
    print_result(bool, test, msgs)


def test_print_seq_no():
    test = "print_seq_no"
    msgs = []
    bool = True
    arr = ["a", "b", "c", "d"]
    with io.StringIO() as buf, redirect_stdout(buf):
        ex7.print_no_repetition_sequences(["h"], 0)
        tst = buf.getvalue()
    if not tst == "\n":
        bool = False
        msgs += [test + "0"]
    with io.StringIO() as buf, redirect_stdout(buf):
        ex7.print_sequences(["c", "v"], 1)
        tst = buf.getvalue()
    if tst != "c\nv\n" and tst != "v\nc\n":
        bool = False
        msgs += [test + "1"]
    with io.StringIO() as buf, redirect_stdout(buf):
        ex7.print_no_repetition_sequences(arr, 2)
        tst = buf.getvalue()
    tst = tst.split("\n")
    real = "ab\nac\nad\nba\nbc\nbd\nca\ncb\ncd\nda\ndb\ndc\n"
    real = real.split("\n")
    if not compare_lists(tst, real):
        bool = False
        msgs += [test + "2"]
    with io.StringIO() as buf, redirect_stdout(buf):
        ex7.print_no_repetition_sequences(arr, 4)
        tst = buf.getvalue()
    tst = tst.split("\n")
    real = "abcd\nabdc\nacbd\nacdb\nadbc\nadcb\nbacd\nbadc\nbcad\nbcda\nbdac\nbdca\ncabd\ncadb\ncbad\ncbda\ncdab" \
           "\ncdba\ndabc\ndacb\ndbac\ndbca\ndcab\ndcba\n "
    real = real.split("\n")
    if not compare_lists(tst, real):
        bool = False
        msgs += [test + "3"]
    print_result(bool, test, msgs)


def test_parentheses():
    bool = True
    msgs = []
    test = "parentheses"
    tst = ex7.parentheses(0)
    if not tst == [""]:
        bool = False
        msgs += [test + "0"]
    tst = ex7.parentheses(4)
    real = ['()()()()', '()()(())', '()(())()', '()(()())', '()((()))', '(())()()', '(())(())', '(()())()', '((()))()',
            '(()()())', '(()(()))', '((())())', '((()()))', '(((())))']
    if not compare_lists(tst, real):
        bool = False
        msgs += [test + "4"]
        if len(tst) < 14:
            msgs += [test + "_too_little"]
        if len(tst) > 14:
            msgs += [test + "_too_many"]
        if not no_duplicates(tst):
            msgs += ["_duplicates"]
    print_result(bool, test, msgs)


def test_flood_fill():
    test = "flood_fill"
    images0 = [[["*", "*", "*", "*"], ["*", ".", ".", "*"], ["*", "*", "*", "*"], ["*", ".", ".", "*"],
                ["*", "*", "*", "*"]],
               [["*", "*", "*", "*"], ["*", ".", ".", "*"], ["*", "*", "*", "*"]],
               [["*", "*", "*", "*"], ["*", ".", ".", "*"], ["*", ".", ".", "*"], ["*", ".", ".", "*"],
                ["*", "*", "*", "*"]],
               [["*", "*", "*"], ["*", ".", "*"], ["*", "*", "*"]],
               [["*", "*", "*", "*", "*"], ["*", ".", "*", ".", "*"], ["*", "*", ".", "*", "*"],
                ["*", ".", "*", ".", "*"],
                ["*", "*", "*", "*", "*"]]]
    images = [[["*", "*", "*", "*"], ["*", ".", ".", "*"], ["*", "*", "*", "*"], ["*", ".", ".", "*"],
               ["*", "*", "*", "*"]],
              [["*", "*", "*", "*"], ["*", ".", ".", "*"], ["*", "*", "*", "*"]],
              [["*", "*", "*", "*"], ["*", ".", ".", "*"], ["*", ".", ".", "*"], ["*", ".", ".", "*"],
               ["*", "*", "*", "*"]],
              [["*", "*", "*"], ["*", ".", "*"], ["*", "*", "*"]],
              [["*", "*", "*", "*", "*"], ["*", ".", "*", ".", "*"], ["*", "*", ".", "*", "*"],
               ["*", ".", "*", ".", "*"],
               ["*", "*", "*", "*", "*"]]]
    starts = [(1, 1), (1, 2), (3, 2), (1, 1), (2, 2)]
    results = [
        [['*', '*', '*', '*'], ['*', '*', '*', '*'], ['*', '*', '*', '*'], ['*', '.', '.', '*'], ['*', '*', '*', '*']],
        [['*', '*', '*', '*'], ['*', '*', '*', '*'], ['*', '*', '*', '*']],
        [['*', '*', '*', '*'], ['*', '*', '*', '*'], ['*', '*', '*', '*'], ['*', '*', '*', '*'], ['*', '*', '*', '*']],
        [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']],
        [['*', '*', '*', '*', '*'], ['*', '.', '*', '.', '*'], ['*', '*', '*', '*', '*'], ['*', '.', '*', '.', '*'],
         ['*', '*', '*', '*', '*']]]
    counter = 0
    for img, img0, st, res in zip(images, images0, starts, results):
        ex7.flood_fill(img, st)
        if not img == res:
            sys.stderr.write("test: \n start = " + str(st) + "\n")
            print_img(img0, "blue")
            sys.stderr.write("right output: \n")
            print_img(res, "green")
            sys.stderr.write("your output: \n")
            print_img(img, "red")
            counter += 1
    print_result(counter == 0, test)


def print_img(img, c):
    for line in img:
        if c == "green":
            sys.stderr.write("\t" + color_green(str(line)) + "\n")
        if c == "red":
            sys.stderr.write("\t" + color_red(str(line)) + "\n")
        if c == "blue":
            sys.stderr.write("\t" + color_blue(str(line)) + "\n")


if __name__ == '__main__':
    with io.StringIO() as buf, redirect_stdout(buf):
        sys.stderr.write(
            color_yellow_bold("This test doesnt test the hanoi function. look at the animation and CHECK IT\n"))
        test_print_to_n()
        test_dig_sum()
        test_is_prime()
        test_print_seq()
        # test_print_seq_no()
        test_parentheses()
        test_flood_fill()
