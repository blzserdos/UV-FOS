def import_data(dtype='arr'): 
    '''
    Import the UV_FOS data set, generated by the PrOSt! project.
	
	arguments
		dtype: determines the data format returned by the function.
				dtype = 'arr' returns numpy array of shape (189, 40)
				dtype = 'pd' returns pandas dataframe of shape (189, 40)

    returns     
        UV_FOS data set. The shape is (189, 40), where shape[0] corresponds to the number of observation
        and shape[1] to the number of featurs. note that shape[1] = 40 which contains
        the 6 target variables!
    '''
    import numpy as np
    import pandas as pd
    
    T = 'c:/Users/furiu/Documents/UV/UV_FOS/python/Target_data.txt'
    I = 'c:/Users/furiu/Documents/UV/UV_FOS/python/Input_data.txt'
    Icols = pd.read_csv(I, nrows=0, header=None, delimiter='\t').columns
    Tcols = pd.read_csv(T, nrows=0, header=None ,delimiter='\t').columns

    Tnames = ['GF3', 'GF2', 'GF', 'G', 'F', 'sumFOS']
    Inames = np.arange(300,200,-3).tolist()

    Inputs = pd.read_csv(I,delimiter='\t', header=None, usecols=Icols[2:])
    Targets = pd.read_csv(T,delimiter='\t', header=None, usecols=Tcols[2:])

    Inputs.columns = Inames
    Targets.columns = Tnames

    if dtype == 'arr':
    	data = pd.concat([Inputs, Targets], axis=1).values
    elif dtype == 'pd':
    	data = pd.concat([Inputs, Targets], axis=1)
    else:
    	print('unknown type, use "arr" or "pd" ')
    return data
