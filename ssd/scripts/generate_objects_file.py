import json
import yaml
import os



def write_json_file(data):
    with open("./build/ssd/TRAIN_objects.json", "w") as outfile:
        json.dump(data, outfile)


def read_labels():
    with open(r"./Fulda_all.yml") as file:
        
        labels_list = yaml.load(file, Loader=yaml.FullLoader)
    return labels_list


def create_directory():
    path = os.getcwd()
    path = path + "/build/ssd"
    try:
        os.mkdir(path)
    except OSError:
        print("Creation of the directory %s failed" % path)
    else:
        print("Successfully created the directory %s " % path)


def generate_label_dict(dict):
    boxes_list = []
    labels_list = []
    difficulties_list = []
    for box in dict.get("objects"):
        class_id = box.get("class_id")
        class_id_4 = str(class_id)[4]
        object_class = int(class_id_4) + 1

        width = box.get("width")
        height = box.get("height")
        x_top_left = box.get("x")
        y_top_left = box.get("y")

        # calculate boundary coordinates
        x_min = x_top_left
        x_max = (x_top_left + width) 
        y_min = y_top_left 
        y_max = (y_top_left + height)

        if(x_min > 2048):
            x_min=2047
        if(x_max > 2048):
            x_max=2047
        if(y_min > 1024):
            y_min=1023
        if(y_max > 1024):
            y_max=1023

        if(x_min < 0):
            x_min=1
        if(x_max < 0):
            x_max=1
        if(y_min < 0):
            y_min=1
        if(y_max < 0):
            y_max=1

        boxes_list.append([x_min, y_min, x_max, y_max])
        labels_list.append(int(object_class))
        difficulties_list.append(0)

    print("please Wait")
    parameter_dict = {
        "boxes": boxes_list,
        "labels": labels_list,
        "difficulties": difficulties_list,
    }
    return parameter_dict


def main():
    data = []
    print("Running")
    labels_List = read_labels()
    create_directory()

    for dict in labels_List:
        print("Here")
        label_dict = generate_label_dict(dict)
        data.append(label_dict)

    write_json_file(data)


if __name__ == "__main__":
    main()
