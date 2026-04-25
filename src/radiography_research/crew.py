import os

from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool

@CrewBase
class RadiographyResearchCrew():
    """RadiographyResearch crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    model_name = os.getenv('OPENAI_MODEL_NAME', 'glm-4.7')
    base_url = os.getenv('OPENAI_API_BASE', 'https://open.bigmodel.cn/api/paas/v4/')

    llm = LLM(
        model=f"openai/{model_name}",
        base_url=base_url,
        temperature=0.2,
        max_tokens=8192
    )
    
    search_tool = SerperDevTool()

    @agent
    def topic_polisher(self) -> Agent:
        return Agent(config=self.agents_config['topic_polisher'], tools=[self.search_tool], llm=self.llm, verbose=True)

    @agent
    def fact_researcher(self) -> Agent:
        return Agent(config=self.agents_config['fact_researcher'], tools=[self.search_tool], llm=self.llm, verbose=True)

    @agent
    def academic_writer(self) -> Agent:
        return Agent(config=self.agents_config['academic_writer'], llm=self.llm, verbose=True)

    @agent
    def humanizer_editor(self) -> Agent:
        return Agent(config=self.agents_config['humanizer_editor'], llm=self.llm, verbose=True)

    @agent
    def final_proofreader(self) -> Agent:
        return Agent(config=self.agents_config['final_proofreader'], llm=self.llm, verbose=True)

    @task
    def polish_topic_task(self) -> Task:
        return Task(config=self.tasks_config['polish_topic_task'])

    @task
    def technical_research_task(self) -> Task:
        return Task(config=self.tasks_config['technical_research_task'])

    @task
    def academic_drafting_task(self) -> Task:
        return Task(config=self.tasks_config['academic_drafting_task'])

    @task
    def ai_detection_bypass_task(self) -> Task:
        return Task(config=self.tasks_config['ai_detection_bypass_task'])

    @task
    def technical_accuracy_check_task(self) -> Task:
        return Task(config=self.tasks_config['technical_accuracy_check_task'], output_file='Research_Paper.md')

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )