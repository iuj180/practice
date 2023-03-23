import pyrfc
import json
import pandas as pd

f=open("credentials.json")
credentials=json.load(f)

with pyrfc.Connection(**credentials) as conn:
    fields=["WERKS", "MATNR", "CHARG", "LGORT", "CLABS"]
    table='MCHB' 
    Where=['WERKS = 3204 AND CLABS > 0']
    maxrow=10000
    fromrow=0

    result=conn.call("RFC_READ_TABLE", QUERY_TABLE=table, DELIMITER=',', FIELDS=fields,
                                OPTIONS=[{'TEXT': x} for x in Where], ROWCOUNT=maxrow, ROWSKIPS=fromrow)

data = []
for line in result["DATA"]:
    raw_data = line["WA"].strip().split(',')
    data.append(raw_data)

df = pd.DataFrame(data, columns=fields)    
print(df)