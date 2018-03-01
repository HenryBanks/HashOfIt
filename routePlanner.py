import sys

class vehicle:

	def __init__(self):
		self.locationX=0
		self.locationY=0
		self.timeWhenFree=0
		self.rideList=[]

	def addRide(self,ride):
		self.rideList.append(rideno)





class RouteFinder:	

	def printMatrix(self):
		for i in range(0,len(self.Matrix)):
			line=""
			for j in range(0,len(self.Matrix[i])):
				line+=self.Matrix[i][j]
			print(line)

	def __init__(self,filename):
		file = open(filename,"r")
		print("Reading file: "+file.name)

		contents=file.readlines()

		values=contents.pop(0).strip("\n").split(" ")
		values = list(map(lambda x: int(x), values))
		print(values)
		self.rows=values[0]
		self.columns=values[1]
		self.vehicles=values[2]
		self.rides=values[3]
		self.bonus=values[4]
		self.steps=values[5]

		self.rideList=[]

		for i in range(0,len(contents)):
			line=contents[i].strip("\n").split(" ")
			line = list(map(lambda x: int(x), line))
			self.rideList.append(line)

		print(self.rideList)

		self.vehicleList=[]

		for i in range(len(self.vehicles)):


		self.vehicleRides=[[]]
		self.carLocations=[[]]
		self.carFree=[]

	def assignRide(self,ride):
		print(ride)
		startX=ride[0]
		startY=ride[1]
		endX=ride[2]
		endY=ride[3]
		earliestStart=ride[4]
		latestEnd=ride[5]

		distance=abs(ride[3]-ride[1])+abs(ride[2]-ride[0])
		print(distance)

	def assignAllRide(self):
		for ride in self.rideList:
			self.assignRide(ride)

	def printSolution(self):

		fout=open(sys.argv[1][:-3]+".out",'w+')

		for vehicleRideList in self.vehiclesRides:
			sliceStr = list(map(lambda x: str(x), vehicleRideList))
			fout.write(len(vehicleRideList)+" ".join(sliceStr)+"\n")



newRouteSet=RouteFinder(sys.argv[1])
newRouteSet.assignAllRide()

