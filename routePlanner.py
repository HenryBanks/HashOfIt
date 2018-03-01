import sys

class Vehicle:

	def __init__(self):
		self.targetX=0
		self.targetY=0
		self.timeUntilFree=0
		self.rideList=[]

	def addRide(self,ride,rideID):
		self.rideList.append(rideID)
		self.timeUntilFree=abs(ride[3]-ride[1])+abs(ride[2]-ride[0])
		self.targetX=ride[2]
		self.targetY=ride[3]

	def printRides(self):
		print(self.rideList)
		sliceStr = list(map(lambda x: str(x), self.rideList))
		return(str(len(self.rideList))+" "+" ".join(sliceStr)+"\n")

	def iterate(self):
		self.timeUntilFree=max(self.timeUntilFree-1,0)




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
			line.append(i)
			self.rideList.append(line)

		#print(self.rideList[33])
		#exit(0)

		self.vehicleList=[]

		for i in range(self.vehicles):
			v=Vehicle()
			self.vehicleList.append(v)

	def transferCost(self,ride,veh):
		startX=ride[0]
		startY=ride[1]
		endX=ride[2]
		endY=ride[3]
		earliestStart=ride[4]
		latestEnd=ride[5]

		distToStart=abs(veh.targetX-startX)+abs(veh.targetY-startY)+veh.timeUntilFree
		distToEnd=abs(endX-startX)+abs(endY-startY)

		return(max(earliestStart,distToStart),distToEnd)

	def journeyCompletionPossible(self, ride, veh):
		startX=ride[0]
		startY=ride[1]
		endX=ride[2]
		endY=ride[3]
		earliestStart=ride[4]
		latestEnd=ride[5]

		distToEnd=abs(endX-startX)+abs(endY-startY)
		distToStart=abs(veh.targetX-startX)+abs(veh.targetY-startY)+veh.timeUntilFree


	def assignRide(self,ride,veh,index):
		#print(ride)
		startX=ride[0]
		startY=ride[1]
		endX=ride[2]
		endY=ride[3]
		earliestStart=ride[4]
		latestEnd=ride[5]
		rideID=ride[6]

		self.rides-=1

		print(self.rideList.pop(index))

		veh.addRide(ride,rideID)



	def assignAllRide(self):
		for t in range(self.steps):
			print(t)
			for veh in self.vehicleList:
				if(len(self.rideList)==0):
					break
				#print("T to free:",veh.timeUntilFree)
				if veh.timeUntilFree>0:
					continue
				minStart=10000000000000000000000000
				ride=None
				for i in range(len(self.rideList)):
					vals=self.transferCost(self.rideList[i],veh)
					if (vals[0]+vals[1]+t)>min(self.rideList[i][5],self.steps):
					 	continue
					timeToStart=vals[0]
					if(minStart>timeToStart):
						ride=self.rideList[i]
						index=i
						minStart=timeToStart
					if(minStart==0):
						break
				if ride!=None:
					self.assignRide(ride,veh,index)
			for veh in self.vehicleList:
				veh.iterate()

		self.printSolution()

		

	def printSolution(self):

		fout=open(sys.argv[1][:-3]+".out",'w+')

		for veh in self.vehicleList:
			fout.write(veh.printRides())



newRouteSet=RouteFinder(sys.argv[1])
newRouteSet.assignAllRide()

