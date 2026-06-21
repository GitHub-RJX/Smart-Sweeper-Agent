from langchain_chroma import Chroma
from utils.config_loader import CHROMA_CONF
from factory.model_factory import embedding_model
from langchain_text_splitters import RecursiveCharacterTextSplitter
from utils.path_tool import get_file_abs_path
from utils.file_handler import load_text, load_pdf, get_dir_files, get_file_md5
from utils.log_handler import LOGGER
import os


class VectorStoreService:
    def __init__(self):
        self.vector_store = Chroma(
            embedding_function=embedding_model,
            persist_directory=CHROMA_CONF['persist_directory'],
            collection_name=CHROMA_CONF['collection_name'],
        )
        self.spliter = RecursiveCharacterTextSplitter(
            chunk_size=CHROMA_CONF['chunk_size'],
            chunk_overlap=CHROMA_CONF['chunk_overlap'],
            separators=CHROMA_CONF['separators'],
            length_function=len,
        )

    def get_retriever(self):
        """
        获取向量库的检索器
        :return: 检索器
        """
        return self.vector_store.as_retriever(search_kwargs={'k': CHROMA_CONF['k']})

    def load_document(self):
        """
        加载文件夹的文件片段 并存入向量库
        """
        file_path_list = get_dir_files(
            dir_path=get_file_abs_path(CHROMA_CONF['resource_data_path']),
            allowed_types=tuple(CHROMA_CONF['allowed_types']),
        )
        for file_path in file_path_list:
            md5_str = get_file_md5(file_path)
            if not self.__check_md5(md5_str):
                LOGGER.info(f'文件【{file_path}】内容已存在与向量库中。')
                continue

            documents = self.__get_file_documents(file_path)
            if not documents:
                LOGGER.warning(f'文件【{file_path}】无内容。')
                continue

            split_documents = self.spliter.split_documents(documents)
            self.vector_store.add_documents(split_documents)
            with open(get_file_abs_path(CHROMA_CONF['md5_str_store']), 'a', encoding='utf-8') as f:
                f.write(md5_str + '\n')

    def __check_md5(self, md5_str: str) -> bool:
        """
        检查md5串是否全新未加入向量库
        :param md5_str: md5串
        :return: 检查结果
        """
        if not os.path.exists(get_file_abs_path(CHROMA_CONF['md5_str_store'])):
            with open(get_file_abs_path(CHROMA_CONF['md5_str_store']), 'w', encoding='utf-8') as f:
                f.write(md5_str + '\n')
            return True
        with open(get_file_abs_path(CHROMA_CONF['md5_str_store'])) as f:
            for line in f.readlines():
                if line.strip() == md5_str:
                    return False
            return True

    def __get_file_documents(self, file_path: str) -> list:
        """
        获取单个文件片段
        :param file_path: 单个文件路径
        :return: 文锦片段
        """
        if file_path.endswith('.txt'):
            return load_text(file_path)
        if file_path.endswith('.pdf'):
            return load_pdf(file_path)

        LOGGER.warning(f'读取文件【{file_path}】仅支持.txt .pdf格式')
        return []


if __name__ == '__main__':
    vss = VectorStoreService()
    vss.load_document()

    retriever = vss.get_retriever()
    for chunk in retriever.invoke("介绍一下智能扫地机器人"):
        print(chunk.page_content)
