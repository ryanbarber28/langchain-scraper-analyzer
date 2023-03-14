# langchain-scraper-analyzer
Python script that scrapes text content from a given URL, saves it to a unique file, and performs LangChain analysis on the text. Users can enter multiple queries to analyze the content, and the script automatically deletes the unique file when they exit or don't respond within 10 minutes.

**Requirements:**

Python 3.6 or later
The following Python packages:
requests
beautifulsoup4
langchain

To install the required packages, use the following pip commands:

pip install requests
pip install beautifulsoup4
pip install langchain

**Usage**

Open your command line terminal (Command Prompt, PowerShell, or a terminal emulator like Git Bash on Windows; Terminal on macOS and Linux).

Navigate to the directory where the scraper_and_analyzer.py file is saved using the cd command.

Run the script with the Python interpreter:


**python scraper_and_analyzer.py**

or

**python3 scraper_and_analyzer.py**

Enter the URL you want to scrape when prompted.

After the script scrapes the content and saves it to a unique file, you can enter multiple queries to perform LangChain analysis.

To exit the script, type 'exit' or after 10 minutes without responding itll terminate and the unique .txt file will be deleted automatically.

**Example:**

python3 langapp.py 
Enter the URL to scrape: **https://en.wikipedia.org/wiki/Turducken**
Scraped text saved to **705869db656dad55c2e6cfd7eedd0cff.txt**
Running Chroma using direct local API.
Using DuckDB in-memory for database. Data will be transient.
Enter a query (or type 'exit' to stop): **How could I make one?**
 
To make a Turducken, you need to take a plump quail, season it with truffles, and make it tender by putting it into champagne. You then put the quail inside a young Bresse chicken, sew up the opening, an
d put dabs of butter all over the chicken. Next, you put the chicken inside a fine Berri turkey, and roast the turkey very carefully before a bright fire. After two hours roasting, you pull the chicken ou
t of the turkey, and the quail out of the chicken. Serve the quail hot, steaming, with its aroma of truffles, after having roasted it to a golden yellow by basting it diligently with the best Gournay butt
er.

Enter a query (or type 'exit' to stop): 
**User input timed out.**
Deleted file:**705869db656dad55c2e6cfd7eedd0cff.txt**
Exiting: Cleaning up .chroma directory

above example shows question was asked and answered using data from URL, then it was left idle for 600 seconds til it was terminated.

**Support**

For Business support or If you encounter any issues or need assistance, please reach out to the script author or consult the respective package documentation:

requests: https://docs.python-requests.org/en/latest/
beautifulsoup4: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
langchain: https://langchain.readthedocs.io/en/latest/
