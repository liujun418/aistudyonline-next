/**
 * Script to enrich all tool descriptions in tools.ts
 *
 * This script reads each tool's existing data (name, tags, useCases, advantages,
 * targetAudience, pricing, useCase) and generates a rich, unique, SEO-friendly
 * description of 200-400 words for each tool.
 *
 * Run with: node scripts/enrich_tool_descriptions.mjs
 */

import fs from 'fs';

const filePath = 'C:/Users/jun/aistudyonline-next/src/lib/tools.ts';
let content = fs.readFileSync(filePath, 'utf8');
const lines = content.split('\n');

const TARGET_CATS = new Set(['productivity', 'writing', 'design', 'marketing']);

// First pass: collect all tool data
function parseTools() {
  const tools = [];
  let current = null;
  let braceDepth = 0;

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    const trimmed = line.trim();

    // Track brace depth
    for (const ch of line) {
      if (ch === '{') braceDepth++;
      if (ch === '}') braceDepth--;
    }

    // Start of a tool object (at depth 1)
    const startMatch = trimmed.match(/^\{$/);
    const nameMatch = trimmed.match(/^name:\s*"([^"]+)"/);
    const catMatch = trimmed.match(/^category:\s*"([^"]+)"/);

    if (braceDepth === 1 && startMatch && current === null) {
      current = { startLine: i, name: '', cat: '', tags: [], useCases: [], advantages: [], targetAudience: '', pricing: '', useCase: '' };
    }

    if (current) {
      if (nameMatch) current.name = nameMatch[1];
      if (catMatch) current.cat = catMatch[1];

      // Collect tags
      if (trimmed.startsWith('tags:')) {
        const tagMatch = trimmed.match(/tags:\s*\[([^\]]*)\]/);
        if (tagMatch) {
          current.tags = tagMatch[1].split(',').map(t => t.trim().replace(/"/g, ''));
        }
      }

      // Collect useCases
      if (trimmed.match(/^"[^"]+"/) && braceDepth > 4) {
        // We need to track array contexts properly - skip for now
      }

      // End of tool object
      if (braceDepth === 0 && current) {
        if (TARGET_CATS.has(current.cat)) {
          current.endLine = i;
          tools.push(current);
        }
        current = null;
      }
    }
  }

  return tools;
}

// Actually, let me just do direct line replacements by reading old descriptions
// and writing new ones. This is more reliable than parsing.

// Collect line numbers for descriptionLong and descriptionLongZh
const descLines = {}; // name -> { descLine, descZhLine, oldDesc, oldDescZh }

let currentName = '';
let currentCat = '';

for (let i = 0; i < lines.length; i++) {
  const s = lines[i].trim();
  const nameMatch = s.match(/^name:\s*"([^"]+)"/);
  const catMatch = s.match(/^category:\s*"([^"]+)"/);

  if (nameMatch) currentName = nameMatch[1];
  if (catMatch) currentCat = catMatch[1];

  if (currentCat && TARGET_CATS.has(currentCat)) {
    const descMatch = s.match(/^( *)descriptionLong:\s*"(.+?)",?\s*$/);
    const descZhMatch = s.match(/^( *)descriptionLongZh:\s*"(.+?)",?\s*$/);

    if (descMatch) {
      if (!descLines[currentName]) descLines[currentName] = {};
      descLines[currentName].descLine = i;
      descLines[currentName].oldDesc = lines[i];
      descLines[currentName].cat = currentCat;
    }
    if (descZhMatch) {
      if (!descLines[currentName]) descLines[currentName] = {};
      descLines[currentName].descZhLine = i;
      descLines[currentName].oldDescZh = lines[i];
      descLines[currentName].cat = currentCat;
    }
  }
}

console.log(`Found ${Object.keys(descLines).length} tools needing description updates.`);
console.log('Tool list:');
Object.entries(descLines).forEach(([name, data]) => {
  console.log(`  ${data.cat}: ${name} (line ${data.descLine})`);
});

// Now generate new descriptions and apply them
// We'll use a structured approach to ensure uniqueness

function generateNewDesc(name, cat, oldDesc) {
  // Return a rich, unique description
  const parts = [];

  switch (name) {
    case 'Notion AI':
      parts.push('Notion AI brings intelligent writing and knowledge management capabilities directly inside your Notion workspace, eliminating the need to switch between separate AI tools. It assists with drafting, summarizing, editing, and brainstorming across docs, databases, and wikis. The AI is deeply integrated into Notion's building blocks: you can generate action items from meeting notes, translate content between languages, fix spelling and grammar, auto-fill database fields, and even create entire project pages from a prompt. For teams already using Notion as their knowledge hub, Notion AI adds a layer of intelligence that transforms how you interact with your content. You can ask questions about your documents and get instant answers, summarize long pages, or generate new ideas based on existing notes. It is particularly valuable for product teams maintaining internal wikis, project managers documenting processes, and knowledge workers who live in Notion. The AI adapts to your writing style over time and learns from your content base to provide more relevant suggestions. If you are already a Notion user, this add-on is the most natural way to bring AI into your existing workflow without learning a new platform.');
      break;
    case 'Gamma':
      parts.push('Gamma is an AI-powered presentation tool that reimagines how slides, documents, and web pages are created. Instead of starting from a blank template and manually arranging content, you describe what you want in plain language, and Gamma generates a complete, beautifully designed deck with smart layouts, relevant imagery, and consistent themes. It handles the entire design process so you can focus entirely on your message. What makes Gamma different from traditional presentation tools like PowerPoint or Google Slides is its AI-first approach: every element is generated and arranged intelligently, from text placement to image selection to color schemes. You can create business presentations, pitch decks, lesson plans, project proposals, and even simple web pages without any design skills. Gamma also supports real-time editing, meaning you can refine the generated content naturally. It includes features like presenter notes, brand customization (colors, fonts, logos), and multiple export formats. Students and educators use Gamma for assignments and lectures; professionals use it for client presentations and internal reports; marketers use it for campaign pitches. For anyone who needs polished presentations fast without hiring a designer, Gamma delivers professional results in minutes.');
      break;
    case 'Beautiful.ai':
      parts.push('Beautiful.ai is an AI presentation tool built around the concept of smart templates that auto-layout your content as you add it. Unlike traditional slide editors where you manually drag, resize, and align every element, Beautiful.ai enforces design rules automatically. As you type text, add images, or insert charts, the AI arranges everything into a professionally balanced layout with consistent spacing, alignment, and typography. This design enforcement means your presentations never suffer from misaligned elements, inconsistent fonts, or cluttered slides. Beautiful.ai is particularly valuable for business professionals who need to maintain brand consistency across presentations without having design expertise. The platform offers a library of professionally designed templates that adapt to your content rather than forcing your content into fixed layouts. Sales teams use it for client pitches that need to look polished; executives use it for board presentations where visual quality matters; marketing teams use it for campaign decks that need on-brand consistency. The collaboration features allow multiple team members to work on the same deck simultaneously. For organizations that value design consistency in their external and internal communications, Beautiful.ai provides the guardrails needed to ensure every presentation meets brand standards.');
      break;
    default:
      // Generic rich description for tools not yet individually handled
      return null;
  }

  return parts.join(' ');
}

// Actually, let me use a simpler approach: just perform the replacements directly
// by building a map of old -> new strings

// Build replacements map
const replacements = [];

for (const [name, data] of Object.entries(descLines)) {
  if (!data.oldDesc || !data.oldDescZh) continue;
  const newDesc = generateNewDesc(name, data.cat, data.oldDesc);
  if (newDesc) {
    replacements.push({
      oldDesc: data.oldDesc,
      newDesc: data.oldDesc.replace(/"[^"]*"/, `"${newDesc}"`),
      oldDescZh: data.oldDescZh,
      newDescZh: data.oldDescZh // Keep same for now, we'll update Chinese later
    });
  }
}

console.log(`\nWould apply ${replacements.length} replacements.`);
console.log('Script ready for expansion with all tools.');
