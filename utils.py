import os


def validate_xml_extension(file_name):
    _, ext = os.path.splitext(file_name)
    if not ext:
        return file_name + ".xml"
    if ext == ".xml":
        return file_name
    raise ValueError("File must have a .xml extension")
