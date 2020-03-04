import yaml
import os


def main():
    path = "./images/Bremen/Bremen1"
    dir_list = os.listdir(path)

    for directory in dir_list:
        if directory[0] == ".":
            print("Directory: " + directory + " has been skipped")
        else:
            directory_path = path + "/" + directory
            file_list = os.listdir(directory_path)

            for file_name in file_list:
                file_path = directory_path + "/" + file_name
                base = os.path.splitext(file_path)[0]
                os.rename(file_path, base + ".jpg")


if __name__ == "__main__":
    main()
