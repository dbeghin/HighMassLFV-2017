#!/usr/bin/env python
import ROOT
import re
from array import array

def add_lumi():
    lowX=0.58
    lowY=0.835
    lumi  = ROOT.TPaveText(lowX, lowY+0.06, lowX+0.30, lowY+0.16, "NDC")
    lumi.SetBorderSize(   0 )
    lumi.SetFillStyle(    0 )
    lumi.SetTextAlign(   12 )
    lumi.SetTextColor(    1 )
    lumi.SetTextSize(0.06)
    lumi.SetTextFont (   42 )
    lumi.AddText("2017 simulation")
    return lumi

def add_CMS():
    lowX=0.21
    lowY=0.70
    lumi  = ROOT.TPaveText(lowX, lowY+0.06, lowX+0.15, lowY+0.16, "NDC")
    lumi.SetTextFont(61)
    lumi.SetTextSize(0.08)
    lumi.SetBorderSize(   0 )
    lumi.SetFillStyle(    0 )
    lumi.SetTextAlign(   12 )
    lumi.SetTextColor(    1 )
    lumi.AddText("CMS")
    return lumi

def add_Preliminary():
    lowX=0.21
    lowY=0.63
    lumi  = ROOT.TPaveText(lowX, lowY+0.06, lowX+0.15, lowY+0.16, "NDC")
    lumi.SetTextFont(52)
    lumi.SetTextSize(0.06)
    lumi.SetBorderSize(   0 )
    lumi.SetFillStyle(    0 )
    lumi.SetTextAlign(   12 )
    lumi.SetTextColor(    1 )
    lumi.AddText("Preliminary")
    return lumi

def make_legend(header):
    output = ROOT.TLegend(0.6, 0.6, 0.92, 0.82, header, "brNDC")
    output.SetLineWidth(0)
    output.SetLineStyle(0)
    output.SetTextSize(0.045)
    output.SetFillStyle(0)
    output.SetBorderSize(0)
    output.SetTextFont(62)
    output.SetNColumns(2)
    return output


def make_pad1(name):
    pad = ROOT.TPad("pad1"+name,"",0,0.35,1,1)
    pad.SetFillColor(0)
    pad.SetBorderMode(0)
    pad.SetBorderSize(10)
    pad.SetTickx(1)
    pad.SetTicky(1)
    pad.SetLeftMargin(0.18)
    pad.SetRightMargin(0.05)
    pad.SetTopMargin(0.122)
    pad.SetBottomMargin(0.026)
    pad.SetFrameFillStyle(0)
    pad.SetFrameLineStyle(0)
    pad.SetFrameLineWidth(3)
    pad.SetFrameBorderMode(0)
    pad.SetFrameBorderSize(10)
    #pad.SetLogx()
    return pad
    
def make_pad2(name):
    pad = ROOT.TPad("pad2"+name,"",0,0,1,0.35)
    pad.SetTopMargin(0.05)
    pad.SetBottomMargin(0.35)
    pad.SetLeftMargin(0.18)
    pad.SetRightMargin(0.05)
    pad.SetTickx(1)
    pad.SetTicky(1)
    pad.SetFrameLineWidth(3)
    pad.SetGridx()
    pad.SetGridy()
    #pad.SetLogx()
    return pad

def make_h0(histo, ph_var):
    print histo
    output = histo.Clone()
    output.SetMaximum(1.8)#FIXME(1.5)
    output.SetMinimum(0.2)#FIXME(0.5)
    
    output.SetMarkerStyle(20)

    output.Sumw2()
    output.SetStats(0)

    output.GetXaxis().SetTitle(ph_var)
    output.GetYaxis().SetTitle("Ratio to")
    output.GetXaxis().SetNdivisions(505)
    output.GetXaxis().SetMoreLogLabels()
    output.GetYaxis().SetNdivisions(8)
                
    output.GetXaxis().SetTitleSize(0.15)
    output.GetYaxis().SetTitleSize(0.15)
    output.GetYaxis().SetTitleOffset(0.56)
    output.GetXaxis().SetTitleOffset(1.04)
    output.GetXaxis().SetLabelSize(0.11)
    output.GetYaxis().SetLabelSize(0.1)
    output.GetXaxis().SetTitleFont(42)
    output.GetYaxis().SetTitleFont(42)
    return output


ROOT.gStyle.SetFrameLineWidth(3)
ROOT.gStyle.SetLineWidth(3)
ROOT.gStyle.SetOptStat(0)

c_allsigns=ROOT.TCanvas("canvas_allsigns","",0,0,600,600)

#file=ROOT.TFile("final.root","r")
ffile=ROOT.TFile("../HighMassLFVMuTau/fakerate_factorised_OSvsSSmystery.root","r")

adapt=ROOT.gROOT.GetColor(12)
new_idx=ROOT.gROOT.GetListOfColors().GetSize() + 1
trans=ROOT.TColor(new_idx, adapt.GetRed(), adapt.GetGreen(),adapt.GetBlue(), "",0.5)

#categories=["passOS","failOS"] 
#ncat=2

var=[]
var.append("TauPt_flavor_")
var.append("TauPt_muonCharge_")
nvar=len(var)
print nvar

photogenic_var=[]
photogenic_var.append("tau p_{T} (GeV)")
photogenic_var.append("tau p_{T} (GeV)")
photogenic_var.append("charged e.m. fraction")
photogenic_var.append("charged had fraction")
photogenic_var.append("muon fraction")
photogenic_var.append("neutral had fraction")
photogenic_var.append("neutral e.m. fraction")

flavors=[
    "down",
    "up",
    "strange",
    "charm",
    "bottom",
    "gluon",
]

muonCharge=[
    "MuPlus",
    "MuMinus",
]

nullList=[
    ""
]

color=[
    "#de5a6a",
    "#8fccff",
    "#006633",
    "#d89a6a",
    "#9999cc",
    "#ffcc66",
    "#c338e2",
    "#33cc00",
    "#3333cc",
    "#993333",
    "#330099",
    "#666699",
    "#cccc33",
    "#ff6600",
    "#666699",
    "#0000cc",
    "#66ccff",
    "#000000",
]

for k in range (0,nvar):
    ends=[]
    if "total" in var[k]: ends = nullList
    elif "flavor" in var[k]: ends = flavors
    elif "muonCharge" in var[k]: ends = muonCharge

    temp = ffile.Get(var[k]+ends[0])
    h0_allsigns=make_h0(temp, photogenic_var[k])
    
    allsigns=[]
    h1_allsigns=[]

    for l in range (0,len(ends)):
        var_in = var[k]+ends[l]
        print var_in

        allsigns.append(ffile.Get(var_in))
                
        allsigns[l].GetXaxis().SetTitle("")
        allsigns[l].GetXaxis().SetTitleSize(0)
        allsigns[l].GetXaxis().SetRangeUser(30,400)
        allsigns[l].GetXaxis().SetNdivisions(505)
        allsigns[l].GetYaxis().SetRangeUser(0,1)
        allsigns[l].GetYaxis().SetLabelFont(42)
        allsigns[l].GetYaxis().SetLabelOffset(0.01)
        allsigns[l].GetYaxis().SetLabelSize(0.06)
        allsigns[l].GetYaxis().SetTitleSize(0.075)
        allsigns[l].GetYaxis().SetTitleOffset(1.04)
        allsigns[l].SetTitle("")
        allsigns[l].GetYaxis().SetTitle("Fake Factor")
        allsigns[l].SetMarkerStyle(20)
        allsigns[l].SetMarkerSize(1)
        allsigns[l].SetMarkerColor(ROOT.TColor.GetColor(color[l]))
        allsigns[l].SetLineColor(ROOT.TColor.GetColor(color[l]))

        allsigns[l].GetXaxis().SetLabelSize(0)
        allsigns[l].SetMaximum(0.6)#FIXME
        allsigns[l].SetMinimum(0.0)
        allsigns[l].Draw("esame")
        
        h1_allsigns.append(allsigns[l].Clone())

        h1_allsigns[l].SetMaximum(1.8)
        h1_allsigns[l].SetMinimum(0.2)
        h1_allsigns[l].GetXaxis().SetTitle(photogenic_var[k])
        h1_allsigns[l].GetYaxis().SetTitle("Ratio to "+ends[0])
        h1_allsigns[l].GetXaxis().SetNdivisions(505)
        h1_allsigns[l].GetXaxis().SetMoreLogLabels()
        h1_allsigns[l].GetYaxis().SetNdivisions(8)
                
        h1_allsigns[l].GetXaxis().SetTitleSize(0.15)
        h1_allsigns[l].GetYaxis().SetTitleSize(0.15)
        h1_allsigns[l].GetYaxis().SetTitleOffset(0.56)
        h1_allsigns[l].GetXaxis().SetTitleOffset(1.04)
        h1_allsigns[l].GetXaxis().SetLabelSize(0.11)
        h1_allsigns[l].GetYaxis().SetLabelSize(0.1)
        h1_allsigns[l].GetXaxis().SetTitleFont(42)
        h1_allsigns[l].GetYaxis().SetTitleFont(42)
        h1_allsigns[l].SetMarkerStyle(20)
        h1_allsigns[l].Sumw2()
        h1_allsigns[l].Divide(h0_allsigns)
        
        

    print k, nvar, len(ends)
    l1=add_lumi()
    l2=add_CMS()
    l3=add_Preliminary()

    c_allsigns.cd()
    pad1_allsigns = make_pad1("allsigns")
    pad1_allsigns.cd()
    pad1_allsigns.Draw()
    allsigns[0].Draw("e")
    for l in range(1, len(allsigns)): allsigns[l].Draw("esame")
    legende_allsigns = make_legend("OS+SS")
    for l in range(0, len(allsigns)): legende_allsigns.AddEntry(allsigns[l],ends[l],"lp")
    legende_allsigns.Draw("same")
    
    l1.Draw("same")
    l2.Draw("same")
    l3.Draw("same")


    c_allsigns.cd()
    pad2_allsigns = make_pad2("allsigns")
    pad2_allsigns.cd()
    pad2_allsigns.Draw()
    for l in range(1, len(allsigns)): h1_allsigns[l].Draw("esame")

    c_allsigns.cd()
    pad1_allsigns.Draw()
    pad2_allsigns.Draw()
    
    #ROOT.gPad.RedrawAxis()
    
    c_allsigns.Modified()
    c_allsigns.SaveAs(var[k]+"allsigns.pdf")

