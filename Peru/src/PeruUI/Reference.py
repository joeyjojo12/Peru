import wx
import PeruConstants, ReferenceDB

def getReferenceNotebookInfo(referencePage):
    output = []
    
    for i in range(0,referencePage.nestedNotebook.GetPageCount()):
        output.append(getReferenceInfo(referencePage.nestedNotebook.GetPage(i)))
    
    return output

def getReferenceInfo(referencePage):    
    return [str(referencePage.RefID.GetValue()),
            str(referencePage.Citation.GetValue()),
            str(referencePage.Archive.GetValue()),
            str(referencePage.Stack.GetValue()),
            str(referencePage.Number.GetValue()),
            str(referencePage.DocName.GetValue()),
            str(referencePage.Author.GetValue()),
            str(referencePage.Year.GetValue()),
            str(referencePage.Type.GetValue()),
            str(referencePage.Notes.GetValue())]

class ReferencePanel(wx.Panel):
    def __init__(self, parent):

        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)


        label0 = wx.StaticText(self, label="Reference ID :")        
        RefID = self.RefID = wx.TextCtrl(self, size=(50,-1))
        label1 = wx.StaticText(self, label="Citation :")        
        Citation = self.Citation = wx.TextCtrl(self, size=(400,-1))
        label2 = wx.StaticText(self, label="Archive :")
        Archive = self.Archive = wx.TextCtrl(self, size=(400,-1))
        label3 = wx.StaticText(self, label="Stack :")
        Stack = self.Stack = wx.TextCtrl(self, size=(400,-1))
        label4 = wx.StaticText(self, label="Number :")
        Number = self.Number = wx.TextCtrl(self, size=(400,-1))        
        label5 = wx.StaticText(self, label="Document Name :")
        DocName = self.DocName = wx.TextCtrl(self, size=(400,-1))
        label6 = wx.StaticText(self, label="Author :")
        Author = self.Author = wx.TextCtrl(self, size=(400,-1))
        label7 = wx.StaticText(self, label="Year :")
        Year = self.Year = wx.TextCtrl(self, size=(50,-1))
        label8 = wx.StaticText(self, label="Type :")
        Type = self.Type = wx.TextCtrl(self, size=(400,-1))
        label9 = wx.StaticText(self, label="Notes :")
        Notes = self.Notes = wx.TextCtrl(self, -1, style=wx.TE_MULTILINE)
        
        space = 6
        infoSizer = wx.GridBagSizer(hgap=space, vgap=space)
        infoSizer.Add(label0,  (1,0))
        infoSizer.Add(RefID,   (1,1))
        infoSizer.Add(label1,  (2,0))
        infoSizer.Add(Citation,(2,1))
        infoSizer.Add(label2,  (3,0))
        infoSizer.Add(Archive, (3,1))
        infoSizer.Add(label3,  (4,0))
        infoSizer.Add(Stack,   (4,1))
        infoSizer.Add(label4,  (5,0))
        infoSizer.Add(Number,  (5,1))
        infoSizer.Add(label5,  (6,0))
        infoSizer.Add(DocName, (6,1))
        infoSizer.Add(label6,  (7,0))
        infoSizer.Add(Author,  (7,1))
        infoSizer.Add(label7,  (8,0))
        infoSizer.Add(Year,    (8,1))
        infoSizer.Add(label8,  (9,0))
        infoSizer.Add(Type,    (9,1))
        infoSizer.Add(label9,  (10,0))
        infoSizer.Add(Notes,   (10,1), (5,20), flag=wx.EXPAND)
        
        self.buttonSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.saveReferenceButton = wx.Button(self, -1, "Save Reference")
        self.readReferenceButton = wx.Button(self, -1, "Read Reference")
        self.deleteReferenceButton = wx.Button(self, -1, "Delete Reference")        
        self.buttonSizer.Add(self.saveReferenceButton, 0, wx.ALIGN_RIGHT)
        self.buttonSizer.Add(self.readReferenceButton, 0, wx.ALIGN_RIGHT)
        self.buttonSizer.Add(self.deleteReferenceButton, 0, wx.ALIGN_RIGHT)
        
        self.Bind(wx.EVT_BUTTON, self.OnButtonSave,   self.saveReferenceButton)
        self.Bind(wx.EVT_BUTTON, self.OnButtonRead,   self.readReferenceButton)
        self.Bind(wx.EVT_BUTTON, self.OnButtonDelete, self.deleteReferenceButton)
            
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(infoSizer, 1, wx.EXPAND)
        sizer.Add(self.buttonSizer, 0, wx.ALIGN_RIGHT)

        self.SetSizer(sizer)
        
    def OnButtonSave(self, evt):
        print (ReferenceDB.InsertUpdateReference(getReferenceInfo(self)))[1]
        
    def OnButtonRead(self, evt):
        print (ReferenceDB.ReadReference(getReferenceInfo(self)))[1]
        
    def OnButtonDelete(self, evt):
        print (ReferenceDB.DeleteReference(getReferenceInfo(self)))[1]
        
class NestedReferencePanel(wx.Panel):
    """
    Panel contains multiple 'Reference' tabs
    """
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent, id=wx.ID_ANY)
        self.oldNumReferences = 1
        
        nestedNotebook = self.nestedNotebook = wx.Notebook(self, wx.ID_ANY)
        
        label1 = wx.StaticText(self, label="Number of References: ")
        numReferences = self.numReferences = wx.ComboBox(self, 500, "1", (90, 50), (50, -1), PeruConstants.TAB_NUMBER_LIST, wx.CB_DROPDOWN | wx.TE_PROCESS_ENTER )        
        self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox, numReferences)
        
        topSizer = self.topSizer = wx.BoxSizer(wx.HORIZONTAL)        
        topSizer.Add(label1, 0, wx.ALIGN_LEFT) 
        topSizer.Add(numReferences, 0, wx.ALIGN_LEFT)

        nestedNotebook.AddPage(ReferencePanel(nestedNotebook), "Reference 1")
            
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(topSizer, 0, wx.ALIGN_LEFT)
        sizer.Add(nestedNotebook, 1, wx.ALL|wx.EXPAND, 5)

        self.SetSizer(sizer)
        
    # When the user selects something, we go here.
    def EvtComboBox(self, evt):
        newNumReferences = int(self.numReferences.GetValue())
        oldNumReferences = int(self.oldNumReferences)
        
        if newNumReferences == oldNumReferences:
            return
        elif newNumReferences < oldNumReferences:
            for i in range(oldNumReferences-1,newNumReferences-1,-1):
                self.nestedNotebook.DeletePage(i)
        else:
            for i in range(oldNumReferences+1,newNumReferences+1):
                self.nestedNotebook.AddPage(ReferencePanel(self.nestedNotebook), "Reference " + str(i))
        
        self.oldNumReferences = newNumReferences