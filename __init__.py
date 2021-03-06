from generators import RandomArrayGenerator,  SineWithNoiseGenerator, GaussGenerator

def main():
	gen1, gen2 = prepareSineGenerators(0.1, 0.1)
	generateDistribution(gen1, gen2, "Sinus_01_01.txt")
		
	gen1, gen2 = prepareSineGenerators(0.3, 0.5)
	generateDistribution(gen1, gen2, "Sinus_03_05.txt")
	
	gen1, gen2 = prepareSineGenerators(1.0, 2.0)
	generateDistribution(gen1, gen2, "Sinus_1_2.txt")
	
	gen1, gen2 = prepareGaussGenerators(1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
	generateDistribution(gen1, gen2, "Gauss_1111.txt")

	gen1, gen2 = prepareGaussGenerators(1.0, 1.0, 1.0, 1.0, 2.0, 1.0)
	generateDistribution(gen1, gen2, "Gauss_1112.txt")

	gen1, gen2 = prepareGaussGenerators(2.0, 1.0, 3.0, 7.0, 3.0, 2.0)
	generateDistribution(gen1, gen2, "Gauss_2137.txt")
	
		
def generateDistribution(gen1, gen2, genName):
	output_file = open(genName, 'w')	
	arrSize = 1000
	for i in range(0, arrSize):
		try:
			data1 = gen1.generateDataSample(arrSize)
			data2 = gen2.generateDataSample(arrSize)
			for j in range(0, arrSize):
				output_file.write(str(data1.getX()[j]))
				output_file.write(' ')	
				output_file.write(str(data1.getY()[j]))
				output_file.write(" ")
				output_file.write(str(data2.getX()[j]))		
				output_file.write(" ")	
				output_file.write(str(data2.getY()[j]))	
				output_file.write(" ")		
				output_file.write("\n")
		except IOError:
			print "I/O error. Aborting..."	
	output_file.close() 	
			

def prepareSineGenerators(noise1, noise2):
	xgen1 = RandomArrayGenerator.RandomArrayGenerator(-10, 10)
	gen1 = SineWithNoiseGenerator.SineWithNoiseGenerator(xgen1, noise1)
	gen2 = SineWithNoiseGenerator.SineWithNoiseGenerator(xgen1, noise2)
	return gen1, gen2

def prepareGaussGenerators(x1, y1, x2, y2, sigma1, sigma2):
	gen1 = GaussGenerator.GaussGenerator(x1, y1, sigma1)
	gen2 = GaussGenerator.GaussGenerator(x2, y2, sigma2)
	return gen1, gen2

if __name__ == "__main__":
	main()
