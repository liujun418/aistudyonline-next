"use client";

import { useEffect } from "react";
import "highlight.js/styles/atom-one-dark.css";
import hljs from "highlight.js/lib/core";
import bash from "highlight.js/lib/languages/bash";
import python from "highlight.js/lib/languages/python";
import javascript from "highlight.js/lib/languages/javascript";
import typescript from "highlight.js/lib/languages/typescript";
import json from "highlight.js/lib/languages/json";
import xml from "highlight.js/lib/languages/xml";
import css from "highlight.js/lib/languages/css";
import plaintext from "highlight.js/lib/languages/plaintext";

hljs.registerLanguage("bash", bash);
hljs.registerLanguage("shell", bash);
hljs.registerLanguage("python", python);
hljs.registerLanguage("javascript", javascript);
hljs.registerLanguage("js", javascript);
hljs.registerLanguage("typescript", typescript);
hljs.registerLanguage("ts", typescript);
hljs.registerLanguage("json", json);
hljs.registerLanguage("html", xml);
hljs.registerLanguage("xml", xml);
hljs.registerLanguage("css", css);
hljs.registerLanguage("plaintext", plaintext);
hljs.registerLanguage("text", plaintext);

export default function CodeBlocks() {
  useEffect(() => {
    document.querySelectorAll("pre").forEach((pre) => {
      if (pre.dataset.codeBlockProcessed) return;
      pre.dataset.codeBlockProcessed = "1";

      const code = pre.querySelector("code");
      const langClass = code?.className.match(/language-(\w+)/);
      const lang = langClass ? langClass[1].toLowerCase() : "text";
      const langLabels: Record<string, string> = {
        bash: "Bash", shell: "Shell", python: "Python",
        javascript: "JavaScript", js: "JavaScript",
        typescript: "TypeScript", ts: "TypeScript",
        json: "JSON", html: "HTML", xml: "XML", css: "CSS",
        text: "Text", plaintext: "Text",
      };
      const langLabel = langLabels[lang] || lang;

      // Wrap pre in container
      const wrapper = document.createElement("div");
      wrapper.className = "code-block-wrapper";
      pre.parentNode?.insertBefore(wrapper, pre);
      wrapper.appendChild(pre);

      // Language badge
      const badge = document.createElement("span");
      badge.className = "code-lang-badge";
      badge.textContent = langLabel;
      wrapper.appendChild(badge);

      // Copy button
      const btn = document.createElement("button");
      btn.className = "code-copy-btn";
      btn.textContent = "Copy";
      btn.setAttribute("aria-label", "Copy code");
      btn.onclick = async () => {
        const text = code?.textContent || "";
        await navigator.clipboard.writeText(text);
        btn.textContent = "Copied!";
        setTimeout(() => (btn.textContent = "Copy"), 2000);
      };
      wrapper.appendChild(btn);

      // Explicitly set language class to prevent highlight.js auto-detection
      if (code) {
        code.className = `language-${lang}`;
      }

      // Apply syntax highlighting
      try {
        hljs.highlightElement(code as HTMLElement);
      } catch {
        // fallback: no highlighting
      }
    });
  }, []);

  return null;
}
