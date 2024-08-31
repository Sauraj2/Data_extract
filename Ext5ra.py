import pandas as pd  
import re

fi='CMdb.xlsx'
df=pd.read_excel(fi)
def fetch_data(inpu):
    #fra3pdtawdhrestgwdb3v
    #AMSPDCLD2-cbam18-appX.cbaminternal
    
    df['CI Name*'] = df['CI Name*'].str.strip().str.lower()
    inpu = inpu.strip().lower()

    # Filter the DataFrame
    filtered_df = df[df['CI Name*'] == inpu][['L1', 'L2','Cloud', 'CI Name*','Tier 1']]
    print(filtered_df.to_string(index=False))
fetch_data('apn01rds02')