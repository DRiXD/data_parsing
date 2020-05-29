import yaml
import os


def read_labels():
    with open(r"./Fulda_all.yml") as file:
        labels_list = yaml.load(file, Loader=yaml.FullLoader)
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
    
    class_id = box.get("class_id")
    print('class_id')
    print(str(class_id)[4])
    object_class = str(class_id)[4]


    width = box.get("width") / 2048
    height = box.get("height") / 1024

    x = (box.get("x") + box.get("width") / 2 + box.get("height") / 2) / 2048
    y = (box.get("y") + box.get("width") / 2 + box.get("height") / 2) / 1024

    if(x<0):
        x = 0.0
    if(y<0):
        y= 0.0
    if(width<0):
        width = 0.0
    if(height<0):
        height = 0.0

    if(x>1.0):
        x = 1.0
    if(y>1.0):
        y= 1.0
    if(width>1.0):
        width = 1.0
    if(height>1.0):
        height = 1.0

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
