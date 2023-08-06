"""This class is the main GUI for the sailsim project."""

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMainWindow
from sailsim.gui.qtmain import Ui_MainWindow

from sailsim.gui.mapView import pointsToPath


class SailsimGUI(QMainWindow):
    """Main GUI for sailsim."""

    def __init__(self, simulation):
        super().__init__()

        self.simulation = simulation
        self.frame = 0

        # Load UI from QT generated file
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Set up timer for play button
        self.timer = QTimer(self)
        self.timer.setInterval(simulation.timestep * 1000)
        self.timer.timeout.connect(self.playStep)

        self.ui.timeSlider.setMaximum(len(simulation))
        self.ui.timeSlider.setValue(self.frame)
        if self.simulation.world.boat.sailor is not None:
            self.ui.mapView.setWaypoints(self.simulation.world.boat.sailor.commandList)
        self.updatePath(5)
        self.updateFrame(0)
        self.updateViewStates()

    def updateFrame(self, frameNr):
        """Update display when the frame changed."""
        frames = self.simulation.frameList.frames
        if frameNr < len(frames):
            self.frame = frameNr
            frame = frames[frameNr]

            # Update widgets
            maxFrame = str(len(self.simulation))
            self.ui.frameNr.setText(str(frameNr).zfill(len(maxFrame)) + "/" + maxFrame)
            self.ui.mapView.viewFrame(frame)
            self.ui.boatInspector.viewFrame(frame)
            self.ui.valueInspector.viewFrame(frame)

    def updatePath(self, pathStep):
        """Update the path displayed on the MapViewWidget with the current data from the simulation."""
        coordinates = self.simulation.frameList.getCoordinateList()
        if len(coordinates) > 0:
            self.ui.mapView.setPath(pointsToPath(coordinates, pathStep))

    def incFrame(self):
        """Move to the next frame if it is in the range of the slider."""
        self.ui.timeSlider.setValue(self.ui.timeSlider.value() + 1)

    def decFrame(self):
        """Move to the previous frame if it is in the range of the slider."""
        self.ui.timeSlider.setValue(self.ui.timeSlider.value() - 1)

    def startFrame(self):
        """Move slider to the frist Frame."""
        self.ui.timeSlider.setValue(self.ui.timeSlider.minimum())

    def endFrame(self):
        """Move slider to the last Frame."""
        self.ui.timeSlider.setValue(self.ui.timeSlider.maximum())

    def pressedPlay(self, active):
        """Start or stop animation depending on active."""
        if active:
            if self.simulation.lastFrame > self.frame:
                self.timer.start()
            else:
                self.playStop()
        else:
            self.playStop()

    def playStop(self):
        """Stop the animation and uncheck the play button."""
        self.timer.stop()
        self.ui.buttonPlay.setChecked(False)

    def playStep(self):
        """Increase the frame if it is still available. Otherwise stop the animation."""
        if self.simulation.lastFrame > self.frame:
            self.incFrame()
        else:
            self.playStop()

    def updateViewStates(self):
        """Load states for QActions from child widgets."""
        # Import states from mapView
        self.ui.actionShowWaypointLink.setChecked(self.ui.mapView.displayWaypointLink)
        self.ui.actionShowWaypoints.setChecked(self.ui.mapView.displayWaypoints)
        self.ui.actionShowMainSailMapView.setChecked(self.ui.mapView.displayMainSail)
        self.ui.actionShowRudderMapView.setChecked(self.ui.mapView.displayRudder)

        # Import states from boatInspector
        self.ui.actionShowBoat.setChecked(self.ui.boatInspector.displayBoat)
        self.ui.actionShowRudderBoatInspector.setChecked(self.ui.boatInspector.displayRudder)
        self.ui.actionShowMainSailBoatInspector.setChecked(self.ui.boatInspector.displayMainSail)
        self.ui.actionShowBoatDirection.setChecked(self.ui.boatInspector.displayBoatDirection)
        self.ui.actionShowSpeed.setChecked(self.ui.boatInspector.displaySpeed)
        self.ui.actionShowForces.setChecked(self.ui.boatInspector.displayForces)

        # Disable actions if boat is hidden
        self.ui.actionShowRudderBoatInspector.setEnabled(self.ui.boatInspector.displayBoat)
        self.ui.actionShowMainSailBoatInspector.setEnabled(self.ui.boatInspector.displayBoat)

    from .actionslots import actionViewShowWaypointLink, actionViewShowWaypoints, actionViewShowMainSailMapView, actionViewShowRudderMapView
    from .actionslots import actionViewShowBoat, actionViewShowBoatDirection, actionViewShowSpeed, actionViewShowMainSailBoatInspector, actionViewShowRudderBoatInspector, actionViewShowForces
