def do_preprocess():
    """Wrangles the data provided by Biomax"""
    import pandas as pd
    import re
    import numpy as np
    # Import SPARQL result
    data = pd.read_csv('data/NanoSolveIT-KnoweldgeBase_eNM-Ontology-term-use_27-9-22.csv')
    data = data.replace(np.NaN, "")
    iriPattern = re.compile(r'[A-Za-z]+[:_]\d+')
    # Split provided eNM term into IRI and Label
    data['iri'] = [re.search(iriPattern, enmTerm).group().replace("_",":") if re.search(iriPattern, enmTerm) is not None else "" for enmTerm in data['eNM term']]
    data['label'] = [enmTerm.replace(re.search(iriPattern, enmTerm).group(), "") for enmTerm in data['eNM term']]
    # Unpivot based on OECD test guideline
    oecd = data['described variable.OECD Testguideline'].apply(lambda x : pd.Series (str(x).split(";"))).stack()
    data = pd.merge(oecd.reset_index(), data.reset_index(), left_on = 'level_0',    right_on = 'index').rename(columns={0:"oecd_guideline"}).drop(["level_0",  "level_1", "index", "described variable.OECD Testguideline"], axis=1)
    # Unpivot based on described nanomaterial
    nanomaterial = data['described Nanomaterial'].apply(lambda x : pd.Series(str    (x).split(";"))).stack()
    data = pd.merge(nanomaterial.reset_index(), data.reset_index(), left_on =   'level_0', right_on = 'index').rename(columns={0:"nanomaterial"}).drop    (["level_0", "level_1", "index", "described Nanomaterial"], axis=1)
    # Unpivot based on described variable
    variable = data['described variable.Variable'].apply(lambda x : pd.Series(str   (x).split(";"))).stack()
    data = pd.merge(variable.reset_index(), data.reset_index(), left_on =   'level_0', right_on = 'index').rename(columns={0:"variable"}).drop(["level_0",    "level_1", "index", "described variable.Variable"], axis=1)
    # Unpivot based on dataset
    dataset = data['described variable.Dataset'].apply(lambda x : pd.Series(str(x). split(";"))).stack()
    data = pd.merge(dataset.reset_index(), data.reset_index(), left_on =    'level_0', right_on = 'index').rename(columns={0:"dataset"}).drop(["level_0",  "level_1", "index", "described variable.Dataset", "eNM term"], axis=1)
    # Rearrange columns
    data = data[["label","iri", "variable", "dataset", "nanomaterial",  "oecd_guideline"]]
    ## Remove trailing spaces
    for column in data.columns:
        data[column] = [i.lstrip() for i in data[column]]
    ## Export
    data.to_csv("nanosolveit.csv", index=False)
    return data

