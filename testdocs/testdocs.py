import collections
import os
import sys
import time


def generate_test_docs(jira_input):
    print('(generate_test_docs) begin::')
    jira_list = jira_input
    if not jira_list:
        return 0
    else:
        print('(generate_test_docs) jira_list::',jira_list)
        for l in jira_list:
            print('(generate_test_docs) item::',l)
            generate_single_doc(l)
        return 1

def generate_single_doc(jira_number):
    if os.path.isfile(jira_number):
        print('(generate_single_doc) found::', jira_number)
    # filepath = ".\output\"+jira_number"
    # filepath = jira_number+"_testing.txt"
    filepath = "output//"+jira_number+"_testing.txt"
    file = open(filepath, "w")
    file.write(jira_number+" -- SUMMARY-PLACEHOLDER\n")
    file.write("\n")
    file.write("https://cashstar.atlassian.net/browse/"+jira_number+"\n")
    file.write("\n")
    file.write("=====================================================\n")
    file.write("\n")
    file.write("FUNCTIONAL CHANGE(S)\n")
    file.write("-----------------------------------------------------\n")
    file.write("\n")
    file.write("\n")

    file.write("ACCEPTANCE CRITERIA\n")
    file.write("-----------------------------------------------------\n")
    file.write("\n")
    file.write("\n")

    file.write("TARGET VERSION / ENVIRONMENT\n")
    file.write("-----------------------------------------------------\n")
    file.write("\n")
    file.write("\n")

    file.write("CONFIG / LAB WORK REQUIRED\n")
    file.write("-----------------------------------------------------\n")
    file.write("\n")
    file.write("\n")

    file.write("QUERIES REQUIRED\n")
    file.write("-----------------------------------------------------\n")
    file.write("\n")
    file.write("\n")

    file.write("TEST / USE CASES\n")
    file.write("-----------------------------------------------------\n")
    file.write("\n")
    file.write("\n")

    file.close()

def generate_sprint_begin_marker(new_sprint):
    print('(generate_sprint_begin_marker) gen_sprint_marker:: SPRINT:',new_sprint)
    sprint_number = str(new_sprint)

    filepath = "output//sprint_"+sprint_number+"_marker.txt"
    if os.path.isfile(filepath):
        print('(generate_sprint_begin_marker) found::', sprint_number)

    file = open(filepath, "w")
    file.write(sprint_number+" -- BEGIN-SPRINT MARKER\n")
    file.write("\n")
    file.write("================================================\n")

    file.close()
    return

def get_new_sprint():
    print('(gns) get_new_sprint:: PLACEHOLDER')
    # sprint 157; 2019-03-21 to 2019-04-03
    return '157'

def load_jiras():
    with open("data/jira_input.txt", "r") as ins:
        tmp = ins.read().split("\n")
        inputlist = [i for i in tmp]
        # inputlist sample, e.g. print(inputlist)
        # ['CAM-0001', 'CAM-0002', 'CAM-0003']
    return inputlist


def main():
    print('(testdocs) main:')
    print()

    new_sprint = get_new_sprint()
    print('(testdocs) sprint::  ',new_sprint)

    generate_sprint_begin_marker(new_sprint)


    jira_list = load_jiras()

    genstatus = generate_test_docs(jira_list)
    print('(main) genstatus::',genstatus)

    print()
    print('(testdocs) end::')
    return 0


# ----------------------------------------
if __name__ == '__main__':
    result = main()
    sys.exit(result)
