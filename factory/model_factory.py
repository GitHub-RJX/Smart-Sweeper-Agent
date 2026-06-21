import os
from abc import ABC, abstractmethod
from typing import Optional
from utils.config_loader import RAG_CONF
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.language_models import BaseChatModel
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.embeddings import Embeddings


class ModelFactory(ABC):
    @abstractmethod
    def generate(self) -> Optional[BaseChatModel | Embeddings]:
        pass


class ChatModelFactory(ModelFactory):
    def generate(self):
        return ChatTongyi(
            model=RAG_CONF['chat_model_name'],
            api_key=os.getenv("DASHSCOPE_API_KEY")
        )


class EmbeddingModelFactory(ModelFactory):
    def generate(self):
        return DashScopeEmbeddings(
            model=RAG_CONF['embedding_model_name']
        )


chat_model: BaseChatModel = ChatModelFactory().generate()
embedding_model: Embeddings = EmbeddingModelFactory().generate()
