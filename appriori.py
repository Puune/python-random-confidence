#!/usr/bin/env python3
__author__ = 'Panu Lindqvist'

import sys, numpy, random, math, copy as cp

#___MAIN___
def main():
    print ('Running appriori randomizer python script')
    print ('With params: ' + str(sys.argv))
    if len(sys.argv) < 5:
        raise RuntimeError('Bad input, refer to REAMDE.md')

    s = open(sys.argv[1], "r")  # open source
    t = open("target.csv","w+") # create target
    l = open("log.csv", "w") # create log
    try:
        if s.mode != 'r':
            raise IOError('Bad file')

        ## preprocess
        lines = s.readlines()
    
        # remove headers from values, store in array
        headers = strip_split(lines.pop(0))

        # convert lines to matrix
        matrix = lines_to_matrix(lines)
    
        # validate input params
        given = validate_candidates(strip_split(sys.argv[2]), headers)
        expected = validate_candidates(strip_split(sys.argv[3]), headers)
        total_perm = int(sys.argv[4])
        # turn names into indexes
        given = param_to_index(given, headers)
        expected = param_to_index(expected, headers)

        ## permutations
        # transactions = [fulfilled initial reqs, fulfilled all reqs]
        transactions = numpy.array([0, 0])
        perm = 0
        while(perm<total_perm):
            display_progress(perm, total_perm)
            matrix = shuffle_matrix(matrix)
            transactions += calc_confidence(matrix, given, expected)
            l.write(matrix)
            perm += 1

        # output
        t.write("Total transactions: " + str(len(matrix) * perm) + "\n")
        t.write("Transactions that fulfill initial requirement: " + str(transactions[0]) + "\n")
        t.write("Transactions that fulfill expection: " + str(transactions[1]) + "\n")
        t.write("Confidence number is: " + str(round(transactions[1] / transactions[0] * 10000) / 10000) + "\n")

    finally:
        s.close()
        t.close()
        l.close()
        
#___CALCULATION___
def calc_confidence(data, given, expected):
    transactions = numpy.array([0, 0])
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
    i = round((current / total) * 25)
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
    matrix = numpy.transpose(matrix) # Transpose matrix so columns are handled as rows
    for index, arr in enumerate(matrix):
        if index != 0:
            numpy.random.shuffle(matrix[index])
    return numpy.transpose(matrix)

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
    main()