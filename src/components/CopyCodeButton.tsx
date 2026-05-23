"use client";

import { useEffect } from "react";

export default function CopyCodeButton() {
  useEffect(() => {
    document.querySelectorAll("pre").forEach((pre) => {
      if (pre.querySelector(".copy-code-btn")) return;
      const btn = document.createElement("button");
      btn.className = "copy-code-btn";
      btn.textContent = "Copy";
      btn.setAttribute("aria-label", "Copy code");
      btn.style.cssText =
        "position:absolute;top:0.5rem;right:0.5rem;padding:0.25rem 0.6rem;font-size:0.75rem;" +
        "background:var(--color-slate-100);border:1px solid var(--color-slate-200);border-radius:0.25rem;" +
        "cursor:pointer;transition:all 0.15s;color:inherit;z-index:5;";
      btn.onclick = async () => {
        const code = pre.querySelector("code")?.textContent || "";
        await navigator.clipboard.writeText(code);
        btn.textContent = "Copied!";
        setTimeout(() => (btn.textContent = "Copy"), 2000);
      };
      pre.style.position = "relative";
      pre.appendChild(btn);
    });
  }, []);

  return null;
}
