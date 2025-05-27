from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Import custom tools
from stockmarket.tools.custom_tool import NewsSentimentTool, TechnicalAnalysisTool, FundamentalDataTool

@CrewBase
class StockmarketCrew():
	"""Stockmarket crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def NewsAgent(self) -> Agent:
		return Agent(
			config=self.agents_config['news_agent'],
			tools=[NewsSentimentTool()],
			verbose=0
		)

	@agent
	def technical_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['technical_agent'],
			tools=[TechnicalAnalysisTool()],
			verbose=0
		)
	
	@agent
	def fundamental_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['fundamental_agent'],
			tools=[FundamentalDataTool()],
			verbose=0
		)
	
	@agent
	def portfolio_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['portfolio_agent'],
			verbose=0
		)
	
	@agent
	def summary_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['summary_agent'],
			verbose=0
		)
	
	# Establish the tasks
	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'],
			agent=self.NewsAgent()
		)

	@task
	def technical_task(self) -> Task:
		return Task(
			config=self.tasks_config['technical_task'],
			agent=self.technical_agent()
		)

	@task
	def fundamental_task(self) -> Task:
		return Task(
			config=self.tasks_config['fundamental_task'],
			agent=self.fundamental_agent()
		)

	@task
	def portfolio_task(self) -> Task:
		return Task(
			config=self.tasks_config['portfolio_task'],
			agent=self.portfolio_agent()
		)

	@task
	def summary_task(self) -> Task:
		return Task(
			config=self.tasks_config['summary_task'],
			agent=self.summary_agent(),
			output_file='output.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Stockmarket crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=1,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
