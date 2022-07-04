import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        'root://eospublic.cern.ch//eos/opendata/cms/Run2015D/DoubleEG/MINIAOD/08Jun2016-v1/10000/00387F48-342F-E611-AB5D-0CC47A4D76AC.root'
    )
)

process.demo = cms.EDAnalyzer('MiniAnalyzer',
	electrons = cms.InputTag("slimmedElectrons")
)

# write the output into a root file
process.TFileService = cms.Service("TFileService", fileName=cms.string("electron_pt.root"))

process.p = cms.Path(process.demo)
