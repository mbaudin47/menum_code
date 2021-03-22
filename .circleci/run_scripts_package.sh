#!/bin/sh

set -xe

export PYTHONPATH="$PWD/Scripts-Eleves/Py3:$PYTHONPATH"

cd ..

#
cd Scripts-Eleves/Py3 && python3 floats.py && cd -
cd Scripts-Eleves/Py3 && python3 fzero.py && cd -
cd Scripts-Eleves/Py3 && python3 interp.py && cd -
cd Scripts-Eleves/Py3 && python3 leastsq.py && cd -
cd Scripts-Eleves/Py3 && python3 linalg.py && cd -
cd Scripts-Eleves/Py3 && python3 numdiff.py && cd -
cd Scripts-Eleves/Py3 && python3 odes.py && cd -
cd Scripts-Eleves/Py3 && python3 optim.py && cd -
cd Scripts-Eleves/Py3 && python3 quadrature.py && cd -

