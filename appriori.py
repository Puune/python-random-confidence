#!/usr/bin/env python3
__author__ = 'Panu Lindqvist'

import sys, numpy as np, random, math, copy as cp
import profiler

#___MAIN___
def entrypoint():
    try:
        args = arg_extract(sys.argv)

        @profiler.profile()
        def profiled_main():
            main(args)

        if 'deb' in args:
            profiled_main()
        else:
            main(args)

    except Exception as e:
        print(e.args)
    
    finally:
        input("press enter to exit")

def main(args):
    print ('Running appriori randomizer python script')
    print ('With params', args)


    s = open(args['in'], "r")  # open source
    t = open("target.csv","w+") # create target    

    try:
        if s.mode != 'r':
            raise Exception('Bad file')

        ## preprocess
        lines = s.readlines()
    
        # remove headers from values, store in array
        headers = strip_split(lines.pop(0))

        # convert lines to matrix
        matrix = lines_to_matrix(lines)
    
        # validate input params
        given = validate_candidates(strip_split(args["giv"]), headers)
        expected = validate_candidates(strip_split(args["exp"]), headers)
        total_perm = int(args["perm"])
        # turn names into indexes
        given = param_to_index(given, headers)
        expected = param_to_index(expected, headers)

        ## permutations
        # transactions = [fulfilled initial reqs, fulfilled all reqs]
        transactions = np.array([0, 0])
        perm = 0
        while(perm<total_perm):
            display_progress(perm, total_perm)
            matrix = shuffle_matrix(matrix)
            transactions += calc_confidence(matrix, given, expected)
            perm += 1
        print("")

        # output
        t.write("Total transactions: " + str(len(matrix) * perm) + "\n")
        t.write("Transactions that fulfill initial requirement: " + str(transactions[0]) + "\n")
        t.write("Transactions that fulfill expection: " + str(transactions[1]) + "\n")
        t.write("Confidence number is: " + str(round(transactions[1] / transactions[0] * 10000) / 10000) + "\n")

    finally:
        s.close()
        t.close()
        print("done")    

def arg_extract(argv):
    argv.pop(0)
    args = { 'none': None }
    iterator = iter(argv)
    for opt in iterator:
        if opt in ('-i', '--input'):
            args['in'] = next(iterator)
        elif opt in ('-g', '--given'):
            args['giv'] = next(iterator)
        elif opt in ('-e', '--expected'):
            args['exp'] = next(iterator)
        elif opt in ('-p', '--permutations'):
            args['perm'] = int(next(iterator))
        elif opt in ('-d', '--debug') and next(iterator) != 'false':
            args['deb'] = True
        else:
            print("unknow option:", opt)
            next(iterator)

    if 'in' not in args:
        raise Exception('No input defined')
    elif None in (args['giv'], args['exp']):
        print("Running without given/expected params")
    return args

#___CALCULATION___
def calc_confidence(data, given, expected):
    transactions = [0,0]
    for arr in data:
        # case has initial requirements
        match_given = recursive_validation(arr, given[0], cp.copy(given))
        if match_given:
            transactions[0] += 1

        # case fulfills expectation
        match_expected = recursive_validation(arr, expected[0], cp.copy(expected))
        if match_given and match_expected:
            transactions[1] += 1
    return transactions

def recursive_validation(arr, current, left):
    if arr[current] == "1":
        if len(left) > 0:
            current = left.pop(0)
            return recursive_validation(arr, current, left) #next recursion
        else: 
            return True # end of recursion
    else: 
        return False # recursion detected mismatch

def calc_standard_confidence(confidences, total):
    a = 0
    for c in confidences:
        a += c
    return round(a / total * 10000) / 10000

#___VISUAL__
def display_progress(current, total):
    out = "Progress: ["
    i = np.round((current / total) * 25)
    k = 0
    while(k<25):
        if(k<i):
            out += "#"
        else:
            out += " "
        k += 1
    print(out + "]", end='\r')

#___UTIL___
def param_to_index(arr, source):
    new_arr = []
    for member in arr:
        new_arr.append(source.index(member))
    return new_arr


def strip_split(toArr):
    toArr = toArr.strip().rstrip().replace(',', ';').replace(' ', '').split(';')
    toArr = remove_empty(toArr)
    return toArr

def validate_candidates(arr, source):
    for a in arr:
        if a not in source:
            error = 'param "' + a + '" not present in source data'
            raise RuntimeError(error)
    return arr

def remove_empty(x):
    x.reverse()
    if x[0] == '':
        x.pop(0)
    x.reverse()
    return x

def lines_to_matrix(lines):
    matrix = [] # Values matrix
    i = 0
    while (i < len(lines)):
        arr = strip_split(lines[i])
        matrix.append(arr)
        i += 1
    return matrix

def shuffle_matrix(matrix):
    matrix = np.transpose(matrix) # Transpose matrix so columns are handled as rows
    for index, arr in enumerate(matrix):
        if index != 0:
            np.random.shuffle(matrix[index])
    return np.transpose(matrix)

def arr_to_string(arr):
    out = ""
    for a in arr:
        out += a + ';'
    return out

def matrix_to_string(matrix):
    new_lines = ""
    for e in matrix:
        new_lines += (arr_to_string(e)) + "\n"
    return new_lines

if __name__ == "__main__":
    entrypoint()