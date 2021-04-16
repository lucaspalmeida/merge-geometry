import arcpy
import os

####################### Definindo a Funçao Merge Folder #######################

def merge_folder(folder_input,folder_output):
    dirlist = os.listdir(folder_input)
    shplist = []

######################### Criando Lista com Shapefile #########################

    for item in dirlist:
        if item[-4:] == '.shp':
            shplist.append(item)
    print('\n')
    print('Executando...\n\n'+'Os arquivos com extensão .shp listados em '
          +folder_input+' são:\n')
    print(shplist)
    print('\n')

######################### Criando Lista com Geometria #########################

    listgeometry = []
    for i in shplist:
        listgeometry.append(arcpy.Describe(folder_input+'\\'+i).shapeType)
    print(listgeometry)
    print('\n')

################### Testando Compatibilidade das Geometrias ###################

    if len(set(listgeometry)) != 1:
        print('Os arquivos não possuem feições compatíveis.\n'+
              'Todos os arquivos devem possuir a mesma geometria.')
        print('\n')
        return
    else:
        print('Todas as geometrias foram verificadas.')
        print('\n')

########################## Executando a Função Merge ##########################

    print('Executando a função merge...\n')
    arcpy.env.workspace = folder_input
    arcpy.Merge_management(shplist,folder_output+'\\'+'merge.shp')
    print('Pronto!')
