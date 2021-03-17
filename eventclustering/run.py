###################################################################################################
#
# run.py
#
# Copyright (C) by Andreas Zoglauer.
# All rights reserved.
#
# Please see the file License.txt in the main repository for the copyright-notice. 
#  
###################################################################################################

  
  
###################################################################################################


import os
import sys
import argparse
import ROOT
from EC import EventClustering
  
  
###################################################################################################


"""
This is the main program for the event clustering testing and training in python.
For all the command line options, try:

python3 run.py --help

"""


parser = argparse.ArgumentParser(description='Perform training and/or testing of the event clustering machine learning tools.')
parser.add_argument('-f', '--file', default='EC.hits4.groups3.eventclusterizer.root', help='File name used for training/testing')
parser.add_argument('-c', '--complete', action='store_true', help='Try to find similar data files and train/test them too')
parser.add_argument('-o', '--output', default='Results', help='Prefix for the output filename and directory')
parser.add_argument('-b', '--energy', default='0,10000', help='Energy bins. Example: 0,10000')
parser.add_argument('-l', '--layout', default='3*N,N', help='Layout of the hidden layer. Default: 3*N,N')
parser.add_argument('-a', '--algorithm', default='MLP', help='Machine learning algorithm. Allowed: MLP')
parser.add_argument('-m', '--maxevents', default='10000', help='Maximum number of events to use')
parser.add_argument('-e', '--onlyevaluate', action='store_true', help='Only test the approach')

args = parser.parse_args()

AI = EventClustering(args.file, args.output, args.algorithm, args.layout, args.energy, int(args.maxevents))

if args.onlyevaluate == False:
  if AI.train(args.complete) == False:
    sys.exit()

if AI.test(args.complete) == False:
  sys.exit()


# prevent Canvases from closing

List = ROOT.gROOT.GetListOfCanvases()
if List.LastIndex() > 0:
  print("ATTENTION: Please exit by clicking: File -> Close ROOT! Do not just close the window by clicking \"x\"")
  print("           ... and if you didn't honor this warning, and are stuck, execute the following in a new terminal: kill " + str(os.getpid()))
  ROOT.gApplication.Run()


# END
###################################################################################################
