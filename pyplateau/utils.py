import os

def get_current_dirs():
    return open(".current").read().split()

def get_available_dirs():
    return sorted(os.listdir(".dirs"))

def get_files(dirs, available_dirs):
    if len(dirs) == 0:
        return []
    else:
        all_found = True
        for d in dirs:
            if d not in available_dirs:
                all_found = False
        if all_found:
            allfiles = {}
            for ad in dirs:
                afiles = open(".dirs/" + ad).read().split()
                for f in afiles:
                    allfiles[f] = allfiles.get(f, 0) + 1

            allfiles = [f for f in allfiles if allfiles[f] == len(dirs)]
            return allfiles
        else:
            return []
