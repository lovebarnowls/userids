from .Utils import Utils

def Not_owned_by_group(setting):
    data = setting.split(':',1)
    filename = data[0]
    group = data[1]
    command = 'ls -l ' + str(filename)
    result = (Utils.run_command(command).decode()).split(' ')[3]
    if result == group:
        return False
    else:
        return True
