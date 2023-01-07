#!/bin/sh

set -xe

export PYTHONPATH="$PWD/Scripts-Eleves/Py3:$PYTHONPATH"
export PYTHONPATH="$PWD/tests:$PYTHONPATH"

cd Python/Scripts && python3 run-all.py && cd -
cd Problemes/Scripts && python3 run-all.py && cd -
cd Flottants/Scripts && python3 run-all.py && cd -
cd Methodes/Scripts && python3 run-all.py && cd -
cd Matrices/Scripts && python3 run-all.py && cd -
cd Syslin/Scripts && python3 run-all.py && cd -
cd Interp/Scripts && python3 run-all.py && cd -
cd Diff/Scripts && python3 run-all.py && cd -
cd Leastsq/Scripts && python3 run-all.py && cd -
cd Integration/Scripts && python3 run-all.py && cd -
cd EDOs/Scripts && python3 run-all.py && cd -
cd Optim/Scripts && python3 run-all.py && cd -
cd Zeros/Scripts && python3 run-all.py && cd -
