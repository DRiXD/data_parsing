import yaml
import os


#path to DriveU anntotations file
annotation_path= "./Fulda_all.yml"

def read_labels():
    with open(annotation_path) as file:
        labels_list = yaml.load(file, Loader=yaml.FullLoader)
    return labels_list


def create_directory():
    path = os.getcwd()
    path = path + "/build/train"
    try:
        os.mkdir(path)

    except OSError:
        print("Creation of the directory %s failed" % path)
    else:
        print("Successfully created the directory %s " % path)


def write_to_file(filename):
    labels_file = open("build/train/train.txt", "a+")
    labels_file.write("./" + filename + ".jpg \n")
    labels_file.close()


def read_image_name(dict):
    path = dict.get("path")
    start_of_image_name = path.rfind("/")
    image_name = ""
    for i in range(start_of_image_name + 1, len(path) - 5):
        image_name = image_name + path[i]
    return image_name


def main():
    labels_List = read_labels()
    create_directory()

    for dict in labels_List:
        filename = read_image_name(dict)
        write_to_file(filename)


if __name__ == "__main__":
    main()
