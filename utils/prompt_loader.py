from utils.config_loader import PROMPT_CONF
from utils.path_tool import get_file_abs_path


def load_system_prompt():
    """
    加载系统提示词
    :return: 系统提示词内容
    """
    system_prompt_path = get_file_abs_path(PROMPT_CONF['system_prompt_path'])
    with open(system_prompt_path, 'r', encoding='utf-8') as f:
        return f.read()


def load_rag_summarize_prompt():
    """
    加载rag总结提示词
    :return: rag总结提示词内容
    """
    rag_summarize_prompt_path = get_file_abs_path(PROMPT_CONF['rag_summarize_prompt_path'])
    with open(rag_summarize_prompt_path, 'r', encoding='utf-8') as f:
        return f.read()


def load_report_prompt():
    """
    加载报告提示词
    :return: 报告提示词内容
    """
    report_prompt_path = get_file_abs_path(PROMPT_CONF['report_prompt_path'])
    with open(report_prompt_path, 'r', encoding='utf-8') as f:
        return f.read()


if __name__ == '__main__':
    print(load_system_prompt())
    print(load_rag_summarize_prompt())
    print(load_report_prompt())
