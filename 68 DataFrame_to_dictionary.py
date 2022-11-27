import pandas as pd
state_df=pd.read_csv('states.csv')
print(state_df)
state_dict=state_df.to_dict()
print("Result dict:\n",state_dict)

#List
state_df=pd.read_csv('states.csv')
print(state_df)
state_dict=state_df.to_dict('list')
print("Result dict:\n",state_dict)

# Series
state_df=pd.read_csv('states.csv')
print(state_df)
state_dict=state_df.to_dict('series')
print("Result dict:\n",state_dict)

# DataFrame to dict without header and index
state_df=pd.read_csv('states.csv')
print(state_df)
state_dict=state_df.to_dict('split')
print("Result dict:\n",state_dict)
print("\n List of values from DF without index and header:\n",state_dict['data'])


#DataFrame to dict by rows
#state_df=pd.read_csv('states.csv')
#print(state_df)
#state_dict=state_df.to_dict('record')
#print("Result dict:\n",state_dict)

# DataFrame to dict by row index

state_df=pd.read_csv('states.csv')
print(state_df)
state_dict=state_df.to_dict('index')
print("Result dict:\n",state_dict)

#DataFrame to dict with one column as the key
state_df=pd.read_csv('states.csv')
print(state_df)
state_dict=state_df.set_index('State').to_dict()['Population']
print(state_dict)