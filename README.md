# radiography research crew

this is a crewai project that generates a technical research paper on radiography + blockchain + zero knowledge cryptography.

it runs a multi-agent pipeline where each agent has one clear job, then hands off to the next one.

## what this crew does

- takes one topic input from [src/radiography_research/main.py](src/radiography_research/main.py)
- refines that topic into a sharper research direction
- gathers technical facts and references using search
- drafts a detailed academic-style paper in markdown
- rewrites for more natural human flow
- runs a final technical + grammar pass
- writes the final output to `Research_Paper.md`

## how it works (pipeline)

the orchestration is in [src/radiography_research/crew.py](src/radiography_research/crew.py), and it uses `process=sequential`.

agents are defined in [src/radiography_research/config/agents.yaml](src/radiography_research/config/agents.yaml):

- topic_polisher
- fact_researcher
- academic_writer
- humanizer_editor
- final_proofreader

tasks are defined in [src/radiography_research/config/tasks.yaml](src/radiography_research/config/tasks.yaml):

- polish_topic_task
- technical_research_task
- academic_drafting_task
- ai_detection_bypass_task
- technical_accuracy_check_task

## run locally (step by step)

1. install python

- use python `>=3.10,<3.14`

2. install uv

```bash
pip install uv
```

3. install dependencies

from project root:

```bash
uv sync
```

4. create your env file

create `.env` in project root and add your real keys:

```dotenv
OPENAI_API_KEY=your_key_here
OPENAI_API_BASE=https://open.bigmodel.cn/api/paas/v4/
OPENAI_MODEL_NAME=glm-4.7
SERPER_API_KEY=your_serper_key_here
```

5. run the crew

```bash
crewai run
```

6. check output

- final paper is written to `Research_Paper.md`

## where to customize

- change input topic in [src/radiography_research/main.py](src/radiography_research/main.py)
- tune agent behavior in [src/radiography_research/config/agents.yaml](src/radiography_research/config/agents.yaml)
- tune task prompts in [src/radiography_research/config/tasks.yaml](src/radiography_research/config/tasks.yaml)
- change llm setup in [src/radiography_research/crew.py](src/radiography_research/crew.py)

## privacy + safety notes

- `.env` is gitignored and should never be committed
- this repo includes [knowledge/user_preference.example.txt](knowledge/user_preference.example.txt) as a safe template
- personal local knowledge files like `knowledge/user_preference.txt` are gitignored
