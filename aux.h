#include "TH1.h"
#include "TH2.h"
#include <vector>
#include <iostream>
#include "TString.h"
#include "TLorentzVector.h"
#include "PU_reWeighting.cc"
#include "GeneralizedEndpoint.cc"
#include "TGraphErrors.h"
#include "TFile.h"

using namespace std;

float norm_F(float x, float y){

  return sqrt(x*x+y*y);

}


vector<TString> GetSys() {
  vector<TString> systematics;
  systematics.push_back("TES");
  systematics.push_back("MES");
  systematics.push_back("mres");
  systematics.push_back("minbias");
  systematics.push_back("muonID");
  systematics.push_back("muonIso");
  systematics.push_back("trigger");
  systematics.push_back("tauID");
  systematics.push_back("eletauFR");
  systematics.push_back("mutauFR");
  systematics.push_back("FRstat");
  systematics.push_back("FRsys");
  systematics.push_back("topPt");

  return systematics;
}


TString GetEtaString(float eta) {
  TString eta_string = "";
  if (fabs(eta) < 1.46) {
    eta_string = "barrel";
  }
  else if (fabs(eta) > 1.56) {
    eta_string = "endcap";
  }
  else {
    eta_string = "";
  }
  return eta_string;
}



double GetPUWeight(int PU, TString mc_nick, TString var) {
  double pu_reweight = 0;
  string mc_nickname = mc_nick.Data();
  if (var == "nom") pu_reweight = PU_2017_Rereco::MC_pileup_weight(PU, mc_nickname, "Data_METcorr_2017BtoF");
  else if (var == "up") pu_reweight = PU_2017_Rereco::MC_pileup_weight(PU, mc_nickname, "Data_METcorr_2017BtoF_high");
  else if (var == "down") pu_reweight = PU_2017_Rereco::MC_pileup_weight(PU, mc_nickname, "Data_METcorr_2017BtoF_low");
  else cout << "PU reweight error" << endl;

  return pu_reweight;
}


double GetHighPtIDWeight(TLorentzVector mu_p4, TString var) {
  TFile* ID_file = new TFile("Reweighting/RunBCDEF_SF_ID_syst.root","R");

  float mu_pt = mu_p4.Pt();
  if (mu_pt > 120) mu_pt = 119;
  float mu_eta = mu_p4.Eta();

  //scale factors                                                                                                                                                                                                                                                                                                                            
  //ID
  TH2F* ID_histo = (TH2F*) ID_file->Get("NUM_HighPtID_DEN_genTracks_pair_newTuneP_probe_pt_abseta");
  int bin_in = ID_histo->FindBin(mu_pt, fabs(mu_eta));
  double highPtID_sf = ID_histo->GetBinContent(bin_in);
  double error = ID_histo->GetBinError(bin_in);

  double weight = 0;
  if (var == "nom") {
    weight = highPtID_sf;
  }
  else if (var == "up") {
    weight = highPtID_sf + error;
  }
  else if (var == "down") {
    weight = highPtID_sf - error;
  }

  ID_file->Close("R");

  return weight;
}


double GetTriggerWeight(float mu_pt, float mu_eta, TString var) {
  double SF = 1;
  if (mu_eta > -2.4 && mu_eta < -2.1) SF = 0.911;
  else if (mu_eta < -1.6) SF = 0.968;
  else if (mu_eta < -1.2) SF = 0.993;
  else if (mu_eta < -0.9) SF = 0.948;
  else if (mu_eta < -0.3) SF = 0.977;
  else if (mu_eta < -0.2) SF = 0.941;
  else if (mu_eta < 0.0)  SF = 0.978;
  else if (mu_eta < 0.2)  SF = 0.975;
  else if (mu_eta < 0.3)  SF = 0.948;
  else if (mu_eta < 0.9)  SF = 0.970;
  else if (mu_eta < 1.2)  SF = 0.942;
  else if (mu_eta < 1.6)  SF = 0.982;
  else if (mu_eta < 2.1)  SF = 0.968;
  else if (mu_eta < 2.4)  SF = 0.921;

  double factor_up = 1;
  double factor_down = 1;
  if (mu_pt < 300) factor_up = .02, factor_down = .02; //normal syst
  else  factor_up = .02, factor_down = 0.06;
  //add prefiring syst
  factor_up = 1+sqrt(pow(factor_up,2) + pow(.02,2));
  factor_down = 1-sqrt(pow(factor_down,2) + pow(.02,2));

  double weight = 0;
  if (var=="nom") weight = SF;
  else if (var=="up") weight = SF*factor_up;
  else if (var=="down") weight = SF*factor_down;

  return weight;
}


double GetTkLooseIsoWeight(float mu_pt, float mu_eta, TString var) {
  if (mu_pt > 120) mu_pt = 119;
  TFile* Iso_file = new TFile("Reweighting/RunBCDEF_SF_ISO_syst.root","R");

  TH2F* Iso_histo = (TH2F*) Iso_file->Get("NUM_LooseRelTkIso_DEN_HighPtIDandIPCut_pair_newTuneP_probe_pt_abseta");
  int bin_in = Iso_histo->FindBin(mu_pt, fabs(mu_eta));
  double tkLooseISO_sf = Iso_histo->GetBinContent(bin_in);
  double factor = Iso_histo->GetBinError(bin_in);

  double weight = 0;
  if (var=="nom") weight = tkLooseISO_sf;
  else if (var=="up") weight = tkLooseISO_sf+factor;
  else if (var=="down") weight = tkLooseISO_sf-factor;

  Iso_file->Close("R");
  return weight;
}




double GetTightTauIDWeight(float tau_pt, TString lepton, TString var) {
  if (lepton != "tau") {
    return 1;
  }
  else {
    double base_weight = 0.95;
    double factor_up   = sqrt( pow(.05,2) + pow(0.05*tau_pt/1000,2) );
    double factor_down = sqrt( pow(.05,2) + pow(-0.35*tau_pt/1000,2) );
    
    double weight = 0;
    if (var=="nom") weight = base_weight;
    else if (var=="up") weight = base_weight*(1+factor_up);
    else if (var=="down") weight = base_weight*(1-factor_down);
    return weight;
  }
}


double GetEleTauFR(float eta, TString lepton, TString var) {
  if (lepton != "ele") {
    return 1;
  }
  else {
    double weight = 1;
    
    if (var=="nom") {
      if (fabs(eta) < 1.460) weight = 1.09;
      else if (fabs(eta) > 1.558) weight = 1.19;
    }
    else if (var=="up") {
      if (fabs(eta) < 1.460) weight = 1.09+0.01;
      else if (fabs(eta) > 1.558) weight = 1.19+0.01;
    }
    else if (var=="down") {
      if (fabs(eta) < 1.460) weight = 1.09-0.01;
      else if (fabs(eta) > 1.558) weight = 1.19-0.01;
    }

    return weight;
  }
}


double GetMuTauFR(float eta, TString lepton, TString var) {
  if (lepton != "mu") {
    return 1;
  }
  else {
    double weight = 1;
    
    if (var=="nom") {
      if (fabs(eta) < 0.4) weight = 1.17;
      else if (fabs(eta) < 0.8 && fabs(eta) > 0.4) weight = 1.29;
      else if (fabs(eta) < 1.2 && fabs(eta) > 0.8) weight = 1.14;
      else if (fabs(eta) < 1.7 && fabs(eta) > 1.2) weight = 0.93;
      else if (fabs(eta) < 2.3 && fabs(eta) > 1.7) weight = 1.61;
    }
    else if (var=="up") {
      if (fabs(eta) < 0.4) weight = 1.17+0.12;
      else if (fabs(eta) < 0.8 && fabs(eta) > 0.4) weight = 1.29+0.30;
      else if (fabs(eta) < 1.2 && fabs(eta) > 0.8) weight = 1.14+0.05;
      else if (fabs(eta) < 1.7 && fabs(eta) > 1.2) weight = 0.93+0.60;
      else if (fabs(eta) < 2.3 && fabs(eta) > 1.7) weight = 1.61+0.60;
    }
    else if (var=="down") {
      if (fabs(eta) < 0.4) weight = 1.17-0.12;
      else if (fabs(eta) < 0.8 && fabs(eta) > 0.4) weight = 1.29-0.30;
      else if (fabs(eta) < 1.2 && fabs(eta) > 0.8) weight = 1.14-0.05;
      else if (fabs(eta) < 1.7 && fabs(eta) > 1.2) weight = 0.93-0.60;
      else if (fabs(eta) < 2.3 && fabs(eta) > 1.7) weight = 1.61-0.60;
    }

    return weight;
  }
}




double FakeRate_noratio(double taupt, TString eta) {
  double SF=0.2;
  if (taupt >= 1000) taupt = 999;

  TFile* fake_file = new TFile("Reweighting/fakerate_MtLow.root","R");

  double reweight = 0;

  TString hname = "eta_"+eta;
  TH1F* h_taupt = (TH1F*) fake_file->Get("FakeRateByTauPt_"+hname);
  int iBin = h_taupt->FindBin(taupt);
  double base_SF = h_taupt->GetBinContent(iBin);
  
  SF = base_SF;
  reweight = SF;

  return reweight;
}



double FakeRateHigh_unfactorised(double taupt, double ratio, TString eta) {
  double SF=0.2;
  if (taupt >= 1000) taupt = 999;
  if (ratio >= 2) ratio = 1.9;

  TFile* fake_file = new TFile("Reweighting/fakerate_unfactorised_MtLow.root","R");

  double reweight = 0;

  TString hname = "eta_"+eta;
  if (taupt > 150) {
    hname += "_taupt_150_1000";
  }
  else {
    hname += "_taupt_0_150";
  }

  TH1F* h_taupt = (TH1F*) fake_file->Get("FakeRateByTauPtAndRatio_"+hname);
  int iBin = h_taupt->FindBin(taupt, ratio);
  double base_SF = h_taupt->GetBinContent(iBin)+h_taupt->GetBinError(iBin);

  SF = base_SF;
  reweight = SF;

  return reweight;
}


double FakeRate_unfactorised(double taupt, double taueta, double ratio, TString var) {
  if (taupt >= 1000) taupt = 999;
  if (ratio >= 2) ratio = 1.9;

  TFile* fake_file = new TFile("Reweighting/fakerate_unfactorised_MtLow.root","R");

  TString eta_string = GetEtaString(taueta);
  if (eta_string == "") {
    fake_file->Close("R");
    return 0;
  }

  TString hname = "eta_"+eta_string;
  if (taupt > 150) {
    hname += "_taupt_150_1000";
  }
  else {
    hname += "_taupt_0_150";
  }

  TH1F* h_taupt = (TH1F*) fake_file->Get("FakeRateByTauPtAndRatio_"+hname);
  int iBin = h_taupt->FindBin(taupt, ratio);
  double base_SF = h_taupt->GetBinContent(iBin);
  double error = h_taupt->GetBinError(iBin);
  
  double weight = 0;
  if (var=="nom") weight = base_SF;
  else if (var=="up") weight = base_SF+error;
  else if (var=="down") weight = base_SF-error;

  fake_file->Close("R");

  return weight;
}




double FakeRate_factorised(double taupt, double ratio, TString eta) {
  double SF=0.2;
  if (taupt >= 1000) taupt = 999;
  if (ratio >= 2) ratio = 1.9;

  TFile* fake_file = new TFile("Reweighting/fakerate_MtLow.root","R");

  double reweight = 0;

  TString hname = "eta_"+eta;
  TH1F* h_taupt = (TH1F*) fake_file->Get("FakeRateByTauPt_"+hname);
  int iBin = h_taupt->FindBin(taupt);
  double base_SF = h_taupt->GetBinContent(iBin);

  TH1F* h_corr = (TH1F*) fake_file->Get("RatioCorrectionFactor_"+hname);
  iBin = h_corr->FindBin(ratio);
  double corr_factor = h_corr->GetBinContent(iBin);

  SF = corr_factor*base_SF;
  reweight = SF;

  return reweight;
}


double FakeRate_DY(double taupt, double taueta, double ratio, TString var) {
  //if (taupt >= 1000) taupt = 999;
  //if (ratio >= 2) ratio = 1.9;
  //
  //TFile* fake_file = new TFile("Reweighting/fakerate_DY.root","R");
  //
  //TString eta_string = GetEtaString(taueta);
  //
  //TString hname = "eta_"+eta_string;
  //if (taupt > 150) {
  //  hname += "_taupt_150_1000";
  //}
  //else {
  //  hname += "_taupt_0_150";
  //}
  //
  //TH1F* h_taupt = (TH1F*) fake_file->Get("FakeRateByTauPtAndRatio_"+hname);
  //int iBin = h_taupt->FindBin(taupt, ratio);
  //double DY_SF = h_taupt->GetBinContent(iBin);
  //double norm_SF = FakeRate_unfactorised(taupt,taueta,ratio,"nom");
  //
  //double weight = 0;
  //if (var=="nom") weight = 1;
  //else if (var=="up") weight = DY_SF/norm_SF;
  //else if (var=="down") weight = (2*norm_SF-DY_SF)/norm_SF;
  //
  //return weight;

  //FIXME
  return 1;
}



double GetTopPtWeightUnc(float top_pt_in) {
  double weight = 0.0;
  if (top_pt_in < 0.0) {
    weight = 0.0;
  } else if (top_pt_in < 150.0) {
    weight = 0.045;
  } else if (top_pt_in < 1000.0) {
    weight = 0.04 * top_pt_in/1000.0 + 0.045;
  } else if (top_pt_in < 1100.0) {
    weight = 0.09;
  } else if (top_pt_in < 1200.0) {
    weight = 0.1;
  } else if (top_pt_in < 1400.0) {
    weight = 0.12;
  } else if (top_pt_in < 1600.0) {
    weight = 0.14;
  } else if (top_pt_in < 1800.0) {
    weight = 0.155;
  } else if (top_pt_in < 2000.0) {
    weight = 0.18;
  } else if (top_pt_in < 2200.0) {
    weight = 0.2;
  } else if (top_pt_in < 2600.0) {
    weight = 0.243;
  } else if (top_pt_in < 3000.0) {
    weight = 0.34;
  } else if (top_pt_in > 2999.9) {
    weight = 0.34;
  }
  return weight;
}



double GetTopPtWeight(float top_pt_1, float top_pt_2, TString var){
  if (top_pt_1 < 0 || top_pt_2 <0) {
    return 1;
  }
  else {
    double tmp_t1 = exp(0.0615-0.0005*top_pt_1);
    double tmp_t2 = exp(0.0615-0.0005*top_pt_2);
    double tmp_t1_uncer = GetTopPtWeightUnc(top_pt_1);
    double tmp_t2_uncer = GetTopPtWeightUnc(top_pt_2);
    
    double w_top_up = sqrt(tmp_t1*(1.0 + tmp_t1_uncer)*tmp_t2*(1.0 + tmp_t2_uncer) );
    double w_top_down = sqrt(tmp_t1*(1.0 - tmp_t1_uncer)*tmp_t2*(1.0 - tmp_t2_uncer) );
    double w_top_nom = sqrt(tmp_t1 * tmp_t2);
    
    double weight = 0;
    if (var=="nom") weight = w_top_nom;
    else if (var=="up") weight = w_top_up;
    else if (var=="down") weight = w_top_down;
    
    return weight;
  }
}


double GeneralWeightFunction(TString sys, int n_vert, TLorentzVector tau_p4, float ratio, TLorentzVector mu_p4, TString lepton, float top_pt_1, float top_pt_2, TString mc_nickname, TString var) {
  vector<TString> systematics = GetSys();

  bool match = false;
  for (unsigned int i=0; i<systematics.size(); ++i) {
    if (systematics[i]=="TES") continue;
    if (sys==systematics[i]) {
      match = true;
      break;
    }
  }

  if (!match) {
    cout << endl << endl <<  "!!!!!!!!!!!!!!!!!!!!!!!!!!!!" << endl;
    cout << "systematic [[ " << sys << " ]] not recognized" << endl;
    cout << "!!!!!!!!!!!!!!!!!!!!!!!!!!!!" << endl << endl << endl;
    return 0;
  }
  else {
    float mu_pt = mu_p4.Pt();
    float mu_eta = mu_p4.Eta();
    float tau_pt = tau_p4.Pt();
    float tau_eta = tau_p4.Eta();

    float weight = 0;

    if (sys == "minbias") weight = GetPUWeight(n_vert,mc_nickname,var);
    else if (sys == "muonID") weight = GetHighPtIDWeight(mu_p4,var);
    else if (sys == "muonIso") weight = GetTkLooseIsoWeight(mu_pt,mu_eta,var);
    else if (sys == "trigger") weight = GetTriggerWeight(mu_pt,mu_eta,var);
    else if (sys == "tauID") weight = GetTightTauIDWeight(tau_pt,lepton,var);
    else if (sys == "eletauFR") weight = GetEleTauFR(tau_eta,lepton,var);
    else if (sys == "mutauFR") weight = GetMuTauFR(tau_eta,lepton,var);
    else if (sys == "FRstat") weight = FakeRate_unfactorised(tau_pt,tau_eta,ratio,var);
    else if (sys == "FRsys") weight = FakeRate_DY(tau_pt,tau_eta,ratio,var);
    else if (sys == "topPt") weight = GetTopPtWeight(top_pt_1,top_pt_2,var); 

    return weight;
  }
}


double GetCollinearMass(TLorentzVector tau, TLorentzVector mu,  TLorentzVector MET) {

  double METproj=fabs((MET.Px()*tau.Px()+MET.Py()*tau.Py())/tau.Pt());
  double xth=1;
  if((tau.Pt()+METproj)!=0) xth=tau.Pt()/(tau.Pt()+METproj);
  double mass_vis=(tau+mu).M();
  double mcol = 0;
  if (mass_vis != mass_vis) mass_vis=0;

  if (xth>0) mcol=mass_vis/sqrt(xth);
  else mcol=0;

  return mcol;
}


pair<TLorentzVector,TLorentzVector> TauEnergyScale(TLorentzVector tau_p4, TLorentzVector met_p4, TString var) {
  TLorentzVector tau_TES_p4;
  tau_TES_p4.SetPxPyPzE(0,0,0,0);
  TLorentzVector met_TES_p4;
  met_TES_p4.SetPxPyPzE(0,0,0,0);
  
  float scale = 0.03; //3 percent for high pt taus
  if (var=="nom")  tau_TES_p4 = tau_p4;
  else if (var=="up")   tau_TES_p4 = tau_p4*(1+scale);
  else if (var=="down") tau_TES_p4 = tau_p4*(1-scale);

  met_TES_p4 = met_p4 - tau_TES_p4 + tau_p4;

  pair<TLorentzVector,TLorentzVector> tes;
  tes.first = tau_TES_p4;
  tes.second = met_TES_p4;
  return tes;
}


pair<TLorentzVector,TLorentzVector> MuResolution(TLorentzVector mu_p4, TLorentzVector met_p4, TString var) {
  TLorentzVector mu_res_p4;
  mu_res_p4.SetPxPyPzE(0,0,0,0);
  TLorentzVector met_res_p4;
  met_res_p4.SetPxPyPzE(0,0,0,0);
  
  float scale = 0;
  TString eta_string = GetEtaString(mu_p4.Eta());
  if (eta_string == "barrel") {
    if (mu_p4.Pt() < 200) scale = 0.003;
    else if (mu_p4.Pt() < 500) scale = 0.005;
    else scale = 0.01;
  }
  else if (eta_string == "endcap") {
    if (mu_p4.Pt() < 200) scale = 0.006;
    else if (mu_p4.Pt() < 500) scale = 0.01;
    else scale = 0.02;
  }

  if (var=="nom")  mu_res_p4 = mu_p4;
  else if (var=="up")   mu_res_p4 = mu_p4*(1+scale);
  else if (var=="down") mu_res_p4 = mu_p4*(1-scale);

  met_res_p4 = met_p4 - mu_res_p4 + mu_p4;

  pair<TLorentzVector,TLorentzVector> mes;
  mes.first = mu_res_p4;
  mes.second = met_res_p4;
  return mes;
}


pair<TLorentzVector,TLorentzVector> MuEnergyScale(TLorentzVector mu_p4, int mu_charge, TLorentzVector met_p4, TString var) {
  TLorentzVector mu_mes_p4;
  mu_mes_p4.SetPxPyPzE(0,0,0,0);
  TLorentzVector met_mes_p4;
  met_mes_p4.SetPxPyPzE(0,0,0,0);
  
  int mode = 0, verbose = 1;

  if (var=="nom")  mode = 0;
  else if (var=="up")   mode = 1;
  else if (var=="down") mode = 2;

  GeneralizedEndpoint* g = new GeneralizedEndpoint();
  float mu_mes_pt = 0;
  float mu_mass = 0.105;
  mu_mes_pt = g->GeneralizedEndpointPt(mu_p4.Pt(), mu_charge, mu_p4.Eta(), mu_p4.Phi(), mode, verbose);
  mu_mes_p4.SetPtEtaPhiM(mu_mes_pt,mu_p4.Eta(),mu_p4.Phi(),mu_mass);
  met_mes_p4 = met_p4 - mu_mes_p4 + mu_p4;

  pair<TLorentzVector,TLorentzVector> mes;
  mes.first = mu_mes_p4;
  mes.second = met_mes_p4;
  return mes;
}


vector<TLorentzVector> GetScaleVariation(TString syst, TString tau_gen, TString mu_gen, TLorentzVector tau_p4, TLorentzVector mu_p4, int mu_charge, TLorentzVector met_p4) {
  TLorentzVector tau_newp4, mu_newp4, met_newp4;

  TString var = "nom";
  if (syst.Contains("up")) var = "up";
  else if (syst.Contains("down")) var = "down";

  if (syst.Contains("TES")) {
    if (tau_gen != "tau") var = "nom";
    tau_newp4 = TauEnergyScale(tau_p4,met_p4,var).first, met_newp4 = TauEnergyScale(tau_p4,met_p4,var).second;
    mu_newp4 = mu_p4;
  }
  else if (syst.Contains("MES")) {
    if (mu_gen != "mu") var = "nom";
    mu_newp4 = MuEnergyScale(mu_p4,mu_charge,met_p4,var).first, met_newp4 = MuEnergyScale(mu_p4,mu_charge,met_p4,var).second;
    tau_newp4 = tau_p4;
  }
  else if (syst.Contains("mres")) {
    if (mu_gen != "mu") var = "nom";
    mu_newp4 = MuResolution(mu_p4,met_p4,var).first, met_newp4 = MuResolution(mu_p4,met_p4,var).second;
    tau_newp4 = tau_p4;
  }

  vector<TLorentzVector> newp4;
  newp4.push_back(tau_newp4);
  newp4.push_back(mu_newp4);
  newp4.push_back(met_newp4);

  return newp4;
}



pair<double,double> getSF (float mupt, float mueta) {
  //highest pt is 120 GeV
  if (mupt >= 120) mupt = 119;
  TFile* id_file = new TFile("Reweighting/RunBCDEF_SF_ID.root","R");
  TH2F* id_histo = (TH2F*) id_file->Get("NUM_HighPtID_DEN_genTracks_pair_newTuneP_probe_pt_abseta");
  int bin_in = id_histo->FindBin(mupt, fabs(mueta));
  double id_sf = id_histo->GetBinContent(bin_in);
  id_file->Close();

  TFile* iso_file = new TFile("Reweighting/RunBCDEF_SF_ISO.root","R");
  TH2F* iso_histo = (TH2F*) iso_file->Get("NUM_LooseRelTkIso_DEN_TrkHighPtID_pair_newTuneP_probe_pt_abseta");
  bin_in = iso_histo->FindBin(mupt, fabs(mueta));
  double iso_sf = iso_histo->GetBinContent(bin_in);
  iso_file->Close();

  if (id_sf == 0) id_sf = 1.0;
  if (iso_sf == 0) iso_sf = 1.0;

  pair<double, double> SF_pair;
  SF_pair.first =  id_sf;  SF_pair.second =iso_sf;
  return  SF_pair;
}


double threeTriggersSF(float mu_eta) {
  double SF = 1;
  if (mu_eta > -2.4 && mu_eta < -2.1) SF = 0.911;
  else if (mu_eta < -1.6) SF = 0.968;
  else if (mu_eta < -1.2) SF = 0.993;
  else if (mu_eta < -0.9) SF = 0.948;
  else if (mu_eta < -0.3) SF = 0.977;
  else if (mu_eta < -0.2) SF = 0.941;
  else if (mu_eta < 0.0)  SF = 0.978;
  else if (mu_eta < 0.2)  SF = 0.975;
  else if (mu_eta < 0.3)  SF = 0.948;
  else if (mu_eta < 0.9)  SF = 0.970;
  else if (mu_eta < 1.2)  SF = 0.942;
  else if (mu_eta < 1.6)  SF = 0.982;
  else if (mu_eta < 2.1)  SF = 0.968;
  else if (mu_eta < 2.4)  SF = 0.921;

  return SF;
}



double GetReweight_mumu(float mu1_pt, float mu1_eta, float mu2_pt, float mu2_eta) {
  //scale factor files that need to be open                                                                                                                                                                                                   
  TFile* tr_file = new TFile("Reweighting/EfficienciesAndSF_RunBtoF_Nov17Nov2017.root","R");
  TH2F* tr_data = (TH2F*) tr_file->Get("IsoMu27_PtEtaBins/efficienciesDATA/pt_abseta_DATA");
  TH2F* tr_MC = (TH2F*) tr_file->Get("IsoMu27_PtEtaBins/efficienciesMC/pt_abseta_MC");
  //Eff. of the trigger: COMPLEMENTARY of the prob. that NONE of the two muons will trigger                                                                                                                                                   

  int bin_in = tr_data->FindBin(mu1_pt, fabs(mu1_eta));
  double mu1_eff_data = tr_data->GetBinContent(bin_in);
  bin_in = tr_data->FindBin(mu2_pt, fabs(mu2_eta));
  double mu2_eff_data = tr_data->GetBinContent(bin_in);
  double tr_eff_data = 1 - (1 - mu1_eff_data)*(1 - mu2_eff_data);
  if (tr_eff_data == 0) tr_eff_data = 1.0;

  bin_in = tr_MC->FindBin(mu1_pt, fabs(mu1_eta));
  double mu1_eff_MC = tr_MC->GetBinContent(bin_in);
  bin_in = tr_data->FindBin(mu2_pt, fabs(mu2_eta));
  double mu2_eff_MC = tr_MC->GetBinContent(bin_in);
  double tr_eff_MC = 1 - (1 - mu1_eff_MC)*(1 - mu2_eff_MC);
  tr_file->Close();
  if (tr_eff_MC == 0) tr_eff_MC = 1.0;

  double tr_sf = tr_eff_data/tr_eff_MC;

  float mu1ID_sf = getSF(mu1_pt, mu1_eta).first, mu1Iso_sf = getSF(mu1_pt, mu1_eta).second;
  float mu2ID_sf = getSF(mu2_pt, mu2_eta).first, mu2Iso_sf = getSF(mu2_pt, mu2_eta).second;


  double weight=tr_sf*mu1ID_sf*mu1Iso_sf*mu2ID_sf*mu2Iso_sf;

  return weight;
}


