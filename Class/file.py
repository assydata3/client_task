import json
import urllib.request
import os , shutil

####========================= LOCAL FILE / FOLDER ===================================####
###1.File Local
def delete_file(file_url):
    if os.path.exists(file_url):
       os.remove(file_url)
    else:
       print("The file does not exist")


def copy_file(source, destination, method):
    if method == 'copyfile':
        shutil.copyfile(source, destination)

    if method == 'copy':
        shutil.copy(source, destination)

    if method == 'copy2':
        shutil.copy2(source, destination)

###2.Folder Local
def delete_folder(path_delete):
   isExist = os.path.exists(path_delete)
   if isExist:
        try:
            shutil.rmtree(path_delete)
        except OSError as e:
            print ("Error: %s - %s." % (e.filename, e.strerror))


def make_folder(path_folder_parent,folder_name):
    path_folder=path_folder_parent + '/' + folder_name
    check_exit_folder = os.path.exists(path_folder)

    if check_exit_folder:
        print(f'''Path: {path_folder } : done''')
    else:
        print(f'''Make Folder: {path_folder }''')
        os.makedirs(path_folder)
    return path_folder
####==================================================================================####





####==================================== JSON FILE ===================================####
def write_json(dic_data,json_file):
    with open(json_file, "w") as outfile:
      json.dump(dic_data, outfile)


def read_json(json_file_name):
    with open(json_file_name) as fp:
      data_load = json.load(fp)
    return data_load


def read_json_web(json_file_name):
    url_server = urllib.request.urlopen(json_file_name)
    data_server = json.loads(url_server.read().decode())
    return data_server
####==================================================================================####


#
# copy_file('C:/assydata.pdf','test/file1.pdf','copyfile')