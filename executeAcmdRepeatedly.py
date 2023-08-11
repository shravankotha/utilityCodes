import os
import sys


def main():    
    nArguments = len(sys.argv)
    if nArguments != 5:
        text = """Four command line arguments are expected: \
                \n\t(1) substring of the directories \
                \n\t(2) starting directory number \
                \n\t(3) ending directory number \
                \n\t(4) command to execute in each directory """
        raise RuntimeError(text)

    directory_substring = str(sys.argv[1])
    startDirectoryNumber = int(sys.argv[2])
    endDirectoryNumber = int(sys.argv[3])
    command_to_execute = str(sys.argv[4])
    pwd = os.getcwd()
    
    for iDir in range(startDirectoryNumber,endDirectoryNumber+1):
        directoryName = str(pwd) + '\\' + str(directory_substring) + str(iDir)
        os.chdir(directoryName)
        print('*************************************************************************************************************************************************************************************')
        print('executing cmd from :', directoryName)
        print('*************************************************************************************************************************************************************************************')
        os.system(command_to_execute)

if __name__ == "__main__":
    main()