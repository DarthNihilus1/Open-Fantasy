#===============================================================================
# Contact: Edmundo Ruiz (Schell Games)
# Created: October 21, 2009
# Purpose: GUI Manager for a DistributedPartyTeamActivity
#===============================================================================
from panda3d.core import TextNode

from direct.gui.DirectButton import DirectButton
from direct.gui.OnscreenText import OnscreenText
from direct.task.Task import Task

from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer

from toontown.parties import PartyUtils
from toontown.parties import PartyGlobals

class TeamActivityGui:
    COUNTDOWN_TASK_NAME = "updateCountdownTask"
    
    timer = None
    statusText = None
    countdownText = None
    exitButton = None
    switchButton = None
    
    def __init__(self, activity):
        self.activity = activity # instance of the DistributedPartyTeamActivity
    
    def load(self):
        buttonModels = loader.loadModel("phase_3.5/models/gui/inventory_gui")
        upButton = buttonModels.find("**//InventoryButtonUp")
        downButton = buttonModels.find("**/InventoryButtonDown")
        rolloverButton = buttonModels.find("**/InventoryButtonRollover")
        
        self.exitButton = DirectButton(
            relief = None,
            text = TTLocalizer.PartyTeamActivityExitButton,
            text_fg = (1, 1, 0.65, 1),
            text_pos = (0, -0.15),
            text_scale = 0.50,
            image = (upButton, downButton, rolloverButton),
            image_color = (1, 0, 0, 1),
            image_scale = (14.5, 1, 9),
            pos = (0, 0, 0.8),
            scale = 0.15,
            command = self.handleExitButtonClick,
            )
        self.exitButton.hide()
        
        if self.activity.toonsCanSwitchTeams():
            self.switchButton = DirectButton(
                relief = None,
                text = TTLocalizer.PartyTeamActivitySwitchTeamsButton,
                text_fg = (1, 1, 1, 1),
                text_pos = (0, 0.1),
                text_scale = 0.50,
                image = (upButton, downButton, rolloverButton),
                image_color = (0, 1, 0, 1),
                image_scale = (15, 1, 15),
                pos = (0, 0, 0.5),
                scale = 0.15,
                command = self.handleSwitchButtonClick,
                )
            self.switchButton.hide()
        else:
            self.switchButton = None
        
        buttonModels.removeNode()
        
        self.countdownText = OnscreenText(
            text = "",
            pos = (0.0, -0.2),
            scale = PartyGlobals.TeamActivityTextScale * 1.2,
            fg = (1.0, 1.0, 0.65, 1.0),
            align = TextNode.ACenter,
            font = ToontownGlobals.getSignFont(),
            mayChange = True,
        ) 
        self.countdownText.hide()
        
        # load general purpose text display element
        self.statusText = OnscreenText(
            text = "",
            pos = (0.0, 0.0),
            scale = PartyGlobals.TeamActivityTextScale,
            fg = PartyGlobals.TeamActivityStatusColor,
            align = TextNode.ACenter,
            font = ToontownGlobals.getSignFont(),
            mayChange = True,
        )
        self.statusText.hide()
        
        # load the timer that displays time left in the game
        self.timer = PartyUtils.getNewToontownTimer()
        self.timer.hide()
    
    def unload(self):
        self.hideWaitToStartCountdown()
        
        if self.exitButton is not None:
            self.exitButton.destroy()
            self.exitButton = None
            
        if self.switchButton is not None:
            self.switchButton.destroy()
            self.switchButton = None
            
        if self.countdownText is not None:
            self.countdownText.destroy()
            self.countdownText.removeNode()
            self.countdownText = None
        
        if self.statusText is not None:
            self.statusText.destroy()
            self.statusText.removeNode()
            self.statusText = None
    
        if self.timer is not None:
            self.timer.destroy()
            del self.timer

#===============================================================================
# Status
#===============================================================================
    
    def showStatus(self, text):
        self.statusText.setText(text)
        self.statusText.show()
        
    def hideStatus(self):
        self.statusText.hide()

#===============================================================================
# Exit
#===============================================================================
    
    def enableExitButton(self):
        self.exitButton.show()
    
    def disableExitButton(self):
        assert(self.activity.notify.debug("GUI: disableExitButton"))
        
        self.exitButton.hide()
        
    def handleExitButtonClick(self):
        self.disableExitButton()
        self.disableSwitchButton()
        self.activity.d_toonExitRequest()
        
#===============================================================================
# Switch Teams button
#===============================================================================
    
    def enableSwitchButton(self):
        self.switchButton.show()
    
    def disableSwitchButton(self):
        assert(self.activity.notify.debug("GUI: disableSwitchButton"))
        
        if self.switchButton is not None:
            self.switchButton.hide()
        
    def handleSwitchButtonClick(self):
        self.disableSwitchButton()
        self.disableExitButton()
        self.activity.d_toonSwitchTeamRequest()
        
#===============================================================================
# Wait To Start Countdown
#===============================================================================

    def showWaitToStartCountdown(self, duration, waitToStartTimestamp, almostDoneCallback=None):
        self._countdownAlmostDoneCallback = almostDoneCallback
        
        currentTime = globalClock.getRealTime()
        waitTimeElapsed = currentTime - waitToStartTimestamp
        
        # if still time left to display countdown
        if (duration - waitTimeElapsed) > 1.0:
            countdownTask = Task(self._updateCountdownTask)
            countdownTask.duration = duration - waitTimeElapsed
            
            self.countdownText.setText( str( int( countdownTask.duration ) ) )
            self.countdownText.show()
            
            taskMgr.remove(TeamActivityGui.COUNTDOWN_TASK_NAME)
            taskMgr.add(countdownTask, TeamActivityGui.COUNTDOWN_TASK_NAME)
            
        else:
            # don't bother showing timer at all
            assert(self.activity.notify.debug("GUI: Server entered WaitToStart %.1f seconds ago. No point in displaying on screen countdown." % waitTimeElapsed ))
    
    def hideWaitToStartCountdown(self):
        assert(self.activity.notify.debug("finishWaitToStart"))
        # it is possible that self.isLocalToonPlaying will be False at this
        # point even though we had the localToon in the activity, so clean up as
        # if the local toon was in.
        taskMgr.remove(TeamActivityGui.COUNTDOWN_TASK_NAME)
        self._countdownAlmostDoneCallback = None
        
        if self.countdownText is not None:
            self.countdownText.hide()
        

    def _updateCountdownTask(self, task):
        countdownTime = int(task.duration - task.time)
        
        seconds = str(countdownTime)
        
        if self.countdownText["text"] != seconds:
            assert(self.activity.notify.debug("GUI: Setting countdown label to %s" % seconds))
            self.countdownText["text"] = seconds
            
            if countdownTime == 3 and self._countdownAlmostDoneCallback is not None:
                self._countdownAlmostDoneCallback()
                self._countdownAlmostDoneCallback = None

        if task.time >= task.duration:
            return Task.done
        else:
            return Task.cont
    
#===============================================================================
# Timer   
#===============================================================================

    def showTimer(self, duration):
        self.timer.setTime(duration)
        self.timer.countdown(duration, self._handleTimerExpired)
        self.timer.show()
        
    def hideTimer(self):
        self.timer.hide()
        self.timer.stop()
        
    def _handleTimerExpired(self):
        assert(self.activity.notify.debug("Timer Expired!"))
        self.activity.handleGameTimerExpired()
        
