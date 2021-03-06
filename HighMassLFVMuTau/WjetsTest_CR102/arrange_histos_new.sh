mkdir -p Arranged_RPV
hadd -f Arranged_RPV/RPV.root Out_RPV_M500_LLE_LQD001/Con*RPV_M500_LLE_LQD001.root 


mkdir -p Arranged_DY
hadd -f Arranged_DY/DY_inclusive.root Out_DY_inclusive*/Con*DY_inclusive*.root 
hadd -f Arranged_DY/DY_400to500.root Out_DY_400to500/Con*DY_400to500.root 
hadd -f Arranged_DY/DY_500to700.root Out_DY_500to700/Con*DY_500to700.root 
hadd -f Arranged_DY/DY_700to800.root Out_DY_700to800/Con*DY_700to800.root 
hadd -f Arranged_DY/DY_800to1000.root Out_DY_800to1000/Con*DY_800to1000.root 
hadd -f Arranged_DY/DY_1000to1500.root Out_DY_1000to1500/Con*DY_1000to1500.root 
hadd -f Arranged_DY/DY_1500to2000.root Out_DY_1500to2000/Con*DY_1500to2000.root 
hadd -f Arranged_DY/DY_2000to3000.root Out_DY_2000to3000/Con*DY_2000to3000.root 


mkdir -p Arranged_TT
hadd -f Arranged_TT/TT_inclusive.root Out_TT_inclusive_powheg/Con*TT_inclusive_powheg.root 
hadd -f Arranged_TT/TT_500to800.root Out_TT_500to800*/Con*TT_500to800*.root 
hadd -f Arranged_TT/TT_800to1200.root Out_TT_800to1200*/Con*TT_800to1200*.root 
hadd -f Arranged_TT/TT_1200to1800.root Out_TT_1200to1800*/Con*TT_1200to1800*.root 
hadd -f Arranged_TT/TT_1800toInf.root Out_TT_1800toInf*/Con*TT_1800toInf*.root 


mkdir -p Arranged_WJets
#hadd -f Arranged_WJets/WJets_inclusive.root Out_WJets_inclusive*/Con*WJets_inclusive.root 
hadd -f Arranged_WJets/WJets_inclusive.root Out_WJets_inclusive_mad*/Con*WJets_inclusive*.root 
hadd -f Arranged_WJets/WJets_100to250.root Out_WJets_100to250*/Con*WJets_100to250.root 
hadd -f Arranged_WJets/WJets_250to400.root Out_WJets_250to400*/Con*WJets_250to400.root 
hadd -f Arranged_WJets/WJets_400to600.root Out_WJets_400to600*/Con*WJets_400to600.root 
hadd -f Arranged_WJets/WJets_600toInf.root Out_WJets_600toInf*/Con*WJets_600toInf.root 


mkdir -p Arranged_QCD
hadd -f Arranged_QCD/QCD_15to30.root Out_QCD_15to30*/Con*.root
hadd -f Arranged_QCD/QCD_30to50.root Out_QCD_30to50*/Con*.root
hadd -f Arranged_QCD/QCD_50to80.root Out_QCD_50to80*/Con*.root
hadd -f Arranged_QCD/QCD_80to120.root Out_QCD_80to120*/Con*.root
hadd -f Arranged_QCD/QCD_120to170.root Out_QCD_120to170*/Con*.root
hadd -f Arranged_QCD/QCD_170to300.root Out_QCD_170to300*/Con*.root
hadd -f Arranged_QCD/QCD_300to470.root Out_QCD_300to470*/Con*.root
hadd -f Arranged_QCD/QCD_470to600.root Out_QCD_470to600*/Con*.root
hadd -f Arranged_QCD/QCD_600to800.root Out_QCD_600to800*/Con*.root
hadd -f Arranged_QCD/QCD_800to1000.root Out_QCD_800to1000*/Con*.root
hadd -f Arranged_QCD/QCD_1000to1400.root Out_QCD_1000to1400*/Con*.root
hadd -f Arranged_QCD/QCD_1400to1800.root Out_QCD_1400to1800*/Con*.root
hadd -f Arranged_QCD/QCD_1800to2400.root Out_QCD_1800to2400*/Con*.root
hadd -f Arranged_QCD/QCD_2400to3200.root Out_QCD_2400to3200*/Con*.root

mkdir -p Arranged_WW
hadd -f Arranged_WW/WW_inclusive.root Out_WW_inclusive/Con*WW_inclusive.root 
hadd -f Arranged_WW/WW_200to600.root Out_WW_200to600/Con*WW*.root 
hadd -f Arranged_WW/WW_600to1200.root Out_WW_600to1200/Con*WW*.root 
hadd -f Arranged_WW/WW_1200to2500.root Out_WW_1200to2500/Con*WW*.root 
hadd -f Arranged_WW/WW_2500toInf.root Out_WW_2500toInf/Con*WW*.root 


mkdir -p Arranged_ZZ
hadd -f Arranged_ZZ/ZZ.root Out_ZZ_inclusive/Con*ZZ_inclusive.root 


mkdir -p Arranged_WZ
hadd -f Arranged_WZ/WZ.root Out_WZ_inclusive/Con*WZ_inclusive.root 


mkdir -p Arranged_ST_top
hadd -f Arranged_ST_top/ST_top.root Out_ST_top/Con*ST_top.root 


mkdir -p Arranged_ST_antitop
hadd -f Arranged_ST_antitop/ST_antitop.root Out_ST_antitop/Con*ST_antitop.root 


mkdir -p Arranged_data
hadd -f Arranged_data/data.root Out_SMu*/*.root