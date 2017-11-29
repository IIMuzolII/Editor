def editor_input():
    cmd = ''
    cont = 1
    while cmd != 'exit':
        cmd = input('%i_ ' % cont)
        cont += 1

editor_input()
