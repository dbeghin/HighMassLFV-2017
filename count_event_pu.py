import os
import ROOT

sample_path = {}




########################### DYJetToLL amc #####################
path_DYToLL_amc=[
'/pnfs/iihe/cms/store/user/amkalsi/2017_ReReco_DeepTau/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/crab_DYJets_v1/200209_073405/0000/',
'/pnfs/iihe/cms/store/user/amkalsi/2017_ReReco_DeepTau/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/crab_DYJets_v1/200209_073405/0001/',
'/pnfs/iihe/cms/store/user/amkalsi/2017_ReReco_DeepTau/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/crab_DYJets_v1/200209_073405/0002/',
'/pnfs/iihe/cms/store/user/amkalsi/2017_ReReco_DeepTau/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/crab_DYJets_v1/200209_073405/0003/',
'/pnfs/iihe/cms/store/user/amkalsi/2017_ReReco_DeepTau/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/crab_DYJets_v1/200209_073405/0004/',
'/pnfs/iihe/cms/store/user/amkalsi/2017_ReReco_DeepTau/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/crab_DYJets_v1/200209_073405/0005/',
'/pnfs/iihe/cms/store/user/amkalsi/2017_ReReco_DeepTau/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/crab_DYJets_v1/200209_073405/0006/',
'/pnfs/iihe/cms/store/user/amkalsi/2017_ReReco_DeepTau/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/crab_DYJets_v1/200209_073405/0007/',
]


path_DYToLL_100to200=['/pnfs/iihe/cms/store/user/amkalsi/2017_ReReco_DeepTau/DYJetsToLL_M-100to200_TuneCP5_13TeV-amcatnloFXFX-pythia8/crab_DYJetsToLL_M-100to200_TuneCP5_13TeV-amcatnloFXFX-pythia8/200209_080807/0000/']
path_DYToLL_200to400=['/pnfs/iihe/cms/store/user/amkalsi/2017_ReReco_DeepTau/DYJetsToLL_M-200to400_TuneCP5_13TeV-amcatnloFXFX-pythia8/crab_DYJetsToLL_M-200to400_TuneCP5_13TeV-amcatnloFXFX-pythia8/200209_080654/0000/']
path_DYToLL_400to500=['/pnfs/iihe/cms/store/user/amkalsi/2017_ReReco_DeepTau/DYJetsToLL_M-400to500_TuneCP5_13TeV-amcatnloFXFX-pythia8/crab_DYJetsToLL_M-400to500_TuneCP5_13TeV-amcatnloFXFX-pythia8/200209_080603/0000/']
path_DYToLL_500to700=['/pnfs/iihe/cms/store/user/amkalsi/2017_ReReco_DeepTau/DYJetsToLL_M-500to700_TuneCP5_13TeV-amcatnloFXFX-pythia8/crab_DYJetsToLL_M-500to700_TuneCP5_13TeV-amcatnloFXFX-pythia8/200209_080533/0000/']
path_DYToLL_700to800=['/pnfs/iihe/cms/store/user/amkalsi/2017_ReReco_DeepTau/DYJetsToLL_M-700to800_TuneCP5_13TeV-amcatnloFXFX-pythia8/crab_DYJetsToLL_M-700to800_TuneCP5_13TeV-amcatnloFXFX-pythia8/200209_080509/0000/']
path_DYToLL_800to1000=['/pnfs/iihe/cms/store/user/amkalsi/2017_ReReco_DeepTau/DYJetsToLL_M-800to1000_TuneCP5_13TeV-amcatnloFXFX-pythia8/crab_DYJetsToLL_M-800to1000_TuneCP5_13TeV-amcatnloFXFX-pythia8/200209_080444/0000/']
path_DYToLL_1000to1500=['/pnfs/iihe/cms/store/user/amkalsi/2017_ReReco_DeepTau/DYJetsToLL_M-1000to1500_TuneCP5_13TeV-amcatnloFXFX-pythia8/crab_DYJetsToLL_M-1000to1500_TuneCP5_13TeV-amcatnloFXFX-pythia8/200209_080833/0000/']
path_DYToLL_1500to2000=['/pnfs/iihe/cms/store/user/amkalsi/2017_ReReco_DeepTau/DYJetsToLL_M-1500to2000_TuneCP5_13TeV-amcatnloFXFX-pythia8/crab_DYJetsToLL_M-1500to2000_TuneCP5_13TeV-amcatnloFXFX-pythia8/200209_080744/0000/']
path_DYToLL_2000to3000=['/pnfs/iihe/cms/store/user/amkalsi/2017_ReReco_DeepTau/DYJetsToLL_M-2000to3000_TuneCP5_13TeV-amcatnloFXFX-pythia8/crab_DYJetsToLL_M-2000to3000_TuneCP5_13TeV-amcatnloFXFX-pythia8/200209_080719/0000/']
path_DYToLL_3000toInf=['/pnfs/iihe/cms/store/user/amkalsi/2017_ReReco_DeepTau/DYJetsToLL_M-3000toInf_TuneCP5_13TeV-amcatnloFXFX-pythia8/crab_DYJetsToLL_M-3000toInf_TuneCP5_13TeV-amcatnloFXFX-pythia8/200209_080628/0000/']



############################# WW ############################


path_WW_2l2nu=[
'/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/WWTo2L2Nu_NNPDF31_TuneCP5_13TeV-powheg-pythia8/crab_WWTo2L2Nu_NNPDF31_TuneCP5_13TeV-powheg-pythia8/200303_174439/0000/',
]

path_WW_200to600=['/pnfs/iihe/cms/store/user/amkalsi/2017_ReReco_DeepTau/WWTo2L2Nu_MLL_200To600_NNPDF31_13TeV-powheg/crab_WWTo2L2Nu_MLL_200To600_NNPDF31_13TeV-powheg/200209_081247/0000/']
path_WW_600to1200=[
'/pnfs/iihe/cms/store/user/amkalsi/2017_ReReco_DeepTau/WWTo2L2Nu_MLL_600To1200_v1_NNPDF31_13TeV-powheg/crab_WWTo2L2Nu_MLL_600To1200_v1_NNPDF31_13TeV-powheg/200209_081153/0000/',
'/pnfs/iihe/cms/store/user/amkalsi/2017_ReReco_DeepTau/WWTo2L2Nu_MLL_600To1200_v2_NNPDF31_13TeV-powheg/crab_WWTo2L2Nu_MLL_600To1200_v2_NNPDF31_13TeV-powheg/200209_081129/0000/',
'/pnfs/iihe/cms/store/user/amkalsi/2017_ReReco_DeepTau/WWTo2L2Nu_MLL_600To1200_v3_NNPDF31_13TeV-powheg/crab_WWTo2L2Nu_MLL_600To1200_v3_NNPDF31_13TeV-powheg/200209_081105/0000/',
]
path_WW_1200to2500=['/pnfs/iihe/cms/store/user/amkalsi/2017_ReReco_DeepTau/WWTo2L2Nu_MLL_1200To2500_NNPDF31_13TeV-powheg/crab_WWTo2L2Nu_MLL_1200To2500_NNPDF31_13TeV-powheg/200209_081311/0000/']
path_WW_2500toInf=['/pnfs/iihe/cms/store/user/amkalsi/2017_ReReco_DeepTau/WWTo2L2Nu_MLL_2500ToInf_NNPDF31_13TeV-powheg/crab_WWTo2L2Nu_MLL_2500ToInf_NNPDF31_13TeV-powheg/200209_081219/0000/']





path_WZ_2l2q=[
'/pnfs/iihe/cms/store/user/amkalsi/2017_ReReco_DeepTau/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/crab_WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/200209_081334/0000/',
'/pnfs/iihe/cms/store/user/amkalsi/2017_ReReco_DeepTau/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/crab_WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/200209_081334/0001/',
]

path_WZ_3lnu=[
'/pnfs/iihe/cms/store/user/amkalsi/2017_ReReco_DeepTau/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/crab_WZTo3LNu_TuneCP5_13TeV/200209_073621/0000/',
]


path_ZZ_2l2nu=[
'/pnfs/iihe/cms/store/user/amkalsi/2017_ReReco_DeepTau/ZZTo2L2Nu_13TeV_powheg_pythia8/crab_ZZTo2L2Nu_13TeV_powheg_pythia8/200209_081427/0000/',
]

path_ZZ_2l2q=[
'/pnfs/iihe/cms/store/user/amkalsi/2017_ReReco_DeepTau/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/crab_ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/200209_081400/0000/',
'/pnfs/iihe/cms/store/user/amkalsi/2017_ReReco_DeepTau/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/crab_ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/200209_081400/0001/',
]

path_ZZ_4l=[
'/pnfs/iihe/cms/store/user/amkalsi/2017_ReReco_DeepTau/ZZTo4L_13TeV_powheg_pythia8/crab_ZZTo4L_13TeV_powheg_pythia8/200209_073556/0000/',
]

################################## ST ###################
path_ST=[
'/pnfs/iihe/cms/store/user/amkalsi/2017_ReReco_DeepTau/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/crab_ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV/200209_073502/0000/',
'/pnfs/iihe/cms/store/user/amkalsi/2017_ReReco_DeepTau/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/crab_ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV/200209_073527/0000/',
]


####################################### TTbar ####################
path_TT_2l2nu=[
'/pnfs/iihe/cms/store/user/amkalsi/2017_ReReco_DeepTau/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/crab_TTTo2L2Nu_TuneCP5_13TeV/200209_073434/0000/',
]

path_TT_500to800_0_20=[
'/pnfs/iihe/cms/store/user/amkalsi/2017_ReReco_DeepTau/TTToLL_MLL_500To800_0to20_NNPDF31_13TeV-powheg/crab_TTToLL_MLL_500To800_0to20_NNPDF31_13TeV-powheg/200209_080951/0000/',
]                 
                  
path_TT_500to800_41_65=[
'/pnfs/iihe/cms/store/user/amkalsi/2017_ReReco_DeepTau/TTToLL_MLL_500To800_41to65_NNPDF31_13TeV-powheg/crab_TTToLL_MLL_500To800_41to65_NNPDF31_13TeV-powheg/200209_080928/0000/',
]

path_TT_800to1200=[
'/pnfs/iihe/cms/store/user/amkalsi/2017_ReReco_DeepTau/TTToLL_MLL_800To1200_NNPDF31_13TeV-powheg/crab_TTToLL_MLL_800To1200_NNPDF31_13TeV-powheg/200209_080902/0000/',
]                 
                  
path_TT_1200to1800=[
'/pnfs/iihe/cms/store/user/amkalsi/2017_ReReco_DeepTau/TTToLL_MLL_1200To1800_NNPDF31_13TeV-powheg/crab_TTToLL_MLL_1200To1800_NNPDF31_13TeV-powheg/200209_081039/0000/',
]                 
                  
path_TT_1800toInf=[
'/pnfs/iihe/cms/store/user/amkalsi/2017_ReReco_DeepTau/TTToLL_MLL_1800ToInf_NNPDF31_13TeV-powheg/crab_TTToLL_MLL_1800ToInf_NNPDF31_13TeV-powheg/200209_081015/0000/',
]






path_WJets_inc = [ 
"/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/crab_WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_v1/200303_174251/0000/",
"/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/crab_WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_v2/200303_174340/0000/",
"/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/crab_WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_v3/200303_174314/0000/",
]                  
path_WJets_50to100 = ["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/WJetsToLNu_Pt-50To100_TuneCP5_13TeV-amcatnloFXFX-pythia8/crab_WJetsToLNu_Pt-50To100_TuneCP5_13TeV-amcatnloFXFX-pythia8/200303_174231/0000/"]
path_WJets_100to250 = [
"/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/WJetsToLNu_Pt-100To250_TuneCP5_13TeV-amcatnloFXFX-pythia8/crab_WJetsToLNu_Pt-100To250_TuneCP5_13TeV-amcatnloFXFX-pythia8/200303_174418/0000/",
"/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/WJetsToLNu_Pt-100To250_TuneCP5_13TeV-amcatnloFXFX-pythia8/crab_WJetsToLNu_Pt-100To250_TuneCP5_13TeV-amcatnloFXFX-pythia8/200303_174418/0001/",
]                  
path_WJets_250to400 = ["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/WJetsToLNu_Pt-250To400_TuneCP5_13TeV-amcatnloFXFX-pythia8/crab_WJetsToLNu_Pt-250To400_TuneCP5_13TeV-amcatnloFXFX-pythia8/200303_174458/0000/"]
path_WJets_400to600 = ["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/WJetsToLNu_Pt-400To600_TuneCP5_13TeV-amcatnloFXFX-pythia8/crab_WJetsToLNu_Pt-400To600_TuneCP5_13TeV-amcatnloFXFX-pythia8/200303_174208/0000/"]
path_WJets_600toInf = ["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/WJetsToLNu_Pt-600ToInf_TuneCP5_13TeV-amcatnloFXFX-pythia8/crab_WJetsToLNu_Pt-600ToInf_TuneCP5_13TeV-amcatnloFXFX-pythia8/200303_174359/0000/"]



path_QCDMu_30to50   = ["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/QCD_Pt-30to50_MuEnrichedPt5_TuneCP5_13TeV_pythia8/crab_QCD_Pt-30to50_MuEnrichedPt5_TuneCP5_13TeV_pythia8/200911_164117/0000/",
                       "/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/QCD_Pt-30to50_MuEnrichedPt5_TuneCP5_13TeV_pythia8/crab_QCD_Pt-30to50_MuEnrichedPt5_TuneCP5_13TeV_pythia8/200911_164117/0001/",
                      ]
path_QCDMu_50to80   = ["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/QCD_Pt-50to80_MuEnrichedPt5_TuneCP5_13TeV_pythia8/crab_QCD_Pt-50to80_MuEnrichedPt5_TuneCP5_13TeV_pythia8/200911_164019/0000/",
                       "/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/QCD_Pt-50to80_MuEnrichedPt5_TuneCP5_13TeV_pythia8/crab_QCD_Pt-50to80_MuEnrichedPt5_TuneCP5_13TeV_pythia8/200911_164019/0001/",
                      ]
path_QCDMu_80to120  = ["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/QCD_Pt-80to120_MuEnrichedPt5_TuneCP5_13TeV_pythia8/crab_QCD_Pt-80to120_MuEnrichedPt5_TuneCP5_13TeV_pythia8/200911_164202/0000/",
                       "/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/QCD_Pt-80to120_MuEnrichedPt5_TuneCP5_13TeV_pythia8/crab_QCD_Pt-80to120_MuEnrichedPt5_TuneCP5_13TeV_pythia8/200911_164202/0001/",
                      ]
path_QCDMu_120to170 = ["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8/crab_QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8/200911_163931/0000/",
                       "/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8/crab_QCD_Pt-120to170_MuEnrichedPt5_TuneCP5_13TeV_pythia8/200911_163931/0001/",
                      ]
path_QCDMu_170to300 = ["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/QCD_Pt-170to300_MuEnrichedPt5_TuneCP5_13TeV_pythia8/crab_QCD_Pt-170to300_MuEnrichedPt5_TuneCP5_13TeV_pythia8/200911_164133/0000/",
                       "/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/QCD_Pt-170to300_MuEnrichedPt5_TuneCP5_13TeV_pythia8/crab_QCD_Pt-170to300_MuEnrichedPt5_TuneCP5_13TeV_pythia8/200911_164133/0001/",
                       "/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/QCD_Pt-170to300_MuEnrichedPt5_TuneCP5_13TeV_pythia8/crab_QCD_Pt-170to300_MuEnrichedPt5_TuneCP5_13TeV_pythia8/200911_164133/0002/",
                      ]
path_QCDMu_300to470 = ["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8/crab_QCD_Pt-300to470_MuEnrichedPt5_TuneCP5_13TeV_pythia8/200911_164001/0000/"]
path_QCDMu_470to600 = ["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8/crab_QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8/200911_164103/0000/",
                       "/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8/crab_QCD_Pt-470to600_MuEnrichedPt5_TuneCP5_13TeV_pythia8/200911_164103/0001/",
                      ]
path_QCDMu_600to800 = ["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/QCD_Pt-600to800_MuEnrichedPt5_TuneCP5_13TeV_pythia8/crab_QCD_Pt-600to800_MuEnrichedPt5_TuneCP5_13TeV_pythia8/200911_164048/0000/"]
path_QCDMu_800to1000 =["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/QCD_Pt-800to1000_MuEnrichedPt5_TuneCP5_13TeV_pythia8/crab_QCD_Pt-800to1000_MuEnrichedPt5_TuneCP5_13TeV_pythia8/200911_163916/0000/"]
path_QCDMu_1000toInf  = ["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/QCD_Pt-1000toInf_MuEnrichedPt5_TuneCP5_13TeV_pythia8/crab_QCD_Pt-1000toInf_MuEnrichedPt5_TuneCP5_13TeV_pythia8/201002_095700/0000/"]
                    
path_QCDEM_30to50   = ["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/QCD_Pt-30to50_EMEnriched_TuneCP5_13TeV_pythia8/crab_QCD_Pt-30to50_EMEnriched_TuneCP5_13TeV_pythia8/200911_163946/0000/"]
path_QCDEM_50to80   = ["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/QCD_Pt-50to80_EMEnriched_TuneCP5_13TeV_pythia8/crab_QCD_Pt-50to80_EMEnriched_TuneCP5_13TeV_pythia8/200911_163901/0000/"]
path_QCDEM_80to120  = ["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/QCD_Pt-80to120_EMEnriched_TuneCP5_13TeV_pythia8/crab_QCD_Pt-80to120_EMEnriched_TuneCP5_13TeV_pythia8/200911_164147/0000/"]
path_QCDEM_120to170 = ["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/QCD_Pt-120to170_EMEnriched_TuneCP5_13TeV_pythia8/crab_QCD_Pt-120to170_EMEnriched_TuneCP5_13TeV_pythia8/200911_164034/0000/"]
path_QCDEM_170to300 = ["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/QCD_Pt-170to300_EMEnriched_TuneCP5_13TeV_pythia8/crab_QCD_Pt-170to300_EMEnriched_TuneCP5_13TeV_pythia8/200911_163844/0000/"]
path_QCDEM_300toInf  = ["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/QCD_Pt-300toInf_EMEnriched_TuneCP5_13TeV_pythia8/crab_QCD_Pt-300toInf_EMEnriched_TuneCP5_13TeV_pythia8/201002_095628/0000/"]


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


path_QBH_200=["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/QBHtoMuTau_n4_ADD_M200_TuneCP5_13TeV-QBH-pythia8/crab_QBHtoMuTau_n4_ADD_M200_TuneCP5_13TeV-QBH-pythia8/200213_114200/0000/"]
path_QBH_400=["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/QBHtoMuTau_n4_ADD_M400_TuneCP5_13TeV-QBH-pythia8/crab_QBHtoMuTau_n4_ADD_M400_TuneCP5_13TeV-QBH-pythia8/200213_112015/0000/"]
path_QBH_600=["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/QBHtoMuTau_n4_ADD_M600_TuneCP5_13TeV-QBH-pythia8/crab_QBHtoMuTau_n4_ADD_M600_TuneCP5_13TeV-QBH-pythia8/200213_110902/0000/"]
path_QBH_800=["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/QBHtoMuTau_n4_ADD_M800_TuneCP5_13TeV-QBH-pythia8/crab_QBHtoMuTau_n4_ADD_M800_TuneCP5_13TeV-QBH-pythia8/200213_111045/0000/"]
path_QBH_1000=["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/QBHtoMuTau_n4_ADD_M1000_TuneCP5_13TeV-QBH-pythia8/crab_QBHtoMuTau_n4_ADD_M1000_TuneCP5_13TeV-QBH-pythia8/200213_111633/0000/"]
path_QBH_1200=["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/QBHtoMuTau_n4_ADD_M1200_TuneCP5_13TeV-QBH-pythia8/crab_QBHtoMuTau_n4_ADD_M1200_TuneCP5_13TeV-QBH-pythia8/200213_113153/0000/"]
path_QBH_1400=["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/QBHtoMuTau_n4_ADD_M1400_TuneCP5_13TeV-QBH-pythia8/crab_QBHtoMuTau_n4_ADD_M1400_TuneCP5_13TeV-QBH-pythia8/200213_110454/0000/"]
path_QBH_1600=["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/QBHtoMuTau_n4_ADD_M1600_TuneCP5_13TeV-QBH-pythia8/crab_QBHtoMuTau_n4_ADD_M1600_TuneCP5_13TeV-QBH-pythia8/200213_111012/0000/"]
path_QBH_1800=["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/QBHtoMuTau_n4_ADD_M1800_TuneCP5_13TeV-QBH-pythia8/crab_QBHtoMuTau_n4_ADD_M1800_TuneCP5_13TeV-QBH-pythia8/200213_114228/0000/"]
path_QBH_2000=["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/QBHtoMuTau_n4_ADD_M2000_TuneCP5_13TeV-QBH-pythia8/crab_QBHtoMuTau_n4_ADD_M2000_TuneCP5_13TeV-QBH-pythia8/200213_105446/0000/"]
path_QBH_2500=["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/QBHtoMuTau_n4_ADD_M2500_TuneCP5_13TeV-QBH-pythia8/crab_QBHtoMuTau_n4_ADD_M2500_TuneCP5_13TeV-QBH-pythia8/200213_110720/0000/"]
path_QBH_3000=["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/QBHtoMuTau_n4_ADD_M3000_TuneCP5_13TeV-QBH-pythia8/crab_QBHtoMuTau_n4_ADD_M3000_TuneCP5_13TeV-QBH-pythia8/200213_105320/0000/"]
path_QBH_3500=["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/QBHtoMuTau_n4_ADD_M3500_TuneCP5_13TeV-QBH-pythia8/crab_QBHtoMuTau_n4_ADD_M3500_TuneCP5_13TeV-QBH-pythia8/200213_105735/0000/"]
path_QBH_4000=["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/QBHtoMuTau_n4_ADD_M4000_TuneCP5_13TeV-QBH-pythia8/crab_QBHtoMuTau_n4_ADD_M4000_TuneCP5_13TeV-QBH-pythia8/200213_111343/0000/"]
path_QBH_4500=["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/QBHtoMuTau_n4_ADD_M4500_TuneCP5_13TeV-QBH-pythia8/crab_QBHtoMuTau_n4_ADD_M4500_TuneCP5_13TeV-QBH-pythia8/200213_105803/0000/"]
path_QBH_5000=["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/QBHtoMuTau_n4_ADD_M5000_TuneCP5_13TeV-QBH-pythia8/crab_QBHtoMuTau_n4_ADD_M5000_TuneCP5_13TeV-QBH-pythia8/200213_112850/0000/"]
path_QBH_6000=["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/QBHtoMuTau_n4_ADD_M6000_TuneCP5_13TeV-QBH-pythia8/crab_QBHtoMuTau_n4_ADD_M6000_TuneCP5_13TeV-QBH-pythia8/200213_111705/0000/"]
path_QBH_7000=["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/QBHtoMuTau_n4_ADD_M7000_TuneCP5_13TeV-QBH-pythia8/crab_QBHtoMuTau_n4_ADD_M7000_TuneCP5_13TeV-QBH-pythia8/200213_111525/0000/"]
path_QBH_8000=["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/QBHtoMuTau_n4_ADD_M8000_TuneCP5_13TeV-QBH-pythia8/crab_QBHtoMuTau_n4_ADD_M8000_TuneCP5_13TeV-QBH-pythia8/200213_114358/0000/"]
path_QBH_9000=["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/QBHtoMuTau_n4_ADD_M9000_TuneCP5_13TeV-QBH-pythia8/crab_QBHtoMuTau_n4_ADD_M9000_TuneCP5_13TeV-QBH-pythia8/200213_110322/0000/"]
path_QBH_10000=["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/QBHtoMuTau_n4_ADD_M10000_TuneCP5_13TeV-QBH-pythia8/crab_QBHtoMuTau_n4_ADD_M10000_TuneCP5_13TeV-QBH-pythia8/200213_112626/0000/"]



path_RPV_l001_200=["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/RPVresonantToMuTau_M-200_LLE_LQD-001_TuneCP5_13TeV-calchep-pythia8/crab_RPVresonantToMuTau_M-200_LLE_LQD-001_TuneCP5_13TeV-calchep-pythia8/200213_111805/0000/"]
path_RPV_l001_300=["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/RPVresonantToMuTau_M-300_LLE_LQD-001_TuneCP5_13TeV-calchep-pythia8/crab_RPVresonantToMuTau_M-300_LLE_LQD-001_TuneCP5_13TeV-calchep-pythia8/200213_110352/0000/"]
path_RPV_l001_400=["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/RPVresonantToMuTau_M-400_LLE_LQD-001_TuneCP5_13TeV-calchep-pythia8/crab_RPVresonantToMuTau_M-400_LLE_LQD-001_TuneCP5_13TeV-calchep-pythia8/200213_105348/0000/"]
path_RPV_l001_600=["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/RPVresonantToMuTau_M-600_LLE_LQD-001_TuneCP5_13TeV-calchep-pythia8/crab_RPVresonantToMuTau_M-600_LLE_LQD-001_TuneCP5_13TeV-calchep-pythia8/200213_113353/0000/"]
path_RPV_l001_700=["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/RPVresonantToMuTau_M-700_LLE_LQD-001_TuneCP5_13TeV-calchep-pythia8/crab_RPVresonantToMuTau_M-700_LLE_LQD-001_TuneCP5_13TeV-calchep-pythia8/200213_105610/0000/"]
path_RPV_l001_800=["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/RPVresonantToMuTau_M-800_LLE_LQD-001_TuneCP5_13TeV-calchep-pythia8/crab_RPVresonantToMuTau_M-800_LLE_LQD-001_TuneCP5_13TeV-calchep-pythia8/200213_114257/0000/"]
path_RPV_l001_900=["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/RPVresonantToMuTau_M-900_LLE_LQD-001_TuneCP5_13TeV-calchep-pythia8/crab_RPVresonantToMuTau_M-900_LLE_LQD-001_TuneCP5_13TeV-calchep-pythia8/200213_110550/0000/"]
path_RPV_l001_1000=["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/RPVresonantToMuTau_M-1000_LLE_LQD-001_TuneCP5_13TeV-calchep-pythia8/crab_RPVresonantToMuTau_M-1000_LLE_LQD-001_TuneCP5_13TeV-calchep-pythia8/200213_110220/0000/"]
path_RPV_l001_1200=["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/RPVresonantToMuTau_M-1200_LLE_LQD-001_TuneCP5_13TeV-calchep-pythia8/crab_RPVresonantToMuTau_M-1200_LLE_LQD-001_TuneCP5_13TeV-calchep-pythia8/200213_113454/0000/"]
path_RPV_l001_1400=["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/RPVresonantToMuTau_M-1400_LLE_LQD-001_TuneCP5_13TeV-calchep-pythia8/crab_RPVresonantToMuTau_M-1400_LLE_LQD-001_TuneCP5_13TeV-calchep-pythia8/200213_105000/0000/"]
path_RPV_l001_1600=["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/RPVresonantToMuTau_M-1600_LLE_LQD-001_TuneCP5_13TeV-calchep-pythia8/crab_RPVresonantToMuTau_M-1600_LLE_LQD-001_TuneCP5_13TeV-calchep-pythia8/200213_111908/0000/"]
path_RPV_l001_1800=["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/RPVresonantToMuTau_M-1800_LLE_LQD-001_TuneCP5_13TeV-calchep-pythia8/crab_RPVresonantToMuTau_M-1800_LLE_LQD-001_TuneCP5_13TeV-calchep-pythia8/200213_112514/0000/"]
path_RPV_l001_2000=["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/RPVresonantToMuTau_M-2000_LLE_LQD-001_TuneCP5_13TeV-calchep-pythia8/crab_RPVresonantToMuTau_M-2000_LLE_LQD-001_TuneCP5_13TeV-calchep-pythia8/200213_112047/0000/"]
path_RPV_l001_2500=["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/RPVresonantToMuTau_M-2500_LLE_LQD-001_TuneCP5_13TeV-calchep-pythia8/crab_RPVresonantToMuTau_M-2500_LLE_LQD-001_TuneCP5_13TeV-calchep-pythia8/200213_114054/0000/"]
path_RPV_l001_3000=["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/RPVresonantToMuTau_M-3000_LLE_LQD-001_TuneCP5_13TeV-calchep-pythia8/crab_RPVresonantToMuTau_M-3000_LLE_LQD-001_TuneCP5_13TeV-calchep-pythia8/200213_111119/0000/"]
path_RPV_l01_3000=["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/RPVresonantToMuTau_M-3000_LLE_LQD-01_TuneCP5_13TeV-calchep-pythia8/crab_RPVresonantToMuTau_M-3000_LLE_LQD-01_TuneCP5_13TeV-calchep-pythia8/200213_112812/0000/"]
path_RPV_l001_3500=["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/RPVresonantToMuTau_M-3500_LLE_LQD-001_TuneCP5_13TeV-calchep-pythia8/crab_RPVresonantToMuTau_M-3500_LLE_LQD-001_TuneCP5_13TeV-calchep-pythia8/200213_113826/0000/"]
path_RPV_l01_3500=["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/RPVresonantToMuTau_M-3500_LLE_LQD-01_TuneCP5_13TeV-calchep-pythia8/crab_RPVresonantToMuTau_M-3500_LLE_LQD-01_TuneCP5_13TeV-calchep-pythia8/200213_113753/0000/"]
path_RPV_l001_4000=["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/RPVresonantToMuTau_M-4000_LLE_LQD-001_TuneCP5_13TeV-calchep-pythia8/crab_RPVresonantToMuTau_M-4000_LLE_LQD-001_TuneCP5_13TeV-calchep-pythia8/200213_105228/0000/"]
path_RPV_l01_4000=["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/RPVresonantToMuTau_M-4000_LLE_LQD-01_TuneCP5_13TeV-calchep-pythia8/crab_RPVresonantToMuTau_M-4000_LLE_LQD-01_TuneCP5_13TeV-calchep-pythia8/200213_104930/0000/"]
path_RPV_l02_4000=["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/RPVresonantToMuTau_M-4000_LLE_LQD-02_TuneCP5_13TeV-calchep-pythia8/crab_RPVresonantToMuTau_M-4000_LLE_LQD-02_TuneCP5_13TeV-calchep-pythia8/200213_110147/0000/"]
path_RPV_l05_4000=["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/RPVresonantToMuTau_M-4000_LLE_LQD-05_TuneCP5_13TeV-calchep-pythia8/crab_RPVresonantToMuTau_M-4000_LLE_LQD-05_TuneCP5_13TeV-calchep-pythia8/200213_114625/0000/"]
path_RPV_l001_4500=["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/RPVresonantToMuTau_M-4500_LLE_LQD-001_TuneCP5_13TeV-calchep-pythia8/crab_RPVresonantToMuTau_M-4500_LLE_LQD-001_TuneCP5_13TeV-calchep-pythia8/200213_111449/0000/"]
path_RPV_l02_4500=["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/RPVresonantToMuTau_M-4500_LLE_LQD-02_TuneCP5_13TeV-calchep-pythia8/crab_RPVresonantToMuTau_M-4500_LLE_LQD-02_TuneCP5_13TeV-calchep-pythia8/200213_110114/0000/"]
path_RPV_l05_4500=["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/RPVresonantToMuTau_M-4500_LLE_LQD-05_TuneCP5_13TeV-calchep-pythia8/crab_RPVresonantToMuTau_M-4500_LLE_LQD-05_TuneCP5_13TeV-calchep-pythia8/200213_114022/0000/"]
path_RPV_l001_5000=["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/RPVresonantToMuTau_M-5000_LLE_LQD-001_TuneCP5_13TeV-calchep-pythia8/crab_RPVresonantToMuTau_M-5000_LLE_LQD-001_TuneCP5_13TeV-calchep-pythia8/200213_111941/0000/"]
path_RPV_l02_5000=["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/RPVresonantToMuTau_M-5000_LLE_LQD-02_TuneCP5_13TeV-calchep-pythia8/crab_RPVresonantToMuTau_M-5000_LLE_LQD-02_TuneCP5_13TeV-calchep-pythia8/200213_112739/0000/"]
path_RPV_l05_5000=["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/RPVresonantToMuTau_M-5000_LLE_LQD-05_TuneCP5_13TeV-calchep-pythia8/crab_RPVresonantToMuTau_M-5000_LLE_LQD-05_TuneCP5_13TeV-calchep-pythia8/200213_110825/0000/"]
path_RPV_l001_5500=["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/RPVresonantToMuTau_M-5500_LLE_LQD-001_TuneCP5_13TeV-calchep-pythia8/crab_RPVresonantToMuTau_M-5500_LLE_LQD-001_TuneCP5_13TeV-calchep-pythia8/200213_114806/0000/"]
path_RPV_l02_5500=["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/RPVresonantToMuTau_M-5500_LLE_LQD-02_TuneCP5_13TeV-calchep-pythia8/crab_RPVresonantToMuTau_M-5500_LLE_LQD-02_TuneCP5_13TeV-calchep-pythia8/200213_113521/0000/"]
path_RPV_l05_5500=["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/RPVresonantToMuTau_M-5500_LLE_LQD-05_TuneCP5_13TeV-calchep-pythia8/crab_RPVresonantToMuTau_M-5500_LLE_LQD-05_TuneCP5_13TeV-calchep-pythia8/200213_113121/0000/"]
path_RPV_l02_6000=["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/RPVresonantToMuTau_M-6000_LLE_LQD-02_TuneCP5_13TeV-calchep-pythia8/crab_RPVresonantToMuTau_M-6000_LLE_LQD-02_TuneCP5_13TeV-calchep-pythia8/200213_114328/0000/"]
path_RPV_l05_6000=["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/RPVresonantToMuTau_M-6000_LLE_LQD-05_TuneCP5_13TeV-calchep-pythia8/crab_RPVresonantToMuTau_M-6000_LLE_LQD-05_TuneCP5_13TeV-calchep-pythia8/200213_105637/0000/"]
path_RPV_l001_6500=["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/RPVresonantToMuTau_M-6500_LLE_LQD-001_TuneCP5_13TeV-calchep-pythia8/crab_RPVresonantToMuTau_M-6500_LLE_LQD-001_TuneCP5_13TeV-calchep-pythia8/200213_113650/0000/"]
path_RPV_l02_6500=["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/RPVresonantToMuTau_M-6500_LLE_LQD-02_TuneCP5_13TeV-calchep-pythia8/crab_RPVresonantToMuTau_M-6500_LLE_LQD-02_TuneCP5_13TeV-calchep-pythia8/200213_110646/0000/"]
path_RPV_l05_6500=["/pnfs/iihe/cms/store/user/dbeghin/Legacy/DeepTau/2017/RPVresonantToMuTau_M-6500_LLE_LQD-05_TuneCP5_13TeV-calchep-pythia8/crab_RPVresonantToMuTau_M-6500_LLE_LQD-05_TuneCP5_13TeV-calchep-pythia8/200213_113256/0000/"]


#sample_path['WW_2l2nu']          =path_WW_2l2nu
#sample_path['WW_200to600']      =path_WW_200to600
#sample_path['WW_600to1200']      =path_WW_600to1200
#sample_path['WW_1200to2500']     =path_WW_1200to2500
#sample_path['WW_2500toInf']      =path_WW_2500toInf
#sample_path['WZ_2l2q']           =path_WZ_2l2q
#sample_path['WZ_3lnu']           =path_WZ_3lnu
#sample_path['ZZ_2l2q']           =path_ZZ_2l2q
#sample_path['ZZ_2l2nu']          =path_ZZ_2l2nu
#sample_path['ZZ_4l']             =path_ZZ_4l
#sample_path['ST']                =path_ST
#sample_path['DYToLL_amc']        =path_DYToLL_amc
#sample_path['DYToLL_100to200']   =path_DYToLL_100to200  
#sample_path['DYToLL_200to400']   =path_DYToLL_200to400  
#sample_path['DYToLL_400to500']   =path_DYToLL_400to500  
#sample_path['DYToLL_500to700']   =path_DYToLL_500to700  
#sample_path['DYToLL_700to800']   =path_DYToLL_700to800  
#sample_path['DYToLL_800to1000']  =path_DYToLL_800to1000 
#sample_path['DYToLL_1000to1500'] =path_DYToLL_1000to1500
#sample_path['DYToLL_1500to2000'] =path_DYToLL_1500to2000
#sample_path['DYToLL_2000to3000'] =path_DYToLL_2000to3000
#sample_path['DYToLL_3000toInf']  =path_DYToLL_3000toInf 
#sample_path['TT_2l2nu']      = path_TT_2l2nu       
#sample_path['TT_500to800_0-20']   = path_TT_500to800_0_20
#sample_path['TT_500to800_41-65']   = path_TT_500to800_41_65
#sample_path['TT_800to1200']  = path_TT_800to1200 
#sample_path['TT_1200to1800'] = path_TT_1200to1800
#sample_path['TT_1800toInf']  = path_TT_1800toInf 

#sample_path['WJetsToLNu']     = path_WJets

#sample_path['WJets_inc'] =      path_WJets_inc         
#sample_path['WJets_50to100'] =  path_WJets_50to100 
#sample_path['WJets_100to250'] = path_WJets_100to250
#sample_path['WJets_250to400'] = path_WJets_250to400
#sample_path['WJets_400to600'] = path_WJets_400to600
#sample_path['WJets_600toInf'] = path_WJets_600toInf



#sample_path['QCDMu_30to50'] = path_QCDMu_30to50   
#sample_path['QCDMu_50to80'] = path_QCDMu_50to80   
#sample_path['QCDMu_80to120'] = path_QCDMu_80to120  
#sample_path['QCDMu_120to170'] = path_QCDMu_120to170 
#sample_path['QCDMu_170to300'] = path_QCDMu_170to300 
#sample_path['QCDMu_300to470'] = path_QCDMu_300to470 
#sample_path['QCDMu_470to600'] = path_QCDMu_470to600 
#sample_path['QCDMu_600to800'] = path_QCDMu_600to800 
#sample_path['QCDMu_800to1000'] = path_QCDMu_800to1000
sample_path['QCDMu_1000toInf'] = path_QCDMu_1000toInf

#sample_path['QCDEM_30to50'] = path_QCDEM_30to50   
#sample_path['QCDEM_50to80'] = path_QCDEM_50to80   
#sample_path['QCDEM_80to120'] = path_QCDEM_80to120  
#sample_path['QCDEM_120to170'] = path_QCDEM_120to170 
#sample_path['QCDEM_170to300'] = path_QCDEM_170to300 
sample_path['QCDEM_300toInf'] = path_QCDEM_300toInf


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



#sample_path['QBH_200']   = path_QBH_200    
#sample_path['QBH_400']   = path_QBH_400  
#sample_path['QBH_600']   = path_QBH_600  
#sample_path['QBH_800']   = path_QBH_800  
#sample_path['QBH_1000']  = path_QBH_1000 
#sample_path['QBH_1200']  = path_QBH_1200 
#sample_path['QBH_1400']  = path_QBH_1400 
#sample_path['QBH_1600']  = path_QBH_1600 
#sample_path['QBH_1800']  = path_QBH_1800 
#sample_path['QBH_2000']  = path_QBH_2000 
#sample_path['QBH_2500']  = path_QBH_2500 
#sample_path['QBH_3000']  = path_QBH_3000 
#sample_path['QBH_3500']  = path_QBH_3500 
#sample_path['QBH_4000']  = path_QBH_4000 
#sample_path['QBH_4500']  = path_QBH_4500 
#sample_path['QBH_5000']  = path_QBH_5000 
#sample_path['QBH_6000']  = path_QBH_6000 
#sample_path['QBH_7000']  = path_QBH_7000 
#sample_path['QBH_8000']  = path_QBH_8000 
#sample_path['QBH_9000']  = path_QBH_9000 
#sample_path['QBH_10000'] = path_QBH_10000
#
#
#sample_path['RPV_l001_200']    = path_RPV_l001_200    
#sample_path['RPV_l001_300']    = path_RPV_l001_300 
#sample_path['RPV_l001_400']    = path_RPV_l001_400 
#sample_path['RPV_l001_600']    = path_RPV_l001_600 
#sample_path['RPV_l001_700']    = path_RPV_l001_700 
#sample_path['RPV_l001_800']    = path_RPV_l001_800 
#sample_path['RPV_l001_900']    = path_RPV_l001_900 
#sample_path['RPV_l001_1000']   = path_RPV_l001_1000
#sample_path['RPV_l001_1200']   = path_RPV_l001_1200
#sample_path['RPV_l001_1400']   = path_RPV_l001_1400
#sample_path['RPV_l001_1600']   = path_RPV_l001_1600
#sample_path['RPV_l001_1800']   = path_RPV_l001_1800
#sample_path['RPV_l001_2000']   = path_RPV_l001_2000
#sample_path['RPV_l001_2500']   = path_RPV_l001_2500
#sample_path['RPV_l001_3000']   = path_RPV_l001_3000
#sample_path['RPV_l01_3000']    = path_RPV_l01_3000 
#sample_path['RPV_l001_3500']   = path_RPV_l001_3500
#sample_path['RPV_l01_3500']    = path_RPV_l01_3500 
#sample_path['RPV_l001_4000']   = path_RPV_l001_4000
#sample_path['RPV_l01_4000']    = path_RPV_l01_4000 
#sample_path['RPV_l02_4000']    = path_RPV_l02_4000 
#sample_path['RPV_l05_4000']    = path_RPV_l05_4000 
#sample_path['RPV_l001_4500']   = path_RPV_l001_4500
#sample_path['RPV_l02_4500']    = path_RPV_l02_4500 
#sample_path['RPV_l05_4500']    = path_RPV_l05_4500 
#sample_path['RPV_l001_5000']   = path_RPV_l001_5000
#sample_path['RPV_l02_5000']    = path_RPV_l02_5000 
#sample_path['RPV_l05_5000']    = path_RPV_l05_5000 
#sample_path['RPV_l001_5500']   = path_RPV_l001_5500
#sample_path['RPV_l02_5500']    = path_RPV_l02_5500 
#sample_path['RPV_l05_5500']    = path_RPV_l05_5500 
#sample_path['RPV_l02_6000']    = path_RPV_l02_6000 
#sample_path['RPV_l05_6000']    = path_RPV_l05_6000 
#sample_path['RPV_l001_6500']   = path_RPV_l001_6500
#sample_path['RPV_l02_6500']    = path_RPV_l02_6500 
#sample_path['RPV_l05_6500']    = path_RPV_l05_6500 



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
