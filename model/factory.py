from abc import ABC, abstractmethod
from typing import Optional

from langchain_openai import OpenAIEmbeddings
from langchain_core.embeddings import Embeddings
from openai import OpenAI

from utils.config_handler import rag_conf


# 抽象类
class BaseModelFactory(ABC):

    # 生成器 我们需要的类型
    @abstractmethod
    def generator(self) -> Optional[Embeddings | OpenAI]:
        pass


class ChatModelFactory(BaseModelFactory):
    def generator(self) -> Optional[Embeddings | OpenAI]:
        return OpenAI(
            base_url=rag_conf["base_url"],
        )


class EmbeddingsFactory(BaseModelFactory):
    def generator(self) -> Optional[Embeddings | OpenAI]:
        # return OpenAIEmbeddings(model=rag_conf["embedding_model_name"])
        embedding = OpenAIEmbeddings(
            model=rag_conf["embedding_model_name"],
            base_url=rag_conf["base_url"],
            # 当前兼容接口要求原始字符串数组，不接受 OpenAI 的 token 数组。
            check_embedding_ctx_length=False,
            # 嵌入接口单次请求最多允许 20 条文本。
            chunk_size=20,
        )

        return embedding


chat_model = ChatModelFactory().generator()
embed_model = EmbeddingsFactory().generator()
