from crewai import Crew

from stock_analysis_agents import StockAnalysisAgents

from dotenv import load_dotenv
load_dotenv()

class AnalysisCrew:
  def __init__(self, company):
    self.company = company

  def run(self):
    agents = StockAnalysisAgents()

    research_analyst_agent = agents.research_analyst()

    crew = Crew(
      agents=[
        research_analyst_agent
      ],
      verbose=True
    )

    result = crew.kickoff()
    return result
  

if __name__ == "__main__":
    print("## Welcome to Financial Analysis Crew")
    print('-------------------------------')
    company = input("What is the company you want to analyze? ")
    
    analysis_crew = AnalysisCrew(company)
    result = analysis_crew.run()
    print("\n\n########################")
    print("## Here is the Report")
    print("########################\n")
    print(result)