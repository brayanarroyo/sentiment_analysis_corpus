import pandas as pd

df = pd.read_csv("data/DL-Secretaria-de-Salud-Colima.csv")
cor = pd.read_csv("data/Lexicon.csv")
cont = 0
result = []
for row in df["message"]:
    if pd.notnull(row):
        pal = row.split()
        for i in pal:
            a = cor[cor["Palabras"] == i]["Valor"]
            if a.empty != True:
                if a.to_string(index=False) == "1":
                    cont += 1
                else:
                    cont -= 1
        if cont > 0:
            result.append("Positivo")
        elif cont < 0:
            result.append("Negativo")
        else:
            result.append("Neutro")
        cont = 0
            #print(dtypes(a))
            #print(a.values)
            # print(a.to_string(index=False))
            #print(type(a))
            # print(a.name)
            # for j in range(len(cor)):
            #     a =cor[cor[i == cor["Palabras"]]]
            #     print(cor.loc[j,"Palabras"])
            #     if i.find(cor.loc[j,"Palabras"]):            
            #         print(cor.loc[j,"Valor"]) 
    else:
        result.append("Neutro")

df["Sentiment"] = result   
print(df) 

print ('exporting data...')
df.to_csv (r'data\data-test-analyzed.csv', index = False, header=True)

