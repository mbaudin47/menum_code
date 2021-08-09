# -*- coding: utf-8 -*-
"""
Exécute les scripts Python dans le répertoire courant. 
"""

from execpython import runDirectory
import os

thisdirectory = os.path.dirname(__file__)
thisdirectory = os.path.abspath(thisdirectory)
runDirectory(thisdirectory, except_script="run-all.py")
