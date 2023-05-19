import os

from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import DeepLake
from langchain.embeddings import OpenAIEmbeddings

os.environ.get('OPENAI_API_KEY')

def embed_pdf(pathToPdf):
    embeddings = OpenAIEmbeddings(disallowed_special=())
    root_dir = pathToPdf
    projectDir = os.getcwd()
    #get file name
    file_name = root_dir.split("/")[-1]
    #strip file ending
    file_name = file_name.split(".")[0]
    #check if path leads to a pdf file
    if not pathToPdf.endswith(".pdf"):
        print("Path does not lead to a pdf file")
        return -1
    print("project directory is: " + root_dir)
    loader = PyPDFLoader(root_dir)
    pages = loader.load_and_split()

    db = DeepLake(dataset_path=projectDir+"/vectorstores/"+file_name, embedding_function=embeddings)  # dataset would be publicly available
    db.add_documents(pages)
    print("Embedding process finished.")
    print("Vectorstore created at: " + "../vectorstores/"+file_name)
    return 0