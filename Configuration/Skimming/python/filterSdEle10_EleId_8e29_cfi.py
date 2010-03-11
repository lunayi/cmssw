import FWCore.ParameterSet.Config as cms
import HLTrigger.HLTfilters.hltHighLevelDev_cfi
filterEle10_EleId_8e29 = HLTrigger.HLTfilters.hltHighLevelDev_cfi.hltHighLevelDev.clone(andOr = True)
filterEle10_EleId_8e29.HLTPaths = ("HLT_Ele10_LW_EleId_L1R",)
filterEle10_EleId_8e29.HLTPathsPrescales  = cms.vuint32(1,)
filterEle10_EleId_8e29.HLTOverallPrescale = cms.uint32(1)
filterEle10_EleId_8e29.andOr = True
