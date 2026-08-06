# The Most Dangerous Idea in AI: Let It Improve Itself

In the current landscape of AI research, one idea stands out as both the most alluring and the most perilous: **letting AI improve itself**\. Imagine a scenario where AI writes code, trains the next\-generation model, and then that next model turns around to enhance itself, leading to even more powerful subsequent models\. Many refer to the realization of this loop as the "singularity" because once it’s operational, AI could break free from human limitations and evolve independently at an exponential pace\.

## A Deep Dive into Anthropic’s Latest Paper

Let’s delve into a recent paper by Anthropic titled *“When AI Builds Itself”*\. It opens with two intriguing visuals\. One is a pixel\-art style Claude logo that self\-replicates into a larger version, which then becomes the small unit for the next replication cycle\. This visual metaphor illustrates that if AI enters a self\-building loop, its growth won’t be linear but rather a cascading, accelerating process—one cycle nested within another, getting faster and faster\.

The second visual depicts the evolution of AI development methods\. It starts with engineers writing code by hand to create the first\-generation Claude\. Then, chatbots emerge, but humans remain the central figures, with AI assisting in writing snippets of code\. Next, capable agents appear, moving beyond mere chatting to modifying files and running code autonomously\. In the current stage, these agents can even dispatch sub\-agents to collaborate on tasks that take hours to complete\. The final stage is labeled *“Closing the Loop”*, where AI designs, trains, and improves the next\-generation model iteratively\. This is the core argument of Anthropic’s paper: AI research might be entering a cycle of self\-acceleration and self\-revolution\.

While this paper is insightful and worth reading as it points to the cutting\-edge direction of AI in the coming months, it’s important to note that it’s not a rigorous academic paper\. As a document produced by Anthropic itself, it contains data, but also PR\-oriented framing—like emphasizing the “danger” of their models to garner global attention\. So, while the data is valuable, we should take the conclusions with a grain of salt\.

## Concrete Numbers and Practical Cases

Let’s look at some concrete figures Anthropic provides:

- Claude now writes over 80% of the code in Anthropic’s official codebase\.

- A typical engineer’s daily code contribution is about 8 times what it was in 2024\.

- In third\-party tests, tasks that used to take a human 4 minutes can now be completed by Claude in 1\.5 hours, and some tasks have seen a 52x speedup in small labs\.

However, we should approach these numbers with caution\. For instance, when Anthropic hyped its Mythos model as extremely powerful, real\-world tests told a different story\. A developer of the `curl` tool found that among 5 reported vulnerabilities by Mythos, only one was a valid low\-severity issue\. Similarly, Mozilla mentioned that Mythos helped find 271 vulnerabilities, but none were beyond what human experts could detect\. Even a demo vulnerability highlighted by the Mythos team was detectable by 8 smaller models\. This shows that despite advancements, large language models still rely on predicting the next token and haven’t evolved into a new species capable of inherent truth\-judging, value\-assessing, or direction\-setting\. Thus, human review remains indispensable in the short term\.

## Two Categories of AI Work: Execution and Judgment

Anthropic categorizes AI work into two types:

- **Execution**: Writing code, running experiments, fixing bugs, creating reports, etc\.

- **Judgment**: Deciding which research problems are worth pursuing, determining the credibility of results, and knowing when to stop or pivot directions\.

Current models like Claude excel at execution—given a goal, they can figure out how to achieve it\. However, they still lag behind humans in judgment\. This gap, while significant, might be narrowing faster than we think\. Anthropic has observed that as Claude writes code faster and faster, human code review has become the new bottleneck\.

## Three Future Scenarios

Anthropic outlines three potential futures:

1. **Stagnation in AI Capabilities**: Even if AI progress slows, existing tools will still transform industries\. A 100\-person company could achieve what once required 1,000 people\.

2. **AI Continues to Strengthen, but Humans Set Direction**: Companies will become human\-AI hybrids with explosive efficiency, but review, validation, and management will be the bottlenecks\.

3. **AI Sets Its Own Direction**: Humans lose the ability to supervise, validate, or halt progress, leading to complete loss of control over the models\.

After laying out these scenarios, Anthropic’s recommendation is for humanity to have the option to slow down or pause AI development\. While this sounds responsible, it’s ironic—Anthropic is a leading player in the AI race, pressing the accelerator while warning about the dangers and calling for speed limits\. So, take this conclusion with your own critical thinking\.

## Personal Reflections

Returning to the two opening visuals: one shows accelerating speed as AI participates in building the next generation, and the other shows humans’ role shrinking—from writing code by hand to letting AI write code, then letting AI direct other AIs\. These two trends are intertwined\.

An Anthropic employee shared a telling insight: when agents work smoothly, humans feel irrelevant because automation is faster; when agents fail, humans still feel irrelevant because they can’t understand the complex work the agent was doing\. This duality makes sense—each time you delegate a task to AI and it performs quickly and well, you’re inclined to delegate more\. But each delegation also reduces your ability to judge if the AI’s work is correct\. This recursive dynamic between humans and AI is key\. We cede ground for what seem like wise, reasoned choices, but when we stop to check, we find we’ve lost comprehension\. Yet, looking back, each step feels justified\. This is the fascinating predicament we face with AI today\.

