#!/usr/bin/env bash
testfile= "./DSLCC-v2/DSLCC-v2.1/test2.txt"
Solnfile= "./DSLCC-v2/DSLCC-v2.1/testSoln2.txt"
Predfile= "./DSLCC-v2/DSLCC-v2.1/myTestSoln2.txt"
python langid.py/build/lib/langid/langid.py -m ./corpus.model/model -n --line < $testfile > $Predfile
python check.py $Solnfile $Predfile
