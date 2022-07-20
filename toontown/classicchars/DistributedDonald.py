"""DistributedDonald module: contains the DistributedDonald class"""

from panda3d.core import *
from direct.interval.IntervalGlobal import *
from . import DistributedCCharBase
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import ClassicFSM, State
from direct.fsm import State
from . import CharStateDatas
from . import CCharChatter
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from toontown.hood import GSHood

class DistributedDonald(DistributedCCharBase.DistributedCCharBase):
    """DistributedDonald class"""

    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedDonald")

    def __init__(self, cr):
        try:
            self.DistributedDonald_initialized
        except:
            self.DistributedDonald_initialized = 1
            DistributedCCharBase.DistributedCCharBase.__init__(self, cr,
                                                               TTLocalizer.Donald,
                                                               'd')
            self.fsm = ClassicFSM.ClassicFSM(self.getName(),
                            [State.State('Off',
                                         self.enterOff,
                                         self.exitOff,
                                         ['Neutral']),
                             State.State('Neutral',
                                         self.enterNeutral,
                                         self.exitNeutral,
                                         ['Walk']),
                             State.State('Walk',
                                         self.enterWalk,
                                         self.exitWalk,
                                         ['Neutral']),
                             ],
                             # Initial State
                             'Off',
                             # Final State
                             'Off',
                             )

            self.fsm.enterInitialState()
        self.handleHolidays()

    def disable(self):
        self.fsm.requestFinalState()
        DistributedCCharBase.DistributedCCharBase.disable(self)

        del self.neutralDoneEvent
        del self.neutral
        del self.walkDoneEvent
        del self.walk
        del self.walkStartTrack
        del self.neutralStartTrack
        self.fsm.requestFinalState()

    def delete(self):
        """
        remove Donald and state data information
        """
        try:
            self.DistributedDonald_deleted
        except:
            self.DistributedDonald_deleted = 1
            del self.fsm
            DistributedCCharBase.DistributedCCharBase.delete(self)
            #self.disable()

    def generate( self ):
        """
        create Donald and state data information
        """
        DistributedCCharBase.DistributedCCharBase.generate(self, self.diffPath)
        name = self.getName()
        self.neutralDoneEvent = self.taskName(name + '-neutral-done')
        self.neutral = CharStateDatas.CharNeutralState(
            self.neutralDoneEvent, self)
        self.walkDoneEvent = self.taskName(name + '-walk-done')
        if self.diffPath == None:
            self.walk = CharStateDatas.CharWalkState(
            self.walkDoneEvent, self)
        else:
            self.walk = CharStateDatas.CharWalkState(
            self.walkDoneEvent, self, self.diffPath)
        self.walkStartTrack = self.actorInterval("trans-back")
        self.neutralStartTrack = self.actorInterval("trans")
        self.fsm.request('Neutral')

    ### Off state ###
    def enterOff(self):
        pass

    def exitOff(self):
        pass

    ### Neutral state ###
    def enterNeutral(self):
        self.notify.debug("Neutral " + self.getName() + "...")
        self.neutral.enter(startTrack = self.neutralStartTrack, playRate = 0.5)
        self.acceptOnce(self.neutralDoneEvent, self.__decideNextState)

    def exitNeutral(self):
        self.ignore(self.neutralDoneEvent)
        self.neutral.exit()

    ### Walk state ###
    def enterWalk(self):
        self.notify.debug("Walking " + self.getName() + "...")
        self.walk.enter(startTrack = self.walkStartTrack)
        self.acceptOnce(self.walkDoneEvent, self.__decideNextState)

    def exitWalk(self):
        self.ignore(self.walkDoneEvent)
        self.walk.exit()

    def __decideNextState(self, doneStatus):
        self.fsm.request('Neutral')

    def setWalk(self, srcNode, destNode, timestamp):
        """
        Parameters: srcNode, were to walk from
                    destNode, where to walk to
                    timestamp, when server started walk

        message sent from the server to say that this
        character should now go into walk state
        """
        if destNode and (not destNode == srcNode):
            self.walk.setWalk(srcNode, destNode, timestamp)
            self.fsm.request("Walk")

    def walkSpeed(self):
        return ToontownGlobals.DonaldSpeed
        
    def handleHolidays(self):
        """
        Handle Holiday specific behaviour
        """
        DistributedCCharBase.DistributedCCharBase.handleHolidays(self)
        if hasattr(base.cr, "newsManager") and base.cr.newsManager:
            holidayIds = base.cr.newsManager.getHolidayIdList()
            if ToontownGlobals.APRIL_FOOLS_COSTUMES in holidayIds and isinstance(self.cr.playGame.hood, GSHood.GSHood):
                self.diffPath = TTLocalizer.Goofy

    def getCCLocation(self):
        if self.diffPath != None:
            return 1
        else:
            return 0

    def getCCChatter(self):
        self.handleHolidays()
        return self.CCChatter
