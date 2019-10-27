import time
from collections import deque


class TractionCircleModel(object):

    def __init__(self, timeSource=time):
        self.timeSource = timeSource
        self.dataList = deque()
        self.dataSubSampleList = deque()
        self.index = 0
        self.SAMPLE_RATIO = 32

    def addDataPoint(self, x, y, z):
        if self.index % 2 == 0:
            self.dataList.append({"time": self.timeSource.time(), "x": x, "y": y, "z": z})

        if self.index % self.SAMPLE_RATIO == 0:
            self.index = self.index % self.SAMPLE_RATIO 
            self.dataSubSampleList.append({"time": self.timeSource.time(), "x": x, "y": y, "z": z})
        self.index = self.index + 1

    def dataPoints(self):
        return deque(self.dataList)
        
    def dataSubSamplePoints(self):
        return deque(self.dataSubSampleList)

    def filterPoints(self, timeSpan, timeSpanShort):
        while len(self.dataList) > 0 and self.dataList[0]["time"] < timeSpanShort :
            self.dataList.popleft()
        while len(self.dataSubSampleList) > 0 and self.dataSubSampleList[0]["time"] < timeSpan :
            self.dataSubSampleList.popleft()