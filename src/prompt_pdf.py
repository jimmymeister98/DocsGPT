import os

from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import DeepLake
from prompt_toolkit import prompt

os.environ.get('OPENAI_API_KEY')


def prompt_pdf(input_path):
    projectDir = os.getcwd()
    questions = buildQuestionsPrompt()
    # return if no questions were given
    if len(questions) == 0:
        print("No questions given, exiting...")
        return
    file_name = input_path.split("/")[-1]
    # strip file ending
    file_name = file_name.split(".")[0]
    embeddings = OpenAIEmbeddings(disallowed_special=())

    db = DeepLake(dataset_path=projectDir + "/vectorstores/" + file_name, read_only=True, embedding_function=embeddings)

    retriever = db.as_retriever()
    retriever.search_kwargs['distance_metric'] = 'cos'
    retriever.search_kwargs['fetch_k'] = 100
    retriever.search_kwargs['maximal_marginal_relevance'] = True
    retriever.search_kwargs['k'] = 10

    # print path to db
    print("path to VectorDB: " + "../vectorstores/" + file_name)
    model = ChatOpenAI()  # switch to 'gpt-4'
    qa = ConversationalRetrievalChain.from_llm(model, retriever=retriever)
    chat_history = []
    for question in questions:
        result = qa({"question": question, "chat_history": chat_history})
        chat_history.append((question, result['answer']))
        print(f"-> **Question**: {question} \n")
        print(f"**Answer**: {result['answer']} \n")


def buildQuestionsPrompt():
    answer = prompt(
        "Enter Your Questions: (ESCAPE followed by ENTER to accept)\n > ", multiline=True
    )
    # make list of questions
    questions = answer.split("\n")
    return questions
