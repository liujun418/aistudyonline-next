# Official Tutorial: Three Ways Codex Can Control Your Computer for You

Codex offers three distinct ways to control your computer and automate tasks\. Which one is right for you? And what are their capabilities and limitations? Jason Liu, former Meta data scientist and current OpenAI Developer Experience Engineer, recently published a post explaining the use cases, features, and advantages of each method\.

## 1\. Computer Use

Computer Use is currently the most powerful and versatile way for an agent to control a computer, and it is the key reason Codex stands out among other agent tools\. It can simulate most operations on your computer, whether it’s WeChat, Feishu, Excel, or video editing software\. As long as the operation involves mouse clicks or keyboard input, it can generally handle it\. It is available on both macOS and Windows, and can switch between different applications when a task involves multiple software programs\.

Jason Liu shared a real example: once his package was stolen, but Amazon customer service had a 25\-minute wait time\. He instructed Codex to check the customer service window every five minutes, switch to checking every minute once the customer service representative connected, and then apply for a refund\. When Jason returned from his shower, the refund had already been processed\. This demonstrates the core strength of Computer Use: it can monitor windows and workflows, taking over tedious but necessary tasks\.

However, it has a clear limitation: it is slow\. Each step requires understanding the interface, locating the button, and then performing the click or input\. This visual loop is time\-consuming, so it is not suitable for tasks requiring extreme efficiency\. But it is ideal for tasks that have no API, no plugins, and can only be completed through the graphical interface\.

## 2\. Codex Chrome Extension

The Codex Chrome Extension is designed for tasks that primarily occur in the browser, especially those requiring a logged\-in state, such as Feishu Docs, Taobao Merchant Backend, and Bilibili Creator Center\. These tools rely on account status, and the extension can directly use your logged\-in browser session to operate\.

The key difference from Computer Use is that Computer Use simulates clicking buttons on the screen, while the Chrome Extension works directly within the browser workflow\. It can read web content and switch between multiple tabs, for example, viewing data, comparing information, and compiling results\. As a result, browser tasks using the Chrome Extension are usually faster, more accurate, and more efficient than using Computer Use\.

Jason Liu uses it long\-term to check private messages, browse news, collect feedback, and save valuable content to local files for easy access later\. However, it has more sensitive permissions: since it uses your real logged\-in state, websites will treat Codex’s clicks, inputs, and submissions as your own actions\. You can safely use it for information collection and content drafting, but you should personally confirm actions like sending messages or making payments\.

## 3\. In\-App Browser

The in\-app browser is more suitable for developers, especially for web frontend development and local tool debugging\. For example, when working on a frontend page, you can have Codex open the local preview address, check for layout issues, button misalignment, or mobile overflow\. After reviewing, it can directly modify the code and then reopen the page for verification\.

Its most valuable feature is that it connects code writing and result viewing\. So the in\-app browser is not for logging into websites; it is more like Codex’s workspace for web development and interface debugging\.

## How to Choose?

- For website tasks requiring a logged\-in state: use the Chrome Extension\.

- For tasks involving desktop software or switching between multiple applications: use Computer Use\.

- For web development, page preview, and interface debugging: use the in\-app browser\.

Jason Liu also emphasized that if a task can be completed using plugins or MCP, you should prioritize using structured tools\. For example, reading Feishu Docs or organizing online tables directly with plugins or interfaces is usually more accurate than having Codex simulate clicks in the interface\.

In other words, Codex’s computer control is not about being as human\-like as possible, but about choosing the right entry point\. A truly strong agent does not mindlessly click the mouse when given a task; it knows when to call an API, when to use the browser, and when to take over the desktop\. This is the most notable change in Codex: it is no longer just a coding tool, but is evolving into a task execution system that revolves around computers, browsers, and local projects\.

