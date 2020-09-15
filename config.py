from io import StringIO
import pandas as pd
import unicodedata
import re




def ordenarEntregas(df):
    newDataFrame = pd.DataFrame(columns =  ['Quantity', 'Product Name','Customer Name','Phone','Address'])
    includeCAM(df,newDataFrame)
    includeLFA(df,newDataFrame)
    includeSAL(df,newDataFrame)
    includeSFO(df,newDataFrame)
    includeExcept(df,newDataFrame)
    ordenarDataFrame = newDataFrame.reset_index()
    return ordenarDataFrame

def removeAccent(text):
        nfkd = unicodedata.normalize('NFKD', text.lower())
        processedText = u"".join([c for c in nfkd if not unicodedata.combining(c)])
        return re.sub('[^a-zA-Z0-9 \\\]', ' ', processedText)

def includeSAL(df,ordenDf):
    for index, x in df.iterrows():
        if removeAccent(str(df['Address'][index])).__contains__("salvador"):
            ordenDf.loc[index] = [df['Quantity'][index],df['Product Name'][index],df['Customer Name'][index],df['Phone'][index],df['Address'][index]]
        x != None

def includeCAM(df,ordenDf):
    for index, x in df.iterrows():
        if removeAccent(str(df['Address'][index])).__contains__("camacari"):
            ordenDf.loc[index] = [df['Quantity'][index],df['Product Name'][index],df['Customer Name'][index],df['Phone'][index],df['Address'][index]]
        x != None

def includeSFO(df,ordenDf):
    for index, x in df.iterrows():
        if removeAccent(str(df['Address'][index])).__contains__("simoes filho"):
            ordenDf.loc[index] = [df['Quantity'][index],df['Product Name'][index],df['Customer Name'][index],df['Phone'][index],df['Address'][index]]
        x != None

def includeLFA(df,ordenDf):
    for index, x in df.iterrows():
        if removeAccent(str(df['Address'][index])).__contains__("lauro de freitas"):
            ordenDf.loc[index] = [df['Quantity'][index],df['Product Name'][index],df['Customer Name'][index],df['Phone'][index],df['Address'][index]]
        x != None

def includeExcept(df,ordenDf):
    for index, x in df.iterrows():
        if not removeAccent(str(df['Address'][index])).__contains__("lauro de freitas") and not removeAccent(str(df['Address'][index])).__contains__("simoes filho") and not removeAccent(str(df['Address'][index])).__contains__("salvador") and not removeAccent(str(df['Address'][index])).__contains__("camacari"):
            ordenDf.loc[index] = [df['Quantity'][index],df['Product Name'][index],df['Customer Name'][index],df['Phone'][index],df['Address'][index]]
        x != None