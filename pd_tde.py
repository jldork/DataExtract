#!/usr/bin/python
# 2/8/2015
# Written in this ipython notebook 
# http://nbviewer.ipython.org/github/Btibert3/tableau-r/blob/master/Python-R-Tableau-Predictive-Modeling.ipynb

import dataextract as tde
import pandas as pd

fieldMap = { 
    'float64' :     tde.Type.DOUBLE,
    'float32' :     tde.Type.DOUBLE,
    'int64' :       tde.Type.DOUBLE,
    'int32' :       tde.Type.DOUBLE,
    'object':       tde.Type.UNICODE_STRING,
    'bool' :        tde.Type.BOOLEAN
}

def pd_tde(df,fname):
	try:
		os.system('rm -f ' + fname)
		os.system('rm -f DataExtract*.log')
		tdefile = tde.Extract(fname)
	except:
		tdefile = tde.Extract(fname)

	tableDef = tde.TableDefinition()
	colnames = df.columns
	coltypes = df.dtypes

	# for each column, add the appropriate info the Table Definition
	for i in range(0, len(colnames)):
		cname = colnames[i]
    		ctype = fieldMap.get(str(coltypes[i]))
    		tableDef.addColumn(cname, ctype)  		

	with tdefile as extract:
		table = extract.addTable("Extract", tableDef)
	
		for r in range(0, df.shape[0]):
        		row = tde.Row(tableDef)
        	for c in range(0, len(coltypes)):
            		if str(coltypes[c]) == 'float64':
            		    row.setDouble(c, df.iloc[r,c])
            		elif str(coltypes[c]) == 'float32':
            		    row.setDouble(c, df.iloc[r,c])
            		elif str(coltypes[c]) == 'int64':
            		    row.setDouble(c, df.iloc[r,c])   
            		elif str(coltypes[c]) == 'int32':
            		    row.setDouble(c, df.iloc[r,c])
            		elif str(coltypes[c]) == 'object':
            		    row.setString(c, df.iloc[r,c]) 
            		elif str(coltypes[c]) == 'bool':
            		    row.setBoolean(c, df.iloc[r,c])
            		else:
            		    row.setNull(c)
        	# insert the row
        	table.insert(row)
