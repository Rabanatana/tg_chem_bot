'''
Файл, в котором хранится аналитический модуль для бота:


Генерация основных дескрипторов лекарствоподобия

Генерация изображения

Генерация InChi из SMILES
'''


from rdkit import Chem
from rdkit.Chem import QED
from rdkit.Chem import Draw

def smiles_to_mol(smiles):
    '''
    Функция, которая переводит SMILES в объект mol из библиотеки rdkit
    '''
    
    return Chem.MolFromSmiles(smiles)

def find_props(smiles):
    '''
    Функция для получения из SMILES  основных характеристик, 
    которые используются в медхимии.
    
    Принимает:
    
    SMILES (str): представление молекулы в виде SMILES
    
    Возвращает:
    
    props_of_mol - именованный список, в котором есть:
        Молярная масса
        Липофильность
        Акцепторы H-связи
        Доноры H-связи
        Полярная площадь
        Вращающиеся связи
        Ароматические кольца
        Структурные алармы
    
    inchi_of_mol (str) - InChi-представление молекулы
    '''
    
    mol = smiles_to_mol(smiles)
    inchi_of_mol = Chem.MolToInchi(mol)
    if mol is None:
        return 'mol is None'
    
    props_of_mol = QED.properties(mol)
    message = (
        f'Молярная масса: {props_of_mol[0]} \n'
        f'Липофильность: {props_of_mol[1]} \n'
        f'Акцепторы H-связи: {props_of_mol[2]} \n'
        f'Доноры H-связи: {props_of_mol[3]} \n'
        f'Полярная площадь: {props_of_mol[4]} \n'
        f'Вращающиеся связи: {props_of_mol[5]} \n'
        f'Ароматические кольца: {props_of_mol[6]} \n'
        f'Структурные алармы: {props_of_mol[7]}'
        
    )
    # print(props_of_mol)
    # print(message)
    return message

def smiles_to_png(smiles):
    '''
    Функция для создания png-картинки из SMILES.
    В будущем начнет читать еще InChi.
    
    Принимает:
    
    smiles (str): представление молекулы в виде SMILES
    
    Возвращает:
    
    Draw.MolToImage - объект изображения
    '''
    print(Draw.MolToImage(smiles_to_mol(smiles)))
    return Draw.MolToImage(smiles_to_mol(smiles))


# smiles_to_png('OC[C@H]1OC(n2c(NC3CCCCC3)nc3c(SCc4ccccc4)ncnc32)[C@H](O)[C@@H]1O').save('test.png')
print(find_props('OC[C@H]1OC(n2c(NC3CCCCC3)nc3c(SCc4ccccc4)ncnc32)[C@H](O)[C@@H]1O'))