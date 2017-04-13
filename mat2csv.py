# Convert .mat files into .csv files

import csv
import scipy.io
import sys
import os
import numpy

def main(pathIn='/home/aspma/MIR/Leveau/goodlabels/',pathOut='/home/aspma/MIR/Leveau/goodlabels/'):
	listOfTxt = os.listdir(pathIn)
	for file in listOfTxt:

		if '.mat' not in file: continue

		mat_file = pathIn+file
		csv_file = pathOut+file[:-3]+'csv'

		sax = scipy.io.loadmat(mat_file)
		onsets = sax['labels_time'].T
		numpy.savetxt(csv_file, onsets, delimiter = '\t')

		

main()
