import argparse as ap
import os

def is_palindrome(word):
    word = ''.join(e for e in word if e.isalnum())
    word = word.lower()
    word_len = len(word)
    word_len_divided = word_len/2
    word_len_divided = int(word_len_divided)
    for i in range(word_len_divided):
        if word[i] != word[word_len - i - 1]:
            return False
    return True

score_file =  "./" + os.path.splitext(__file__)[0]+ "_score.txt"

def get_test_data():
    test_data = {"level": True, "poop": True, "canal": False,"firetruck":False,"avvaa":False, "aavva":False, "A man a plan a canal, Panama!":True}
    return test_data

def write_result_file(resultstr, num_error, num_test):
    score = int(round((float(num_test - num_error)/num_test)*100))
    #with open(score_file,'w') as f:
    print(resultstr + "\n\n")
    print("Score: " + str(num_test - num_error) + " out of " + \
                str(num_test) + " = " + str(score) + "%\n\n")
    print("*************Original submission*************")
    #print ("Scores written to " + score_file)

def grade():
    # First evaluate tests and store results.
    test_data = get_test_data()
    error_list = []
    correct_list = []
    num_test = 0

    for i, test_case in enumerate(test_data.keys()):
        num_test += 1
        student_result = is_palindrome(test_case)
        correct_result = test_data[test_case]
        if (correct_result != student_result):
            error_list.append((i,student_result,correct_result))
        else:
            correct_list.append((i,student_result))
    # Now report results.
    resultstr = ""
    if (len(error_list)==0):
        resultstr = 'Summary: All tests passed.'
    else:
        failure_spelling = ' failure' + ('s ' if len(error_list) > 1 else ' ')
        resultstr = 'Summary: Student output has ' + \
                str(len(error_list)) + failure_spelling + \
                'in ' + str(num_test) + ' tests.\n\nDetailed report:\n'
        for test_num,s_result,c_result in error_list:
            resultstr += '\nTest ' + str(test_num) + ' failed:\n   Student had:\t' + \
                    str(s_result) + '\n   Should have:\t' + str(c_result)
    for test_num,c_result in correct_list:
        resultstr += '\nTest ' + str(test_num) + ' succeeded:\n   Result is:\t' + \
                str(c_result) + '\n'

    write_result_file(resultstr, len(error_list), num_test)

if __name__ == '__main__':
    # Get the input arguments
    parser = ap.ArgumentParser(description="in_place_autograder")
    parser.add_argument('-g','--grade',dest='grader_mode', action='store_true',
            help='Indicates if the users wants the grader mode.')

    args, leftovers = parser.parse_known_args()
    if args.grader_mode:
        grade()
    else:
        print(str(is_palindrome(leftovers[0])))
