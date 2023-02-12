import user_interface as ui

def name_file (n):
    n1=n+'.txt'
    f = open (n1, 'w')
    f.close
    return n

def record_data (n,x,y,z,w):
    name = n+'.txt'
    l = []
    f = open (name, 'a')
    f.writelines (f'\n{x},{y},{z},{w}')
    f.close
