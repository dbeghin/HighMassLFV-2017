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
    lumi.AddText("2016, 35.9 fb^{-1} (13 TeV)")
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

def make_legend():
    output = ROOT.TLegend(0.65, 0.4, 0.92, 0.82, "", "brNDC")
    output.SetLineWidth(0)
    output.SetLineStyle(0)
    output.SetFillStyle(0)
    output.SetBorderSize(0)
    output.SetTextFont(62)
    return output

ROOT.gStyle.SetFrameLineWidth(3)
ROOT.gStyle.SetLineWidth(3)
ROOT.gStyle.SetOptStat(0)

c=ROOT.TCanvas("canvas","",0,0,600,600)
c.cd()

file=ROOT.TFile("histos_fakerate_SSMtLow.root","r")

adapt=ROOT.gROOT.GetColor(12)
new_idx=ROOT.gROOT.GetListOfColors().GetSize() + 1
trans=ROOT.TColor(new_idx, adapt.GetRed(), adapt.GetGreen(),adapt.GetBlue(), "",0.5)

#categories=["passOS","failOS"] 
#ncat=2

var=[]
var.append("mu_pt")
var.append("mu_eta")
var.append("mu_phi")
var.append("tau_pt")
var.append("tau_eta")
var.append("tau_phi")
var.append("ev_Nvertex")
var.append("ev_DRmutau")
var.append("ev_MET")
var.append("ev_Mcol")
var.append("ev_Mvis")
var.append("ev_Mtot")
var.append("ev_Mt")
len_tau = len(var)
#var.append("taupt_jetpt_pass")
#var.append("taupt_jetpt_fail")

dms=[]
dms.append("DM0")
dms.append("DM1")
dms.append("DM10")

eta=[]
eta.append("barrel")
eta.append("endcap")

taun=[]
taun.append("realtau")
taun.append("faketau")

var_log_dic = {
"mu_pt"            : True,
"mu_eta"           : False,
"mu_phi"           : False,
"tau_pt"           : True,
"tau_eta"          : False,
"tau_phi"          : False,
"ev_Nvertex"       : False,
"ev_DRmutau"       : False,
"ev_MET"           : True,
"ev_Mcol"          : True,
"ev_Mvis"          : True,
"ev_Mtot"          : True,
"ev_Mt"            : True,
}

nvar=len(var)
print nvar, len_tau

photogenic_var={
"mu_pt"            : "p_{T} (#mu)",
"mu_eta"           : "#eta (#mu)",
"mu_phi"           : "#phi (#mu)",
"tau_pt"           : "p_{T} (#tau)",
"tau_eta"          : "#eta (#tau)",
"tau_phi"          : "#phi (#tau)",
"ev_Nvertex"       : "N_{vertex}",
"ev_DRmutau"       : "#DeltaR (#mu #tau)",
"ev_MET"           : "E_{T}^{miss} (GeV)",
"ev_Mcol"          : "m_{col} (GeV)",
"ev_Mvis"          : "m_{vis} (GeV)",
"ev_Mtot"          : "m_{tot} (GeV)",
"ev_Mt"            : "m_{T} (GeV)",
"taupt_jetpt_pass" : ["p_{T} (#tau)", "p_{T} (jet)"],
"taupt_jetpt_fail" : ["p_{T} (#tau)", "p_{T} (jet)"],
}

for k in range (0,nvar):
    var_in = ""
    var_in = var[k]
    Data=file.Get("data_"+var_in)
    TT=file.Get("TT_"+var_in)
    VV=file.Get("VV_"+var_in)
    DY=file.Get("DY_"+var_in)
    ST=file.Get("ST_"+var_in)
    #Signal=file.Get("Signal_"+var_in)
    
    rebin = 1
    if "taupt" in var_in: rebin=10
    
    Data.GetXaxis().SetTitle("")
    Data.GetXaxis().SetTitleSize(0)
    Data.GetXaxis().SetNdivisions(505)
    Data.GetYaxis().SetLabelFont(42)
    Data.GetYaxis().SetLabelOffset(0.01)
    Data.GetYaxis().SetLabelSize(0.06)
    Data.GetYaxis().SetTitleSize(0.075)
    Data.GetYaxis().SetTitleOffset(1.04)
    Data.SetTitle("")
    Data.GetYaxis().SetTitle("Events/bin")
    
    
    #QCD.SetFillColor(ROOT.TColor.GetColor("#ffccff"))
    #W.SetFillColor(ROOT.TColor.GetColor("#de5a6a"))
    VV.SetFillColor(ROOT.TColor.GetColor("#d89a6a"))
    TT.SetFillColor(ROOT.TColor.GetColor("#9999cc"))
    DY.SetFillColor(ROOT.TColor.GetColor("#ffcc66"))
    ST.SetFillColor(ROOT.TColor.GetColor("#c338e2"))
    
    Data.SetMarkerStyle(20)
    Data.SetMarkerSize(1)
    Data.Rebin(rebin)
    #QCD.SetLineColor(1)
    #QCD.Rebin(rebin)
    #W.SetLineColor(1)
    #W.Rebin(rebin)
    VV.SetLineColor(1)
    VV.Rebin(rebin)
    TT.SetLineColor(1)
    TT.Rebin(rebin)
    DY.SetLineColor(1)
    DY.Rebin(rebin)
    ST.SetLineColor(1)
    ST.Rebin(rebin)
    Data.SetLineColor(1)
    Data.SetLineWidth(2)
    
    
    stack=ROOT.THStack("stack","stack")
    stack.Add(ST)
    #stack.Add(QCD)
    #stack.Add(W)
    stack.Add(VV)
    stack.Add(TT)
    stack.Add(DY)
    
    errorBand = TT.Clone()
    #errorBand.Add(QCD)
    errorBand.Add(ST)
    errorBand.Add(DY)
    errorBand.Add(VV)
    errorBand.SetMarkerSize(0)
    errorBand.SetFillColor(new_idx)
    errorBand.SetFillStyle(3001)
    errorBand.SetLineWidth(1)
    
    pad1 = ROOT.TPad("pad1","pad1",0,0.35,1,1)
    pad1.Draw()
    pad1.cd()
    pad1.SetFillColor(0)
    pad1.SetBorderMode(0)
    pad1.SetBorderSize(10)
    pad1.SetTickx(1)
    pad1.SetTicky(1)
    pad1.SetLeftMargin(0.18)
    pad1.SetRightMargin(0.05)
    pad1.SetTopMargin(0.122)
    pad1.SetBottomMargin(0.026)
    pad1.SetFrameFillStyle(0)
    pad1.SetFrameLineStyle(0)
    pad1.SetFrameLineWidth(3)
    pad1.SetFrameBorderMode(0)
    pad1.SetFrameBorderSize(10)
    if (var_log_dic[var[k]]): pad1.SetLogy()
    
    Data.GetXaxis().SetLabelSize(0)
    if (var_log_dic[var[k]]):
        Data.SetMaximum(Data.GetMaximum()*1000)#1.5)#FIXME
    else:
        Data.SetMaximum(Data.GetMaximum()*1.2)#2.5)#FIXME
    Data.SetMinimum(0.01)
    Data.Draw("e")
    stack.Draw("histsame")
    errorBand.Draw("e2same")
    Data.Draw("esame")
    
    
    #Signal.SetLineColor(2)
    #Signal.SetLineWidth(2)
    #Signal.Draw("histsame")
    
    
    legende=make_legend()
    legende.AddEntry(Data,"Observed","elp")
    #legende.AddEntry(Signal,"RPV#rightarrow #mu #tau","f")
    legende.AddEntry(DY,"Drell-Yann","f")
    legende.AddEntry(TT,"t#bar{t}+jets","f")
    #legende.AddEntry(W,"W+jets","f")
    legende.AddEntry(VV,"Diboson","f")
    #legende.AddEntry(QCD,"QCD multijet","f")
    legende.AddEntry(ST,"Single Top","f")
    legende.AddEntry(errorBand,"Uncertainty","f")
    legende.Draw()
    
    l1=add_lumi()
    l1.Draw("same")
    l2=add_CMS()
    l2.Draw("same")
    l3=add_Preliminary()
    l3.Draw("same")
    
    pad1.RedrawAxis()
    
    finalstate  = ROOT.TLegend(0.21, 0.52+0.013, 0.43, 0.70+0.155)
    finalstate.SetBorderSize(   0 )
    finalstate.SetFillStyle(    0 )
    finalstate.SetTextAlign(   12 )
    finalstate.SetTextSize ( 0.06 )
    finalstate.SetTextColor(    1 )
    #finalstate.SetTextFont (   41 )
    finalstate.SetHeader("#mu #mu")
    finalstate.Draw("same")
    
    '''
    categ  = ROOT.TPaveText(0.21, 0.45+0.013, 0.43, 0.65+0.155, "NDC")
    categ.SetBorderSize(   0 )
    categ.SetFillStyle(    0 )
    categ.SetTextAlign(   12 )
    categ.SetTextSize ( 0.06 )
    categ.SetTextColor(    1 )
    categ.SetTextFont (   41 )
    categ.AddText("OS iso #mu anti-iso #tau")
    #categ.AddText("Z#rightarrow#mu#mu CR")
    categ.Draw("same")
    '''
    
    c.cd()
    pad2 = ROOT.TPad("pad2","pad2",0,0,1,0.35)
    pad2.SetTopMargin(0.05)
    pad2.SetBottomMargin(0.35)
    pad2.SetLeftMargin(0.18)
    pad2.SetRightMargin(0.05)
    pad2.SetTickx(1)
    pad2.SetTicky(1)
    pad2.SetFrameLineWidth(3)
    pad2.SetGridx()
    pad2.SetGridy()
    pad2.Draw()
    pad2.cd()
    h1=Data.Clone()
    h1.SetMaximum(1.7)#FIXME(1.5)
    h1.SetMinimum(0.5)#FIXME(0.5)
    h1.SetMarkerStyle(20)
    h3=errorBand.Clone()
    hwoE=errorBand.Clone()
    for iii in range (1,hwoE.GetSize()-2):
        hwoE.SetBinError(iii,0)
    h3.Sumw2()
    h1.Sumw2()
    h1.SetStats(0)
    h1.Divide(hwoE)
    h3.Divide(hwoE)
    h1.GetXaxis().SetTitle(photogenic_var[var[k]])
    h1.GetXaxis().SetLabelSize(0.08)
    h1.GetYaxis().SetLabelSize(0.08)
    h1.GetYaxis().SetTitle("Obs./Exp.")
    h1.GetXaxis().SetNdivisions(505)
    h1.GetYaxis().SetNdivisions(10)
    
    h1.GetXaxis().SetTitleSize(0.15)
    h1.GetYaxis().SetTitleSize(0.15)
    h1.GetYaxis().SetTitleOffset(0.56)
    h1.GetXaxis().SetTitleOffset(1.04)
    h1.GetXaxis().SetLabelSize(0.11)
    h1.GetYaxis().SetLabelSize(0.11)
    h1.GetXaxis().SetTitleFont(42)
    h1.GetYaxis().SetTitleFont(42)
    
    h1.Draw("ep")
    h3.Draw("e2same")
    
    c.cd()
    pad1.Draw()
    
    ROOT.gPad.RedrawAxis()
    
    c.Modified()
    c.SaveAs(var_in+".png")


