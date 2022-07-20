#-------------------------------------------------------------------------------
# Contact: Shawn Patton
# Created: Oct 2008
#
# Purpose: PartyEditorGridSquares can have PartyEditorGridElements dragged on
#          top of them.
#-------------------------------------------------------------------------------

from panda3d.core import Vec3,Vec4,Point3,TextNode,VBase4

from direct.gui.DirectGui import DirectFrame,DirectButton,DirectLabel,DirectScrolledList,DirectCheckButton
from direct.gui import DirectGuiGlobals
from direct.showbase.DirectObject import DirectObject
from otp.otpbase import PythonUtil

from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from toontown.parties import PartyGlobals
from toontown.parties.PartyInfo import PartyInfo
from toontown.parties import PartyUtils

class PartyEditorGridSquare(DirectObject):
    """
    PartyEditorGridSquares can have PartyEditorGridElements dragged onto them
    """
    notify = directNotify.newCategory("PartyEditorGridSquare")
    
    def __init__(self, partyEditor, x, y):
        self.partyEditor = partyEditor
        self.x = x
        self.y = y
        self.gridElement = None

    def getPos(self):
        return Point3(
            PartyGlobals.PartyEditorGridBounds[0][0] + self.x*PartyGlobals.PartyEditorGridSquareSize[0] + PartyGlobals.PartyEditorGridSquareSize[0]/2.0,
            0.0,
            PartyGlobals.PartyEditorGridBounds[1][1] + (PartyGlobals.PartyEditorGridSize[1]-1-self.y)*PartyGlobals.PartyEditorGridSquareSize[1] + PartyGlobals.PartyEditorGridSquareSize[1]/2.0,
        )

    def destroy(self):
        # Grid elements get destroyed by their list element
        del self.gridElement