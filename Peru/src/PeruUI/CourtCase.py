import wx
import  wx.calendar
import PeruConstants

def getCourtCaseInfo(self, CourtCase):
    output = []
    
    output.append([str(CourtCase.CourtCaseID.GetValue()),
                   str(CourtCase.StartDateMonth.GetValue()),
                   str(CourtCase.StartDateDay.GetValue()),
                   str(CourtCase.StartDateYear.GetValue()),
                   str(CourtCase.EndDateMonth.GetValue()),
                   str(CourtCase.EndDateDay.GetValue()),
                   int(CourtCase.EndDateYear.GetValue())])
    
    return output

class CourtCase(wx.Panel):
    def __init__(self, parent):

        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)

        label1 = wx.StaticText(self, label="Court Case ID :")
        CourtCaseID = self.CourtCaseID = wx.TextCtrl(self, size=(50,-1))
        
        label2 = wx.StaticText(self, label="Start Date :")
        StartDateMonth = self.StartDateMonth = wx.TextCtrl(self, size=(50,-1))
        StartDateDay = self.StartDateDay = wx.TextCtrl(self, size=(50,-1))
        StartDateYear = self.StartDateYear = wx.TextCtrl(self, size=(50,-1))
        
        label3 = wx.StaticText(self, label="End Date :")
        EndDateMonth = self.EndDateMonth = wx.TextCtrl(self, size=(50,-1))
        EndDateDay = self.EndDateDay = wx.TextCtrl(self, size=(50,-1))
        EndDateYear = self.EndDateYear = wx.TextCtrl(self, size=(50,-1))
        
        space = 6
        infoSizer = wx.FlexGridSizer(cols=6, hgap=space, vgap=space)
        infoSizer.AddMany([ (0,25),(0,0),(0,0),(0,0),(0,0),(0,0),
                        label1, CourtCaseID,(0,0),(0,0),(0,0),(0,0),
                        label2, StartDateMonth, wx.StaticText(self, label="/") , StartDateDay, wx.StaticText(self, label="/"), StartDateYear,
                        label3, EndDateMonth, wx.StaticText(self, label="/") , EndDateDay, wx.StaticText(self, label="/"), EndDateYear])
        
        self.buttonSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.saveFileButton = wx.Button(self, -1, "Save File")
        self.loadFileButton = wx.Button(self, -1, "Load File")
        self.buttonSizer.Add(self.saveFileButton, 0, wx.ALIGN_RIGHT)
        self.buttonSizer.Add(self.loadFileButton, 0, wx.ALIGN_RIGHT)
            
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(infoSizer, 1, wx.EXPAND)
        sizer.Add(self.buttonSizer, 0, wx.ALIGN_RIGHT)

        self.SetSizer(sizer)