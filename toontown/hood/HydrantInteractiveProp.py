from direct.actor import Actor
from direct.directnotify import DirectNotifyGlobal
from direct.interval.IntervalGlobal import Sequence, Func
from toontown.hood import InteractiveAnimatedProp
from toontown.hood import GenericAnimatedProp
from toontown.toonbase import ToontownGlobals, ToontownBattleGlobals, TTLocalizer


class HydrantInteractiveProp(InteractiveAnimatedProp.InteractiveAnimatedProp):
    notify = DirectNotifyGlobal.directNotify.newCategory(
        'HydrantInteractiveProp')
    BattleCheerText = TTLocalizer.InteractivePropTrackBonusTerms[
        ToontownBattleGlobals.SQUIRT_TRACK]
    ZoneToIdles = {ToontownGlobals.ToontropolisPlaza: (('tt_a_ara_ttc_hydrant_idle0',
                                                      1,
                                                      1,
                                                      None,
                                                      3,
                                                      10),
                                                     ('tt_a_ara_ttc_hydrant_idle2',
                                                      1,
                                                      1,
                                                      None,
                                                      3,
                                                      10),
                                                     ('tt_a_ara_ttc_hydrant_idle1',
                                                      1,
                                                      1,
                                                      None,
                                                      3,
                                                      10),
                                                     ('tt_a_ara_ttc_hydrant_idleAwesome3',
                                                      1,
                                                      1,
                                                      None,
                                                      3,
                                                      10)),
                   ToontownGlobals.ToontropolisDocks: (('tt_a_ara_ttc_hydrant_idle0',
                                                  1,
                                                  1,
                                                  None,
                                                  3,
                                                  10),
                                                 ('tt_a_ara_ttc_hydrant_idle2',
                                                  1,
                                                  1,
                                                  None,
                                                  3,
                                                  10),
                                                 ('tt_a_ara_ttc_hydrant_idle1',
                                                  1,
                                                  1,
                                                  None,
                                                  3,
                                                  10),
                                                 ('tt_a_ara_ttc_hydrant_idleAwesome3',
                                                  1,
                                                  1,
                                                  None,
                                                  3,
                                                  10)),
                   ToontownGlobals.FloweringGrove: (('tt_a_ara_dga_hydrant_idle0',
                                                   3,
                                                   10,
                                                   'tt_a_ara_dga_hydrant_idle0settle',
                                                   3,
                                                   10),
                                                  ('tt_a_ara_dga_hydrant_idleLook1',
                                                   1,
                                                   1,
                                                   None,
                                                   3,
                                                   10),
                                                  ('tt_a_ara_dga_hydrant_idleSneeze2',
                                                   1,
                                                   1,
                                                   None,
                                                   3,
                                                   10),
                                                  ('tt_a_ara_dga_hydrant_idleAwesome3',
                                                   1,
                                                   1,
                                                   None,
                                                   3,
                                                   10)),
                   ToontownGlobals.TheLandOfMusic: (('tt_a_ara_mml_hydrant_idle0',
                                                        3,
                                                        10,
                                                        'tt_a_ara_mml_hydrant_idle0settle',
                                                        3,
                                                        10),
                                                       ('tt_a_ara_mml_hydrant_idle2',
                                                        3,
                                                        10,
                                                        'tt_a_ara_mml_hydrant_idle2settle',
                                                        3,
                                                        10),
                                                       ('tt_a_ara_mml_hydrant_idle1',
                                                        3,
                                                        10,
                                                        'tt_a_ara_mml_hydrant_idle1settle',
                                                        3,
                                                        10),
                                                       ('tt_a_ara_mml_hydrant_idleAwesome3',
                                                        1,
                                                        1,
                                                        None,
                                                        3,
                                                        10)),
                   ToontownGlobals.TundraWonderland: (('tt_a_ara_tbr_hydrant_idleShiver1',
                                                1,
                                                1,
                                                None,
                                                3,
                                                10),
                                               ('tt_a_ara_tbr_hydrant_idleRubNose0',
                                                1,
                                                1,
                                                None,
                                                3,
                                                10),
                                               ('tt_a_ara_tbr_hydrant_idleSneeze2',
                                                1,
                                                1,
                                                None,
                                                3,
                                                10),
                                               ('tt_a_ara_tbr_hydrant_idleAwesome3',
                                                1,
                                                1,
                                                None,
                                                3,
                                                10)),
                   ToontownGlobals.TwilightDreamland: (('tt_a_ara_ddl_hydrant_idle0',
                                                       3,
                                                       10,
                                                       None,
                                                       0,
                                                       0),
                                                      ('tt_a_ara_ddl_hydrant_idle1',
                                                       1,
                                                       1,
                                                       None,
                                                       0,
                                                       0),
                                                      ('tt_a_ara_ddl_hydrant_idle2',
                                                       1,
                                                       1,
                                                       None,
                                                       0,
                                                       0),
                                                      ('tt_a_ara_ddl_hydrant_idleAwesome3',
                                                       1,
                                                       1,
                                                       None,
                                                       0,
                                                       0))}
    ZoneToIdleIntoFightAnims = {ToontownGlobals.ToontropolisPlaza: 'tt_a_ara_ttc_hydrant_idleIntoFight',
                                ToontownGlobals.ToontropolisDocks: 'tt_a_ara_ttc_hydrant_idleIntoFight',
                                ToontownGlobals.FloweringGrove: 'tt_a_ara_dga_hydrant_idleIntoFight',
                                ToontownGlobals.TheLandOfMusic: 'tt_a_ara_mml_hydrant_idleIntoFight',
                                ToontownGlobals.TundraWonderland: 'tt_a_ara_tbr_hydrant_idleIntoFight',
                                ToontownGlobals.TwilightDreamland: 'tt_a_ara_ddl_hydrant_idleIntoFight'}
    ZoneToVictoryAnims = {ToontownGlobals.ToontropolisPlaza: 'tt_a_ara_ttc_hydrant_victoryDance',
                          ToontownGlobals.ToontropolisDocks: 'tt_a_ara_ttc_hydrant_victoryDance',
                          ToontownGlobals.FloweringGrove: 'tt_a_ara_dga_hydrant_victoryDance',
                          ToontownGlobals.TheLandOfMusic: 'tt_a_ara_mml_hydrant_victoryDance',
                          ToontownGlobals.TundraWonderland: 'tt_a_ara_tbr_hydrant_victoryDance',
                          ToontownGlobals.TwilightDreamland: 'tt_a_ara_ddl_hydrant_victoryDance'}
    ZoneToSadAnims = {ToontownGlobals.ToontropolisPlaza: 'tt_a_ara_ttc_hydrant_fightSad',
                      ToontownGlobals.ToontropolisDocks: 'tt_a_ara_ttc_hydrant_fightSad',
                      ToontownGlobals.FloweringGrove: 'tt_a_ara_dga_hydrant_fightSad',
                      ToontownGlobals.TheLandOfMusic: 'tt_a_ara_mml_hydrant_fightSad',
                      ToontownGlobals.TundraWonderland: 'tt_a_ara_tbr_hydrant_fightSad',
                      ToontownGlobals.TwilightDreamland: 'tt_a_ara_ddl_hydrant_fightSad'}
    ZoneToFightAnims = {ToontownGlobals.ToontropolisPlaza: ('tt_a_ara_ttc_hydrant_fightBoost', 'tt_a_ara_ttc_hydrant_fightCheer', 'tt_a_ara_ttc_hydrant_fightIdle'),
                        ToontownGlobals.ToontropolisDocks: ('tt_a_ara_ttc_hydrant_fightBoost', 'tt_a_ara_ttc_hydrant_fightCheer', 'tt_a_ara_ttc_hydrant_fightIdle'),
                        ToontownGlobals.FloweringGrove: ('tt_a_ara_dga_hydrant_fightBoost', 'tt_a_ara_dga_hydrant_fightCheer', 'tt_a_ara_dga_hydrant_fightIdle'),
                        ToontownGlobals.TheLandOfMusic: ('tt_a_ara_mml_hydrant_fightBoost', 'tt_a_ara_mml_hydrant_fightCheer', 'tt_a_ara_mml_hydrant_fightIdle'),
                        ToontownGlobals.TundraWonderland: ('tt_a_ara_tbr_hydrant_fightBoost', 'tt_a_ara_tbr_hydrant_fightCheer', 'tt_a_ara_tbr_hydrant_fightIdle'),
                        ToontownGlobals.TwilightDreamland: ('tt_a_ara_ddl_hydrant_fightBoost', 'tt_a_ara_ddl_hydrant_fightCheer', 'tt_a_ara_ddl_hydrant_fightIdle')}
    IdlePauseTime = base.config.GetFloat('prop-idle-pause-time', 0.0)

    def __init__(self, node):
        self.leftWater = None
        self.rightWater = None
        InteractiveAnimatedProp.InteractiveAnimatedProp.__init__(
            self, node, ToontownGlobals.HYDRANTS_BUFF_BATTLES)
        return

    def setupActor(self, node):
        InteractiveAnimatedProp.InteractiveAnimatedProp.setupActor(self, node)
        if not self.hoodId == ToontownGlobals.TundraWonderland:
            water = loader.loadModel(
                'phase_5/models/char/tt_m_efx_hydrantSquirt')
            self.leftWater = water.find('**/efx_hydrantSquirtLeft')
            self.rightWater = water.find('**/efx_hydrantSquirtRight')
            dx_left_water = self.node.find('**/dx_left_water')
            if self.leftWater:
                self.leftWater.reparentTo(dx_left_water)
                base.leftWater = self.leftWater
                self.leftWater.hide()
            else:
                self.notify.warning(
                    'couldnt find %s in rig for hood %d' %
                    ('dx_left_water', self.hoodId))
            dx_right_water = self.node.find('**/dx_right_water')
            if self.rightWater:
                self.rightWater.reparentTo(dx_right_water)
                self.rightWater.hide()
            else:
                self.notify.warning(
                    'couldnt find %s in rig for hood %d' %
                    ('dx_left_water', self.hoodId))

    def hideWater(self):
        if self.leftWater:
            self.leftWater.hide()
        if self.rightWater:
            self.rightWater.hide()

    def showWater(self):
        if self.leftWater:
            self.leftWater.show()
        if self.rightWater:
            self.rightWater.show()

    def hasOverrideIval(self, origAnimName):
        result = False
        if ('fightBoost' in origAnimName or 'fightCheer' in origAnimName) and not self.hoodId == ToontownGlobals.TundraWonderland:
            result = True
        return result

    def getOverrideIval(self, origAnimName):
        result = Sequence()
        if ('fightBoost' in origAnimName or 'fightCheer' in origAnimName) and not self.hoodId == ToontownGlobals.TundraWonderland:
            result.append(Func(self.showWater))
            if 'fightBoost' in origAnimName:
                animKey = 'fight0'
            else:
                animKey = 'fight1'
            animAndSound = self.createAnimAndSoundIval(animKey)
            result.append(animAndSound)
            result.append(Func(self.hideWater))
        return result
