

from direct.gui import DirectGui
from direct.gui.DirectGui import *
from direct.showbase.DirectObject import DirectObject
from panda3d.core import *
from direct.interval.LerpInterval import *
from direct.directnotify import DirectNotifyGlobal


class OptionsMenu(DirectObject):
    '''The base editor menu all Editors will inherit from'''

    def __init__(self):
        self.showOptions = True
        self.accept('space', self.hideOrShowOptions)
        self.accept('wheel_up', self.scrollFrameUp)
        self.accept('wheel_down', self.scrollFrameDown)

        notify = DirectNotifyGlobal.directNotify.newCategory('OptionsMenu')
        notify.setDebug(1)
        self.currentPage = 0 # Keeps track of which frame to scroll down.

        # General GUI variables
        self.mainGeom = loader.loadModel('phase_3/models/gui/dialog_box_gui.bam')
        self.editorLabelFont = loader.loadFont('phase_3/models/fonts/MickeyFont.bam')
        self.modalFont = loader.loadFont('phase_3/models/fonts/ImpressBT.ttf')
        self.guiClickSound = loader.loadSfx('phase_3/audio/sfx/GUI_create_toon_fwd.ogg')
        self.guiRolloverSound = loader.loadSfx('phase_3/audio/sfx/GUI_rollover.ogg')

        sliderImage = 'phase_3/maps/slider.png'

        # This menu frame contains all of the

        self.menuFrame = DirectGui.DirectFrame(
            parent=aspect2d,
            geom=self.mainGeom,
            geom_pos=(-0.05,0,0),
            pos=(0.15,0,0),
            geom_scale=(1.5, 1, 1),
            geom_hpr=(0, 9, 0),
            relief=None,
            sortOrder=0
        )


############# FIRST PAGE #########################

        self.firstPage = DirectGui.DirectFrame(
            parent=self.menuFrame,
            geom_scale=0.15,
            pos=(0, 0, 0.1),
            geom_hpr=(0, 9, 0),
            relief=None,
            sortOrder=2
        )

        self.firstPageOptionsScroll = DirectGui.DirectScrolledFrame(
            parent=self.firstPage,
            # GUI of the box
            frameSize=(-0.8, 0.665, -0.55, 0.35),
            canvasSize=(-1, 0, -7, 1),
            frameColor=(0, 0, 0, 0),
            pos=(0, 0, -0.025),

            # GUI DirectScrollBar attributes
            # Getting rid of the horizontal scroll
            horizontalScroll_frameSize=(0, 0, 0, 0),

            # The button you click and hold.
            # verticalScroll_thumb_relief=None,
            verticalScroll_thumb_geom_scale=(0.1),
            verticalScroll_thumb_clickSound=self.guiClickSound,
            verticalScroll_thumb_rolloverSound=self.guiRolloverSound,

            # The (invisible) bar you slide across.
            verticalScroll_range=(0, 1),
            verticalScroll_incButton_relief=None,
            verticalScroll_decButton_relief=None,
            # verticalScroll_geom=OnscreenImage(sliderImage),
            verticalScroll_geom_pos=(0.81, 0, -0.10),
            verticalScroll_geom_hpr=(0, 0, 90),
            verticalScroll_geom_scale=(0.2, 0.1, 0.1),
            sortOrder=3
        )
        self.menuLabelFrame = DirectGui.DirectFrame(
            parent=self.firstPageOptionsScroll.getCanvas(),
            frameSize=(0, 1.6, 0, 0.15),
            pos=(-1.05, 0, 0.85),
            relief=None,
            sortOrder=2
        )
        self.menuLabel = OnscreenText(
            font=self.editorLabelFont,
            text='General',
            parent=self.menuLabelFrame,
            fg=(0.28, 0.665111111111, 1.08888888889, 1),
            scale=0.175,
            pos=(0.80, 0, 0.665),
            align=TextNode.ACenter
        )

        self.musicCheck = OptionsToggle(self.firstPageOptionsScroll.getCanvas(), 'Music:', 0.65, self.updateMusic)
        self.soundEffectsCheck = OptionsToggle(self.firstPageOptionsScroll.getCanvas(), 'Sound Effects:', 0.45, self.updateSfx)
        self.acceptingNewFriends = OptionsToggle(self.firstPageOptionsScroll.getCanvas(), "Accepting New Friends", 0.25, self.updateAcceptingFriends)
        self.acceptingWhispers = OptionsToggle(self.firstPageOptionsScroll.getCanvas(), "Accepting Whispers", 0, self.updateAcceptingWhispers)


############# FIRST PAGE ENDS HERE #########################

############# SECOND PAGE #########################

        self.secondPage = DirectGui.DirectFrame(
            parent=self.menuFrame,
            geom_scale=0.15,
            pos = (0,0,0.1),
            geom_hpr=(0, 9, 0),
            relief=None,
            sortOrder=2
        )

        self.secondPageOptionsScroll = DirectGui.DirectScrolledFrame(
            parent=self.secondPage,
            # GUI of the box
            frameSize=(-0.8, 0.665, -0.55, 0.35),
            canvasSize=(-1, 0, -7, 1),
            frameColor=(0, 0, 0, 0),
            pos=(0, 0, -0.025),
            # geom=OnscreenImage(sliderImage),

            # GUI DirectScrollBar attributes
            # Getting rid of the horizontal scroll
            horizontalScroll_frameSize=(0, 0, 0, 0),

            # The button you click and hold.
            verticalScroll_thumb_geom_scale=(0.1),
            verticalScroll_thumb_clickSound=self.guiClickSound,
            verticalScroll_thumb_rolloverSound=self.guiRolloverSound,

            # The (invisible) bar you slide across.
            verticalScroll_range=(0, 1),
            verticalScroll_incButton_relief=None,
            verticalScroll_decButton_relief=None,
            verticalScroll_geom_pos=(0.81, 0, -0.10),
            verticalScroll_geom_hpr=(0, 0, 90),
            verticalScroll_geom_scale=(0.2, 0.1, 0.1),
            sortOrder=3
        )


# ############# SECOND PAGE ENDS HERE #########################

# ############# THIRD PAGE #########################

        self.thirdPage = DirectGui.DirectFrame(
            parent=self.menuFrame,
            geom_scale=0.15,
            pos=(0, 0, 0.1),
            geom_hpr=(0, 9, 0),
            relief=None,
            sortOrder=2
        )

        self.thirdPageOptionsScroll = DirectGui.DirectScrolledFrame(
            parent=self.thirdPage,
            # GUI of the box
            frameSize=(-0.8, 0.665, -0.55, 0.35),
            canvasSize=(-1, 0, -7, 1),
            frameColor=(0, 0, 0, 0),
            pos=(0, 0, -0.025),
            # geom=OnscreenImage(sliderImage),

            # GUI DirectScrollBar attributes
            # Getting rid of the horizontal scroll
            horizontalScroll_frameSize=(0, 0, 0, 0),

            # The button you click and hold.
            verticalScroll_thumb_geom_scale=(0.1),
            verticalScroll_thumb_clickSound=self.guiClickSound,
            verticalScroll_thumb_rolloverSound=self.guiRolloverSound,

            # The (invisible) bar you slide across.
            verticalScroll_range=(0, 1),
            verticalScroll_incButton_relief=None,
            verticalScroll_decButton_relief=None,
            verticalScroll_geom_pos=(0.81, 0, -0.10),
            verticalScroll_geom_hpr=(0, 0, 90),
            verticalScroll_geom_scale=(0.2, 0.1, 0.1),
            sortOrder=3
        )

# ############# THIRD PAGE ENDS HERE #########################


# ############# FOURTH PAGE #########################

        self.fourthPage = DirectGui.DirectFrame(
            parent=self.menuFrame,
            geom_scale=0.15,
            pos=(0, 0, 0.1),
            geom_hpr=(0, 9, 0),
            relief=None,
            sortOrder=2
        )

        self.fourthPageOptionsScroll = DirectGui.DirectScrolledFrame(
            parent=self.fourthPage,
            # GUI of the box
            frameSize=(-0.8, 0.665, -0.55, 0.35),
            canvasSize=(-1, 0, -7, 1),
            frameColor=(0, 0, 0, 0),
            pos=(0, 0, -0.025),
            # geom=OnscreenImage(sliderImage),

            # GUI DirectScrollBar attributes
            # Getting rid of the horizontal scroll
            horizontalScroll_frameSize=(0, 0, 0, 0),

            # The button you click and hold.
            verticalScroll_thumb_geom_scale=(0.1),
            verticalScroll_thumb_clickSound=self.guiClickSound,
            verticalScroll_thumb_rolloverSound=self.guiRolloverSound,

            # The (invisible) bar you slide across.
            verticalScroll_range=(0, 1),
            verticalScroll_incButton_relief=None,
            verticalScroll_decButton_relief=None,
            verticalScroll_geom_pos=(0.81, 0, -0.10),
            verticalScroll_geom_hpr=(0, 0, 90),
            verticalScroll_geom_scale=(0.2, 0.1, 0.1),
            sortOrder=3
        )

############# FOURTH PAGE ENDS HERE #########################

        self.secondPage.hide()
        self.thirdPage.hide()
        self.fourthPage.hide()

############# TABS #########################

        self.firstTab = DirectGui.DirectButton(
            parent=self.menuFrame,
            geom_scale=0.15,
            frameSize=(-0.15, 0.15, -0.15, 0.15),
            pos=(-0.60, 1, 0.625),
            sortOrder=1,
            command=self.showFirst
        )

        self.secondTab = DirectGui.DirectButton(
            parent=self.menuFrame,
            geom_scale=0.15,
            frameSize=(-0.15, 0.15, -0.15, 0.15),
            pos=(-0.20, 1, 0.625),
            sortOrder=1,
            command=self.showSecond
        )

        self.thirdTab = DirectGui.DirectButton(
            parent=self.menuFrame,
            geom_scale=0.15,
            frameSize=(-0.15, 0.15, -0.15, 0.15),
            pos=(0.20, 1, 0.625),
            sortOrder=1,
            command=self.showThird
        )

        self.fourthTab = DirectGui.DirectButton(
            parent=self.menuFrame,
            geom_scale=0.15,
            frameSize=(-0.15, 0.15, -0.15, 0.15),
            pos=(0.60, 1, 0.625),
            sortOrder=1,
            command=self.showFourth
        )

    # Editor Functions

    def hideOrShowOptions(self):
        if self.showOptions:
            self.showOptions = False
            self.menuFrame.hide()
        else:
            self.showOptions = True
            self.menuFrame.show()

    def showFirst(self):
        '''Shows the first page and hides every other one'''
        self.firstPage.show()
        self.secondPage.hide()
        self.thirdPage.hide()
        self.fourthPage.hide()
        self.currentPage = 0

    def showSecond(self):
        '''Shows the second page and hides every other one'''
        self.firstPage.hide()
        self.secondPage.show()
        self.thirdPage.hide()
        self.fourthPage.hide()
        self.currentPage = 1

    def showThird(self):
        '''Shows the third page and hides every other one'''
        self.firstPage.hide()
        self.secondPage.hide()
        self.thirdPage.show()
        self.fourthPage.hide()
        self.currentPage = 2

    def showFourth(self):
        '''Shows the fourth page and hides every other one'''
        self.firstPage.hide()
        self.secondPage.hide()
        self.thirdPage.hide()
        self.fourthPage.show()
        self.currentPage = 3

    def scrollFrameUp(self):
        '''Scrolls the current direct scrolling frame up'''
        if self.currentPage == 0:
            self.firstPageOptionsScroll['verticalScroll_value']-=0.05
        elif self.currentPage == 1:
            self.secondPageOptionsScroll['verticalScroll_value']-=0.05
        elif self.currentPage == 2:
            self.thirdPageOptionsScroll['verticalScroll_value']-=0.05
        elif self.currentPage == 3:
            self.fourthPageOptionsScroll['verticalScroll_value']-=0.05
        else:
            self.notify.debug('This page does not exist.')
    
    def scrollFrameDown(self):
        '''Scrolls the current direct scrolling frame down'''
        if self.currentPage == 0:
            self.firstPageOptionsScroll['verticalScroll_value'] += 0.05
        elif self.currentPage == 1:
            self.secondPageOptionsScroll['verticalScroll_value'] += 0.05
        elif self.currentPage == 2:
            self.thirdPageOptionsScroll['verticalScroll_value'] += 0.05
        elif self.currentPage == 3:
            self.fourthPageOptionsScroll['verticalScroll_value'] += 0.05
        else:
            self.notify.debug('This page does not exist.')

# All the Options Menu related functions

    def updateMusic(self):
        if base.musicActive:
            base.enableMusic(0)
            base.settings.updateSetting('music', False)
        else:
            base.enableMusic(1)
            base.settings.updateSetting('music', True)
        self.settingsChanged = 1

    def updateSfx(self):
        if base.sfxActive:
            base.enableSoundEffects(0)
            base.settings.updateSetting('sfx', False)
        else:
            base.enableSoundEffects(1)
            base.settings.updateSetting('sfx', True)
        self.settingsChanged = 1

    def updateAcceptingFriends(self):
        messenger.send('wakeup')
        if base.localAvatar.acceptingNewFriends:
            base.localAvatar.acceptingNewFriends = 0
            base.settings.updateSetting('accepting-new-friends', False)
        else:
            base.localAvatar.acceptingNewFriends = 1
            base.settings.updateSetting('accepting-new-friends', True)

    def updateAcceptingWhispers(self):
        messenger.send('wakeup')
        if base.localAvatar.acceptingNonFriendWhispers:
            base.localAvatar.acceptingNonFriendWhispers = 0
            base.settings.updateSetting('accepting-non-friend-whispers', False)
        else:
            base.localAvatar.acceptingNonFriendWhispers = 1
            base.settings.updateSetting('accepting-non-friend-whispers', True)

# All the Options related Classes

class OptionsLabel:
    '''Used as labels for the bigger letters
    Lower Z means lower on the DirectScrolledFrame'''
    notify = DirectNotifyGlobal.directNotify.newCategory('OptionsLabel')
    notify.setDebug(1)

    def __init__(self, labelParent, labelText, z):
        label_outer_font = loader.loadFont('phase_3/fonts/MinnieFont.ttf')

        self.label = DirectGui.DirectLabel(
            parent=labelParent,
            pos=(-0.95, 0, z),
            frameColor=(1, 1, 1, 0),
            frameSize=(-50, 50, 0, 0.1)
        )

        self.labelText = OnscreenText(
            text=labelText,
            font=label_outer_font,
            fg=(0, 0, 0, 1),
            scale=0.1,
            align=TextNode.ALeft
        )
        self.labelText.reparentTo(self.label)


class OptionsModal(DirectGui.DirectFrame):
    '''This is the left part of any Options Modal, everything else past this class inherits from this and adds to it'''
    notify = DirectNotifyGlobal.directNotify.newCategory('OptionsModal')
    notify.setDebug(1)

    def __init__(self, modalParent, modalText, z):
        self.guiClickSound = loader.loadSfx('phase_3/audio/sfx/GUI_create_toon_fwd.ogg')
        self.guiRolloverSound = loader.loadSfx('phase_3/audio/sfx/GUI_rollover.ogg')
        self.modalFont = loader.loadFont('phase_3/models/fonts/ImpressBT.ttf')

        self.containerFrame = DirectGui.DirectLabel(
            parent=modalParent,
            pos=(-0.95, 0, z),
            frameColor=(0, 0, 0, 0),
            frameSize=(-0.01, 0.9, -0.01, 0.06),
            scale=0.9,
        )

        self.modalTextNode = OnscreenText(
            align=TextNode.ALeft,
            text=modalText,
            font=self.modalFont
        )

        self.modalTextNode.reparentTo(self.containerFrame)


class OptionsSlider(OptionsModal):
    '''Creates a Slider which is useful for functions with arguments that include a range'''
    notify = DirectNotifyGlobal.directNotify.newCategory('OptionsSlider')
    notify.setDebug(1)

    def __init__(self, modalParent, modalText, z, slider_command=None, given_range=(0, 100)):
        super().__init__(modalParent, modalText, z)  # Creates the text on the left

        self.slider = DirectGui.DirectSlider(
            thumb_geom_scale=(0.4, 0.1, 0.25),
            thumb_relief=None,
            thumb_frameSize=(-0.25, 0.25, -0.25, 0.25),
            thumb_clickSound=self.guiClickSound,
            thumb_rolloverSound=self.guiRolloverSound,
            geom_scale=0.5,
            scale=(0.3, 0.1, 0.4),
            relief=None,
            command=slider_command,
            range=given_range
        )
        self.slider.reparentTo(self.containerFrame)
        self.slider.setPos(1.3, 0, 0)


class OptionsToggle(OptionsModal):
    '''Creates a toggle that creates an off/on switch'''
    notify = DirectNotifyGlobal.directNotify.newCategory('OptionsToggle')
    notify.setDebug(1)

    def __init__(self, modalParent, modalText, z, toggle_command=None):
        super().__init__(modalParent, modalText, z)  # Creates the text on the left

        def executeFunction(self, toggle_command=None):
            if toggle_command:
                toggle_command()

            animateToggle()

        self.button = DirectGui.DirectCheckButton(
            scale=0.15,
            # relief=None,
            boxImageScale=1,
            boxPlacement=('right'),
            # boxRelief=None,
            pressEffect=1,
            clickSound=self.guiClickSound,
            rolloverSound=self.guiRolloverSound,
            command=executeFunction,
            extraArgs=[toggle_command]
        )

        self.button.reparentTo(self.containerFrame)
        self.button.setPos(1.25, 0, 0.025)

        def animateToggle():
            if self.button['indicatorValue']:
                toggle_forward_interval = LerpPosInterval(
                    self.button, 0.15, (1.35, 0, 0), (1.25, 0, 0))
                toggle_forward_interval.start()
            else:
                toggle_back_interval = LerpPosInterval(
                    self.button, 0.15, (1.25, 0, 0), (1.35, 0, 0))
                toggle_back_interval.start()


class OptionsChoosingMenu(OptionsModal):
    '''modalParent - sets parent as the parent of the menu
       modalText(string) - what text does the model show?
       x(float) - What position in the x-position (left or right) do you want the menu?
       z(float) - What position in the z direction (up or down) do you want the menu?
       height_of_selectables(float) - How much space do you want in the selection menu? Lower numbers means a bigger height
       width_of_clickable(float) - How big do you want the button you click to open a selectable menu
       used_dictionary - What dictionary should this menu read from?
       chosen_command - What function does this menu run once an object in the selection menu is chosen?
       keyOrValue - 0 returns the key, 1 returns the value in the used_dictionary 
    '''

    notify = DirectNotifyGlobal.directNotify.newCategory('OptionsChoosingMenu')
    notify.setDebug(1)

    def __init__(self, modalParent, modalText, x, z, width_of_clickable, used_dictionary=None, chosen_command=None, keyOrValue=1):
        super().__init__(modalParent, modalText, z)
        self.selectableGUIFont = self.modalFont
        self.dynamicFrameFile = loader.loadModel(
            'phase_3/models/gui/ttr_m_gui_gen_dynamicFrame.bam')
        self.clickable = self.generateClickableFrame(
            x, width_of_clickable, chosen_command, keyOrValue, used_dictionary)
        self.selectables = self.generateSelectablesFrame(
            x, used_dictionary, width_of_clickable)
        self.populateBoolean = False

    def generateClickableFrame(self,
                               x,
                               width_of_clickable,
                               function_to_execute,
                               keyOrValueNum,
                               selectablesDictionary
                               ):
        '''Creates the small frame that the player will click on'''
        clickableTopLeftModel = self.dynamicFrameFile.find('**/topLeft')
        clickableTopMiddleModel = self.dynamicFrameFile.find('**/topMiddle')
        clickableTopRightModel = self.dynamicFrameFile.find('**/topRight')
        clickableCenterLeftModel = self.dynamicFrameFile.find('**/centerLeft')
        clickableCenterMiddleModel = self.dynamicFrameFile.find(
            '**/centerMiddle')
        clickableCenterRightModel = self.dynamicFrameFile.find(
            '**/centerRight')
        clickableBottomLeftModel = self.dynamicFrameFile.find('**/bottomLeft')
        clickableBottomMiddleModel = self.dynamicFrameFile.find(
            '**/bottomMiddle')
        clickableBottomRightModel = self.dynamicFrameFile.find(
            '**/bottomRight')

        self.clickableNode = NodePath('clickable_frame_node')

        # The Top Left piece
        clickableTopLeftModel.setScale(0.05)
        clickableTopLeftModel.reparentTo(self.clickableNode)
        clickableTopLeftModel.setPos(0, 0, 0.5)

        # The top middle piece
        clickableTopMiddleModel.reparentTo(self.clickableNode)
        clickableTopMiddleModel.setScale(0.05)
        clickableTopMiddleModel.setPos(clickableTopLeftModel.getX() +
                                       0.05, 0, clickableTopLeftModel.getZ())

        # The Top Middle repetitions
        for i in range(1, width_of_clickable):
            self.topCenterCopy = clickableTopMiddleModel.copyTo(
                self.clickableNode)
            self.topCenterCopy.setPos(
                clickableTopMiddleModel.getX()+(i*0.05), 0, clickableTopMiddleModel.getZ())

        # The Top Right piece
        clickableTopRightModel.reparentTo(self.clickableNode)
        clickableTopRightModel.setScale(0.05)
        clickableTopRightModel.setPos(self.topCenterCopy.getX()+0.05, 0, 0.5)

        # The Middle Left piece

        clickableCenterLeftModel.reparentTo(self.clickableNode)
        clickableCenterLeftModel.setScale(0.05)
        clickableCenterLeftModel.setPos(
            clickableTopLeftModel.getX(), 0, clickableTopLeftModel.getZ()-0.05)

        clickableCenterMiddleModel.reparentTo(self.clickableNode)
        clickableCenterMiddleModel.setScale(0.05)
        clickableCenterMiddleModel.setPos(
            clickableCenterLeftModel.getX()+0.05, 0, clickableCenterLeftModel.getZ())

        # The Center Middle repetitions
        for i in range(1, width_of_clickable):
            self.centerMiddleCopy = clickableCenterMiddleModel.copyTo(
                self.clickableNode)
            self.centerMiddleCopy.setPos(
                clickableCenterMiddleModel.getX()+(i*0.05), 0, clickableCenterMiddleModel.getZ())

        # The Center Right piece
        clickableCenterRightModel.setScale(0.05)
        clickableCenterRightModel.reparentTo(self.clickableNode)
        clickableCenterRightModel.setPos(
            self.centerMiddleCopy.getX()+0.05, 0, clickableCenterMiddleModel.getZ())

        clickableBottomLeftModel.setScale(0.05)
        clickableBottomLeftModel.reparentTo(self.clickableNode)
        clickableBottomLeftModel.setPos(
            clickableCenterLeftModel.getX(), 0, clickableCenterLeftModel.getZ()-0.05)

        clickableBottomMiddleModel.setScale(0.05)
        clickableBottomMiddleModel.reparentTo(self.clickableNode)
        clickableBottomMiddleModel.setPos(
            clickableBottomLeftModel.getX()+0.05, 0, clickableCenterLeftModel.getZ()-0.05)

        # The Bottom Middle repetitions
        for i in range(1, width_of_clickable):
            self.bottom_middle_copy = clickableBottomMiddleModel.copyTo(
                self.clickableNode)
            self.bottom_middle_copy.setPos(
                clickableBottomMiddleModel.getX()+(i*0.05), 0, clickableBottomMiddleModel.getZ())

        clickableBottomRightModel.setScale(0.05)
        clickableBottomRightModel.reparentTo(self.clickableNode)
        clickableBottomRightModel.setPos(
            self.bottom_middle_copy.getX()+0.05, 0, clickableBottomMiddleModel.getZ())

        self.clickableNode.setPos(0.5, 0, -0.45)
        self.clickableNode.flattenStrong()

        # The actual button
        self.clickableButton = DirectFrame(
            geom=self.clickableNode,
            parent=self.containerFrame,
            pos=(x, 0, 0),
            relief=None
        )

        self.clickable_text = DirectButton(
            parent=self.clickableButton,
            text='None',
            text_scale=0.075,
            text_font=self.modalFont,
            text_align=TextNode.ALeft,
            pos=(0.5, 0, -0.025),
            relief=None,
            frameSize=(0, width_of_clickable*0.055, -0.05, 0.1),
            command=self.showSelectables,
            extraArgs=[function_to_execute,
                       keyOrValueNum, selectablesDictionary],
            clickSound=self.guiClickSound,
            rolloverSound=self.guiRolloverSound,
        )

        return self.clickableButton

    def showAndHide(self, function, args_to_insert):
        '''This basically reparents clickable so you can see it again and hides the selectables_frame'''
        self.clickable.show()
        self.clickable_text['text'] = str(args_to_insert)
        self.selectablesFrame.hide()
        try:
            function(args_to_insert)
        except:
            self.notify.debug(
                "Nothing will happen as this selectable frame isn't hooked up to a particular function.")

    def generateSelectablesFrame(self,
                                 x_position,
                                 selectablesDictionary=None,
                                 width=6,
                                 height=6):
        '''Creates the selectable menu based on the provided args'''
        dynamicFrameFile = loader.loadModel(
            'phase_3/models/gui/ttr_m_gui_gen_dynamicFrame.bam')
        topLeftModel = dynamicFrameFile.find('**/topLeft')
        topMiddleModel = dynamicFrameFile.find('**/topMiddle')
        topRightModel = dynamicFrameFile.find('**/topRight')
        centerLeftModel = dynamicFrameFile.find('**/centerLeft')
        centerMiddleModel = dynamicFrameFile.find('**/centerMiddle')
        centerRightModel = dynamicFrameFile.find('**/centerRight')
        bottomLeftModel = dynamicFrameFile.find('**/bottomLeft')
        bottomMiddleModel = dynamicFrameFile.find('**/bottomMiddle')
        bottomRightModel = dynamicFrameFile.find('**/bottomRight')

        self.selectableDynamicFrame = NodePath('selectableFrame')

        topPiece = NodePath('top_half')

        # The Top Left piece
        topLeftModel.setScale(0.05)
        topLeftModel.reparentTo(topPiece)
        topLeftModel.setPos(0, 0, 0)

        # The top middle piece
        topMiddleModel.setScale(0.05)
        topMiddleModel.reparentTo(topPiece)
        topMiddleModel.setPos(topLeftModel.getX() +
                              0.05, 0, topLeftModel.getZ())

        # The Top Middle repetitions
        for i in range(1, width):
            self.top_center_copy = topMiddleModel.copyTo(topPiece)
            self.top_center_copy.setPos(topMiddleModel.getX()+(0.05*i), 0, 0)

        # The Top Right piece
        topRightModel.setScale(0.05)
        topRightModel.reparentTo(topPiece)
        topRightModel.setPos(topMiddleModel.getX()+(0.05*width), 0, 0)

        topPiece.flattenStrong()
        topPiece.reparentTo(self.selectableDynamicFrame)
        topPiece.setPos(0, 0, 0)
        # Let's make a node that we can duplicate.

        middlePiece = NodePath('middle_half')
        middlePiece.reparentTo(self.selectableDynamicFrame)
        middlePiece.setPos(0, 0, -0.05)

        centerLeftModel.setScale(0.05)
        centerLeftModel.reparentTo(middlePiece)
        centerLeftModel.setPos(0, 0, 0)

        centerMiddleModel.setScale(0.05)
        centerMiddleModel.reparentTo(middlePiece)
        centerMiddleModel.setPos(0.05, 0, 0)

        # The Center Middle repetitions
        for i in range(1, width+1):
            self.center_middle_copy = centerMiddleModel.copyTo(middlePiece)
            self.center_middle_copy.setPos(0.05*i, 0, 0)

        centerRightModel.setScale(0.05)
        centerRightModel.reparentTo(middlePiece)
        centerRightModel.setPos((width+1)*0.05, 0, 0)

        # Now let's duplicate the amount of times the thing is made.

        middlePiece.flattenStrong()

        for i in range(1, height):
            self.middlePiece_copy = middlePiece.copyTo(
                self.selectableDynamicFrame)
            self.middlePiece_copy.setPos(0, 0, (i * -0.05))

        bottom_piece = NodePath('bottom_half')
        bottom_piece.reparentTo(self.selectableDynamicFrame)
        bottom_piece.setPos(0, 0, height * -0.05)

        bottomLeftModel.setScale(0.05)
        bottomLeftModel.reparentTo(bottom_piece)
        bottomLeftModel.setPos(0, 0, -0.05)

        bottomMiddleModel.setScale(0.05)
        bottomMiddleModel.reparentTo(bottom_piece)
        bottomMiddleModel.setPos(0.05, 0, -0.05)

        # The Bottom Middle repetitions
        for i in range(1, width+1):
            self.bottom_middle_copy = bottomMiddleModel.copyTo(bottom_piece)
            self.bottom_middle_copy.setPos((0.05*i), 0, -0.05)

        # self.selectableDynamicFrame.ls()
        bottomRightModel.setScale(0.05)
        bottomRightModel.reparentTo(bottom_piece)
        bottomRightModel.setPos((width+1)*0.05, 0, -0.05)

        bottom_piece.flattenStrong()

        self.selectablesFrame = DirectGui.DirectFrame(
            geom=self.selectableDynamicFrame,
            parent=self.containerFrame,
            pos=((x_position+0.5), 0, 0.05),
            relief=None,
        )

        # If you want to debug the amount of items ya got, uncomment the line under.

        # print(f"{self.modalTextNode['text']} : {len(selectablesDictionary)} items")

        selectable_height = (len(selectablesDictionary)) * -0.1005

        self.selectableListFrame = DirectGui.DirectScrolledFrame(
            parent=self.selectablesFrame,
            frameSize=(0, width*0.052, -0.4, 0),
            canvasSize=(0, 1.5, selectable_height, 0),

            verticalScroll_incButton_relief=None,
            verticalScroll_decButton_relief=None,
            verticalScroll_range=(0, 0.5),
            verticalScroll_value=0,
            verticalScroll_manageButtons=True,
            verticalScroll_resizeThumb=True,
            verticalScroll_thumb_frameSize=(-15, 15, -15, 15),
            horizontalScroll_relief=None,
            horizontalScroll_thumb_relief=None,
            horizontalScroll_incButton_relief=None,
            horizontalScroll_decButton_relief=None,
            scrollBarWidth=0.05,
            relief=None,
        )

        self.selectablesFrame.hide()

    def showSelectables(self,
                        command_to_execute,
                        keyOrValue,
                        selectablesDictionary):
        self.selectablesFrame.show()
        self.clickable.hide()

        if self.populateBoolean:
            pass  # We've already populated it.
        else:
            self.notify.info('Generating Selectable Frame for the first time')
            if keyOrValue == 1:  # If we want to return the values
                i = 0
                for item in selectablesDictionary.keys():
                    i += 1
                    button = DirectButton(
                        parent=self.selectableListFrame.getCanvas(),
                        text=item,
                        text_font=self.selectableGUIFont,
                        text_align=TextNode.ALeft,
                        text_scale=0.3,
                        scale=0.2,
                        pos=(0, 0, 0 - (i*0.1)),
                        pad=(5, 0),
                        relief=None,
                        command=self.showAndHide,
                        clickSound=self.guiClickSound,
                        rolloverSound=self.guiRolloverSound,
                        extraArgs=[command_to_execute,
                                   selectablesDictionary[item]]
                    )
            else:  # If we want to return the key
                i = 0
                for item in selectablesDictionary.keys():
                    i += 1
                    button = DirectButton(
                        parent=self.selectableListFrame.getCanvas(),
                        text=item,
                        text_font=self.selectableGUIFont,
                        text_align=TextNode.ALeft,
                        text_scale=0.3,
                        scale=0.2,
                        pos=(0, 0, 0 - (i*0.1)),
                        pad=(5, 0),
                        relief=None,
                        command=self.showAndHide,
                        clickSound=self.guiClickSound,
                        rolloverSound=self.guiRolloverSound,
                        extraArgs=[command_to_execute, item]
                    )
            self.populateBoolean = True
