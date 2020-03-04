import yaml
import os


def read_labels():
    with open(r"./DTLD_Labels copy/Bremen_all.yml") as file:
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
    path = path + "/build/darknet_labels"
    try:
        os.mkdir(path)
    except OSError:
        print("Creation of the directory %s failed" % path)
    else:
        print("Successfully created the directory %s " % path)


def write_labels_to_file(label_string, filename):
    labels_file = open("build/darknet_labels/" + str(filename) + ".txt", "a+")
    labels_file.write(label_string + "\n")
    labels_file.close()


def generate_label_string(box):
    # Format: <object-class> <x_center> <y_center> <width> <height>

    object_class = box.get("class_id")

    width = box.get("width") / 2048
    height = box.get("height") / 1024

    x = (box.get("x") + width / 2 - height / 2) / 2048
    y = (box.get("y") + width / 2 - height / 2) / 1024

    parameter_string = (
        str(object_class)
        + " "
        + str(x)
        + " "
        + str(y)
        + " "
        + str(width)
        + " "
        + str(height)
    )
    return parameter_string


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
        for box in dict.get("objects"):
            label_string = generate_label_string(box)
            write_labels_to_file(label_string, filename)


if __name__ == "__main__":
    main()
