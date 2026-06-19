# Building a Practical Multi\-Agent System for Unattended Long\-Task Execution



In the realm of AI development, building a multi \- agent system that can handle long tasks unattended is a challenging yet rewarding endeavor\. This article delves into a practical case where a multi \- agent system ran unattended for 4 days, generating 140,000 lines of code\. We'll explore the architecture, key techniques, and practical steps to replicate such a system\.

## The Challenge of Long \- Task Execution in AI

When dealing with complex, long \- running tasks, AI models often suffer from context forgetting\. As the task progresses, earlier details get pushed out of the context window, causing the task to deviate\. Even models with large context windows only delay this forgetting curve rather than eliminating it\.

To address this, the solution is to **break tasks into small chunks, maintain clean context for each chunk, and have agents hand off tasks after completion**\.

## Architecture: Graph \- Based Orchestration of Agents

The system uses a graph \- based approach to orchestrate multiple agents\. Each node in the graph is an agent, and edges represent the transfer of structured data between agents\.

- **Node Responsibility**: Each node \(agent\) is responsible for only one specific task, such as analysis, coding, testing, etc\.

- **Communication**: Agents don't have free \- form conversations\. They transfer predefined structured data\. For example, when a coding agent finishes, it hands off a structured object containing code details, modification logs, and the next step to the testing agent\.

Here's a simplified example of how the orchestration can be defined in a YAML file \(a core configuration file for the system\):

```yaml
pipeline:
  - name: analyzer
    type: agent
    responsibility: task analysis
    next: [coder]
  - name: coder
    type: agent
    responsibility: code generation
    next: [tester, quality_gate]
  - name: tester
    type: agent
    responsibility: code testing
    next: [reviewer]
  - name: quality_gate
    type: agent
    responsibility: code quality check
    after: tester
    next: [reviewer]
  - name: reviewer
    type: agent
    responsibility: code review
    next: [committer]
  - name: committer
    type: agent
    responsibility: code commit
```

## Key Components and Their Roles

### 1\. Codex: The Orchestrator

Codex acts as the brain of the system\. Its responsibilities include:

- **Task Allocation**: It takes high \- level tasks \(like an issue or voice command\) and generates a structured task draft\.

- **Graph Initiation**: It selects a YAML template based on the task type and initiates the pipeline\.

- **Monitoring and Fallback**: It continuously polls the status of each node, monitors for failures, and can intervene \(like stopping or rolling back\) when necessary\.

### 2\. YAML: The Core Interface

YAML is not just a configuration file; it's the core interface that defines the entire orchestration logic\. It includes:

- **Topology**: Defines the structure of the agent graph \(serial, parallel, fan \- out, fan \- in, etc\.\)\.

- **Agent Definition**: Specifies the role, responsibility, and system prompt of each agent\.

- **Model Profile**: Defines which AI model each agent uses \(useful for cost optimization\)\.

- **Environment**: Specifies the Docker image for each agent \(e\.g\., a coding agent might use a basic worker image, while a frontend testing agent uses an image with Chrome and Puppeteer\)\.

### 3\. Scorecard: The Audit Layer

To ensure the reliability of the system, a Scorecard layer is introduced\. Instead of just trusting an agent's claim of "task completed", Scorecard verifies against real records:

- **Node Handoff Check**: Ensures the handoff format between nodes is correct\.

- **Command Execution Check**: Verifies that test commands have actual outputs\.

- **PR Association Check**: Ensures pull requests are linked to the correct issues\.

## Practical Implementation Steps

### 1\. Set Up the Orchestration Graph

Define your pipeline in a YAML file as shown earlier\. This file should be version \- controlled\.

### 2\. Implement Agents

Each agent should be a standalone module with a clear system prompt\. For example, a coder agent's system prompt might look like this:

```text
You are a senior software developer specializing in TypeScript. Your task is to convert Python modules to TypeScript, ensuring type safety and adherence to the defined API contracts. After coding, you must generate a structured handoff including code, modification details, and the next steps.
```

### 3\. Deploy the Environment

Use Docker to containerize each agent's environment\. For a frontend testing agent, the Dockerfile might be:

```dockerfile
FROM node:18
RUN npm install -g puppeteer
COPY test-scripts /app/test-scripts
CMD ["node", "/app/test-scripts/run-tests.js"]
```

### 4\. Set Up Monitoring with Codex

Write a Python script for Codex to monitor the pipeline\. Here's a simplified version:

```python
import requests
import time

def monitor_pipeline(pipeline_id):
    while True:
        response = requests.get(f"http://api.example.com/pipeline/{pipeline_id}/status")
        status = response.json()["status"]
        if status in ["completed", "failed"]:
            break
        print(f"Pipeline status: {status}")
        time.sleep(30)  # Poll every 30 seconds
    print(f"Pipeline finished with status: {status}")

# Initiate the pipeline and get the ID
pipeline_response = requests.post("http://api.example.com/pipeline", json={"task": "TS refactoring"})
pipeline_id = pipeline_response.json()["pipeline_id"]
monitor_pipeline(pipeline_id)
```

## Performance and Optimization

In the 4 \- day unattended run:

- **Task Volume**: 416 tasks were executed, 374 completed successfully\.

- **Code Output**: 140,000 lines of code were generated, with 516 files committed\.

- **Token Usage**: 1\.29 billion tokens were consumed, mostly by worker agents\.

### Optimization Points

- **Codex Monitoring Frequency**: Initially, Codex's monitoring was too frequent, leading to high costs\. Adjust the polling interval based on task urgency\.

- **Parallel Pipelines**: The initial setup was serial\. For better efficiency, design multiple pipelines to run in parallel, each handling a different module\.

- **Environment Isolation**: Use Docker Compose to manage multi \- container environments for complex tasks\.

## Conclusion

Building a multi \- agent system for unattended long \- task execution is feasible with the right architecture\. By leveraging graph \- based orchestration, structured communication, and rigorous auditing, you can create a system that autonomously handles complex tasks\. The key is to start small, define clear interfaces \(like YAML\), and iteratively optimize based on real \- world performance\. As AI models and tooling evolve, such systems will become increasingly powerful and accessible\.
