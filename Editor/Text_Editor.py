import os

def editor_input():
    cont = 1
    nome = input("Name of the File: ")

    while 1:
        cmd = input('%i  ' % cont)

        if cmd == 'exit':
            break

        elif cmd == 'compile':
            os.system('cls')
            os.system('python %s' % nome)
            os.system('pause')
            os.system('cls')
            break
            

        save(cmd, nome)
        cont += 1

def save(cmd, nome):
    fl = open(nome, 'a')
    fl.write(cmd + '\n')
    fl.close()

editor_input()
    
