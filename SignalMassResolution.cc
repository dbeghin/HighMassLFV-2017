#define IIHEAnalysis_cxx
#include "IIHEAnalysis_old.h"
//#include <TH1.h>
//#include <TLorentzVector.h>
//#include <TCanvas.h>
#include "TString.h"
#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char** argv) {
  string out = *(argv + 1);
  string out_name= out;
  string in = *(argv + 2);
  string inname= in;
  string controlregion_in = *(argv + 3);
  string controlregion= controlregion_in;
  string type_in = *(argv + 4);
  string type= type_in;
  TFile *fIn = TFile::Open(inname.c_str());
  TH1F* hCounter = (TH1F*) fIn->Get("h1");
  TH1F* hCounter2 = (TH1F*) fIn->Get("h2");
  TTree* tree = (TTree*) fIn->Get("IIHEAnalysis");

  IIHEAnalysis* a = new IIHEAnalysis(tree);
  a->Loop(controlregion, type, out_name, hCounter, hCounter2);
  return 0;
}

void IIHEAnalysis::Loop(string controlregion, string type_of_data, string out_name, TH1F* hCounter, TH1F* hCounter2) {
   if (fChain == 0) return;


   //string out_name = "out_"+type_of_data+".root";
   TFile* file_out = new TFile(out_name.c_str(),"RECREATE");

   const float mu_mass = 0.10565837;
   const float pi = 3.14159;

   //list here the names and x-axis ranges of all gen-level histos we wish to create :
   vector<TString> histo_names;         vector<int> nBins;      vector<float> x_min,    x_max; 
   histo_names.push_back("Mgen");       nBins.push_back(8000);  x_min.push_back(0);     x_max.push_back(8000);
   histo_names.push_back("Mvis");       nBins.push_back(8000);  x_min.push_back(0);     x_max.push_back(8000);
   histo_names.push_back("Mtot");       nBins.push_back(8000);  x_min.push_back(0);     x_max.push_back(8000);
   histo_names.push_back("Mcol");       nBins.push_back(8000);  x_min.push_back(0);     x_max.push_back(8000);
   histo_names.push_back("oldMcol");    nBins.push_back(8000);  x_min.push_back(0);     x_max.push_back(8000);
   histo_names.push_back("Mvis_res");   nBins.push_back(2000);  x_min.push_back(-1);    x_max.push_back(1);
   histo_names.push_back("Mtot_res");   nBins.push_back(2000);  x_min.push_back(-1);    x_max.push_back(1);
   histo_names.push_back("Mcol_res");   nBins.push_back(2000);  x_min.push_back(-1);    x_max.push_back(1);
   histo_names.push_back("oldMcol_res");nBins.push_back(2000);  x_min.push_back(-1);    x_max.push_back(1);

   vector<TH1F*> h;
   for (unsigned int i = 0; i<histo_names.size(); ++i) {
     h.push_back( new TH1F(histo_names[i], histo_names[i], nBins[i], x_min[i], x_max[i]) ); 
     h[i]->Sumw2();
   }



   Long64_t nEntries = fChain->GetEntriesFast();
   Long64_t nbytes = 0, nb = 0;
   long n1=0, n2=0;
   int print_count = 0;
   //start loop over all events
   for (Long64_t jEntry = 0; jEntry < nEntries; ++jEntry) {
      Long64_t iEntry = LoadTree(jEntry);
      if (iEntry < 0) break;
      if (jEntry % 1000 == 0) fprintf(stdout, "\r  Processed events: %8d of %8d ", jEntry, nEntries);

      nb = fChain->GetEntry(jEntry);
      nbytes += nb;

      float first_weight = 1;//fChain->GetLeaf("event_weight")->GetValue();
      double final_weight = first_weight;
      

      //start loop over all simulated particules
      int moth_ind = -1, tau_ind = -1;
      TLorentzVector gen_mup4, gen_taup4, gen_totalp4, p4;

      for (unsigned int iMC = 0; iMC < mc_pt->size(); ++iMC) {
	moth_ind = mc_mother_index->at(iMC).at(0);
	if (abs(mc_pdgId->at(iMC)) == 15) {
	  p4.SetPxPyPzE(mc_px->at(iMC), mc_py->at(iMC), mc_pz->at(iMC), mc_energy->at(iMC));
	  if (mc_pt->at(iMC) > 20) {	
	    if (p4.Pt() < 20) continue;
	    if (p4.Pt() > 10000) continue;
	    gen_taup4 = p4;
	    tau_ind = iMC;
	  }
	}
      }

      for (unsigned int iMC = 0; iMC < mc_pt->size(); ++iMC) {
	moth_ind = mc_mother_index->at(iMC).at(0);
	if (abs(mc_pdgId->at(iMC))  == 13) {
	  if (mc_pt->at(iMC) < 10) continue;
	  p4.SetPxPyPzE(mc_px->at(iMC), mc_py->at(iMC), mc_pz->at(iMC), mc_energy->at(iMC));
	  if (p4.Pt() < 10) continue;
	  if (p4.Pt() > 10000) continue;
	  if (moth_ind == tau_ind) continue;
	  gen_mup4 = p4;
	}
	if (print_count < 20) {
	  ++print_count;
	  cout << endl;
	  for (unsigned int iMC = 0; iMC < mc_pt->size(); ++iMC) cout << iMC << "  " << mc_pdgId->at(iMC) << "  " << mc_mother_index->at(iMC).at(0) << "  " << mc_pt->at(iMC) << endl;
	}
      }
      gen_totalp4 = gen_taup4 + gen_mup4;
      h[0]->Fill(gen_totalp4.M(), final_weight);


      bool PassMuonTrigger = false;
      if (trig_HLT_Mu50_accept || trig_HLT_TkMu50_accept) PassMuonTrigger = true;
      //if (trig_HLT_IsoMu27_accept || trig_HLT_IsoTkMu27_accept) PassMuonTrigger = true;
      if (!PassMuonTrigger) continue;


      //start muon counting loop
      int Nmu = 0;
      for (unsigned int iMu = 0; iMu < mu_gt_pt->size(); ++iMu) {
        if(mu_isPFMuon->at(iMu) && mu_gt_pt->at(iMu) > 20 && fabs(mu_gt_eta->at(iMu)) < 2.4 && fabs(mu_gt_dxy_firstPVtx->at(iMu)) < 0.045 && fabs(mu_gt_dz_firstPVtx->at(iMu)) < 0.2 && mu_pfIsoDbCorrected04->at(iMu) < 0.3 && mu_isMediumMuon->at(iMu)) ++Nmu;
        if (Nmu > 1) break;
      }
      if (Nmu > 1) continue; //2nd muon veto                                                                                                                                                                

      //electron veto
      bool electron = false;
      for (unsigned int iEle = 0; iEle < gsf_pt->size(); ++iEle) {
	if (gsf_VIDLoose->at(iEle) && gsf_pt->at(iEle) > 20 && fabs(gsf_eta->at(iEle)) < 2.5 && fabs(gsf_dxy_firstPVtx->at(iEle)) < 0.045 && fabs(gsf_dz_firstPVtx->at(iEle)) < 0.2 && gsf_passConversionVeto->at(iEle) && gsf_nLostInnerHits->at(iEle) <= 1 && gsf_relIso->at(iEle) < 0.3) electron = true;
        if (electron) break;
      }
      if (electron) continue;

      //bjet veto (medium WP for the bjet)                                                                                                                           
      /*bool bjet = false;
      for (unsigned int iJet = 0; iJet < jet_pt->size(); ++iJet) {
        if (jet_CSVv2->at(iJet) > 0.800 && jet_pt->at(iJet) > 20 && fabs(jet_eta->at(iJet)) < 2.4) bjet = true;
        if (bjet) break;
      }
      if (bjet) continue;*/



      //Sort muons, taus by decreasing pt
      float pt = 0.0;
      int highest = -1;
      vector<int> orderedMu, orderedTau;
      vector<int> rest, rest2;



      //sorting muons
      for (unsigned int ii = 0; ii < mu_ibt_pt->size(); ++ii) {
        rest.push_back(ii);
      }
      while (rest.size()>0) {
	rest2.clear();
	highest = -1;
        pt = -10000;
        for (unsigned int ii = 0; ii < rest.size(); ++ii) {
          if (mu_ibt_pt->at(rest[ii]) > pt) {
            pt = mu_ibt_pt->at(rest[ii]);
            if (highest > -1) rest2.push_back(highest);
            highest = rest[ii];
          }
          else {
	    rest2.push_back(rest[ii]);
	  }
        }
        orderedMu.push_back(highest);
        rest = rest2;
      }

      //sorting taus
      rest.clear();
      for (unsigned int ii = 0; ii < tau_pt->size(); ++ii) {
        rest.push_back(ii);
      }
      while (rest.size()>0) {
	rest2.clear();
	highest = -1;
        pt = -10000;
        for (unsigned int ii = 0; ii < rest.size(); ++ii) {
          if (tau_pt->at(rest[ii]) > pt) {
            pt = tau_pt->at(rest[ii]);
            if (highest > -1) rest2.push_back(highest);
            highest = rest[ii];
          }
          else {
	    rest2.push_back(rest[ii]);
	  }
        }
        orderedTau.push_back(highest);
        rest = rest2;
      }



      //start loop over reconstructed muons
      bool filled_histos = false;
      for (unsigned int ii = 0; ii < orderedMu.size(); ++ii) {
	if (filled_histos) break;//if we've filled the histos once, break out of the loop
	int iMu = orderedMu[ii];
	if (mu_ibt_pt->at(iMu) < 53.0) continue;
	if (!mu_isHighPtMuon->at(iMu)) continue;
	if (fabs(mu_ibt_eta->at(iMu)) > 2.4) continue;
	bool goodGlob = mu_isGlobalMuon->at(iMu) && mu_gt_normalizedChi2->at(iMu) < 3 && mu_combinedQuality_chi2LocalPosition->at(iMu) < 12 && mu_combinedQuality_trkKink->at(iMu) < 20;
	bool isMedium2016 = mu_isLooseMuon->at(iMu) && mu_innerTrack_validFraction->at(iMu) > 0.49 && mu_segmentCompatibility->at(iMu) > (goodGlob ? 0.303 : 0.451);


	TLorentzVector mu_p4, mu_ibt_transp4;
	mu_p4.SetPtEtaPhiM(mu_ibt_pt->at(iMu), mu_ibt_eta->at(iMu), mu_ibt_phi->at(iMu), mu_mass);
	mu_ibt_transp4.SetPxPyPzE(mu_ibt_px->at(iMu), mu_ibt_py->at(iMu), 0, mu_ibt_pt->at(iMu));

	//start loop over reconstructed taus
	for (unsigned int jj = 0; jj < orderedTau.size(); ++jj) {
	  if (filled_histos) break;//if we've filled the histos once, break out of the loop
	  int iTau = orderedTau[jj];

	  TLorentzVector tau_p4, tau_TES_p4, vis_p4, met_p4, metmu_p4, total_p4;
	  float met_px = MET_T1Txy_Px;
	  float met_py = MET_T1Txy_Py;
	  float met_pt = MET_T1Txy_Pt;
	  tau_p4.SetPtEtaPhiE(tau_pt->at(iTau), tau_eta->at(iTau), tau_phi->at(iTau), tau_energy->at(iTau));
	  met_p4.SetPxPyPzE(met_px, met_py, 0, met_pt);
	  
	  vis_p4 = tau_p4 + mu_p4;
	  total_p4 = vis_p4 + met_p4;
	  metmu_p4 = met_p4 + mu_p4;
	  
	  if (tau_pt->at(iTau) < 0) continue;
	  if (tau_p4.Pt() < 30.0) continue;
	  if (fabs(tau_eta->at(iTau)) > 2.3) continue;
	  if (tau_decayModeFinding->at(iTau) < 0.5) continue;
	  if (tau_againstMuonTight3->at(iTau) < 0.5) continue;
	  if (tau_againstElectronVLooseMVA6->at(iTau) < 0.5) continue;
	  //if (tau_ptLeadChargedCand->at(iTau) < 5) continue;
	  //if (fabs(tau_dz->at(iTau)) > 0.2) continue;
	  if (fabs(tau_charge->at(iTau)) != 1) continue;

	  float reliso = mu_isoTrackerBased03->at(iMu); //use instead sumofpts divided by muon ibt pt

	  
	  float Mt = -1;
	  if (2 * ( mu_p4.Pt() * met_p4.Pt()  - mu_p4.Px()*met_p4.Px() - mu_p4.Py()*met_p4.Py() ) < 0) {
	    Mt = 0;
	  }
	  else {
	    Mt = sqrt(2 * ( mu_p4.Pt() * met_p4.Pt()  - mu_p4.Px()*met_p4.Px() - mu_p4.Py()*met_p4.Py() ) );
	  }

	  if (reliso > 0.1) continue;
	  if (tau_byTightIsolationMVArun2v1DBoldDMwLT->at(iTau) < 0.5) continue;

	  //MET recalculation because we're using the high-pt muon ID
	  TLorentzVector mu_gt_p4, mu_gt_transp4;
	  mu_gt_p4.SetPxPyPzE(0, 0, 0, 0);
	  mu_gt_transp4.SetPxPyPzE(0, 0, 0, 0);

	  float min_dR = 0.2;
	  for (unsigned int kk=0; kk<mu_gt_pt->size(); ++kk) {
	    if (!mu_isPFMuon->at(kk)) continue;
	    mu_gt_p4.SetPtEtaPhiM(mu_gt_pt->at(kk), mu_gt_eta->at(kk), mu_gt_phi->at(kk), mu_mass);
	    if (mu_gt_p4.DeltaR(mu_p4) > min_dR) continue;
	    min_dR = mu_gt_p4.DeltaR(mu_p4);
	    mu_gt_transp4.SetPxPyPzE(mu_gt_px->at(kk), mu_gt_py->at(kk), 0, mu_gt_pt->at(kk));
	  }
	  met_p4 = met_p4 + mu_gt_transp4 - mu_ibt_transp4;

	  if (Mt < 120) continue;
	  

	  //Pzeta calculation
	  float norm_zeta= norm_F( tau_p4.Px()/tau_p4.Pt()+mu_p4.Px()/mu_p4.Pt(), tau_p4.Py()/tau_p4.Pt()+mu_p4.Py()/mu_p4.Pt() );
	  //cout << norm_zeta << endl;
	  float x_zeta= (tau_p4.Px()/tau_p4.Pt()+mu_p4.Px()/mu_p4.Pt())/norm_zeta;
	  float y_zeta= (tau_p4.Py()/tau_p4.Pt()+mu_p4.Py()/mu_p4.Pt())/norm_zeta;
	  float p_zeta_mis=met_p4.Px()*x_zeta+met_p4.Py()*y_zeta;
	  float pzeta_vis=(tau_p4.Px()+mu_p4.Px())*x_zeta+(tau_p4.Py()+mu_p4.Py())*y_zeta;
	  float cut_zeta= p_zeta_mis-0.85*pzeta_vis;


	  if (final_weight != final_weight) {
	    cout << "Not a number!!!!!!!" << endl;
	    continue;
	  }



	  
	  float dR = tau_p4.DeltaR(mu_p4);
	  float dphi_mutau = 100, dphi_METtau = 100;
	  float large_phi = 100;
	  float small_phi = 100;
	  if (tau_p4.Phi() > mu_p4.Phi()) {
	    large_phi = tau_p4.Phi();
	    small_phi = mu_p4.Phi();
	  }
	  else {
	    small_phi = tau_p4.Phi();
	    large_phi = mu_p4.Phi();
	  }
	  if (fabs(large_phi-small_phi) > fabs(large_phi-(small_phi+2*pi))) {
	    dphi_mutau = fabs(large_phi-(small_phi+2*pi));
	  }
	  else {
	    dphi_mutau = fabs(large_phi-small_phi);
	  }

	  if (tau_p4.Phi() > met_p4.Phi()) {
	    large_phi = tau_p4.Phi();
	    small_phi = met_p4.Phi();
	  }
	  else {
	    small_phi = tau_p4.Phi();
	    large_phi = met_p4.Phi();
	  }
	  if (fabs(large_phi-small_phi) > fabs(large_phi-(small_phi+2*pi))) {
	    dphi_METtau = fabs(large_phi-(small_phi+2*pi));
	  }
	  else {
	    dphi_METtau = fabs(large_phi-small_phi);
	  }


	  float Mcol = GetCollinearMass(tau_p4, mu_p4, met_p4);
	  filled_histos = true;

	  if (dR < 0.5) continue;
	  h[1]->Fill(vis_p4.M(), final_weight);
	  h[2]->Fill(total_p4.M(), final_weight);
	  h[3]->Fill(Mcol, final_weight);

	  float Mres = (vis_p4.M() - gen_totalp4.M())/gen_totalp4.M();
	  h[4]->Fill(Mres, final_weight);

	  Mres = (total_p4.M() - gen_totalp4.M())/gen_totalp4.M();
	  h[5]->Fill(Mres, final_weight);
	  
	  Mres = (Mcol - gen_totalp4.M())/gen_totalp4.M();
	  h[6]->Fill(Mres, final_weight);
	}//loop over taus
      }//loop over muons
   }//loop over events


   file_out->cd();
   for (unsigned int i = 0; i<histo_names.size(); ++i) h[i]->Write();
   file_out->Close();
}
