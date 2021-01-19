#include <iostream>
#include <vector>
#include <utility>
#include <map>
#include <string>
#include "TH1.h"
#include "TH2.h"
#include "TH3.h"
#include "TFile.h"
#include "TMath.h"
#include "TSystem.h"
#include "TCanvas.h"
#include "TFrame.h"
#include "TLegend.h"
#include "THStack.h"
#include "TStyle.h"

using namespace std;
void Normalise(TH1D* h) {
  double weighted_sum = 0, norm_factor = 0;
  for (unsigned int iBin=1; iBin<h->GetNbinsX()+1; ++iBin) {
    double bin_content = h->GetBinContent(iBin);
    double bin_error = h->GetBinError(iBin);

    weighted_sum += 1/pow(bin_error, 2) * bin_content;
    norm_factor += 1/pow(bin_error, 2);
  }
  double av_fr = weighted_sum/norm_factor;
  h->Scale(1./av_fr);
  cout << av_fr << endl;
}



int main(/*int argc, char** argv*/) {
  TFile* file_out = new TFile("HighMassLFVMuTau/fakerate_factorised_OSvsSSmystery.root", "RECREATE");
  //TFile* file_out = new TFile("HighMassLFVMuTau/fakerate_factorised_OSvsSSmystery_SS.root", "RECREATE");
  //TFile* file_out = new TFile("HighMassLFVMuTau/fakerate_factorised_OSvsSSmystery_OS.root", "RECREATE");
  TFile* file_in  = new TFile("Figures/histos_fakerate_OSvsSSmystery.root", "R");

  vector<TString> names;
  names.push_back("WJets_");

  vector<TString> vars,                                 vars_out,		          vars_out2,		             vars_out3;		    
  vars.push_back("tauPt_chHadFrac_neutHadFrac_pass");   vars_out.push_back("TauPt");      vars_out2.push_back("ChHadFrac");  vars_out3.push_back("NeutHadFrac");
  vars.push_back("taupt_chHadFrac_neutHadFrac_fail");   vars_out.push_back("denh1");	  vars_out2.push_back("dench1");     vars_out3.push_back("dencch1");
  vars.push_back("chEmFrac_muonFrac_neutEmFrac_pass");  vars_out.push_back("ChEmFrac");   vars_out2.push_back("MuonFrac");   vars_out3.push_back("NeutEmFrac");
  vars.push_back("chEmFrac_muonFrac_neutEmFrac_fail");  vars_out.push_back("denh2");	  vars_out2.push_back("dench2");     vars_out3.push_back("dencch2");

  vector<vector<TString>> vars_out_tot;
  vars_out_tot.push_back(vars_out);
  vars_out_tot.push_back(vars_out2);
  vars_out_tot.push_back(vars_out3);

  vector<TString> flavor;
  flavor.push_back("down");
  flavor.push_back("up");
  flavor.push_back("strange");
  flavor.push_back("charm");
  flavor.push_back("bottom");
  flavor.push_back("gluon");


  vector<TString> muonCharge;
  muonCharge.push_back("MuPlus");
  muonCharge.push_back("MuMinus");


  vector<TString> DM;
  DM.push_back("DM0");
  DM.push_back("DM1");
  DM.push_back("DM10");
  DM.push_back("DM11");

  vector<TString> eta;
  eta.push_back("barrel");
  eta.push_back("endcap");

  //vector<float> xpoints_taupt {0, 30, 50, 100, 500};
  vector<float> xpoints_taupt {0, 30, 500};
  vector<float> xpoints_frac {0, 0.04, 0.1, 0.3, 0.5, 0.8, 1.};
  vector<float> xpoints_muonfrac {0, 0.02, 0.06, 0.2, 0.4, 1.};

  vector<TH3D*> h[names.size()][vars.size()][flavor.size()][DM.size()][muonCharge.size()];
  for (unsigned int j=0; j<names.size(); ++j) {
    for (unsigned int k=0; k<vars.size(); ++k) { 
      for (unsigned int l=0; l<flavor.size(); ++l) {
	for (unsigned int dd=0; dd<DM.size(); ++dd) {
	  for (unsigned int nn=0; nn<muonCharge.size(); ++nn) {
	    for (unsigned int m=0; m<eta.size(); ++m) {
	      TString name_in = names[j]+vars[k]+"_nominal_MtLow_SS_"+eta[m]+"_"+flavor[l]+"_"+DM[dd]+"_"+muonCharge[nn];
	      //TString name_in = names[j]+vars[k]+"_nominal_MtLow_OS_"+eta[m]+"_"+flavor[l]+"_"+DM[dd]+"_"+muonCharge[nn];
	      h[j][k][l][dd][nn].push_back( (TH3D*) file_in->Get(name_in) );
	      h[j][k][l][dd][nn][m]->SetName(names[j]+vars[k]+"_"+eta[m]+"_"+flavor[l]+"_"+DM[dd]+"_"+muonCharge[nn]);
	      name_in = names[j]+vars[k]+"_nominal_MtLow_OS_"+eta[m]+"_"+flavor[l]+"_"+DM[dd]+"_"+muonCharge[nn];
	      TH3D* htemp = (TH3D*) file_in->Get(name_in);
	      h[j][k][l][dd][nn][m]->Add(htemp);
	      delete htemp;
	    }
	  }
	}
      }
    }
  }


  vector<TH3D*> h_MC[vars.size()];
  for (unsigned int k=0; k<vars.size(); ++k) {
    for (unsigned int l=0; l<flavor.size(); ++l) {
      for (unsigned int dd=0; dd<DM.size(); ++dd) {
	for (unsigned int nn=0; nn<muonCharge.size(); ++nn) {
	  for (unsigned int m=0; m<eta.size(); ++m) {
	    TString name_in = vars[k]+"_"+eta[m]+"_"+flavor[l]+"_"+DM[dd]+"_"+muonCharge[nn];
	    h_MC[k].push_back( (TH3D*) h[0][k][l][dd][nn][m]->Clone("MC_"+name_in) );
	  }
	}
      }
    }
  }



  //data
  int half_var = vars.size()/2;//even->pass, odd->fail
  vector<TH1D*> hpass_MC[half_var][h_MC[0].size()];
  vector<TH1D*> hfail_MC[half_var][h_MC[0].size()];

  vector<TH1D*> hpass_MC_flavor[half_var][flavor.size()];
  vector<TH1D*> hfail_MC_flavor[half_var][flavor.size()];

  vector<TH1D*> hpass_MC_flavor_DM[half_var][flavor.size()][DM.size()];
  vector<TH1D*> hfail_MC_flavor_DM[half_var][flavor.size()][DM.size()];

  vector<TH1D*> hpass_MC_flavor_muonCharge[half_var][flavor.size()][muonCharge.size()];
  vector<TH1D*> hfail_MC_flavor_muonCharge[half_var][flavor.size()][muonCharge.size()];

  vector<TH1D*> hpass_MC_muonCharge[half_var][muonCharge.size()];
  vector<TH1D*> hfail_MC_muonCharge[half_var][muonCharge.size()];

  vector<TH1D*> hpass_MC_muonCharge_DM[half_var][muonCharge.size()][DM.size()];
  vector<TH1D*> hfail_MC_muonCharge_DM[half_var][muonCharge.size()][DM.size()];

  vector<TH1D*> hpass_MC_total[half_var];
  vector<TH1D*> hfail_MC_total[half_var];
  for (unsigned int k=0; k<vars.size(); ++k) {
    for (unsigned int i=0; i<h_MC[k].size(); ++i) {
      int l = i/(DM.size()*muonCharge.size()*eta.size()), dd = (i % (DM.size()*muonCharge.size()*eta.size()))/(muonCharge.size()*eta.size()), nn = (i % (muonCharge.size()*eta.size()))/eta.size(), m = i % eta.size();

      vector<float> xxpoints, yypoints, zzpoints;
      xxpoints.clear(), yypoints.clear(), zzpoints.clear();
      if (k<2) xxpoints = xpoints_taupt;
      else xxpoints = xpoints_frac;
      yypoints = xpoints_frac;
      if (k>=2) yypoints = xpoints_muonfrac;
      zzpoints = xpoints_frac;

      int array_size_x = xxpoints.size();
      float rebin_array_x[array_size_x];
      for (unsigned int iVector=0; iVector<array_size_x; ++iVector) rebin_array_x[iVector] = xxpoints[iVector];
      int array_size_y = yypoints.size();
      float rebin_array_y[array_size_y];
      for (unsigned int iVector=0; iVector<array_size_y; ++iVector) rebin_array_y[iVector] = yypoints[iVector];
      int array_size_z = zzpoints.size();
      float rebin_array_z[array_size_z];
      for (unsigned int iVector=0; iVector<array_size_z; ++iVector) rebin_array_z[iVector] = zzpoints[iVector];

      int half_k = k/2;
        
      //even->pass, odd->fail
      
      for (unsigned int iName=0; iName<vars_out_tot.size(); ++iName) {
	if (k%2 == 0) {
	  TString name_in = vars_out_tot[iName][k]+"_"+eta[m]+"_"+flavor[l]+"_"+DM[dd]+"_"+muonCharge[nn];
	  if (iName == 0) hpass_MC[half_k][i].push_back( new TH1D(name_in, name_in, array_size_x-1, rebin_array_x) );
	  else if (iName == 1) hpass_MC[half_k][i].push_back( new TH1D(name_in, "", array_size_y-1, rebin_array_y) );
	  else if (iName == 2) hpass_MC[half_k][i].push_back( new TH1D(name_in, "", array_size_z-1, rebin_array_z) );
	}
	else {
	  TString name_in = vars_out_tot[iName][k]+"_"+eta[m]+"_"+flavor[l]+"_"+DM[dd]+"_"+muonCharge[nn];
	  if (iName == 0) hfail_MC[half_k][i].push_back( new TH1D(name_in, name_in, array_size_x-1, rebin_array_x) );
	  else if (iName == 1) hfail_MC[half_k][i].push_back( new TH1D(name_in, "", array_size_y-1, rebin_array_y) );
	  else if (iName == 2) hfail_MC[half_k][i].push_back( new TH1D(name_in, "", array_size_z-1, rebin_array_z) );
	}
      }
        

      //integrate out the Y & Z part
      int jBinX = 1, binStartX = 1;
      int nBinsX = h_MC[k][i]->GetNbinsX();
      int nBinsY = h_MC[k][i]->GetNbinsY();
      int nBinsZ = h_MC[k][i]->GetNbinsZ();
      while (jBinX <= array_size_x) { 
	unsigned int iBinX=binStartX;
	float bin_content = 0, bin_error=0;
	while (h_MC[k][i]->GetXaxis()->GetBinCenter(iBinX) < rebin_array_x[jBinX]) {
	  if (h_MC[k][i]->GetXaxis()->GetBinCenter(iBinX) > rebin_array_x[jBinX-1]) {
	    double error_temp_MC;
	    float integral_MC = h_MC[k][i]->IntegralAndError(iBinX, iBinX, 1, nBinsY, 1, nBinsZ, error_temp_MC, "");
	    bin_content += integral_MC;
	    bin_error += pow(error_temp_MC, 2);
	  }
	  ++iBinX;
	}
	  
	if (bin_content < 0) bin_content = 0;
	if (k%2 == 0) {
	  hpass_MC[half_k][i][0]->SetBinContent(jBinX, bin_content);
	  hpass_MC[half_k][i][0]->SetBinError(jBinX, sqrt(bin_error));
	}
	else {
	  hfail_MC[half_k][i][0]->SetBinContent(jBinX, bin_content);
	  hfail_MC[half_k][i][0]->SetBinError(jBinX, sqrt(bin_error));
	}	    
	  
	++jBinX;
	binStartX = iBinX;
      }


      //same for the X & Z axis
      int jBinY = 1, binStartY = 1;
      while (jBinY <= array_size_y) { 
	unsigned int iBinY=binStartY;
	float bin_content = 0, bin_error=0;
	while (h_MC[k][i]->GetYaxis()->GetBinCenter(iBinY) < rebin_array_y[jBinY]) {
	  if (h_MC[k][i]->GetYaxis()->GetBinCenter(iBinY) > rebin_array_y[jBinY-1]) {
	    double error_temp_MC;
	    float integral_MC = h_MC[k][i]->IntegralAndError(1, nBinsX, iBinY, iBinY, 1, nBinsZ, error_temp_MC);
	    bin_content += integral_MC;
	    bin_error += pow(error_temp_MC, 2);
	  }
	  ++iBinY;
	}
	  
	if (bin_content < 0) bin_content = 0;
	if (k%2 == 0) {
	  hpass_MC[half_k][i][1]->SetBinContent(jBinY, bin_content);
	  hpass_MC[half_k][i][1]->SetBinError(jBinY, sqrt(bin_error));
	}
	else {
	  hfail_MC[half_k][i][1]->SetBinContent(jBinY, bin_content);
	  hfail_MC[half_k][i][1]->SetBinError(jBinY, sqrt(bin_error));
	}	    
	  
	++jBinY;
	binStartY = iBinY;
      }


      //same for the X & Y axis
      int jBinZ = 1, binStartZ = 1;
      while (jBinZ <= array_size_z) { 
	unsigned int iBinZ=binStartZ;
	float bin_content = 0, bin_error=0;
	while (h_MC[k][i]->GetZaxis()->GetBinCenter(iBinZ) < rebin_array_z[jBinZ]) {
	  if (h_MC[k][i]->GetZaxis()->GetBinCenter(iBinZ) > rebin_array_z[jBinZ-1]) {
	    double error_temp_MC;
	    float integral_MC = h_MC[k][i]->IntegralAndError(1, nBinsX, 1, nBinsY, iBinZ, iBinZ, error_temp_MC);
	    bin_content += integral_MC;
	    bin_error += pow(error_temp_MC, 2);
	  }
	  ++iBinZ;
	}
	  
	if (bin_content < 0) bin_content = 0;
	if (k%2 == 0) {
	  hpass_MC[half_k][i][2]->SetBinContent(jBinZ, bin_content);
	  hpass_MC[half_k][i][2]->SetBinError(jBinZ, sqrt(bin_error));
	}
	else {
	  hfail_MC[half_k][i][2]->SetBinContent(jBinZ, bin_content);
	  hfail_MC[half_k][i][2]->SetBinError(jBinZ, sqrt(bin_error));
	}	    
	  
	++jBinZ;
	binStartZ = iBinZ;
      }
        
        
      //if (k%2 != 0) hfail_taupt_MC[half_k][i]->Add(hpass_taupt_MC[half_k][i]);
      //remove this, was causing issue with the 

      if (i==0) {
	for (unsigned int iName=0; iName<vars_out_tot.size(); ++iName) {
	  if (k%2 != 0) hfail_MC_total[half_k].push_back( (TH1D*) hfail_MC[half_k][i][iName]->Clone(vars_out_tot[iName][k]+"_total") );
	  if (k%2 == 0) hpass_MC_total[half_k].push_back( (TH1D*) hpass_MC[half_k][i][iName]->Clone(vars_out_tot[iName][k]+"_total") );
	}
      }
      else {
	for (unsigned int iName=0; iName<vars_out_tot.size(); ++iName) {
	  if (k%2 != 0) hfail_MC_total[half_k][iName]->Add(hfail_MC[half_k][i][iName]);
	  if (k%2 == 0) hpass_MC_total[half_k][iName]->Add(hpass_MC[half_k][i][iName]);
	}
      }

      if (m==0 && nn==0) {
	for (unsigned int iName=0; iName<vars_out_tot.size(); ++iName) {
	  if (k%2 != 0) hfail_MC_flavor_DM[half_k][l][dd].push_back( (TH1D*) hfail_MC[half_k][i][iName]->Clone(vars_out_tot[iName][k]+"_flavorDM_"+flavor[l]+"_"+DM[dd]) );
	  if (k%2 == 0) hpass_MC_flavor_DM[half_k][l][dd].push_back( (TH1D*) hpass_MC[half_k][i][iName]->Clone(vars_out_tot[iName][k]+"_flavorDM_"+flavor[l]+"_"+DM[dd]) );
	}
      }
      else {
	for (unsigned int iName=0; iName<vars_out_tot.size(); ++iName) {
	  if (k%2 != 0) hfail_MC_flavor_DM[half_k][l][dd][iName]->Add(hfail_MC[half_k][i][iName]);
	  if (k%2 == 0) hpass_MC_flavor_DM[half_k][l][dd][iName]->Add(hpass_MC[half_k][i][iName]);
	}
      }

      if (m==0 && dd==0) {
	for (unsigned int iName=0; iName<vars_out_tot.size(); ++iName) {
	  if (k%2 != 0) hfail_MC_flavor_muonCharge[half_k][l][nn].push_back( (TH1D*) hfail_MC[half_k][i][iName]->Clone(vars_out_tot[iName][k]+"_flavorMuonCharge_"+flavor[l]+"_"+muonCharge[nn]) );
	  if (k%2 == 0) hpass_MC_flavor_muonCharge[half_k][l][nn].push_back( (TH1D*) hpass_MC[half_k][i][iName]->Clone(vars_out_tot[iName][k]+"_flavorMuonCharge_"+flavor[l]+"_"+muonCharge[nn]) );
	}
      }
      else {
	for (unsigned int iName=0; iName<vars_out_tot.size(); ++iName) {
	  if (k%2 != 0) hfail_MC_flavor_muonCharge[half_k][l][nn][iName]->Add(hfail_MC[half_k][i][iName]);
	  if (k%2 == 0) hpass_MC_flavor_muonCharge[half_k][l][nn][iName]->Add(hpass_MC[half_k][i][iName]);
	}
      }

      if (dd==0 && m==0 && nn==0) {
	for (unsigned int iName=0; iName<vars_out_tot.size(); ++iName) {
	  if (k%2 != 0) hfail_MC_flavor[half_k][l].push_back( (TH1D*) hfail_MC[half_k][i][iName]->Clone(vars_out_tot[iName][k]+"_flavor_"+flavor[l]) );
	  if (k%2 == 0) hpass_MC_flavor[half_k][l].push_back( (TH1D*) hpass_MC[half_k][i][iName]->Clone(vars_out_tot[iName][k]+"_flavor_"+flavor[l]) );
	}
      }
      else {
	for (unsigned int iName=0; iName<vars_out_tot.size(); ++iName) {
	  if (k%2 != 0) hfail_MC_flavor[half_k][l][iName]->Add(hfail_MC[half_k][i][iName]);
	  if (k%2 == 0) hpass_MC_flavor[half_k][l][iName]->Add(hpass_MC[half_k][i][iName]);
	}
      }

      if (dd==0 && m==0 && l==0) {
	for (unsigned int iName=0; iName<vars_out_tot.size(); ++iName) {
	  if (k%2 != 0) hfail_MC_muonCharge[half_k][nn].push_back( (TH1D*) hfail_MC[half_k][i][iName]->Clone(vars_out_tot[iName][k]+"_muonCharge_"+muonCharge[nn]) );
	  if (k%2 == 0) hpass_MC_muonCharge[half_k][nn].push_back( (TH1D*) hpass_MC[half_k][i][iName]->Clone(vars_out_tot[iName][k]+"_muonCharge_"+muonCharge[nn]) );
	}
      }
      else {
	for (unsigned int iName=0; iName<vars_out_tot.size(); ++iName) {
	  if (k%2 != 0) hfail_MC_muonCharge[half_k][nn][iName]->Add(hfail_MC[half_k][i][iName]);
	  if (k%2 == 0) hpass_MC_muonCharge[half_k][nn][iName]->Add(hpass_MC[half_k][i][iName]);
	}
      }


      if (m==0 && l==0) {
	for (unsigned int iName=0; iName<vars_out_tot.size(); ++iName) {
	  if (k%2 != 0) hfail_MC_muonCharge_DM[half_k][nn][dd].push_back( (TH1D*) hfail_MC[half_k][i][iName]->Clone(vars_out_tot[iName][k]+"_muonChargeDM_"+muonCharge[nn]+"_"+DM[dd]) );
	  if (k%2 == 0) hpass_MC_muonCharge_DM[half_k][nn][dd].push_back( (TH1D*) hpass_MC[half_k][i][iName]->Clone(vars_out_tot[iName][k]+"_muonChargeDM_"+muonCharge[nn]+"_"+DM[dd]) );
	}
      }
      else {
	for (unsigned int iName=0; iName<vars_out_tot.size(); ++iName) {
	  if (k%2 != 0) hfail_MC_muonCharge_DM[half_k][nn][dd][iName]->Add(hfail_MC[half_k][i][iName]);
	  if (k%2 == 0) hpass_MC_muonCharge_DM[half_k][nn][dd][iName]->Add(hpass_MC[half_k][i][iName]);
	}
      }


      if (k%2 != 0) {
	for (unsigned int iName=0; iName<vars_out_tot.size(); ++iName) hpass_MC[half_k][i][iName]->Divide(hfail_MC[half_k][i][iName]);
      }
    }
  }

  for (unsigned int iName=0; iName<vars_out_tot.size(); ++iName) {
    for (unsigned int half_k=0; half_k<half_var; ++half_k) {
      hpass_MC_total[half_k][iName]->Divide(hfail_MC_total[half_k][iName]);
      for (unsigned int l=0; l<flavor.size(); ++l) {
	hpass_MC_flavor[half_k][l][iName]->Divide(hfail_MC_flavor[half_k][l][iName]);
	for (unsigned int dd=0; dd<DM.size(); ++dd) {
	  hpass_MC_flavor_DM[half_k][l][dd][iName]->Divide(hfail_MC_flavor_DM[half_k][l][dd][iName]);
	}
      }

      for (unsigned int nn=0; nn<muonCharge.size(); ++nn) {
	hpass_MC_muonCharge[half_k][nn][iName]->Divide(hfail_MC_muonCharge[half_k][nn][iName]);
	for (unsigned int dd=0; dd<DM.size(); ++dd) {
	  hpass_MC_muonCharge_DM[half_k][nn][dd][iName]->Divide(hfail_MC_muonCharge_DM[half_k][nn][dd][iName]);
	}
	for (unsigned int l=0; l<flavor.size(); ++l) {
	  hpass_MC_flavor_muonCharge[half_k][l][nn][iName]->Divide(hfail_MC_flavor_muonCharge[half_k][l][nn][iName]);
	}
      }
    }
  }



  file_out->cd();
  for (unsigned int iName=0; iName<vars_out_tot.size(); ++iName) {
    for (unsigned int half_k=0; half_k<half_var; ++half_k) {
      hpass_MC_total[half_k][iName]->Write();
      for (unsigned int l=0; l<flavor.size(); ++l) {
	hpass_MC_flavor[half_k][l][iName]->Write();
	for (unsigned int dd=0; dd<DM.size(); ++dd) {
	  hpass_MC_flavor_DM[half_k][l][dd][iName]->Write();
	}
      }

      for (unsigned int nn=0; nn<muonCharge.size(); ++nn) {
	hpass_MC_muonCharge[half_k][nn][iName]->Write();
	for (unsigned int dd=0; dd<DM.size(); ++dd) {
	  hpass_MC_muonCharge_DM[half_k][nn][dd][iName]->Write();
	}
	for (unsigned int l=0; l<flavor.size(); ++l) {
	  hpass_MC_flavor_muonCharge[half_k][l][nn][iName]->Write();
	}
      }
    }
    for (unsigned int half_k=0; half_k<half_var; ++half_k) {
      for (unsigned int i=0; i<h_MC[0].size(); ++i) {
	hpass_MC[half_k][i][iName]->Write();
      }
    }
  }
  file_out->Close();



  return 0;
}
