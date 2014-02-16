
import wx

def getHealingNotesInfo(self, HealingNotesPage):
    return str(HealingNotesPage.Charges)
        
class HealingNotesPanel(wx.Panel):
    def __init__(self, parent):

        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
                
        HealingNotes = self.HealingNotes = wx.TextCtrl(self, -1, "", wx.DefaultPosition, (975,515),wx.TE_MULTILINE|wx.SUNKEN_BORDER)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(HealingNotes, 1, wx.ALL|wx.EXPAND, 5)

        self.SetSizer(sizer)