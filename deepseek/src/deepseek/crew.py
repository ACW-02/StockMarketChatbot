from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from deepseek.tools.custom_tool import NewsSentimentTool, TechnicalAnalysisTool, FundamentalDataTool

@CrewBase
class Deepseek():
	"""Stockmarket crew"""
	
	# Establish the agents
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'  

	deepseek_llm = LLM(
		model="ollama/deepseek-r1:7b",
		base_url="http://localhost:11434"
    )

	@agent
	def NewsAgent(self) -> Agent:
		return Agent(
			config=self.agents_config['news_agent'],
			#tools=[NewsSentimentTool()],
			llm=self.deepseek_llm,
			verbose=1
		)

	@agent
	def technical_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['technical_agent'],
			#tools=[TechnicalAnalysisTool()],
			llm=self.deepseek_llm,
			verbose=1
		)
	
	@agent
	def fundamental_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['fundamental_agent'],
			#tools=[FundamentalDataTool()],
			llm=self.deepseek_llm,
			verbose=1
		)
	
	@agent
	def portfolio_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['portfolio_agent'],
			verbose=1,
			llm=self.deepseek_llm
		)
	
	@agent
	def summary_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['summary_agent'],
			verbose=1,
			llm=self.deepseek_llm
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
			output_file='deepseekOuutput.md'
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
