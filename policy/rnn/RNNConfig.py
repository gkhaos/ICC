import tensorflow as tf
import numpy as np
from util.dataLoader import loadNormalData
from util.Util import Normalize
from xml.dom.minidom import parse

from IPython import embed

class RNNConfig:
	_instance = None

	@classmethod
	def __getInstance(cls):
		return cls.__instance

	@classmethod
	def instance(cls, *args, **kargs):
		print("RNNConfig instance is created")
		cls.__instance = cls(*args, **kargs)
		cls.instance = cls.__getInstance
		return cls.__instance

	def __init__(self):
		self._motion = None

		self._lstmLayerSize = 512
		self._lstmLayerNumber = 4

		self._rootDimension = 5
		self._rootAngleIdx = 2


		# training parametres
		self._stepSize = 48
		self._numEpoch = 4
		self._batchSize = 32
		self._epochNumber = 4

		self._footSlideWeight = 6

		# User control prediction
		self._useControlPrediction = False

	# load motion related parameters
	def loadData(self, motion):
		self._motion = motion
		xMean, xStd = loadNormalData("../motions/%s/data/xNormal.dat"%(self._motion))
		yMean, yStd = loadNormalData("../motions/%s/data/yNormal.dat"%(self._motion))
		self._xNormal = Normalize(xMean, xStd)
		self._yNormal = Normalize(yMean, yStd)

		self._rootDimension = self._yNormal.get_zero_removed_index(self._rootDimension)
		self._rootAngleIdx = self._yNormal.get_zero_removed_index(self._rootAngleIdx)

		if self._motion == "walkrunfall":
			self._xDimension = 3
			self._yDimension = 111
		elif self._motion == "chicken":
			self._xDimension = 2
			self._yDimension = 107
		else:
			print("RNNConfig : Unspecified motion!")
			exit()



	@property
	def useControlPrediction(self):
		return self._useControlPrediction
	

	@property
	def motion(self):
		if self._motion is None:
			print("RNNConfig : Motion is unspecified !")
			exit()
		return self._motion
	
	@property
	def xNormal(self):
		return self._xNormal

	@property
	def yNormal(self):
		return self._yNormal
	
	

	@property
	def lstmLayerSize(self):
		return self._lstmLayerSize

	@property
	def lstmLayerNumber(self):
		return self._lstmLayerNumber

	@property
	def stepSize(self):
		return self._stepSize

	@property
	def numEpoch(self):
		return self._numEpoch
	

	@property
	def batchSize(self):
		return self._batchSize

	@batchSize.setter
	def batchSize(self, value):
		self._batchSize = value

	@property
	def epochNumber(self):
		return self._epochNumber

	@property
	def footSlideWeight(self):
		return self._footSlideWeight

	@property
	def rootDimension(self):
		return self._rootDimension

	@property
	def rootAngleIdx(self):
		return self._rootAngleIdx
	

	@property
	def xDimension(self):
		return self._xDimension

	@property
	def yDimension(self):
		return self._yDimension
	
	
	
	
	
	
	
		
	
	
	
	
	
	
	
	

