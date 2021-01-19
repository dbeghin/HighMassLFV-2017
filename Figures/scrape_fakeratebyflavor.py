#!/usr/bin/env python
import ROOT
import re
from array import array


file=ROOT.TFile("../HighMassLFVMuTau/fakerate_factorised_OSvsSSmystery.root","r")


ends=[
    "total",
    "flavor_down",
    "flavor_up",
    "flavor_strange",
    "flavor_charm",
    "flavor_bottom",
    "flavor_gluon",
]

var="TauPt_"



file_out=open("fakeratebyflavor.tex", "w")
header="\\documentclass[11pt]{beamer}\n"
header+="\\usetheme{Copenhagen}\n"
header+="\\usepackage[utf8]{inputenc}\n"
header+="\\usepackage[T1]{fontenc}\n"
header+="\\usepackage{amsmath}\n"
header+="\\usepackage{amsfonts}\n"
header+="\\usepackage{amssymb}\n"
header+="\\usepackage{changepage}\n"
header+="\\usepackage{multirow}\n\n"

header+="\\begin{document}\n"
header+="\\begin{frame}\n"
header+="\\begin{adjustwidth}{-2.5em}{-2em}\n"
#header+="\\tiny\n"
header+="\\fontsize{0.15cm}{0.17cm}\\selectfont\n"
header+="\\begin{tabular}{|l|c|}\n"
header+="\\hline\n"

file_out.write(header)
file_out.write("Jet flavor & Significance with cut \\\\\n")
file_out.write("\\hline\n")
for flavor in ends:
    h_fl=file.Get(var+flavor)

    value = round(h_fl.GetBinContent(2),3)
    error = round(h_fl.GetBinError(2),3)

    file_out.write("%s & $%s \\pm %s$ \\\\\n" %(flavor, value, error))

file_out.write("\\hline\n")

closer="\\end{tabular}\n"
closer+="\\end{adjustwidth}\n"
closer+="\\end{frame}\n"
closer+="\\end{document}\n"
file_out.write(closer)
file_out.close()
