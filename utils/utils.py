import pandas as pd

pd.options.mode.chained_assignment = None  # default='warn'

df = pd.read_csv('https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/somministrazioni-vaccini-summary-latest.csv')

df["data_somministrazione"] = pd.to_datetime(df.data_somministrazione)
df = df.sort_values(by=['data_somministrazione'])

regioni = pd.read_csv("regioni.tsv",sep="\t")
it_pop = sum(regioni["popolazione"])

def get_data(regione):
    if regione not in set(regioni["regione"]):
        print ("Errore! Controlla il nome corretto della regione o area amministrativa:", set(regioni["regione"]))
        return None, None,None,None,None
    code = regioni[regioni["regione"]==regione]["codice"].values[0]
    pop = regioni[regioni["regione"]==regione]["popolazione"].values[0]
    rg = df[df["area"]==code]
    return code, pop, rg,df,it_pop