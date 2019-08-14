import argparse as ap
import os

def credit_card_concealer(exposed_card_number):
    l = exposed_card_number.split(" ")
    concealed = ""
    for i in range(len(l)):
        elem = l[i]
        if i == len(l) - 1:
            concealed = concealed + elem
        else:
            elem_length = len(elem)
            to_add = "X"*elem_length
            concealed = concealed + to_add + " "

    return concealed

score_file =  "./" + os.path.splitext(__file__)[0]+ "_score.txt"

def get_test_data():
    test_data = {"4353 1234 1232 3674": "XXXX XXXX XXXX 3674", "7777 1232 3674": "XXXX XXXX 3674","777712323674":-1,"777 abvc 3654":-2}
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
        student_result = credit_card_concealer(test_case)
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
        print(str(credit_card_concealer(leftovers[0])))
