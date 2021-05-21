from netpyne import specs
from netpyne.batch import Batch

def changeIClamp():
        # Create variable of type ordered dictionary (NetPyNE's customized version)
        params = specs.ODict()

        # fill in with parameters to explore and range of values (key has to coincide with a variable in simConfig)
        params['clampAmplitude']=[0.05, 0.1, 0.2, 0.4, 0.6]
        params['stimDur']=[10, 100, 200, 500]

        # create Batch object with parameters to modify, and specifying files to use
        b = Batch(params=params, cfgFile='tut8_cfg_IClamp.py', netParamsFile='tut8_netParams_IClamp.py',)

        # Set output folder, grid method (all param combinations), and run configuration
        b.batchLabel = 'IClamp'
        b.saveFolder = 'tut8_data_IClamp'
        b.method = 'grid'
        b.runCfg = {'type': 'mpi_bulletin',
                            'script': 'tut8_init.py',
                            'skip': True}

        # Run batch simulations
        b.run()

def changeNetStims():
        # Create variable of type ordered dictionary (NetPyNE's customized version)
        params = specs.ODict()

        # fill in with parameters to explore and range of values (key has to coincide with a variable in simConfig)
        params['netWeight']=[0.0005, 0.0010, 0.0025]
        params['interStimInterval'] = [ 5, 2.5, 1, 0.5, 0.1]

        # create Batch object with parameters to modify, and specifying files to use
        b = Batch(params=params, cfgFile='tut8_cfg_NetStims.py', netParamsFile='tut8_netParams_NetStims.py',)

        # Set output folder, grid method (all param combinations), and run configuration
        b.batchLabel = 'NetStims'
        b.saveFolder = 'tut8_data_NetStims'
        b.method = 'grid'
        b.runCfg = {'type': 'mpi_bulletin',
                            'script': 'tut8_init.py',
                            'skip': True}

        # Run batch simulations
        b.run()

def changeCellParameters():
        # Create variable of type ordered dictionary (NetPyNE's customized version)
        params = specs.ODict()

        # fill in with parameters to explore and range of values (key has to coincide with a variable in simConfig)
        # params['gkBar'] = [0.036,0.072,0.108]
        params['eLeak'] = [-90, -80, -70, -60]

        # create Batch object with parameters to modify, and specifying files to use
        b = Batch(params=params, cfgFile='tut8_cfg_CellParams.py', netParamsFile='tut8_netParams_CellParams.py',)

        # Set output folder, grid method (all param combinations), and run configuration
        b.batchLabel = 'CellParams'
        b.saveFolder = 'tut8_data_CellParams'
        b.method = 'grid'
        b.runCfg = {'type': 'mpi_bulletin',
                            'script': 'tut8_init.py',
                            'skip': True}

        # Run batch simulations
        b.run()

def changeNetworkParameters():
        # Create variable of type ordered dictionary (NetPyNE's customized version)
        params = specs.ODict()

        # fill in with parameters to explore and range of values (key has to coincide with a variable in simConfig)
        params['conProb']=[0.1, 0.25, 0.5, 1.0]
        
        # create Batch object with parameters to modify, and specifying files to use
        b = Batch(params=params, cfgFile='tut8_cfg_NetPar.py', netParamsFile='tut8_netParams_NetPar.py',)

        # Set output folder, grid method (all param combinations), and run configuration
        b.batchLabel = 'NetPar'
        b.saveFolder = 'tut8_data_NetPar'
        b.method = 'grid'
        b.runCfg = {'type': 'mpi_bulletin',
                            'script': 'tut8_init.py',
                            'skip': True}

        # Run batch simulations
        b.run()

# Main code
if __name__ == '__main__':
        # changeIClamp()
        changeNetStims()
        # changeCellParameters()
        # changeNetworkParameters()