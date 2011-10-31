#!/usr/bin/env python

from Quartz import *
import sys
import os

if len (sys.argv) == 1:
    print "pdf2png file1.pdf [file2.pdf [...]]"
    sys.exit(1)

def dumpPNG(pdf, pageNumber, outFileBase):
    if pageNumber is None:
        outFile = outFileBase + ".png"
        pageNumber = 1
    else:
        outFile = outFileBase + "-%03d.png" % pageNumber

    w = CGPDFDocumentGetTrimBox(pdf,pageNumber).size.width
    h = CGPDFDocumentGetTrimBox(pdf,pageNumber).size.height

    ctx = CGBitmapContextCreateWithColor(int(w), int(h), CGColorSpaceCreateDeviceRGB(), (1,1,1,1))
    ctx.drawPDFDocument(CGPDFDocumentGetTrimBox(pdf,pageNumber), pdf, pageNumber)
    ctx.writeToFile(outFile, kCGImageFormatPNG)
    return outFile

for aFile in sys.argv[1:]:
    pdf = CGPDFDocumentCreateWithProvider(CGDataProviderCreateWithFilename(aFile))
    numberOfPages = CGPDFDocumentGetNumberOfPages(pdf)

    outFile = os.path.splitext(aFile)[0]

    if numberOfPages == 1:
        dumpPNG(pdf, None, outFile)
    else:
        for pageNumber in xrange(1, numberOfPages+1):
            writtenPath = dumpPNG(pdf, pageNumber, outFile)
            print "Wrote page #%d as %s" % (pageNumber, writtenPath)

