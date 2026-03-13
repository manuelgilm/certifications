# Get Started with AI agent development on Azure

## What are AI agents?
An ai agent is a smart application that can understand what the user needs and also take actions to help the user. What differentiates an agent from a simple chatbot is that the agent can remember the conversation (Memory) and has the ability to do things.

### Security best practices.

* Control access tightly: Enforce role-based access controls (RBAC) and least privilege permissions - agents should only access what they absolutely need.

* Validate all inputs: Add prompt filtering and validation layers to catch and block injection atrtacks before they reach you agent. 

* **add human oversight for critical actions** : Sandbox or gate sensitive operations behind **human-in-the-loop** approvals -do not let agents make high-stakes decisions alone.

* **Track everything**: Maintain **comprehensive logging and traceability** for all agent actions - you need to know who did what, when and why. 

* **Monitor your supply chain**: Audit third-party dependencies and traceability for all agent actions - you need to know who did what when and why.

* **Keep your models healthy** : Continuously retrain and validate models to detect data drift or poisoining attempts - agent quality degrades over time without maintanance. 

### Microsoft Agent Framework

The Microsoft Agent Framework is a lightweight development kit that you can use to build AI agents and orchestrate multi-agent solutions. The framework serves as a platform specifically optimized for creating agents and implementing agentic solution patterns.

### AutoGen

AutoGen is an open-source framework for developing agents rapidly. It's useful as a research and ideation tool when experimenting with agents.

### Microsoft 365 agents SDK

Developers can create self-hosted agents for delivery through a wide range of channels by using the Microsoft 365 Agents SDK. Despite the name, agents built using this SDK aren't limited to Microsoft 365, but can be delivered through channels like Slack or Messenger.

### Microsoft Copilot Studio

Microsoft Copilot Studio provides a low-code development environment that "citizen developers" can use to quickly build and deploy agents that integrate with a Microsoft 365 ecosystem or commonly used channels like Slack and Messenger. The visual design interface of Copilot Studio makes it a good choice for building agents when you have little or no professional software development experience.

### Copilot Studio lite experience in Microsoft 365 Copilot

Business users can use the declarative Copilot Studio lite experience tool in Microsoft 365 Copilot to author basic agents for common tasks. The declarative nature of the tool enables users to create an agent by describing the functionality they need, or they can use an intuitive visual interface to specify options for their agent.

## Components of an agent

Agents developed using Foundry Agent Service have the following elements:

* **Model**: A deployed generative AI model that enables the agent to reason and generate natural language responses to prompts.

* **Knowledge**: Data sources that enable the agent to ground prompts with contextual data. Potential knowledege sources include internet search results from Microsoft Bing, an Azure AI Search Index, or your own data and documents. 

* **Tools** Programatic functions that enable the agent to automate actions. Built-in tools to access knowledge in Azure AI Searcha... 


