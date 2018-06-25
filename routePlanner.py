import sys
import math

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

		self.averageStartX=0
		self.averageStartY=0

		self.sumXsquared=0
		self.sumYsquared=0

		for i in range(0,len(contents)):
			line=contents[i].strip("\n").split(" ")
			line = list(map(lambda x: int(x), line))
			line.append(i)
			self.averageStartX+=line[0]
			self.averageStartY+=line[1]
			self.sumXsquared+=line[0]*line[0]
			self.sumYsquared+=line[1]*line[1]
			self.rideList.append(line)

		self.averageStartX=self.averageStartX/self.rides
		self.averageStartY=self.averageStartY/self.rides

		self.sumXsquared=self.sumXsquared/self.rides
		self.sumYsquared=self.sumYsquared/self.rides

		self.stdX=math.sqrt(self.sumXsquared-self.averageStartX*self.averageStartX)
		self.stdY=math.sqrt(self.sumYsquared-self.averageStartY*self.averageStartY)

		print(self.averageStartX,self.averageStartY,self.stdX,self.stdY)

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

		close=True
		if endX>self.averageStartX+3*self.stdX or endX<self.averageStartX-3*self.stdX:
			close=False
		if endY>self.averageStartY+3*self.stdY or endY<self.averageStartY-3*self.stdY:
			close=False

		return(max(earliestStart,distToStart),close)

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
					#if (not vals[1]):
					# 	continue
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

