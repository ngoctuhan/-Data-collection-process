from datetime import datetime
import pandas as pd


def timestamp2offset(file_path: str, output_path: str) -> None:
    """ Covert time column from timestamp format to elan offset format.

    Args:
        file_path(str): directory path of the file need to convert.
        output_path(str): directory path of the file need to write as output.
    
    """
    
    column_names = ['timestamp','x1', 'y1', 'z1','x2', 'y2', 'z2']
    df = pd.read_csv(file_path, header=None, names=column_names)

    data = []
    
    # divide 1000 in order to convert milis to s
    root_time = int(df['timestamp'][0]) /1000.
    
    for idx in range(0, len(df['timestamp'])):
        current_time =  int(df['timestamp'][idx]) 
       
        time = current_time/1000. - root_time
       
        value = (time, df['x1'][idx], df['y1'][idx], df['z1'][idx], df['x2'][idx], df['y2'][idx], df['z2'][idx])
        data.append(value)
    column_names = ['times','x1', 'y1', 'z1','x2', 'y2', 'z2']
    df_save = pd.DataFrame(data, columns = column_names) 
    df_save.to_csv(output_path, header=column_names, sep=',', encoding='utf-8', index=False, float_format="%0.6f")
    # return len(df['timestamp'])


# timestamp2offset("HHHH.txt", 'HHHH.csv')
# timestamp2offset("R.txt", 'R.csv')
