# AI Beginner's Quick Guide: Common Jargon Explained

If you've ever tried to learn AI, you've probably felt overwhelmed by terms like "large model," "Codex," "Skill," and "Prompt" floating around online\. This guide breaks down these key concepts using real\-life examples, so you can understand them clearly and apply them right away\.

## 1\. Large Language Model \(LLM\)

A large language model is like the **brain** of an AI system\. Different models have different capabilities—some are better at reasoning, others at coding, and some at creative writing\.

### Example

- **Model A**: When told "the table is dirty," it only writes a note saying "the table is dirty" instead of cleaning it\.

- **Model B**: When told "the table is dirty," it immediately grabs a cloth and cleans the table\.

This shows that the model you choose directly determines how "smart" your AI will be\.

### Common LLM Examples

- GPT\-4o

- Claude 3

- Gemini

- Doubao

- DeepSeek

## 2\. Prompt

A prompt is the **command** you give to an AI\. The more specific your prompt is, the more accurate the AI's response will be\.

### Bad Prompt Example

```Plain Text
Give me something to drink.
```

This vague prompt might result in the AI giving you a watering can instead of a beverage\.

### Good Prompt Example

```Plain Text
I am a human. It's very hot today, and I want to drink something cold, sweet, tasty, and cheap.
```

This clear prompt will likely result in the AI giving you a suitable cold drink\.

## 3\. Agent

An Agent is an **AI employee** that can understand tasks, use tools, and work independently to complete them\.

### Example

When you ask an Agent to find a book:

1. The Agent first checks the fridge \(no books there\)\.

2. It then searches its internal knowledge base \(no books there\)\.

3. Finally, it checks the external library and finds the book you want\.

This shows that an Agent can take initiative to solve problems without constant guidance\.

## 4\. Codex

Codex is a **programming\-savvy AI employee** that specializes in writing and understanding code\.

### Example

If you ask an Agent to find a book, it will search for books\. If you ask Codex to find a book, it might write a Python script to search for books automatically:

```python
def find_book(book_title):
    library = ["The Great Gatsby", "1984", "To Kill a Mockingbird"]
    for book in library:
        if book_title.lower() in book.lower():
            return f"Found: {book}"
    return "Book not found"

print(find_book("1984"))
```

## 5\. Skill

A Skill is a **standard operating procedure \(SOP\)** for an Agent\. It tells the Agent how to perform a specific task consistently\.

### Example

If an Agent keeps finding the wrong books, you can give it a Skill document that says:

```Plain Text
Book Search Skill:
1. Only search the bookshelf in the living room.
2. Look for books with red covers.
3. Check the first page to confirm it's the right book.
```

Now, every time the Agent searches for a book, it will follow these steps and find the right one\.

## 6\. Workflow

A Workflow is a **sequence of steps** that an Agent follows to complete a task\.

### Example

A workflow for finding and returning a book might be:

1. Find the book\.

2. Clean the book\.

3. Return the book to the shelf\.

## 7\. API

An API is a **plug** that connects an AI to other tools or software\.

### Example

If you want your AI to send emails, you can use an email API to connect your AI to an email service\. This way, the AI can send emails without having its own built\-in email functionality\.

## 8\. Knowledge Base

A Knowledge Base is a **database** that limits the information an AI can use\.

### Example

If you want your AI to only answer questions about your company's products, you can set up a knowledge base that only contains information about your products\. This way, the AI won't use information from the internet or other sources\.

## Summary

- **Large Language Model**: The brain of the AI\.

- **Prompt**: The command you give to the AI\.

- **Agent**: An AI employee that can work independently\.

- **Codex**: An AI employee that specializes in coding\.

- **Skill**: A standard operating procedure for an Agent\.

- **Workflow**: A sequence of steps for completing a task\.

- **API**: A plug that connects an AI to other tools\.

- **Knowledge Base**: A database that limits the AI's information sources\.

