import socket, traceback
import pandas as pd
import time
from sklearn.externals import joblib
from tsfresh.feature_extraction import extract_features, EfficientFCParameters, MinimalFCParameters,ComprehensiveFCParameters
from io import StringIO
from sklearn.ensemble import RandomForestClassifier

header = ['Timestamp','Ac-x','Ac-y','Ac-z','Gy-x','Gy-y','Gy-z','marker']
fc_parameters = {
    'abs_energy':None,
    'maximum': None,
    'mean': None,
    'median': None,
    'minimum': None,
    'standard_deviation': None,
    'variance': None,
    'kurtosis': None,
    'skewness': None,
}
rf_model = joblib.load('RandomForest')
host = '192.168.43.1'
port = 5545

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind((host, port))
count = 40
while 1:
    row = ''
    for i in range(40):
        try:
            message, address = s.recvfrom(8192)
            row = row + bytes.decode(message)[:-2] + ',1\n'
        except (KeyboardInterrupt, SystemExit):
            #dataset.close()
            print('\nClosing.')
            raise
        except:
            traceback.print_exc()
    df = pd.read_csv(StringIO(row))
    df.columns = header
    df_proccessed = extract_features(df,fc_parameters,n_jobs=3,column_sort='Timestamp',column_id='marker',disable_progressbar=True)
    print(rf_model.predict(df_proccessed.as_matrix()))
