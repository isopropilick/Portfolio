from os import listdir
from os.path import *
import pandas as pd
import os.path


def run():
    files = [f for f in listdir('Out/') if isfile(join('Out/', f))]
    FEjsons = []
    XLSXjsons = []
    for x in files:
        if "json" in x and "availabledata" not in x:
            if "FE" in x:
                FEjsons.append(x)
            else:
                XLSXjsons.append(x)

    for z in XLSXjsons:
        FEdata = pd.read_json('Out/FE-'+z)
        XLSXdata = pd.read_json('Out/'+z)
        if XLSXdata.empty or FEdata.empty:
            print("\033[91mError al procesar " + z + " & FE-" + z + " ", end='')
            if XLSXdata.empty and FEdata.empty:
                print("archivos vacios.")
            elif XLSXdata.empty and not FEdata.empty:
                print("excel vacio, fornt-end con datos.")
            elif FEdata.empty and not XLSXdata.empty:
                print("front-end vacio, excel con datos.")
            else:
                print("error desconocido.")
        else:
            print("\033[96mProcesando "+z+" & FE-"+z+" ...")
            # Check name occurrences
            # Veces que aparece un nombre listado en excel en el front-end
            print("   * Validando concurrencia de nombres...")
            nameoccurrences = pd.DataFrame(columns=['name', 'number', 'ids'])
            for name in XLSXdata['Personnel Name'].unique():
                ids = []
                for num in FEdata.index[FEdata.name == str(name)].tolist():
                    ids.append(FEdata.at[num, 'id'])
                nameoccurrences = nameoccurrences.append({
                    'name': name,
                    'number': FEdata['name'].str.count(name).sum(),
                    'ids': ids
                }, ignore_index=True)

            # Verify total amount
            # Por cada aparicion de una comision en el front end se verifica su existencia exacta en el excel
            print("   * Validando total de comisiones...")
            i=0
            consolidateregistry = pd.DataFrame(columns=['FE-id', 'name', 'FE-amount', 'XLSX-amounts', 'XLSX-total', 'match'])
            for registry in FEdata['id'].unique():
                XLSXamounts=[]
                #print(XLSXdata.index[XLSXdata['Personnel Name'] == FEdata.at[i, 'name']].tolist())
                for currname in XLSXdata.index[XLSXdata['Personnel Name'] == FEdata.at[i, 'name']].tolist():
                    XLSXamounts.append(XLSXdata.at[currname, 'Comision Total a Pagar'])
                consolidateregistry = consolidateregistry.append({
                    'FE-id': registry,
                    'name': FEdata.at[i, 'name'],
                    'FE-amount': FEdata.at[i, 'amountTotal'],
                    'XLSX-amounts': XLSXamounts,
                    'XLSX-total': str(sum(XLSXamounts)),
                    'match': FEdata.at[i, 'amountTotal'] == sum(XLSXamounts)
                }, ignore_index=True)
                i=i+1
            print("   * Escribiendo "+'Out/'+z[:-5]+'/checks.xlsx ...')
            os.mkdir('Out/' + z[:-5] + '/')
            with pd.ExcelWriter('Out/'+z[:-5]+'/checks.xlsx') as writer:
                nameoccurrences.to_excel(writer, sheet_name='Names check')
                consolidateregistry.to_excel(writer, sheet_name='Totals check')
