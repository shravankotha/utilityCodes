import os
import sys
import numpy as np
import matplotlib.pyplot as plt  
from plotScatter2D import plotLine2D, plotScatter2D
#import argparse
        
def main():
    #parser = argparse.ArgumentParser()
    #parser.add_argument("datafilename")
    #parser.add_argument("--plottype",choices=['line','scatter'],default='line')
    #args = parser.parse_args()
    #print(args.echo)



    nArguments = len(sys.argv)    
    if nArguments < 10:
        text = """Nine command line arguments are expected: \
                \n\t(1) fileName \
                \n\t(2) Number of header lines to ignore \
                \n\t(3) column ID for X-data \
                \n\t(4) column ID for Y-data \
                \n\t(5) starting fraction of data to plot (0-1) \
                \n\t(6) ending fraction of data to plot (0-1) \                
                \n\t(7) type of plot (scatter/line)\
                \n\t(8) save the image (0/1) \
                \n\t(9) figure name to save
               """
                
        raise RuntimeError(text)
    
    # set all the optional arguments here
    markerStyle         = "o"
    markerSize          = 24
    markerColor         = "black"
    xScale              = "linear"
    yScale              = "linear"
    labelX              = "t (s)"
    labelY              = "T (C)"
    fontSizeXlabel      = 24
    fontSizeYlabel      = 24
    fontSizeXticks      = 24
    fontSizeYticks      = 24  
    lineColor           = "black"
    lineWidth           = 2
    lineStyle           = "solid" 
    fontName            = "Times New Roman"
    fontWeight          = "normal"
    nPixelsPerInch      = 1000 
    
    # parse required arguments
    fileName            = str(sys.argv[1])
    nHeaderLines        = int(sys.argv[2])
    columnID_xData      = int(sys.argv[3])
    columnID_yData      = int(sys.argv[4])
    fractionStart       = float(sys.argv[5])
    fractionEnd         = float(sys.argv[6])
    typePlot            = str(sys.argv[7])
    shouldSaveThePlot   = int(sys.argv[8])    
    figFileNameToSave   = str(sys.argv[9])
    
    data                = np.loadtxt(fileName, skiprows = nHeaderLines)
    dataX               = data[:,columnID_xData-1]
    dataY               = data[:,columnID_yData-1]
    idRowStart          = int(fractionStart*len(dataX))
    idRowEnd            = int(fractionEnd*len(dataX))
     
    
    if typePlot == "scatter":
        plotScatter2D(dataX[idRowStart:idRowEnd],
                      dataY[idRowStart:idRowEnd],
                      shouldSaveThePlot,
                      figFileNameToSave,
                      markerStyle,
                      markerSize,
                      markerColor,
                      labelX,
                      labelY,
                      xScale,
                      yScale,
                      fontSizeXlabel,
                      fontSizeYlabel,
                      fontSizeXticks,
                      fontSizeYticks,
                      fontName,
                      fontWeight,
                      nPixelsPerInch=nPixelsPerInch)
        
    elif typePlot == "line":               
        plotLine2D(dataX[idRowStart:idRowEnd],
                   dataY[idRowStart:idRowEnd],
                   shouldSaveThePlot,
                   figFileNameToSave,
                   lineColor,
                   lineWidth,
                   lineStyle,
                   labelX,
                   labelY,
                   xScale,
                   yScale,
                   fontSizeXlabel,
                   fontSizeYlabel,
                   fontSizeXticks,
                   fontSizeYticks,
                   fontName,
                   fontWeight,
                   nPixelsPerInch)
                  



if __name__ == "__main__":
    main()