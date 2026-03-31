'''
Файл, в котором хранится аналитический модуль для бота:


Генерация основных дескрипторов лекарствоподобия

Генерация изображения

Генерация InChi из SMILES
'''


from rdkit import Chem
from rdkit.Chem import QED
from rdkit.Chem import Draw
from pathlib import Path

def smiles_to_mol(smiles):
    '''
    Функция, которая переводит SMILES в объект mol из библиотеки rdkit
    '''
    
    return Chem.MolFromSmiles(smiles)

def file_availability(filename, folder):
    '''
    Функция для проверки наличия файла в папке
    
    Принимает:
    
    filename (str): название файла
    
    folder (str): папка, в которой может находиться файл
    
    Возвращает:
    
    True - файл есть
    
    False - файла нет
    '''
    
    if Path(f'{folder}/{filename}').is_file():
        return True
    return False

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
        print(1)
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
    
    png_name (str) - путь к файлу с изображением
    '''
    
    png_name = smiles + '.png'
    print(f'Название файла: {png_name}')
    print(f'SMILES: {smiles}')
    if file_availability(png_name, 'mol_png'):
        print(f'Файл есть в базе, название: {png_name}')
        return png_name
    Draw.MolToImage(smiles_to_mol(smiles)).save(f'mol_png/{smiles}.png')
    print(2)
    # return Draw.MolToImage(smiles_to_mol(smiles))
    return png_name


smiles_to_png('COc1cc(OC)cc(N(CCCN2CCC(N)C2)c2ccc3ncc(-c4cnn(C)c4)nc3c2)c1.Cl')
print('конец алгоритма')
# print(find_props('OC[C@H]1OC(n2c(NC3CCCCC3)nc3c(SCc4ccccc4)ncnc32)[C@H](O)[C@@H]1O')).save(f'COc1cc(OC)cc(N(CCCN2CCC(N)C2)c2ccc3ncc(-c4cnn(C)c4)nc3c2)c1.Cl.png')