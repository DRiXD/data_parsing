import yaml
import os


def read_labels():
    with open(r"./Fulda_all.yml") as file:
        # The FullLoader parameter handles the conversion from YAML
        # scalar values to Python the dictionary format
        labels_list = yaml.load(file, Loader=yaml.FullLoader)

        # print(labels_list[0])
        # print("TEST")
        # print(labels_list[0].get("objects")[0].get("x"))
        # print(len(labels_list))
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
    labels_file.write("E:\Datasets\DriveU_Fulda/" + filename + ".jpg \n")
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
