from subprocess import Popen

def open_file(path, file_type):

    cmd = ''

    processes = {}

    if file_type == ".pdf":
        cmd = 'evince'

    else:
        cmd = 'vlc'
        
    commands = [[cmd, path, '-f'],['irexec', './src/'+cmd+'_lircrc']]

    for i in commands:
        processes[i[0]] = Popen(i) 

    #Checks if evince has ended, then kills the irexec process
    while True:
        if processes[cmd].poll() != None:
            processes['irexec'].kill()
            return
