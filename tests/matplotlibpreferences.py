# Copyright (C) 2013 - 2020 - Michael Baudin

import matplotlib

# Increase font size
def load_preferences(usetex=False):
    if usetex:
        matplotlib.rcParams["text.usetex"] = True
        matplotlib.rcParams["font.family"] = "serif"
        matplotlib.rcParams["font.size"] = "10"

