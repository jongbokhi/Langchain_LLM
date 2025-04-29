from rag.base import RetrievalChain
from langchain_community.document_loaders import CSVLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from typing import List, Annotated, Union
import glob
import os


class CSVRetrievalChain(RetrievalChain):
    def __init__(self, source_uri: Union[str, List[str]]):
        if isinstance(source_uri, str):
            self.source_uri = [source_uri]
        else:
            self.source_uri = source_uri
        self.k = 10

    def load_documents(self, source_uris: List[str]):
        docs = []
        for source_uri in source_uris:
            # 디렉토리인 경우 모든 CSV 파일을 로드
            if os.path.isdir(source_uri):
                csv_files = glob.glob(os.path.join(source_uri, "*.csv"))
                for csv_file in csv_files:
                    loader = CSVLoader(file_path=csv_file)
                    docs.extend(loader.load())
            # 단일 파일인 경우
            else:
                loader = CSVLoader(file_path=source_uri)
                docs.extend(loader.load())

        return docs

    def create_text_splitter(self):
        return RecursiveCharacterTextSplitter(
            chunk_size=1000,  # 재무제표 데이터는 일반적으로 크기 때문에 청크 크기를 더 크게 설정
            chunk_overlap=200,
            separators=["\n\n", "\n", " ", ""],
        )
