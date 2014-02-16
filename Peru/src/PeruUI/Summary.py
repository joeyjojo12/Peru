import wx

def getSummaryInfo(self, SummaryPage):
    return str(SummaryPage.Charges)
        
class SummaryPanel(wx.Panel):
    def __init__(self, parent):

        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
                
        Summary = self.Summary = wx.TextCtrl(self, -1, "", wx.DefaultPosition, (975,515), wx.TE_MULTILINE|wx.SUNKEN_BORDER)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(Summary, 1, wx.ALL|wx.EXPAND, 5)

        self.SetSizer(sizer)