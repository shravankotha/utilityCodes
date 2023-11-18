import os
import sys
import numpy as np
import matplotlib.pyplot as plt  
from plotScatter2D import plotLine2D, plotScatter2D
from plotHistogram import plotHistogram
        
def main():
    nArguments = len(sys.argv)    
    if nArguments < 9:
        text = """Eight command line arguments are expected: \
                \n\t(1) fileName \
                \n\t(2) Number of header lines to ignore \
                \n\t(3) column ID of the data \
                \n\t(4) starting fraction of data to plot (0-1) \
                \n\t(5) ending fraction of data to plot (0-1) \
                \n\t(6) Y-axis data type (count/prodDensity/Fraction) \
                \n\t(7) bin width \
                \n\t(8) save the image (0/1) \
                \n\t(9) figure name to save
               """
                
        raise RuntimeError(text)
    
    # set all the optional arguments here
    histogramBinType    = "bar"
    binFillColor        = "black"
    binEdgecolor        = "white"
    labelX              = "Angle [$^{\circ}$]"
    labelY              = "Fraction of pixels"
    scaleX              = "linear"
    scaleY              = "linear"
    fontSizeXlabel      = 36
    fontSizeYlabel      = 36
    fontSizeXticks      = 24
    fontSizeYticks      = 24
    fontName            = "Times New Roman"
    fontWeight          = "bold"
    nPixelsPerInch      = 1000 
    
    # parse required arguments
    fileName            = str(sys.argv[1])
    nHeaderLines        = int(sys.argv[2])
    columnID_Data       = int(sys.argv[3])    
    fractionStart       = float(sys.argv[4])
    fractionEnd         = float(sys.argv[5])
    yDataType           = str(sys.argv[6])
    binWidth            = float(sys.argv[7])
    shouldSaveThePlot   = int(sys.argv[8])    
    figFileNameToSave   = str(sys.argv[9])
    
    dataFile            = np.genfromtxt(fileName, skip_header = nHeaderLines, dtype = 'str')
    data = []
    if len(np.shape(dataFile)) == 1:
        for ii in range(0,len(dataFile)):
            data.append(float(dataFile[ii]))
    else:
        for ii in range(0,len(dataFile[:,0])):
            data.append(float(dataFile[ii,columnID_Data-1]))

    idRowStart          = int(fractionStart*len(data))
    idRowEnd            = int(fractionEnd*len(data))
    
    dataToPlot = data[idRowStart:idRowEnd]
    bins = [binWidth*ii for ii in range(0,int(max(dataToPlot)/binWidth))]
    plotHistogram(data[idRowStart:idRowEnd],
                  bins = bins,
                  yDataType = yDataType,
                  shouldSaveThePlot = shouldSaveThePlot,
                  pathFigNameToSave = figFileNameToSave,
                  histogramBinType = histogramBinType,
                  binFillColor = binFillColor,
                  binEdgecolor = binEdgecolor,
                  labelX = labelX,
                  labelY = labelY,
                  scaleX = scaleX,
                  scaleY = scaleY,
                  fontSizeXlabel = fontSizeXlabel,
                  fontSizeYlabel = fontSizeYlabel,
                  fontSizeXticks = fontSizeXticks,
                  fontSizeYticks = fontSizeYticks,
                  fontName = fontName,
                  fontWeight = fontWeight,
                  nPixelsPerInch = nPixelsPerInch,
                  xTickSkipFrequency = sys.maxsize,
                  yTickSkipFrequency = 2 
                  )    

if __name__ == "__main__":
    main()