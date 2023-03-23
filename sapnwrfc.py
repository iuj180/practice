from pyrfc import Connection
import re


class main():
    def __init__(self):
        ASHOST='165.244.245.200'
        CLIENT='100'
        SYSNR='00'
        USER='c002102'
        PASSWD='whflq11+'
        self.conn = Connection(ashost=ASHOST, sysnr=SYSNR, client=CLIENT, user=USER, passwd=PASSWD)
    
    def qry(self, Fields, SQLTable, Where = '', MaxRows=50, FromRow=0):
        """A function to query SAP with RFC_READ_TABLE"""


        # By default, if you send a blank value for fields, you get all of them
        # Therefore, we add a select all option, to better mimic SQL.
        if Fields[0] == '*':
            Fields = ''
        else:
            Fields = [{'FIELDNAME':x} for x in Fields] # Notice the format


        # the WHERE part of the query is called "options"
        options = [{'TEXT': x} for x in Where] # again, notice the format


        # we set a maximum number of rows to return, because it's easy to do and
        # greatly speeds up testing queries.
        rowcount = MaxRows


        # Here is the call to SAP's RFC_READ_TABLE
        tables = self.conn.call("RFC_READ_TABLE", QUERY_TABLE=SQLTable, DELIMITER='|', FIELDS = Fields,
                                OPTIONS=options, ROWCOUNT = MaxRows, ROWSKIPS=FromRow)


        # We split out fields and fields_name to hold the data and the column names
        fields = []
        fields_name = []


        data_fields = tables["DATA"] # pull the data part of the result set
        data_names = tables["FIELDS"] # pull the field name part of the result set


        headers = [x['FIELDNAME'] for x in data_names] # headers extraction
        long_fields = len(data_fields) # data extraction
        long_names = len(data_names) # full headers extraction if you want it


        # now parse the data fields into a list
        for line in range(0, long_fields):
            fields.append(data_fields[line]["WA"].strip())


        # for each line, split the list by the '|' separator
        fields = [x.strip().split('|') for x in fields ]


        # return the 2D list and the headers
        return fields, headers

# Choose your fields and table
fields = ['WERKS', 'MATNR', 'CHARG', 'LGORT', 'CLABS'] 
table = 'MCHB' 

# you need to put a where condition in there... could be anything
# where = ['PERNR = 00001111 AND STATUS = 30 AND WORKDATE = 20150803']
where = ['WERKS = 3204 AND CLABS > 0']

# max number of rows to return
maxrows = 10000

# starting row to return
fromrow = 0

# query SAP
s=main()
results, headers = s.qry(fields, table, where, maxrows, fromrow)

# print(headers)
# print(results)

import pandas as pd
df = pd.DataFrame(results, columns = ['WERKS','MATNR','CHARG','LGORT','CLABS'])
print(df)




