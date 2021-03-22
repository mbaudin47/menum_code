#!/bin/sh

set -xe

export PYTHONPATH="$PWD/Scripts-Eleves/Py3:$PYTHONPATH"
export PYTHONPATH="$PWD/tests:$PYTHONPATH"

cd Python/Scripts/Py3 && python3 run-all.py && cd -
cd Problemes/Scripts/Py3 && python3 run-all.py && cd -
cd Flottants/Scripts/Py3 && python3 run-all.py && cd -
cd Methodes/Scripts/Py3 && python3 run-all.py && cd -
cd Matrices/Scripts/Py3 && python3 run-all.py && cd -
cd Syslin/Scripts/Py3 && python3 run-all.py && cd -
cd Interp/Scripts/Py3 && python3 run-all.py && cd -
cd Diff/Scripts/Py3 && python3 run-all.py && cd -
cd Leastsq/Scripts/Py3 && python3 run-all.py && cd -
cd Integration/Scripts/Py3 && python3 run-all.py && cd -
cd EDOs/Scripts/Py3 && python3 run-all.py && cd -
cd Optim/Scripts/Py3 && python3 run-all.py && cd -
cd Zeros/Scripts/Py3 && python3 run-all.py && cd -

