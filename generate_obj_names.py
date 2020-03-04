import yaml
import os


def read_file(path):
    with open(path) as file:
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
    path = path + "/build/obj_names"
    try:
        os.mkdir(path)
    except OSError:
        print("Creation of the directory %s failed" % path)
    else:
        print("Successfully created the directory %s " % path)


def write_to_file(label_string):
    labels_file = open("build/obj_names/obj.names", "a+")
    labels_file.write(str(label_string) + "\n")
    labels_file.close()


def check_file_for_duplicates(filepath):
    lines_seen = set()  # holds lines already seen
    outfile = open("build/obj_names/duplicates", "w")
    for line in open(filepath, "r"):
        if line not in lines_seen:  # not a duplicate
            outfile.write(line)
            lines_seen.add(line)
            print(lines_seen)
    outfile.close()


def main():
    labels_List = read_file("./DTLD_Labels copy/Bremen_all.yml")
    create_directory()

    class_ids = []
    # print(labels_List)
    for dict in labels_List:
        for box in dict.get("objects"):
            class_id = box.get("class_id")
            class_ids.append(class_id)

    class_ids = list(dict.fromkeys(class_ids))

    for class_id in class_ids:
        write_to_file(class_id)

    check_file_for_duplicates("build/obj_names/obj.names")


if __name__ == "__main__":
    main()
