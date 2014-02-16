import wx

#Import UI elements
import PeruConstants, CourtCase, Prosecutor, Witness, Official, Defendant, Reference, Plaintiff, Charges, Summary, CaseNotes, FurtherNotes, HealingNotes

class PeruNotebook(wx.Notebook):
    
    def __init__(self, parent):
        wx.Notebook.__init__(self, parent, id=wx.ID_ANY, style=wx.BK_DEFAULT)

        self.AddPage(CourtCase.CourtCase(self), "Court Case")
        self.AddPage(Reference.NestedReferencePanel(self), "Reference")
        self.AddPage(Official.OfficialPanel(self), "Official")
        self.AddPage(Defendant.NestedDefendantPanel(self), "Defendant")
        self.AddPage(Plaintiff.NestedPlaintiffPanel(self), "Plaintiff")
        self.AddPage(Prosecutor.NestedProsecutorPanel(self), "Prosecutor")
        self.AddPage(Witness.NestedWitnessPanel(self), "Witness")
        self.AddPage(Charges.ChargesPanel(self), "Charges")
        self.AddPage(Summary.SummaryPanel(self), "Summary")
        self.AddPage(CaseNotes.CaseNotesPanel(self), "Case Notes")
        self.AddPage(HealingNotes.HealingNotesPanel(self), "Healing Notes")
        self.AddPage(FurtherNotes.FurtherNotesPanel(self), "Further Research Notes")
        

########################################################################

class PeruFrame(wx.Frame):
    """
    Frame that holds all other widgets
    """

    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, wx.ID_ANY,"Traditional Healers - Peru",size=(1200,800))        
        self.CenterOnScreen()

        self.CreateStatusBar()
        self.SetStatusText("I love you!")

        # Prepare the menu bar
        menuBar = wx.MenuBar()

        menu1 = wx.Menu()
        menu1.Append(101, "&Close", "Close")
        menuBar.Append(menu1, "&File")
        
        menu2 = wx.Menu()
        menu2.Append(201, "&About", "Program Information")
        menuBar.Append(menu2, "&About")

        self.SetMenuBar(menuBar)

        self.Bind(wx.EVT_MENU, self.CloseWindow, id=101)
        self.Bind(wx.EVT_MENU, self.AboutInfo, id=201)

        
        self.notebook = PeruNotebook(self)

        self.buttonSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.saveCaseButton = wx.Button(self, -1, "Save Court Case")
        self.readCaseButton = wx.Button(self, -1, "Read Court Case")
        self.buttonSizer.Add(self.saveCaseButton, 0, wx.ALIGN_RIGHT)
        self.buttonSizer.Add(self.readCaseButton, 0, wx.ALIGN_RIGHT)
        
        self.Bind(wx.EVT_BUTTON, self.OnButtonSave, self.saveCaseButton)
        
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.notebook, 1, wx.EXPAND)
        self.sizer.Add(self.buttonSizer, 0, wx.EXPAND)
        
        self.SetSizer(self.sizer)
        self.Layout()

        self.Show()
        
    def OnButtonSave(self, evt):
        dlg = wx.MessageDialog(self, 'Jeremy, are you sure you want to save this case?', 'Save Case?', wx.YES_NO )
        if dlg.ShowModal() == wx.ID_YES:
                        
            courtCaseInfo = self.getCourtCaseInfo(self.notebook.GetPage(0))
            officialInfo = self.getOfficialInfo(self.notebook.GetPage(1))
            referenceInfo = self.getReferenceInfo(self.notebook.GetPage(2))
            defendantInfo = self.getDefendantInfo(self.notebook.GetPage(3))
            plaintiffInfo = self.getPlaintiffInfo(self.notebook.GetPage(4))
            prosecutorInfo = self.getProsecutorInfo(self.notebook.GetPage(5))
            witnessInfo = self.getWitnessInfo(self.notebook.GetPage(6))
            chargesInfo = self.getChargesInfo(self.notebook.GetPage(7))
            summaryInfo = self.getSummaryInfo(self.notebook.GetPage(8))
            caseNotesInfo = self.getCaseNotesInfo(self.notebook.GetPage(9))
            healingNotesInfo = self.getHealingNotesInfo(self.notebook.GetPage(10))
            furtherNotesInfo = self.getFurtherNotesInfo(self.notebook.GetPage(11))
            
        dlg.Destroy()

    def CloseWindow(self, event):
        self.Close()

    def AboutInfo(self, event):
        dlg = wx.MessageDialog(self, 'I love you', 'About', wx.OK )
        dlg.ShowModal()
        dlg.Destroy()

#----------------------------------------------------------------------
if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = PeruFrame()
    app.MainLoop()
