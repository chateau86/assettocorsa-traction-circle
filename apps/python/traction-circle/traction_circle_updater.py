import time

class TractionCircleUpdater:
    def __init__(self, AC, view, model, timeSource=time, maxTimeRange=5):
        self.AC = AC
        self.view = view
        self.model = model
        self.timeSource = timeSource
        self.maxTimeRange = maxTimeRange

    def doUpdate(self, deltaT):
        x, y, z = self.AC.getAccelerations()

        self.model.addDataPoint(x, y, z)

        timeSpan = self.timeSource.time() - self.maxTimeRange
        timeSpanShort = self.timeSource.time() - 0.5
        self.model.filterPoints(timeSpan, timeSpanShort)
        self.view.render()

    def setMaxTimeRange(self, timeRange):
        self.maxTimeRange = timeRange