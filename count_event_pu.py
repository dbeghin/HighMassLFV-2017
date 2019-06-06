import os
import ROOT

sample_path = {}



########################### DYJetToLL amc #####################
path_DYToLL_amc=[
'/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/crab_DYJetsToLL_M-50_v1/190518_075646/0000/',
'/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/crab_DYJetsToLL_M-50_v1/190518_075646/0001/',
'/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/crab_DYJetsToLL_M-50_v2/190518_075705/0000/',
'/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/crab_DYJetsToLL_M-50_v2/190518_075705/0001/',
'/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/crab_DYJetsToLL_M-50_v2/190518_075705/0002/',
'/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/crab_DYJetsToLL_M-50_v2/190518_075705/0003/',
'/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/crab_DYJetsToLL_M-50_v2/190518_075705/0004/',
'/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/crab_DYJetsToLL_M-50_v2/190518_075705/0005/',
'/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/crab_DYJetsToLL_M-50_v2/190518_075705/0006/',
'/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/crab_DYJetsToLL_M-50_v2/190518_075705/0007/',
]


path_DYToLL_400to500=[
'/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017/DYJetsToLL_M-400to500_TuneCP5_13TeV-amcatnloFXFX-pythia8/crab_DYJetsToLL_M-400to500/190518_075724/0000/',
]                    
                     
path_DYToLL_500to700=[
'/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017/DYJetsToLL_M-500to700_TuneCP5_13TeV-amcatnloFXFX-pythia8/crab_DYJetsToLL_M-500to700/190518_075743/0000/',
]                    
                     
path_DYToLL_700to800=[
'/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017/DYJetsToLL_M-700to800_TuneCP5_13TeV-amcatnloFXFX-pythia8/crab_DYJetsToLL_M-700to800/190518_075802/0000/',
]                    
                     
path_DYToLL_800to1000=[
'/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017/DYJetsToLL_M-800to1000_TuneCP5_13TeV-amcatnloFXFX-pythia8/crab_DYJetsToLL_M-800to1000/190518_075821/0000/',
]                    
                     
path_DYToLL_1000to1500=[
'/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017/DYJetsToLL_M-1000to1500_TuneCP5_13TeV-amcatnloFXFX-pythia8/crab_DYJetsToLL_M-1000to1500/190518_075843/0000/',
]                    
                     
path_DYToLL_1500to2000=[
'/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017/DYJetsToLL_M-1500to2000_TuneCP5_13TeV-amcatnloFXFX-pythia8/crab_DYJetsToLL_M-1500to2000/190518_075902/0000/',
]                    
                     
path_DYToLL_2000to3000=[
'/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017/DYJetsToLL_M-2000to3000_TuneCP5_13TeV-amcatnloFXFX-pythia8/crab_DYJetsToLL_M-2000to3000/190518_075921/0000/',
]                    
                     
path_DYToLL_3000toInf=[
'/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017/DYJetsToLL_M-3000toInf_TuneCP5_13TeV-amcatnloFXFX-pythia8/crab_DYJetsToLL_M-3000toInf/190518_075939/0000/',
]



############################# WW ############################


path_WW=[
'/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017/WW_TuneCP5_13TeV-pythia8/crab_WW_v1/190518_080211/0000/',
'/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017/WW_TuneCP5_13TeV-pythia8/crab_WW_v2/190518_080230/0000/',
]

path_WW_2l2nu=[
'/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017/WWTo2L2Nu_NNPDF31_TuneCP5_13TeV-powheg-pythia8/crab_WWTo2L2Nu_v1/190524_140316/0000/',
]

path_WW_200to600=[
'/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017/WWTo2L2Nu_MLL_200To600_NNPDF31_13TeV-powheg/crab_WWTo2L2Nu_MLL_200To600/190604_134642/0000/',
]

path_WW_600to1200=[
'/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017/WWTo2L2Nu_MLL_600To1200_v1_NNPDF31_13TeV-powheg/crab_WWTo2L2Nu_MLL_600To1200_v1/190524_140216/0000/',
'/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017/WWTo2L2Nu_MLL_600To1200_v2_NNPDF31_13TeV-powheg/crab_WWTo2L2Nu_MLL_600To1200_v2/190524_140156/0000/',
'/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017/WWTo2L2Nu_MLL_600To1200_v3_NNPDF31_13TeV-powheg/crab_WWTo2L2Nu_MLL_600To1200_v3/190524_140137/0000/',
]

path_WW_1200to2500=[
'/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017/WWTo2L2Nu_MLL_1200To2500_NNPDF31_13TeV-powheg/crab_WWTo2L2Nu_MLL_1200To2500/190524_140255/0000/',
]

path_WW_2500toInf=[
'/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017/WWTo2L2Nu_MLL_2500ToInf_NNPDF31_13TeV-powheg/crab_WWTo2L2Nu_MLL_2500ToInf/190524_140235/0000/',
]




path_WZ=[
'/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017/WZ_TuneCP5_13TeV-pythia8/crab_WZ/190518_080249/0000/',
]

path_ZZ=[
'/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017/ZZ_TuneCP5_13TeV-pythia8/crab_ZZ/190518_080308/0000/',
]

################################## ST ###################
path_ST=[
'/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/crab_ST_tW_antitop_v1/190518_080017/0000/',
'/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/crab_ST_tW_antitop_v2/190518_080036/0000/',
'/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/crab_ST_tW_antitop_v3/190518_080056/0000/',
'/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/crab_ST_tW_top/190518_075958/0000/',
]


####################################### TTbar ####################
path_TT_2l2nu=[
'/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/crab_TTTo2L2Nu/190518_080115/0000/',
'/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/crab_TTTo2L2Nu_v1/190524_140336/0000/',
]

path_TT_500to800=[
'/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017/TTToLL_MLL_500To800_41to65_NNPDF31_13TeV-powheg/crab_TTToLL_MLL_500To800/190524_140040/0000/',
]                 
                  
path_TT_800to1200=[
'/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017/TTToLL_MLL_800To1200_NNPDF31_13TeV-powheg/crab_TTToLL_MLL_800To1200/190524_140021/0000/',
]                 
                  
path_TT_1200to1800=[
'/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017/TTToLL_MLL_1200To1800_NNPDF31_13TeV-powheg/crab_TTToLL_MLL_1200To1800/190524_140119/0000/',
]                 
                  
path_TT_1800toInf=[
'/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017/TTToLL_MLL_1800ToInf_NNPDF31_13TeV-powheg/crab_TTToLL_MLL_1800ToInf/190524_140058/0000/',
]



path_TT_SemiLeptonic=[
'/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/crab_TTToSemiLeptonic/190518_080152/0000/',
'/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/crab_TTToSemiLeptonic/190518_080152/0001/',
]

path_TT_had = [
'/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/crab_TTToHadronic/190518_080134/0000/',
'/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/crab_TTToHadronic/190518_080134/0001/',
]



############################### Signal ####################
path_ZPrime_500 =["/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017_Signal/ZPrimeToMuTau_M_500_TuneCP5_13TeV_pythia8/crab_ZPrimeToMuTau_M_500/190530_204219/0000/"]  
path_ZPrime_600 =["/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017_Signal/ZPrimeToMuTau_M_600_TuneCP5_13TeV_pythia8/crab_ZPrimeToMuTau_M_600/190530_204304/0000/"]  
path_ZPrime_700 =["/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017_Signal/ZPrimeToMuTau_M_700_TuneCP5_13TeV_pythia8/crab_ZPrimeToMuTau_M_700/190530_204318/0000/"]  
path_ZPrime_800 =["/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017_Signal/ZPrimeToMuTau_M_800_TuneCP5_13TeV_pythia8/crab_ZPrimeToMuTau_M_800/190530_204333/0000/"]  
path_ZPrime_900 =["/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017_Signal/ZPrimeToMuTau_M_900_TuneCP5_13TeV_pythia8/crab_ZPrimeToMuTau_M_900/190530_204349/0000/"]  
path_ZPrime_1000=["/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017_Signal/ZPrimeToMuTau_M_1000_TuneCP5_13TeV_pythia8/crab_ZPrimeToMuTau_M_1000/190530_203700/0000/"]
path_ZPrime_1100=["/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017_Signal/ZPrimeToMuTau_M_1100_TuneCP5_13TeV_pythia8/crab_ZPrimeToMuTau_M_1100/190530_203715/0000/"]
path_ZPrime_1200=["/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017_Signal/ZPrimeToMuTau_M_1200_TuneCP5_13TeV_pythia8/crab_ZPrimeToMuTau_M_1200/190530_203730/0000/"]
path_ZPrime_1300=["/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017_Signal/ZPrimeToMuTau_M_1300_TuneCP5_13TeV_pythia8/crab_ZPrimeToMuTau_M_1300/190530_203745/0000/"]
path_ZPrime_1400=["/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017_Signal/ZPrimeToMuTau_M_1400_TuneCP5_13TeV_pythia8/crab_ZPrimeToMuTau_M_1400/190530_203801/0000/"]
path_ZPrime_1500=["/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017_Signal/ZPrimeToMuTau_M_1500_TuneCP5_13TeV_pythia8/crab_ZPrimeToMuTau_M_1500/190530_203817/0000/"]
path_ZPrime_1600=["/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017_Signal/ZPrimeToMuTau_M_1600_TuneCP5_13TeV_pythia8/crab_ZPrimeToMuTau_M_1600/190530_203832/0000/"]
path_ZPrime_1700=["/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017_Signal/ZPrimeToMuTau_M_1700_TuneCP5_13TeV_pythia8/crab_ZPrimeToMuTau_M_1700/190530_203847/0000/"]
path_ZPrime_1800=["/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017_Signal/ZPrimeToMuTau_M_1800_TuneCP5_13TeV_pythia8/crab_ZPrimeToMuTau_M_1800/190530_203902/0000/"]
path_ZPrime_1900=["/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017_Signal/ZPrimeToMuTau_M_1900_TuneCP5_13TeV_pythia8/crab_ZPrimeToMuTau_M_1900/190530_203917/0000/"]
path_ZPrime_2000=["/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017_Signal/ZPrimeToMuTau_M_2000_TuneCP5_13TeV_pythia8/crab_ZPrimeToMuTau_M_2000/190530_203932/0000/"]
path_ZPrime_2200=["/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017_Signal/ZPrimeToMuTau_M_2200_TuneCP5_13TeV_pythia8/crab_ZPrimeToMuTau_M_2200/190530_203947/0000/"]
path_ZPrime_2400=["/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017_Signal/ZPrimeToMuTau_M_2400_TuneCP5_13TeV_pythia8/crab_ZPrimeToMuTau_M_2400/190530_204003/0000/"]
path_ZPrime_2600=["/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017_Signal/ZPrimeToMuTau_M_2600_TuneCP5_13TeV_pythia8/crab_ZPrimeToMuTau_M_2600/190530_204018/0000/"]
path_ZPrime_2800=["/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017_Signal/ZPrimeToMuTau_M_2800_TuneCP5_13TeV_pythia8/crab_ZPrimeToMuTau_M_2800/190530_204037/0000/"]
path_ZPrime_3000=["/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017_Signal/ZPrimeToMuTau_M_3000_TuneCP5_13TeV_pythia8/crab_ZPrimeToMuTau_M_3000/190530_204051/0000/"]
path_ZPrime_3500=["/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017_Signal/ZPrimeToMuTau_M_3500_TuneCP5_13TeV_pythia8/crab_ZPrimeToMuTau_M_3500/190530_204114/0000/"]
path_ZPrime_4000=["/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017_Signal/ZPrimeToMuTau_M_4000_TuneCP5_13TeV_pythia8/crab_ZPrimeToMuTau_M_4000/190530_204135/0000/"]
path_ZPrime_4500=["/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017_Signal/ZPrimeToMuTau_M_4500_TuneCP5_13TeV_pythia8/crab_ZPrimeToMuTau_M_4500/190530_204149/0000/"]
path_ZPrime_5000=["/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017_Signal/ZPrimeToMuTau_M_5000_TuneCP5_13TeV_pythia8/crab_ZPrimeToMuTau_M_5000/190530_204204/0000/"]
path_ZPrime_5500=["/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017_Signal/ZPrimeToMuTau_M_5500_TuneCP5_13TeV_pythia8/crab_ZPrimeToMuTau_M_5500/190530_204234/0000/"]
path_ZPrime_6000=["/pnfs/iihe/cms/store/user/amkalsi/Legacy_2017_Signal/ZPrimeToMuTau_M_6000_TuneCP5_13TeV_pythia8/crab_ZPrimeToMuTau_M_6000/190530_204249/0000/"]





#sample_path['WW']                =path_WW
#sample_path['WW_2l2nu']          =path_WW_2l2nu
sample_path['WW_200to600']      =path_WW_200to600
#sample_path['WW_600to1200']      =path_WW_600to1200
#sample_path['WW_1200to2500']     =path_WW_1200to2500
#sample_path['WW_2500toInf']      =path_WW_2500toInf
#sample_path['WZ']                =path_WZ
#sample_path['ZZ']                =path_ZZ
#sample_path['ST']                =path_ST
#sample_path['DYToLL_amc']        =path_DYToLL_amc
#sample_path['DYToLL_400to500']   =path_DYToLL_400to500  
#sample_path['DYToLL_500to700']   =path_DYToLL_500to700  
#sample_path['DYToLL_700to800']   =path_DYToLL_700to800  
#sample_path['DYToLL_800to1000']  =path_DYToLL_800to1000 
#sample_path['DYToLL_1000to1500'] =path_DYToLL_1000to1500
#sample_path['DYToLL_1500to2000'] =path_DYToLL_1500to2000
#sample_path['DYToLL_2000to3000'] =path_DYToLL_2000to3000
#sample_path['DYToLL_3000toInf']  =path_DYToLL_3000toInf 
#sample_path['TT_had']        = path_TT_had       
#sample_path['TT_semilep']    = path_TT_SemiLeptonic
#sample_path['TT_2l2nu']      = path_TT_2l2nu       
#sample_path['TT_500to800']   = path_TT_500to800  
#sample_path['TT_800to1200']  = path_TT_800to1200 
#sample_path['TT_1200to1800'] = path_TT_1200to1800
#sample_path['TT_1800toInf']  = path_TT_1800toInf 


#sample_path['ZPrime_500']   = path_ZPrime_500 
#sample_path['ZPrime_600']   = path_ZPrime_600 
#sample_path['ZPrime_700']   = path_ZPrime_700 
#sample_path['ZPrime_800']   = path_ZPrime_800 
#sample_path['ZPrime_900']   = path_ZPrime_900 
#sample_path['ZPrime_1000']  = path_ZPrime_1000
#sample_path['ZPrime_1100']  = path_ZPrime_1100
#sample_path['ZPrime_1200']  = path_ZPrime_1200
#sample_path['ZPrime_1300']  = path_ZPrime_1300
#sample_path['ZPrime_1400']  = path_ZPrime_1400
#sample_path['ZPrime_1500']  = path_ZPrime_1500
#sample_path['ZPrime_1600']  = path_ZPrime_1600
#sample_path['ZPrime_1700']  = path_ZPrime_1700
#sample_path['ZPrime_1800']  = path_ZPrime_1800
#sample_path['ZPrime_1900']  = path_ZPrime_1900
#sample_path['ZPrime_2000']  = path_ZPrime_2000
#sample_path['ZPrime_2200']  = path_ZPrime_2200
#sample_path['ZPrime_2400']  = path_ZPrime_2400
#sample_path['ZPrime_2600']  = path_ZPrime_2600
#sample_path['ZPrime_2800']  = path_ZPrime_2800
#sample_path['ZPrime_3000']  = path_ZPrime_3000
#sample_path['ZPrime_3500']  = path_ZPrime_3500
#sample_path['ZPrime_4000']  = path_ZPrime_4000
#sample_path['ZPrime_4500']  = path_ZPrime_4500
#sample_path['ZPrime_5000']  = path_ZPrime_5000
#sample_path['ZPrime_5500']  = path_ZPrime_5500
#sample_path['ZPrime_6000']  = path_ZPrime_6000


for sample_name in sample_path:
    H_pu=ROOT.TH1F("pileup_%s"%(sample_name),"",120,0,120)
    H_pu.Scale(0)
    nEventsraw = 0
    neventsweight = 0
    nEventsStored = 0
    nEventsiihe = 0
    for path in sample_path[sample_name]:
        print path
        filenames = os.listdir(path)
        for fname in filenames:
            filename = path +  fname
            if 'root' not in fname: continue
            f = ROOT.TFile.Open(filename)
            if not f: print 'not exist'+fname
            tree_in = f.Get('IIHEAnalysis')
            tree_meta = f.Get('meta')
            nEventsiihe += tree_in.GetEntries()
            tree_meta.GetEntry(0)
            nEventsraw += tree_meta.nEventsRaw
            nEventsStored += tree_meta.nEventsStored
            neventsweight += tree_meta.mc_nEventsWeighted
            h_tmp=f.Get("pileupDist")
            H_pu.Add(h_tmp,1)
            f.Close()
    fout=ROOT.TFile("./mc_pu/%s.root"%(sample_name),"RECREATE")
    fout.cd()
    H_pu.Write("pileup")
    fout.Close()
    print '#####################'
    print '%s'%(sample_name) 
    print 'nEventsraw %d   '%(nEventsraw)
    print 'neventsweight %d   '%(neventsweight)
    print 'nEventsStored %d   '%(nEventsStored)
    print 'nEventsiihe %d   '%(nEventsiihe)
    print '#####################' 
