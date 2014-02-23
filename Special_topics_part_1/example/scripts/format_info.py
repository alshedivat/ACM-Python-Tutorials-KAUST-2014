#!/usr/bin/env python

import sys

name = str(sys.argv[1])
height = float(sys.argv[2])
weight = float(sys.argv[3])
age = int(sys.argv[4])

f = open('results/patient_' + name + '_' + str(age) + '.txt', 'w')

f.write( "patient's name: " + name + "\n")
f.write( "patient's age: " + str(age) + " Years\n")
f.write( "patient's Weight: " + str(weight) + " kgs\n")
f.write( "patient's height: " + str(height) + " Meters\n")

f.close
