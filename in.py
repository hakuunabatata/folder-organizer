import os

basePath = os.getcwd()


def createPath(paths):
    return '/'.join(paths)


def organizeFolder(path):

    print(f'...organizing {path}')

    os.chdir(path)

    files = os.listdir(path)

    for file in files:
        filePath = createPath([path, file])

        if ('.' in file):
            print(f'...analysing file {file}')
            name, extension = file.split('.')

            if (extension not in os.listdir(path)):
                os.mkdir(extension)
                print(f'...creating dir {extension} in {path}')

            os.rename(filePath,
                      createPath([path, extension, file]))

            print(f'...moving {name} to {extension} folder')
        else:
            print(f'...analysing folder {file}')
            if (os.listdir(filePath) == []):
                os.rmdir(filePath)
                print(f'...deleting empty folder {file}')

            else:
                organizeFolder(filePath)
                os.chdir(path)


path = createPath([basePath, input('Qual diretório quer organizar?\n\n')])

organizeFolder(path)
