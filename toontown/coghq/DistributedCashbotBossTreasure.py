from toontown.safezone import DistributedSZTreasure
from toontown.toonbase import ToontownGlobals
from direct.interval.IntervalGlobal import *
from pandac.PandaModules import Point3
Models = {ToontownGlobals.ToontropolisPlaza: 'phase_4/models/props/icecream',
          ToontownGlobals.ToontropolisDocks: 'phase_6/models/props/starfish_treasure',
          ToontownGlobals.TundraWonderland: 'phase_8/models/props/snowflake_treasure',
          ToontownGlobals.TheLandOfMusic: 'phase_6/models/props/music_treasure',
          ToontownGlobals.FloweringGrove: 'phase_8/models/props/flower_treasure',
          ToontownGlobals.TwilightDreamland: 'phase_8/models/props/zzz_treasure'}


class DistributedCashbotBossTreasure(
        DistributedSZTreasure.DistributedSZTreasure):

    def __init__(self, cr):
        DistributedSZTreasure.DistributedSZTreasure.__init__(self, cr)
        self.grabSoundPath = 'phase_4/audio/sfx/SZ_DD_treasure.ogg'

    def setStyle(self, hoodId):
        newModel = Models[hoodId]
        if self.modelPath != newModel:
            if self.modelPath:
                self.loadModel(newModel)
            self.modelPath = newModel

    def setGoonId(self, goonId):
        self.goonId = goonId

    def setFinalPosition(self, x, y, z):
        if not self.nodePath:
            self.makeNodePath()
        if self.treasureFlyTrack:
            self.treasureFlyTrack.finish()
            self.treasureFlyTrack = None
        startPos = None
        goon = self.cr.doId2do[self.goonId]
        if goon:
            startPos = goon.getPos()
        lerpTime = 1
        self.treasureFlyTrack = Sequence(
            Func(
                self.collNodePath.stash), Parallel(
                ProjectileInterval(
                    self.treasure, startPos=Point3(
                        0, 0, 0), endPos=Point3(
                        0, 0, 0), duration=lerpTime, gravityMult=2.0), LerpPosInterval(
                            self.nodePath, lerpTime, Point3(
                                x, y, z), startPos=startPos)), Func(
                                    self.collNodePath.unstash))
        self.treasureFlyTrack.start()
        return
