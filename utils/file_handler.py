"""
文件处理器
"""
import hashlib
import os
from log_handler import LOGGER
from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader, TextLoader


def get_file_md5(file_path: str) -> str:
    """
    获取文件内容的md5加密串
    :param file_path: 文件路径
    :return: md5加密串
    """
    # 判断文件路径是否存在
    if not os.path.exists(file_path):
        LOGGER.error(f'路径【{file_path}】不存在！')
    # 判断路径所指的是否为文件
    if not os.path.isfile(file_path):
        LOGGER.error(f'路径【{file_path}】不是文件！')

    md5_str = hashlib.md5(open(file_path, 'rb').read()).hexdigest()
    return md5_str


def get_dir_files(dir_path: str, allowed_types: tuple) -> tuple:
    """
    获取文件夹下的文件列表
    :param dir_path: 文件夹路径
    :param allowed_types: 允许加载的文件类型
    :return: 文件列表
    """
    # 判断文件路径是否存在
    if not os.path.exists(dir_path):
        LOGGER.error(f'路径【{dir_path}】不存在！')
    # 判断路径所指的是否为文件夹
    if not os.path.isdir(dir_path):
        LOGGER.error(f'路径【{dir_path}】不是文件夹！')

    file_list = [os.path.join(dir_path, file) for file in os.listdir(dir_path) if file.endswith(allowed_types)]
    return tuple(file_list)


def load_pdf(file_path: str, password: str = None) -> list[Document]:
    """
    加载PDF文件
    :param file_path: 文件路径
    :param password: 文件密码（非必须）
    :return: 文件片段列表
    """
    return PyPDFLoader(file_path, password).load()


def load_text(file_path: str) -> list[Document]:
    """
    加载Text文件
    :param file_path: 文件路径
    :return: 文件片段列表
    """
    return TextLoader(file_path).load()
