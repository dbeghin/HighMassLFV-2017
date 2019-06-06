#include <iostream>
#include <vector>
#include <utility>
#include <map>
#include <string>
#include "TH1.h"
#include "TH2.h"
#include "TFile.h"
#include "TMath.h"
#include "TSystem.h"
#include "TCanvas.h"
#include "TFrame.h"
#include "TLegend.h"
#include "THStack.h"
#include "TStyle.h"
#include "aux.h"

using namespace std;


TH1F* MC_histo(TString var, TFile* file_in, TFile* file_in_d, double xs, int rebin) {

  cout << file_in->GetName() << endl;

  TH1F* h_events_data = (TH1F*) file_in_d->Get("weighted_events");
  double full_data = 7.3968038e+08;
  double succ_data_ratio = h_events_data->Integral()/full_data;
  cout << "succesfull data ratio " << succ_data_ratio << endl;
  double lumi = 41.529 * pow(10,3) * succ_data_ratio; //luminosity in pb^-1                                                                                                                                 

  TH1F* h_events = (TH1F*) file_in->Get("weighted_events");
  double Nevents = h_events->Integral();

  double e_Nevents = pow(Nevents,0.5);
  double e_xs = 0.01*xs;

  //Weight                                                                                                                                                                                                  
  double w = 0;
  if (Nevents != 0) w = xs*lumi/Nevents;
  cout << "Events in data/events in MC " << w << endl;

  TH1F* h = (TH1F*) file_in -> Get(var);

  h -> Scale(w);
  h -> Rebin(rebin);

  return h;

}


TH2F* MC_histo_TH2(TString var, TFile* file_in, TFile* file_in_d, double xs, int rebin) {

  cout << file_in->GetName() << endl;

  TH1F* h_events_data = (TH1F*) file_in_d->Get("weighted_events");
  double full_data = 7.3968038e+08;
  double succ_data_ratio = h_events_data->Integral()/full_data;
  cout << "succesfull data ratio " << succ_data_ratio << endl;
  double lumi = 41.529 * pow(10,3) * succ_data_ratio; //luminosity in pb^-1                                                                                                                                 

  TH1F* h_events = (TH1F*) file_in->Get("weighted_events");
  double Nevents = h_events->Integral();

  double e_Nevents = pow(Nevents,0.5);
  double e_xs = 0.01*xs;

  //Weight                                                                                                                                                                                                  
  double w = 0;
  if (Nevents != 0) w = xs*lumi/Nevents;
  cout << "Events in data/events in MC " << w << endl;

  TH2F* h = (TH2F*) file_in -> Get(var);

  h -> Scale(w);
  h -> RebinX(rebin);
  h -> RebinY(rebin);

  return h;

}



int main(int argc, char** argv) {


  int rebin = 1;

  //TString folder_in = "HighMassLFVMuTau/FakeRate_SSMtLow";
  TString folder_in = "HighMassLFVMuTau/SignalRegion_CR100";
  TString name_out = "histos_fakerate_MtLow";

  TFile* file_out = new TFile("Figures/"+name_out+".root", "RECREATE");

  vector<TFile*> DY_files;
  DY_files.push_back( new TFile(folder_in+"/Arranged_DY/DY_inclusive.root", "R") );  
  DY_files.push_back( new TFile(folder_in+"/Arranged_DY/DY_400to500.root", "R") );   
  DY_files.push_back( new TFile(folder_in+"/Arranged_DY/DY_500to700.root", "R") );   
  DY_files.push_back( new TFile(folder_in+"/Arranged_DY/DY_700to800.root", "R") );   
  DY_files.push_back( new TFile(folder_in+"/Arranged_DY/DY_800to1000.root", "R") );  
  DY_files.push_back( new TFile(folder_in+"/Arranged_DY/DY_1000to1500.root", "R") ); 
  DY_files.push_back( new TFile(folder_in+"/Arranged_DY/DY_1500to2000.root", "R") ); 
  DY_files.push_back( new TFile(folder_in+"/Arranged_DY/DY_2000to3000.root", "R") ); 
  DY_files.push_back( new TFile(folder_in+"/Arranged_DY/DY_3000toInf.root", "R") );  


  vector<TFile*> TT_files;
  TT_files.push_back( new TFile(folder_in+"/Arranged_TT/TT_semilep.root", "R") ); //semilep
  TT_files.push_back( new TFile(folder_in+"/Arranged_TT/TT_had.root", "R") ); //had
  TT_files.push_back( new TFile(folder_in+"/Arranged_TT/TT_2l2nu.root", "R") ); //2l2nu
  TT_files.push_back( new TFile(folder_in+"/Arranged_TT/TT_500to800.root", "R") );   
  TT_files.push_back( new TFile(folder_in+"/Arranged_TT/TT_800to1200.root", "R") );  
  TT_files.push_back( new TFile(folder_in+"/Arranged_TT/TT_1200to1800.root", "R") ); 
  TT_files.push_back( new TFile(folder_in+"/Arranged_TT/TT_1800toInf.root", "R") );  
  

  vector<TFile*> WW_files;
  WW_files.push_back( new TFile(folder_in+"/Arranged_WW/WW_inclusive.root", "R") );  
  WW_files.push_back( new TFile(folder_in+"/Arranged_WW/WW_600to1200.root", "R") );  
  WW_files.push_back( new TFile(folder_in+"/Arranged_WW/WW_1200to2500.root", "R") ); 
  WW_files.push_back( new TFile(folder_in+"/Arranged_WW/WW_2500toInf.root", "R") );

  TFile* file_in_WZ = new TFile(folder_in+"/Arranged_WZ/WZ.root", "R");
  TFile* file_in_ZZ = new TFile(folder_in+"/Arranged_ZZ/ZZ.root", "R");

  TFile* file_in_ST = new TFile(folder_in+"/Arranged_ST/ST.root", "R");

  TFile* file_in_data = new TFile(folder_in+"/Arranged_data/data.root", "R");
  

  vector<TString> vars_TH2;
  vars_TH2.push_back("taupt_ratio_pass");
  vars_TH2.push_back("taupt_ratio_fail");

  vector<TString> Mth;
  Mth.push_back("MtLow_OS");
  Mth.push_back("MtLow_SS");

  
  vector<TString> systs;
  systs.push_back("nominal");

  vector<TString> systs_aux = GetSys();
  for (unsigned int iAux=0; iAux<systs_aux.size(); ++iAux) {
    systs.push_back(systs_aux[iAux]+"_up");
    systs.push_back(systs_aux[iAux]+"_down");
  }

  vector<TString> eta;
  eta.push_back("barrel");
  eta.push_back("endcap");

  vector<TString> taun;
  taun.push_back("realtau");
  //taun.push_back("faketau");


  //cross-sections
  //6225.4/5941 = 1.048 factor from NLO to NNLO
  float kNNLO = 1.048;

  vector<double> xs_DY;
  double xs_DY_lowmass   = 6225.4;           xs_DY.push_back(xs_DY_lowmass);   
  double xs_DY_400to500  = kNNLO*0.4065;     xs_DY.push_back(xs_DY_400to500);  
  double xs_DY_500to700  = kNNLO*0.2334;     xs_DY.push_back(xs_DY_500to700);  
  double xs_DY_700to800  = kNNLO*0.03614;    xs_DY.push_back(xs_DY_700to800);  
  double xs_DY_800to1000 = kNNLO*0.03047;    xs_DY.push_back(xs_DY_800to1000); 
  double xs_DY_1000to1500= kNNLO*0.01636;    xs_DY.push_back(xs_DY_1000to1500);
  double xs_DY_1500to2000= kNNLO*0.00218;    xs_DY.push_back(xs_DY_1500to2000);
  double xs_DY_2000to3000= kNNLO*0.0005156;  xs_DY.push_back(xs_DY_2000to3000);
  double xs_DY_3000toInf = kNNLO*0.0005156;  xs_DY.push_back(xs_DY_3000toInf);


  vector<double> xs_TT;
  xs_TT.push_back(831.76*0.438); //semilep
  xs_TT.push_back(831.76*0.457); //had
  xs_TT.push_back(831.76*0.105); //2l2nu
  double xs_TT_500to800 = 0.319;             xs_TT.push_back(xs_TT_500to800);
  double xs_TT_800to1200 = 3.196e-2;         xs_TT.push_back(xs_TT_800to1200);
  double xs_TT_1200to1800 = 2.987e-3;        xs_TT.push_back(xs_TT_1200to1800);
  double xs_TT_1800toInf = 1.711e-4;         xs_TT.push_back(xs_TT_1800toInf);

  vector<double> xs_WW;
  double xs_WW_lowm = 12.178;                xs_WW.push_back(xs_WW_lowm);
  //double xs_WW_200to600 = 1.39;              xs_WW.push_back(xs_WW_200to600); 
  double xs_WW_600to1200 = 5.7e-2;	     xs_WW.push_back(xs_WW_600to1200); 
  double xs_WW_1200to2500 = 3.6e-3;	     xs_WW.push_back(xs_WW_1200to2500); 
  double xs_WW_2500toInf = 5.4e-5;           xs_WW.push_back(xs_WW_2500toInf); 

  double xs_ST = 38.09;
  double xs_WZ = 22.82;
  double xs_ZZ = 10.32;
  double xs_signal = 20;

  TString var_in, var_out;

  file_out->cd();
  for (unsigned int i = 0; i<vars_TH2.size(); ++i) {
    for (unsigned int m = 0; m<Mth.size(); ++m) {
      for (unsigned int j = 0; j<systs.size(); ++j) {
        for (unsigned int k = 0; k<eta.size(); ++k) {
          for (unsigned int l = 0; l<taun.size(); ++l) {
            var_in = vars_TH2[i]+"_"+systs[j]+"_"+Mth[m]+"_"+eta[k]+"_"+taun[l];
	    var_out = var_in;
	    
	    cout << endl << endl <<var_in << endl;
            
	    vector<TH2F*> h_DY_vector;
	    for (unsigned int iBin = 0; iBin<DY_files.size(); ++iBin) {
	      h_DY_vector.push_back( MC_histo_TH2(var_in, DY_files[iBin], file_in_data, xs_DY[iBin], rebin) ); 
	    }
	    TH2F* h_DY = (TH2F*) h_DY_vector[0]->Clone("DY_"+var_out);
	    for (unsigned int iBin = 1; iBin<DY_files.size(); ++iBin) {
	      h_DY->Add(h_DY_vector[iBin]);
	    }
	    h_DY->Write();
	    delete h_DY;
	    for (unsigned int iBin = 0; iBin<DY_files.size(); ++iBin) delete h_DY_vector[iBin];

	    vector<TH2F*> h_TT_vector;
	    for (unsigned int iBin = 0; iBin<TT_files.size(); ++iBin) {
	      h_TT_vector.push_back( MC_histo_TH2(var_in, TT_files[iBin], file_in_data, xs_TT[iBin], rebin) ); 
	    }
	    TH2F* h_TT = (TH2F*) h_TT_vector[0]->Clone("TT_"+var_out);
	    for (unsigned int iBin = 1; iBin<h_TT_vector.size(); ++iBin) {
	      h_TT->Add(h_TT_vector[iBin]);
	    }
	    h_TT->Write();
	    delete h_TT;
	    for (unsigned int iBin = 0; iBin<TT_files.size(); ++iBin) delete h_TT_vector[iBin];
            
	    vector<TH2F*> h_WW_vector;
	    for (unsigned int iBin = 0; iBin<WW_files.size(); ++iBin) {
	      h_WW_vector.push_back( MC_histo_TH2(var_in, WW_files[iBin], file_in_data, xs_WW[iBin], rebin) ); 
	    }
	    TH2F* h_WW = (TH2F*) h_WW_vector[0]->Clone("WW_"+var_out);
	    for (unsigned int iBin = 1; iBin<h_WW_vector.size(); ++iBin) {
	      h_WW->Add(h_WW_vector[iBin]);
	    }
            
	    TH2F* h_WZ = MC_histo_TH2(var_in, file_in_WZ, file_in_data, xs_WZ, rebin);
	    TH2F* h_ZZ = MC_histo_TH2(var_in, file_in_ZZ, file_in_data, xs_ZZ, rebin);
	    TH2F* h_VV = (TH2F*) h_WW->Clone("VV_"+var_out);
	    h_VV->Add(h_WZ);
	    h_VV->Add(h_ZZ);
	    h_VV->Write();
	    delete h_WW;
	    delete h_WZ;
	    delete h_ZZ;
	    delete h_VV;
	    for (unsigned int iBin = 0; iBin<WW_files.size(); ++iBin) delete h_WW_vector[iBin];
            
	    TH2F* h_ST = MC_histo_TH2(var_in, file_in_ST, file_in_data, xs_ST, rebin);
	    h_ST->SetName("ST_"+var_out);
	    h_ST->Write();
	    delete h_ST;
	    
	    cout << "a" << endl;
	    TH2F* h_data = (TH2F*) file_in_data -> Get(var_in);//Data is, by definition, normalized
	    cout << "b" << endl;
	    h_data -> SetName("data_"+var_out);
	    cout << "c" << endl;
	    h_data->RebinX(rebin);
	    h_data->RebinY(rebin);
	    h_data->Write();
	    cout << "d" << endl;
	    delete h_data;
	  }
	}
      }
    }
  }
  file_out->Close();


  return 0;
}
