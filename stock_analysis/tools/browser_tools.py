import json
import os

import requests
from dotenv import load_dotenv
from crewai import Agent, Task
from langchain.tools import tool
from unstructured.partition.html import partition_html
from scrapingant_client import ScrapingAntClient
from tools.ollama_model_manager import OllamaModelManager

class BrowserTools():

  @tool("Scrape website content")
  def scrape_and_summarize_website(website):
    """Useful to scrape and summarize a website content"""
    # url = f"https://chrome.browserless.io/content?token={os.environ['BROWSERLESS_API_KEY']}"
    # payload = json.dumps({"url": website})
    # headers = {'cache-control': 'no-cache', 'content-type': 'application/json'}
    # response = requests.request("POST", url, headers=headers, data=payload)
    try:
      client = ScrapingAntClient(token=os.environ['SCRAPINGANT_API_KEY'])
      print('\n*****Website****** ' + website + ' **********\n')
      response = client.general_request(url=website)
      elements = partition_html(text=response.text)
      content = "\n\n".join([str(el) for el in elements])
      content = [content[i:i + 8000] for i in range(0, len(content), 8000)]
      summaries = []
      for chunk in content:
        agent = Agent(
            role='Principal Researcher',
            goal=
            'Summarize the content of the website in a clear and concise manner.',
            backstory=
            "You're a Principal Researcher at a big company and you need to do research about a given topic.",
            allow_delegation=False,
            verbose=True,
            llm = OllamaModelManager.getDefaultModel())
        task = Task(
            agent=agent,
            description=
            f'Analyze and summarize the content below, make sure to include the most relevant information in the summary, return only the summary nothing else.\n\nCONTENT\n----------\n{chunk}'
        )
        summary = task.execute()
        summaries.append(summary)
      return "\n\n".join(summaries)
    except Exception as e:
      print('exception: ' + str(e))
      return '\n\n'.join(['a'])


# if __name__ == "__main__":
#   load_dotenv()
#   print(BrowserTools.scrape_and_summarize_website('https://crewai.net/'))