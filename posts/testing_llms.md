---
tags: post
layout: base.njk
title: How do you test LLM output?
date: 2025-02-20
---

# How do you test LLM output?

<blockquote>
  <b>TLDR:</b> testing LLMs as components in an app is hard, many tools
  offer to test LLM output, but rolling your own LLM-evaluating-LLM as
  an automated unit tester is probably your best best.
</blockquote>

With the recent advent of LLMs, and surge of applications based on them, determining the quality of LLM output is critical. Determining quality of LLM output when training is quite similar to performance assessment in usual machine learning. Here we are interested in evaluating its performance as a component of an application. This is far more diffuse, consider for instance the following:

<blockquote>
  <p>
    <b>User:</b> Describe the city of Oslo in one sentence, using
    flowery language.
  </p>
  <p>
    <b>Deepseek-r1:14b:</b> Oslo, where the whispers of ancient Vikings
    echo through its cobblestone streets, stands as a resilient city
    cradled by towering cliffs and emerald forests, its heart beating
    with cultural richness, culinary treasures, and the soothing rythm
    of the Norwegian Sea.
  </p>
  <p>
    <b>ChatGPT o3-mini:</b> Oslo unfolds like a cherished sonnet of
    nature and culture, where luminous fjords embrace verdant parks and
    storied streets whisper tales of ancient splendor intermingled with
    modern artistic dreams.
  </p>
</blockquote>

Which is the better answer? Presumably you are using LLMs to add flexibility to your application, however this flexibilty now comes at the cost of lessened control over the components of your application.

In software engineering circles, it is widely understood that getting instant feedback on changes made, most often through the use of tests, is necessary for iterating fast on a new application. There is a rough hierarchy of tests:

1. <b>Unit tests</b> [runtime: &lt;1s ]: these are tests checking the fundamental integrity of your application. Typically run on every code change. Useful when adding new features and modifing your application domain. For instance they would answer the scenario/question: "We used to only support green grapes in our app. We're now adding support for red ones. Which assumptions have we made that are now broken, and need modification?"
2. <b>Integration tests</b> [runtime: &lt;1h] These are tests of assumptions made about external dependencies of your app. For instance, about the shape of an API you're using. These tests typically answer a question such as: "Are we certain that the brreg.no API still functions the same as last month?" This kind of tests can save you a lot of time when chasing bugs.
3. <b>Human testing</b> [runtime: variable] These are manual tests: someone goes through the application and uses it manually, both like they expect the end user to, and also in a more adversarial way. These tests are expensive, as someone must dedicate time to them, but are useful in verifying the soundness of the whole application.

This test hierarchy is usually such that you should mostly use levels 1 and 2, and turn to human testing in the final stages of a new deployment of the app.

But here lies the problem: _How do you unit test an LLM?_ If I modify the system prompt, how do I know whether I broke something, or if the quality of the output is reduced?


The current status on this problem seems to be that there aren't any standout optimal solutions. It is of course possible to do human testing, but given the range of possible inputs (all of human language? all possible sequence of characters?), anything but happy-path testing, or minor adversarial deviations, is unfeasible. For simple tasks, it is possible to write simple keyword matches, or tests that the LLM performs certain expected tool calls, or tests that the output corresponds to an expected JSON format. But if your tasks very simple, are you sure you shouldn't just give the user a button to press instead, and avoid AI slop?


The most reasonable answer to the above problem is to use **LLMs-testing-LLMs**, i.e. setup another LLM to verify the output of the first one. For instance, you might provide the whole conversation between user and LLM to a second one, with one of the following prompts:


- "Here is a conversation between a user and a chatbot. Did the
  chatbot answer the users query correctly?"
- "Based on the above conversation, is the answer from the chatbot
  relevant and in compliance with the following policies: [...]"


Setting up such an evaluation rig shouldn't be too time consuming, and you can then hopefully redirect the human testing to meta-evaluation of the LLM-evaluator, and get their efforts multiplied as the LLM-evaluator is put into an automated testing set.


A drawback of this approach is cost and latency. Running hundreds of such LLM-evaluations would be both time consuming and expensive. And merely builing a good test set will take time and most likely require the service to have seen some actual user action in production.

There are tools that manage the complexity of monitoring and evaluating LLMs, however my understanding of these tools is that they primarily provide interfaces for looking at the results and output of the LLMs. Several of these provide nice dashboards, some of them have SAAS/cloud offerings. 


This can of course be nice, but I suspect you're better of building your own tools, especially if good LLM output is an integral part of your application. Realistically, say in an entreprise application, are your users likely to go into a hosted web-panel and annotate answers as good or bad? I think meeting them where they are, providing e.g. a spreadsheet to a panel of application owners, is more likely to result in fast and good feedback. Moreover, writing the 200 lines of python code required to mirror the main evaluation-capabilities of the frameworks probably will be easier to maintain in the long run than to add a large dependency.

## Relevant links and tools

Here is a list of links and tools I've looked into when writing this piece:

- [Langfuse](https://langfuse.com) - a Y-combinator backed monitoring and evaluation setup, with both a cloud offering and self-hosting support. Integrates with several of the other tools. Seems like the largest open-source player. If I had to choose a tool it would be this one.
- [Langsmith](https://www.langchain.com/langsmith) - Evaluation and monitoring platform made by LangChain. Maybe nice if you're already inside their ecosystem. They offer self hosting on their Entreprise plan for their "largest, most security-conscious customers".
- [DeepEval](https://docs.confident-ai.com) - open-source evaluation framework of LLMs, however they do seem to want you to sign up to [Confident AI](https://www.confident-ai.com), their hosted platform for LLM monitoring.
- [TraceLoop/OpenLLMetry](https://www.traceloop.com) - open-source monitoring of LLM output, with an added SAAS offering. Bonus points for using the OpenTelemetry standard, should also be nice if you have complex agentic workflows.
- [ChainForge](https://www.chainforge.ai) - an open-source visual low-code-ish prompt and model testing environment.
- [Simon Willison's blog - Entries tagged with "eval"](https://simonwillison.net/tags/evals/) Contains many further interesting links, thoughts and discussions on how to evaluate LLM output.
