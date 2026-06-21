import logging
import os

from utils.path_tool import get_file_abs_path
from datetime import datetime

# 获取日志保存目录的绝对路径
LOG_ROOT_PATH = get_file_abs_path('logs')

# 确保日志保存目录存在
os.makedirs(LOG_ROOT_PATH, exist_ok=True)

# 配置日志格式
DEFAULT_LOG_FORMAT = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s')


def get_logger(name: str, console_level: int = logging.INFO, file_level: int = logging.DEBUG, log_file: str = None
               ) -> logging.Logger:
    """
    获取日志处理器
    :param name: 日志名称
    :param console_level: 控制台日志级别
    :param file_level: 文件日志级别
    :param log_file: 日志文件路径
    :return: 日志处理器
    """
    # 创建日志器实例
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # 为日志器添加处理器
    # 先校验是否已存在处理器，避免重复添加处理器
    if logger.handlers:
        return logger
    # 添加控制台处理器
    console_handler = logging.StreamHandler()
    console_handler.setLevel(console_level)
    console_handler.setFormatter(DEFAULT_LOG_FORMAT)
    logger.addHandler(console_handler)
    # 添加文件处理器
    if not log_file:
        log_file = os.path.join(LOG_ROOT_PATH, f'{name}_{datetime.now().strftime("%Y%m%d")}.log')
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setLevel(file_level)
    file_handler.setFormatter(DEFAULT_LOG_FORMAT)
    logger.addHandler(file_handler)

    return logger


LOGGER: logging.Logger = get_logger('Smart-Sweeper-Agent')

if __name__ == '__main__':
    LOGGER.debug('调试日志')
    LOGGER.info('信息日志')
    LOGGER.warning('警告日志')
    LOGGER.error('错误日志')
    LOGGER.fatal('致命日志')
