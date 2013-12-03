#!/usr/bin/env python
from sys import argv
from os import system

e = argv[1][:-3]
print e

system("pandoc -s --mathjax='http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML' --highlight-style tango " + e +  ".md -o " + e + ".html")
system("pandoc -s " + e +  ".md -o " + e + ".docx")
system("pandoc -s --listings -V geometry:margin=1.5cm " + e +  ".md -o " + e + ".pdf")
