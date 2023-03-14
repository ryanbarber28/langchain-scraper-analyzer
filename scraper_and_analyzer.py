import os
import requests
import signal
from bs4 import BeautifulSoup
import hashlib
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains import VectorDBQA
from langchain.document_loaders import TextLoader

os.environ["OPENAI_API_KEY"] = "YOUR OPENAI API KEY"

# Timeout handler
def handler(signum, frame):
    raise TimeoutError("User input timed out.")

# Custom input function with a timeout
def timed_input(prompt, timeout=600):
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(timeout)
    try:
        return input(prompt)
    except TimeoutError as e:
        print(f"\n{e}")
        return None
    finally:
        signal.alarm(0)

def get_page_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error while fetching the URL: {e}")
        return None

def parse_html_content(content):
    soup = BeautifulSoup(content, "html.parser")
    return ' '.join(soup.stripped_strings)

def save_to_file(filename, content):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)

def generate_unique_filename(url):
    url_hash = hashlib.md5(url.encode('utf-8')).hexdigest()
    return f"{url_hash}.txt"

def langchain_analysis(filename):
    loader = TextLoader(filename)
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings()
    vectordb = Chroma.from_documents(texts, embeddings)

    qa = VectorDBQA.from_chain_type(llm=OpenAI(), chain_type="stuff", vectorstore=vectordb)

    while True:
        query = timed_input("Enter a query (or type 'exit' to stop): ", timeout=600)
        if query is None or query.lower() == 'exit':
            break

        response = qa.run(query)
        print(response)

    # Delete the file
    os.remove(filename)
    print(f"Deleted file: {filename}")

def main():
    url = input("Enter the URL to scrape: ").strip()
    content = get_page_content(url)

    if content:
        text = parse_html_content(content)
        filename = generate_unique_filename(url)
        save_to_file(filename, text)
        print(f"Scraped text saved to {filename}")

        # Perform LangChain analysis
        langchain_analysis(filename)
    else:
        print("Failed to fetch content from the URL")

if __name__ == "__main__":
    main()
