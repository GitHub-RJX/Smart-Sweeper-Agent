"""
为整个项目提供统一的绝对路径
"""
import os


def get_project_root_path() -> str:
    """
    获取项目所在根目录的绝对路径
    :return: 根目录的绝对路径
    """
    # 获取当前文件的绝对路径
    cur_file_path = os.path.abspath(__file__)
    # 获取当前文件所在目录的绝对路径
    cur_dir_path = os.path.dirname(cur_file_path)
    # 获取项目根目录的绝对路径
    project_root_path = os.path.dirname(cur_dir_path)

    return project_root_path


def get_file_abs_path(relative_path: str) -> str:
    """
    根据相对路径获取文件的绝对路径
    :param relative_path: 文件的相对路径
    :return: 文件的绝对路径
    """
    # 获取项目根目录的绝对路径
    project_root_path = get_project_root_path()
    # 拼接相对路径获取文件的绝对路径
    file_abs_path = os.path.join(project_root_path, relative_path)

    return file_abs_path


if __name__ == '__main__':
    path = get_file_abs_path("config/config.json")
    print(path)
