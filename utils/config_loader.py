"""
配置文件加载器
"""

import yaml
from path_tool import get_file_abs_path


def load_rag_config(config_file_path: str, encoding: str = 'utf-8'):
    with open(config_file_path, 'r', encoding=encoding) as f:
        return yaml.load(f, Loader=yaml.FullLoader)


def load_chroma_config(config_file_path: str, encoding: str = 'utf-8'):
    with open(config_file_path, 'r', encoding=encoding) as f:
        return yaml.load(f, Loader=yaml.FullLoader)


def load_prompt_config(config_file_path: str, encoding: str = 'utf-8'):
    with open(config_file_path, 'r', encoding=encoding) as f:
        return yaml.load(f, Loader=yaml.FullLoader)


def load_agent_config(config_file_path: str, encoding: str = 'utf-8'):
    with open(config_file_path, 'r', encoding=encoding) as f:
        return yaml.load(f, Loader=yaml.FullLoader)


RAG_CONF = load_rag_config(get_file_abs_path('config/rag_conf.yaml'))
CHROMA_CONF = load_rag_config(get_file_abs_path('config/chroma_conf.yaml'))
PROMPT_CONF = load_rag_config(get_file_abs_path('config/prompt_conf.yaml'))
AGENT_CONF = load_rag_config(get_file_abs_path('config/agent_conf.yaml'))

if __name__ == '__main__':
    print(RAG_CONF['chat_model_name'])
    print(RAG_CONF['embedding_model_name'])
