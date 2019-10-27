import ac
import traceback
from traction_circle_g_plotter import GPlotter
from traction_circle_model import TractionCircleModel
from traction_circle_view import TractionCircleView
from traction_circle_updater import TractionCircleUpdater
from moving_average_plotter import MovingAveragePlotter
from assettocorsa import AssettoCorsa

appHeight = 200
appWidth = 320
maxG = 2

updater = 0
numSecondsSpinner = 0

def acMain(ac_version):
    global updater, appHeight, appWidth, appWindow, numSecondsSpinner
    appWindow = ac.newApp("Traction Circle")
    ac.setSize(appWindow, appWidth, appHeight)
    ac.drawBorder(appWindow, 0)

    try:
        model = TractionCircleModel()
        assetto_corsa = AssettoCorsa()

        maxTimeSpan = 3
        numSecondsSpinner = ac.addSpinner(appWindow, 'Time Span(s)')
        ac.setPosition(numSecondsSpinner, 0, appHeight - 20)
        ac.setSize(numSecondsSpinner, 100, 20)
        ac.setRange(numSecondsSpinner, 1, 60)
        ac.setValue(numSecondsSpinner, maxTimeSpan)
        ac.addOnValueChangeListener(numSecondsSpinner, updateMaxTimeRange)

        gPlotter = GPlotter(appWidth, appHeight, maxG, maxG)
        view = TractionCircleView(appWindow, model, gPlotter, MovingAveragePlotter(10) )
        updater = TractionCircleUpdater(assetto_corsa, view, model, maxTimeRange=maxTimeSpan)

        ac.addRenderCallback(appWindow, doUpdate)
    except Exception as e:
        ac.log(str(traceback.format_exc()))

    return "Traction Circle"

def doUpdate(deltaT):
    global updater
    updater.doUpdate(deltaT)

def updateMaxTimeRange(value):
    global updater
    updater.setMaxTimeRange(value)

