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

# Reasoning techniques

## Chain-of-Thought Prompting

Explicitly asking the AI to lay out its step-by-step reasoning before giving a conclusion.

## Self-Ask Prompting

Self-Ask Prompting encourages your AI to generate and answer its own follow-up questions to deepen the analysis.
Instead of you outlining every reasoning step (as in Chain-of-Thought), the AI takes the lead—identifying what questions need to be explored and addressing each one systematically.

## Meta Prompting

Meta-Prompting means asking the AI to help you design better prompts or structured approaches for complex, unfamiliar, or open-ended tasks. Instead of diving straight into the work, you partner with the AI to plan how to ask for what you need.

# Workflow Techniques

## Approach 1 - The single massive prompt.
## Approach 2 – The Prompt Chain

## Prompt Chaining

Prompt Chaining means breaking a complex task into a sequence of focused prompts, where each one builds on the output of the previous step.

Instead of trying to do everything in one massive prompt, you guide your AI Assistant through a structured workflow—just like you would brief a colleague step-by-step.

### Building Effective Chains
1.  Each prompt should
* Have one clear focus
* Build on previous outputs explicitly
* USe the appropriate prompting technique for that step.
* Follow the COIE structure

2. Connect Prompts By:
* Starting with: 
* Referencing specific findings or insights
* Maintaining cumulative context without repeating everything.

3. Sequence Logically:
* Research → Strategy → Execution → Refinement
* Foundation → Building → Finishing
* Understanding → Planning → Creating

## Clearly Structuring Prompts.

Structuring your prompts means organizing them with clear sections, labels, and formatting so both you and your AI Assistant can easily understand what’s being asked.

### why structure matters?
* Reduces ambiguity and misinterpretation
* Makes complex prompts manageable and reusable
* Helps you think more clearly about what you need
* Creates templates that save time and ensure consistency
* Makes it easier to refine and iterate as you go

### Structure Best Practices
**Use clear labels**
    * Formal Structure: Context:, Outcome:, Instruction:, Example:

**Use Formatting**
    * Add line breaks between sections
    * Use bullet points for lists.
    * Use numbers for sequences or steps.
    * Use bold or capitalization for emphasis (sparingly)

**Group Related Information**
    * All context in one section
    * All requirements in another
    * All examples or references at the end

**Be explicit about relationships**
    * “Based on the context above…”
    * “Using this information…”
    * “Given these constraints…”