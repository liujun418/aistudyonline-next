# Google\&\#39;s 5 Skill Design Patterns for Stable Agent Output: A Practical Guide for Overseas Web Development



In the realm of AI agent development, especially for overseas web projects, ensuring stable and high\-quality output from agents is crucial\. Google has summarized five Skill design patterns that address common 失控 \(loss of control\) scenarios and provide practical solutions\. Let’s dive into these patterns with a focus on their applicability for overseas website teams\.

## 1\. Tool Wrapper: On\-Demand Knowledge Injection

One common pitfall is overloading agents with irrelevant knowledge, leading to confusion and inefficiency\. The **Tool Wrapper** pattern solves this by injecting knowledge only when needed\.

### How It Works

- Define trigger conditions in `SKILL\.md` to identify when specific domain knowledge is required\.

- Store domain\-specific knowledge \(e\.g\., React style guides, SQL best practices\) in a `references/` directory\.

- The agent loads and applies this knowledge only when the task matches the trigger conditions\.

### Practical Example for Overseas Web Teams

Suppose you’re building a multilingual e\-commerce site with React\. Instead of embedding all React documentation into the agent’s system prompt, use Tool Wrapper:

```markdown
# SKILL.md (Trigger Logic)
When the task involves modifying React components, load references/react-i18n-style-guide.md.

# references/react-i18n-style-guide.md
- Use react-intl for localization.
- Follow ISO 639-1 language codes (e.g., "en-US", "es-ES").
- Wrap all static text in <FormattedMessage> components.
```

This way, the agent only accesses localization\-specific React knowledge when working on UI components, keeping context lean and relevant\.

## 2\. Generator: Standardize Output Structure

Inconsistent output formats \(e\.g\., varying API documentation styles or report structures\) are a headache for overseas teams\. The **Generator** pattern enforces consistent output using templates and style guides\.

### How It Works

- `SKILL\.md` defines what content to generate \(e\.g\., an API document\)\.

- `references/` contains style guides \(e\.g\., tone, formatting rules\)\.

- `assets/` holds templates \(e\.g\., API doc templates\)\.

- The agent fills variables in templates and applies style rules for uniform output\.

### Practical Example: API Documentation for Global APIs

For an overseas payment gateway’s API docs, use Generator to ensure consistency:

```markdown
# SKILL.md
Generate API documentation with sections: Endpoint, Parameters, Response, Error Codes. Use the tone from references/api-style-guide.md.

# references/api-style-guide.md
- Use formal, concise language suitable for developers worldwide.
- List parameters with data types and required/optional status.
- Explain errors with HTTP status codes and user-friendly messages.

# assets/api-template.md
## {Endpoint Name}
- Method: {HTTP Method}
- URL: {Base URL}{Path}
- Parameters:
  {Parameter List}
- Response:
  {Response Schema}
- Error Codes:
  {Error Code List}
```

This ensures every API document follows the same structure, making it easy for developers across regions to understand\.

## 3\. Reviewer: Separate Review Standards and Process

Overseas teams often need to adapt to different compliance standards \(e\.g\., GDPR for Europe, CCPA for California\)\. The **Reviewer** pattern separates *what to check* \(standards\) from *how to check* \(process\)\.

### How It Works

- `SKILL\.md` defines the review process \(e\.g\., steps to audit code\)\.

- `review\-checklist\.md` in `references/` lists specific standards \(e\.g\., GDPR compliance checks\)\.

- The agent applies the process to different checklists, ensuring flexibility\.

### Practical Example: Multi\-Region Compliance Audits

For a web app serving EU and US users, create a reusable review process:

```markdown
# SKILL.md (Review Process)
1. Load the relevant checklist from references/.
2. Audit the code against each checklist item.
3. Generate a report with error, warning, and info levels.

# references/gdpr-checklist.md
- [ ] All user data is encrypted in transit and at rest.
- [ ] Privacy policy links are present on all data-collecting pages.
- [ ] Users can request data deletion via a dedicated endpoint.

# references/ccpa-checklist.md
- [ ] "Do Not Sell My Personal Information" option is visible on the homepage.
- [ ] Users are notified of data collection at the point of collection.
```

This way, the same review process can adapt to GDPR, CCPA, or other regional standards by swapping out checklists\.

## 4\. Inversion: Gather Information Before Acting

Overseas projects often involve unclear requirements \(e\.g\., a client’s vague request for a “multilingual blog”\)\. The **Inversion** pattern flips the script: the agent asks questions to clarify requirements before generating output\.

### How It Works

- **Phase 1: Discovery** – Ask what problem needs solving \(e\.g\., “Who is the target audience for the blog?”\)\.

- **Phase 2: Constraints** – Clarify boundaries \(e\.g\., “Which languages are required? What’s the budget for translation?”\)\.

- **Phase 3: Synthesis** – Generate output only after all information is gathered\.

### Practical Example: Building a Global Marketing Landing Page

If a client requests a “high\-converting landing page for our new product,” the agent uses Inversion:

```text
// Phase 1: Discovery
- Who is the target audience? (e.g., European SMEs, US startups)
- What’s the primary call-to-action? (e.g., sign up for a demo, make a purchase)

// Phase 2: Constraints
- Which languages are needed? (e.g., English, German, French)
- Are there any brand guidelines (colors, fonts) to follow?
- What’s the deadline for launch?

// Phase 3: Synthesis
Only after receiving answers to these questions does the agent generate the landing page code, copy, and design.
```

## 5\. Pipeline: Enforce Step\-by\-Step Execution

Complex tasks \(e\.g\., launching a multiregional web app\) require strict step\-by\-step execution\. The **Pipeline** pattern defines a sequential workflow with gatekeepers to prevent skipping steps\.

### How It Works

- Break the task into stages \(e\.g\., Parse → Generate → Assemble → Verify\)\.

- Each stage has a “gate” that must be passed before moving to the next\.

- `SKILL\.md` defines the workflow and gate conditions\.

### Practical Example: Automated API Documentation for Overseas Developers

For a process that generates API docs for a global audience, use Pipeline:

```markdown
# SKILL.md (Pipeline Definition)
Step 1: Parse API code to extract endpoints and parameters. (Gate: All endpoints are identified.)
Step 2: Generate docstrings for each endpoint. (Gate: Docstrings follow references/api-style-guide.md.)
Step 3: Assemble docstrings into a single document. (Gate: All endpoints are included.)
Step 4: Verify documentation for accuracy and completeness. (Gate: No errors found in review.)
```

This ensures no step \(like skipping verification\) is missed, critical for maintaining quality in overseas projects\.

## Choosing the Right Pattern for Your Overseas Project

Use this decision flow to pick the right pattern:

1. **Does the task require template\-based output?** → Use **Generator**\.

2. **Is the goal to load knowledge on demand?** → Use **Tool Wrapper**\.

3. **Is the task a review/audit with changing standards?** → Use **Reviewer**\.

4. **Do you need to clarify requirements before acting?** → Use **Inversion**\.

5. **Does the task have strict, sequential steps?** → Use **Pipeline**\.

These patterns can also be combined\. For example, a Generator can be paired with Inversion to gather requirements before filling a template, or a Pipeline can use Tool Wrapper to load region\-specific knowledge at each step\.

By implementing these patterns, overseas web teams can ensure their AI agents deliver consistent, high\-quality output—whether they’re building multilingual UIs, complying with global regulations, or launching complex web applications\. Start by identifying your team’s most common pain points \(e\.g\., inconsistent docs, unclear requirements\) and apply the corresponding pattern to see immediate improvements\.
