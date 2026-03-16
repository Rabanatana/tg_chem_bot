'''
Файл, в котором хранится аналитический модуль для бота:


Генерация основных дескрипторов лекарствоподобия

Генерация изображения

Генерация InChi из SMILES
'''


from rdkit import Chem
from rdkit.Chem import QED

def convert(smiles):
    mol = Chem.MolFromSmiles(smiles)
    inchi_of_mol = Chem.MolToInchi(mol)
    if mol is None:
        return 'mol is None'
    
    prop_of_mol = QED.properties(mol)
    return prop_of_mol, inchi_of_mol

def smiles_to_png(smiles):
    pass


