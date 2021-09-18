import os

def get_current_dirs():
    """
    Fetch all tags that the user has selected at the moment
    """
    return open(".current").read().split()

def get_available_dirs():
    """
    Fetch all tags that have some associated files to them
    """
    return sorted(os.listdir(".dirs"))

def get_files(dirs):
    """
    Get files associated with the tags provided in 'dirs'.
    """
    available_dirs = get_available_dirs()
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

def filter_files(filenames, dirs):
    """
    Filter available files from provided list of filenames
    """
    available_files = get_files(dirs)
    available_filenames = [f.split("_")[-1] for f in available_files]
    selected_files = [f for f, fname in zip(available_files, available_filenames) if fname in filenames]
    return selected_files

def tag_file(filename, tags):
    """
    Tag file with new tags
    """
    assert len(tags) > 0, "Provide at least 1 tag"

    available_dirs = get_available_dirs()
    selected_dirs = get_current_dirs()
    current_files = get_files(selected_dirs)
    full_filename = current_files[[f.split("_")[-1] for f in current_files].index(filename)]

    for tag in tags:
        current_files = []
        if tag in available_dirs:
            current_files = open(".dirs/" + tag).read().split()

        plain_names = [fname.split("_")[-1] for fname in current_files]
        
        if filename not in plain_names:
            new_files = current_files + [full_filename]

            outf = open(".dirs/" + tag, "w")
            outf.write(" ".join(new_files))
            outf.close()

def open_files(filenames):
    """
    Open all files in 'filenames' that are in current directory
    """
    selected_dirs = get_current_dirs()
    available_dirs = get_available_dirs()
    available_files = get_files(selected_dirs)

    if len(available_files) > 0:
        for f in available_files:
            if f.split("_")[-1] in filenames:
                os.system("open .files/" + f)

def touch_files(filenames):
    """
    Create empty files in the current folder
    """
    letters = string.ascii_lowercase
    
    available_dirs = get_available_dirs()
    selected_dirs = get_current_dirs()
    current_files = get_files(selected_dirs)
    humanreadable_current_files = [f.split("_")[-1] for f in current_files]

    if len(filenames) >= 1:
        if len(selected_dirs) == 0:
            print("No tags available; can't create file!")
            print("Available tags:")
            if len(available_dirs) < 7:
                print("\n".join(available_dirs))
            else:
                print("\n".join(available_dirs[:5]))
                print("...")
                print("\n".join(available_dirs[-1:]))
        else:
            for humanname in filenames:
                if humanname not in humanreadable_current_files:
                    filename = ''.join(random.choice(letters) for i in range(16))
                    filename = filename + "_" + humanname
                    print("Create file: " + humanname)

                    for d in selected_dirs:
                        dpath = ".dirs/" + d
                        d_content = open(dpath).read().split()
                        d_content = d_content + [filename]

                        f = open(dpath, "w")
                        f.write(" ".join(d_content))
                        f.close()

                    filename = ".files/" + filename
                    f = open(filename, "w")
                    f.close()
                else:
                    print(humanname + " already exists for these tags!")

def rm_files(filenames):
    """
    Remove files in current directory.

    Returns True if files were deleted, otherwise false.
    """
    selected_dirs = get_current_dirs()
    available_dirs = get_available_dirs()
    available_files = get_files(selected_dirs)

    if len(selected_dirs) == 0:
        print("Filesystem root")
        return False
    else:
        print("Current tags:")
        print(" ".join(selected_dirs))
        filenames = get_files(selected_dirs)
        if len(filenames) == 0:
            return False
        else:
            humanreadable_files = [f.split("_")[-1] for f in filenames]
            for rmfile in args.rmfiles:
                if rmfile in humanreadable_files:
                    ix = humanreadable_files.index(rmfile)
                    filename = filenames[ix]
                    os.system("rm .files/" + filename)
                    for tag in selected_dirs:
                        dir_files = open(".dirs/" + tag).read().split()
                        dir_files = [f for f in dir_files if "_" + rmfile not in f]
                        d = open(".dirs/" + tag, "w")
                        d.write(" ".join(dir_files))
                        d.close()

            return True

