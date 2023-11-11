import os
from dotenv import load_dotenv
from llama_index import SimpleWebPageReader, VectorStoreIndex


def main(url:str)-> None:
    documents = SimpleWebPageReader(html_to_text=True).load_data(urls=[url])
    pass


if __name__ == '__main__':
    load_dotenv()
    print("hello world, llamaindex")
    print(f"OPEN AP API key : {os.environ['OPENAI_API_KEY']}")

    main(url='https://cbarkinozer.medium.com/an-overview-of-the-llamaindex-framework-9ee9db787d16')