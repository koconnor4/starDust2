import time
import sncosmo
import classify
import imp
read_des_datfile = imp.load_source("read_des_datfile","/home/bradley/Documents/sncosmo/classTest/read_des_datfile.py")
import os
from matplotlib import pyplot as plt
import sys

directory = "/home/bradley/Documents/sncosmo/classTest/simulatedChallange/DES_BLIND+HOSTZ"
p1aarr = []
p11arr = []
p1bcarr = []
dataArr = []

numberOfSteps = 1000
numberOfClassifications = 1000
numberOfPoints = 20
maxIter = 5000
template = 'snana'

theOutputFile = ("snanaTester" + str(numberOfSteps/1000) + ".txt")
#print theOutputFile

def getTheZerr(theFile): #gets the z error for the host galaxy
	with open(theFile) as f:
		content = f.readlines()
	amatch = [s for s in content if "HOST_GALAXY_PHOTO-Z" in s]
	thematch = amatch[0].split("+-")
	thereturn = float(thematch[1].strip())
	return thereturn

while(True):
	outputFile = open(theOutputFile,"a+")
	outputFile.write("maxIter: %d\n" % maxIter)
	outputFile.write("npts: %d\n" % numberOfPoints)
	outputFile.write("SNID\t1aProb\t11Prob\t1bcProb\trealtype\tClassTime\tbestModel\n")
	outputFile.close()

	counter = numberOfClassifications
	for filename in sorted(os.listdir(directory)):
		if "SN" in filename and filename.endswith(".DAT"):
			print filename
			counter -= 1
			inputFile = os.path.join(directory, filename)
			zerror = getTheZerr(inputFile) #this is because the snana read strips the zerror
			metadata, data = read_des_datfile.read_des_datfile(inputFile)
			theID = metadata["SNID"]

			outputFile = open(theOutputFile,"a+")
			outputFile.write("%d\t" % theID)
			outputFile.close()
	
			start = time.time()
			#print start
			classWorked = False
			#print "noPts: %d", numberOfPoints;
			#print "noSteps: %d", numberOfSteps;
			#print "noClass: %d", counter;
			
			example_classification = classify.classify(data, zhost=metadata['HOST_GALAXY_PHOTO-Z'], zhosterr=zerror, zminmax=[metadata['HOST_GALAXY_PHOTO-Z'] - (2*zerror), metadata['HOST_GALAXY_PHOTO-Z'] + (2*zerror)],
			npoints=numberOfPoints, maxiter=maxIter, nsteps_pdf=numberOfSteps, templateset=template,verbose=0)
			classWorked = True
			'''
			try:
			except:
				outputFile = open(theOutputFile,"a+")
				outputFile.write("0.00\t0.00\t0.00\t0\t0\n") #if there's an error all values to be 0
				outputFile.close()
				counter += 1
				print("error:", sys.exc_info()[0])
			'''
			#print example_classification['bestmodel']
			time1 = time.time() - start
			#print ("classification time: "),
			#print(time1)

			#print('P(Ia|D) = %.2f' % example_classification['pIa'])
			#print('P(II|D) = %.2f' % example_classification['pII'])
			#print('P(Ibc|D) = %.2f' % example_classification['pIbc'])

			with open ("../classTest/simulatedChallange/DES_UNBLIND+HOSTZ.KEY","r") as myfile:
				for line in myfile:
					data = line
					dataArr = data.split()
					theMatchID = dataArr[1]
					try:
						if(theID == int(theMatchID)):
							break
					except:
						continue #TODO:: add "not found"

			if(classWorked):
				outputFile = open(theOutputFile,"a+")
				outputFile.write("%.2f\t%.2f\t%.2f\t%s\t%.2f\t%s\n" % (example_classification['pIa'], example_classification['pII'], example_classification['pIbc'], dataArr[2], time1, example_classification['bestmodel']))
				outputFile.close()
	
			end = time.time()
			#print ("Classifications left: "),
			#print counter
			if(counter == 0):
				outputFile = open(theOutputFile,"a+")
				outputFile.write("\n")
				outputFile.close()
				break
			continue
		else: #skips files that are not SN data files (there are other files in the directory, such as a readme)
			continue
	
	numberOfClassifications-=5
	outputFile = open(theOutputFile,"a+")
	outputFile.write("end\n")
	outputFile.close()
