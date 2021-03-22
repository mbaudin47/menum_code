#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Une librairie pour exécuter des scripts Python.
"""
import subprocess
import os


def updatePYTHONPATH(pythonpath):
    """
    Met à jour la variable PYTHONPATH
    
    Exemple:
    pythonpath=os.path.join(thisdirectory,"..","..","..","Scripts-Eleves","Py3")
    updatePYTHONPATH(pythonpath)
    """
    pythonpath = pythonpath.replace("\\", "/")
    environnement = [i for i in os.environ]
    if "PYTHONPATH" in environnement:
        os.environ["PYTHONPATH"] = pythonpath + ":" + os.environ["PYTHONPATH"]
    else:
        os.environ["PYTHONPATH"] = pythonpath
    return


def executeOneScript(filename):
    """
    Exécute le script Python filename 
    et affiche le résultat dans la console. 
    
    Exemple:
        executeOneScript("numpy-demo.py")
    """
    print(u"+ Running %s" % (filename))
    cmd = "python " + filename
    cp = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE)
    s = cp.stdout.decode("utf8")
    print(s)
    return None


def generateOutputFromPythonScript(pythonscript):
    """
    Generates the output text file of a Python script.
    
    Exemple:
        generateOutputFromPythonScript("numpy-demo.py")

    génère le fichier numpy-demo.txt
    """
    print(u"+ Executing ", pythonscript)
    dirname = os.path.dirname(pythonscript)
    basename = os.path.basename(pythonscript)
    fileName, fileExtension = os.path.splitext(basename)
    outputfilename = os.path.join(dirname, fileName + ".txt")
    print(u"Output: ", outputfilename)
    # Execute the command
    command = "python3 " + pythonscript + " > " + outputfilename
    print(command)
    returncode = os.system(command)
    if returncode != 0:
        raise ValueError("Wrong return code = %s" % (returncode))
    # Print the output, line by line
    f = open(outputfilename, "r")
    all_lines = f.readlines()
    f.close()
    for line in all_lines:
        singleline = line.replace("\n", "")
        print(singleline)
    return None


def runOneScript(filename):
    """
    Exécute le script Python filename. 
    
    Exemple:
        runOneScript("numpy-demo.py")
    """
    # Ancienne fonction.
    # executeOneScript(filename)
    # Nouvelle fonction
    generateOutputFromPythonScript(filename)
    return None


def runDirectory(dirname, except_script="run-all.py", except_pattern="squelette"):
    """
    Exécute les scripts Python dans le répertoire, 
    à l'exception du script "except_script" (sinon, cela génère 
    un appel récursif sans fin).
    """
    print(u"Searching in ", dirname, "...")
    nbfiles = 0
    for dirpath, dirnames, filenames in os.walk(dirname):
        for shortfilename in filenames:
            filename, fileExtension = os.path.splitext(shortfilename)
            fn = os.path.join(dirpath, shortfilename)
            if (
                fileExtension == ".py"
                and shortfilename != except_script
                and except_pattern not in shortfilename
            ):
                print(u"(%d) %-40s : Python" % (nbfiles, fn))
                runOneScript(fn)
                nbfiles = nbfiles + 1

    print(u"Number of Python files:", nbfiles)
    return None
