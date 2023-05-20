import os

from dotenv import load_dotenv

from src.pdf_embedder import embed_pdf
from src.prompt_pdf import prompt_pdf

pdf_path = "path/to/pdf"

if __name__ == '__main__':
    load_dotenv()
    pdf_file_name = pdf_path.split("/")[-1]
    pdf_file_name = pdf_file_name.split(".")[0]

    #generate vectorstore folder if not exists
    if not os.path.exists(os.getcwd() + '/vectorstores'):
        os.makedirs(os.getcwd() + '/vectorstores')

    if len(os.listdir(os.getcwd() + '/vectorstores')) == 0 or not os.path.exists(
            os.getcwd() + '/vectorstores/' + pdf_file_name):
        print("No vectorstore found.")
        print("Start embedding process...")
        # embed the pdf and exit if the embedding was not successful
        if embed_pdf(pdf_path) == -1:
            exit()
        prompt_pdf(pdf_path)

    else:
        print("Vectorstore found.")
        prompt_pdf(pdf_path)
