# Free Access to Codex, Hermes, and More: A Practical Guide for Overseas Users

In the realm of AI tools, accessing powerful resources like Codex and Hermes often comes with costs or restrictions\. However, this guide will walk you through a practical, long\-term free method to utilize these tools, perfect for those running overseas websites who need reliable AI capabilities without breaking the bank\.

## Leveraging Codex\+\+ and Agnes API

First, we introduce **Codex\+\+**, an open\-source tool that allows you to replace the underlying model of Codex\. Paired with **Agnes API**, a free offering from a top 10 global AI lab, you can access robust AI capabilities at no cost\.

Agnes provides three flagship multimodal models for free:

- **Text \& Agent**: `Agnes-2.0-Flash`

- **Image Generation**: `Agnes-Image-2.1-Flash`

- **Video Generation**: `Agnes-Video-V2.0`

These models cover text, image, and video generation, making them suitable for a wide range of tasks for overseas websites, such as content creation, product image generation, and more\.

## Step\-by\-Step Setup for Codex\+\+ with Agnes

1. **Get Codex\+\+ from GitHub**
Navigate to the Codex\+\+ repository on GitHub and set it up\. This tool acts as a bridge to connect Codex with alternative models\.

2. **Configure the Supplier in Codex\+\+**

    - Go to the Codex\+\+ management console\.

    - In "Supplier Configuration", click "Add"\.

    - Fill in the details:

        - **Name**: Agnes

        - **Access Method**: Pure API

        - **Base URL**: `https://apihub.agnes-ai.com/v1`

        - **API Key**: Generate an API key from the Agnes platform and paste it here\.

    - Select "Chat" for the upstream protocol and fetch models from the upstream\.

    - Save and restart Codex\.

3. **Test the Configuration**
Open Codex, select `agnes-2.0-flash` as the model, and send a test message like "Hello" to verify it works\.

## Building Custom Skills with Playwright CLI

To extend functionality, we can create custom skills using Playwright CLI\. Here’s how to set up a skill for generating images with Agnes\-Image\-2\.1\-Flash:

1. **Create a Project Folder**
Make a new folder \(e\.g\., `agnes_project`\) and open it in the terminal\.

2. **Install Dependencies**
Run the following commands:

    ```bash
    npm install -g @playwright/cli@latest
    playwright-cli install --skills
    ```

3. **Configure the Skill Folder**
Rename the folder storing skills from `.claude` to `.codex` within your project directory\.

4. **Develop an Image Generation Skill**
Use the Skill Creator in Codex to define a skill that calls the Agnes\-Image\-2\.1\-Flash API\. Here’s a sample script structure:

    ```python
    import requests
    import json
    import urllib.request
    import urllib.error
    
    # Configuration
    API_KEY = "YOUR_AGNES_API_KEY"  # Replace with your actual API key
    BASE_URL = "https://apihub.agnes-ai.com/v1"
    ENDPOINT = "/images/generations"
    MODEL = "agnes-image-2.1-flash"
    
    def generate_image(prompt, size="1024x1024", image_url=None, save_path=None):
        payload = {
            "model": MODEL,
            "prompt": prompt,
            "size": size,
        }
        if image_url:
            payload["extra_body"] = {
                "image_urls": [image_url],
                "response_format": "url"
            }
        data = json.dumps(payload).encode('utf-8')
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }
        response = requests.post(f"{BASE_URL}{ENDPOINT}", headers=headers, data=data)
        response_data = response.json()
        if save_path and "data" in response_data:
            image_url = response_data["data"][0]["url"]
            urllib.request.urlretrieve(image_url, save_path)
        return response_data
    ```

5. **Test the Skill**
Run the script with a prompt:

    ```bash
    python .codex/skills/agnes-imagegen/script/generate.py --prompt "A futuristic cityscape"
    ```

## Deploying Hermes Agent with Agnes API

Hermes Agent is a powerful tool, but it can be token\-heavy\. By integrating it with Agnes API, you can use it for free:

1. **Set Up WSL \(Windows Subsystem for Linux\)**
Use WSL as the runtime environment for Hermes\.

2. **Install Hermes Agent**
Run the installation command:

    ```bash
    curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
    ```

3. **Configure Agnes API in Hermes**

    - When prompted, select `custom (direct API)`\.

    - Set the **API base URL** to `https://apihub.agnes-ai.com/v1`\.

    - Enter your Agnes API key\.

    - Choose `Chat Completions` for the API format and select `agnes-2.0-flash` as the model\.

4. **Add a Messaging Channel \(e\.g\., WeChat\)**
Run:

    ```bash
    hermes gateway setup
    ```

    Select WeChat, scan the QR code to link your account, and follow the prompts to complete setup\.

5. **Test Hermes**
Send a message like "What’s the weather like in Qingdao?" to your Hermes\-enabled WeChat\. Approve the tool call when prompted with `/approve` to get the result\.

## Practical Applications for Overseas Websites

- **Content Creation**: Use Agnes\-Image\-2\.1\-Flash to generate unique images for blog posts or product pages\. For example, to create a series of images for a "Little Horse Crossing the River" children’s ebook:

    ```bash
    python .codex/skills/agnes-imagegen/script/generate.py --prompt "A cute little horse by a river, watercolor style"
    ```

- **Automated Tasks**: Deploy Hermes to handle customer inquiries, fetch data, or automate content updates on your overseas site\.

- **Multimodal Marketing**: Leverage Agnes\-Video\-V2\.0 to create promotional videos for your products, all for free\.

By following this guide, you can harness the power of Codex, Hermes, and Agnes API to enhance your overseas website’s functionality without incurring costs, making your AI\-driven projects both practical and budget\-friendly\.
