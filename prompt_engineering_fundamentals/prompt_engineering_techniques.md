# Prompting Approaches and their Matching Techniques

## Structured and Specific -> Zero-Shot Prompting

This technique is better when you know exactly what we need. It is a straightforward task (e.g., writing an email or summarizing a short document)

**Example Task**: Summarize the content of a video given the script.

* You give the model a clear, specific instruction **without examples**.
* Works best for **simple, well-defined requests** where clarity and structure matter more than creativity.
* Think of this as "tell it what you need - clearly and directly"

## Analytical and Data-Driven -> Chain-of-Thought Prompting

This approach is better when the task requires reasoning, analysis, or step-by-step recommendations (e.g. competitive analysis or interpreting study results).

* Encourages the model to show its reasoning or break down its thinking process step-by-step
* Useful for **complex or multi-part questions** where the logic behind the answer matters as much as the conclusion.
* Think of this as "walk me through how you got there"

## Context-Rich and Goal-Oriented -> Few-Shot or Self-Ask Prompting.

This approach is more suitable when the task is dynamic or multi-faceted. (e.g. planning meetings, preparing conversation guides)

* Few-shot: You provide one or more examples of the type of response you want.
* Self-Ask: The model is guided to ask clarifying questions before responding. Helping tailor its answer to your goal.
* Think of this as "let's make sure we're on the same page before you answer"
