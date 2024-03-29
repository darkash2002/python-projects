import os


def checks_if_file_already_exits(directory: str, filename: str) -> bool:
    """
    :param directory: the directory of the file
    :param filename: the filename
    :return: if the file exists or not
    """
    return os.path.exists(os.path.join(directory, filename))


def create_directory(directory: str):
    """
    :param directory: the directory to create
    """
    try:
        os.mkdir(directory)
    except FileExistsError:
        return
    except Exception as e:
        print(f"ERROR: Error occurred {e}")
