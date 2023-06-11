import os
import shutil

def function(directory, new_derictory):
    for file_name in os.listdir(directory):
        if file_name.endswith(".jpg"):
            first_word = file_name.split(" ", 1)[0].split("(")[0].split(".")[0].split("_")[0]
            new_folder = new_directory + first_word
            if not os.path.exists(new_folder):
                os.mkdir(new_folder)
                shutil.copy(directory + file_name, new_folder + "\\" + file_name)
            else:
                shutil.copy(directory + file_name, new_folder + "\\" + file_name)

if __name__ == '__main__':
    directory = "E:\\code\\sort_folders\\foto-filtry-nordfil\\"
    new_directory = "E:\\code\\sort_folders\\foto-filtry-nordfil-go\\"
    function(directory, new_directory)
