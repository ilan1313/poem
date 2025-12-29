import os

from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task






@CrewBase
class PoetryCreationStudioCrew:
    """PoetryCreationStudio crew"""

    
    @agent
    def orchestrator(self) -> Agent:
        
        return Agent(
            config=self.agents_config["orchestrator"],
            
            
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    
    @agent
    def poet(self) -> Agent:
        
        return Agent(
            config=self.agents_config["poet"],
            
            
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    
    @agent
    def critic(self) -> Agent:
        
        return Agent(
            config=self.agents_config["critic"],
            
            
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                temperature=0.7,
            ),
            
        )
    

    
    @task
    def parse_request(self) -> Task:
        return Task(
            config=self.tasks_config["parse_request"],
            markdown=False,
            
            
        )
    
    @task
    def draft_poem(self) -> Task:
        return Task(
            config=self.tasks_config["draft_poem"],
            markdown=False,
            
            
        )
    
    @task
    def critique_poem(self) -> Task:
        return Task(
            config=self.tasks_config["critique_poem"],
            markdown=False,
            
            
        )
    
    @task
    def final_decision(self) -> Task:
        return Task(
            config=self.tasks_config["final_decision"],
            markdown=False,
            
            
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the PoetryCreationStudio crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            chat_llm=LLM(model="openai/gpt-4o-mini"),
        )

    def _load_response_format(self, name):
        with open(os.path.join(self.base_directory, "config", f"{name}.json")) as f:
            json_schema = json.loads(f.read())

        return SchemaConverter.build(json_schema)
