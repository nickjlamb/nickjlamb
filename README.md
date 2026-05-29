# Hi, I'm Nick Lamb 👋

***I build AI systems that verify before they generate.***

**Applied AI engineer** working on LLM systems for healthcare — verification, regulatory review, patient communication. Particularly interested in constraining model behaviour to reduce harm in high-stakes domains (the subject of my recent publication, below). Founder of [PharmaTools.AI](https://pharmatools.ai), a suite of production AI tools used by clinicians, medical writers, and patients.

## 🧭 How I think about AI

- Retrieve evidence rather than invent it
- Expose uncertainty rather than conceal it
- Constrain capability where consequences are high
- Help humans audit reasoning, not replace judgement

## 📄 Research

**Lamb NJ.** *Translation, not Interpretation: Rethinking Language Model Design for Healthcare.* SN Comprehensive Clinical Medicine. 2026;8:71. [![DOI](https://img.shields.io/badge/DOI-10.1007/s42399--026--02316--9-blue)](https://doi.org/10.1007/s42399-026-02316-9) [![Open Access](https://img.shields.io/badge/Open_Access-CC_BY_4.0-green)](https://doi.org/10.1007/s42399-026-02316-9)

> Argues that LLMs in healthcare should be **constrained to translational tasks** — restructuring information across clinical, scientific, regulatory and patient-facing domains — rather than performing open-ended interpretation. A scoping argument aligned with capability-control approaches to AI safety: narrower model surface, clearer accountability, lower harm ceiling.

**Lamb NJ.** *Validation of an AI-powered mobile application for personalizing medical note explanations.* medRxiv, 2025. [![DOI](https://img.shields.io/badge/DOI-10.1101/2025.09.17.25335707-orange)](https://doi.org/10.1101/2025.09.17.25335707) [![Preprint](https://img.shields.io/badge/Preprint-medRxiv-B61F1F)](https://www.medrxiv.org/content/10.1101/2025.09.17.25335707v1)

> A three-phase validation of Patiently AI — computational readability metrics across 210 outputs, expert review by 15 clinicians, and a 54-patient survey — finding **87.3% of outputs rated clinically safe**, **70% patient preference** over standard notes, and Flesch–Kincaid grade level reduced by ~3. Empirical evidence for the "translation, not interpretation" thesis above, applied in a shipped product.

## 🏆 Featured Products

### [Patiently AI](https://getpatiently.ai) — Patient Communication
Transforms complex medical notes into clear, patient-friendly language.
**Approach:** constrained simplification to a target audience and reading level, gated so the model stays in *translation* — restating what the note already says, never crossing into diagnosis or new clinical interpretation.

```mermaid
flowchart TD
    A["Source medical note"] --> T["Constrained simplification<br/>to target audience + reading level"]
    Au["Audience — patient / carer / clinician"] --> T
    T --> G{"Translation only?<br/>no new diagnosis or<br/>clinical interpretation added"}
    G -- no --> T
    G -- yes --> O["Audience-appropriate explanation<br/>same clinical facts, clearer language"]
```

**5× Award Winner** — PMEA 2025 (Innovation & Patient Education), Communiqué 2025 Progress Award, HTN AI & Data 2025 (Highly Commended), Best Mobile App Awards.

[![App Store](https://img.shields.io/badge/App_Store-0D96F6?style=flat&logo=app-store&logoColor=white)](https://apps.apple.com/app/patiently-ai/id6670164706)
[![Play Store](https://img.shields.io/badge/Google_Play-34A853?style=flat&logo=google-play&logoColor=white)](https://play.google.com/store/apps/details?id=ai.patiently.app)
[![Web App](https://img.shields.io/badge/Web_App-2A8B7F?style=flat&logo=pwa&logoColor=white)](https://getpatiently.ai)

---

### [RefCheckr](https://refcheckr.pharmatools.ai) — Medical Writing
Verifies clinical claims against supporting references for medical writers and MLR reviewers.
**Approach:** the user's draft claim is judged against each reference by an LLM that must cite verbatim passages; a post-hoc integrity check rejects any citation that can't be located in the source PDF (hallucinated quotes get the verdict downgraded). References can be uploaded PDFs (with OCR fallback) or fetched live from PubMed / ClinicalTrials.gov / DailyMed. Output is an annotated PDF with colour-coded highlights.

```mermaid
flowchart TD
    A[Draft claim] --> V
    B["References — uploads, library,<br/>or live search via PubCrawl MCP"] --> X[PDF text extraction<br/>OCR fallback for scans]
    X --> V[Per-reference LLM verification<br/>judges claim against full source text]
    V --> O[Verdict + confidence +<br/>quoted passages with PDF locations]
    O --> G{Can each quote be matched<br/>in the source PDF?}
    G -- no --> D[Downgrade verdict<br/>hallucinated quotes rejected]
    G -- yes --> P[Annotated PDF<br/>colour-coded highlights]
    D --> P
```

[![Web App](https://img.shields.io/badge/Web_App-2A8B7F?style=flat&logo=pwa&logoColor=white)](https://refcheckr.pharmatools.ai)
[![Word Add-in](https://img.shields.io/badge/Word_Add--in-2B579A?style=flat&logo=microsoftword&logoColor=white)](https://marketplace.microsoft.com/en-us/product/WA200010362?tab=Overview)

---

### [MedCheckr](https://pharmatools.ai) — Regulatory Compliance
AI-powered regulatory review tool that checks promotional claims against the ABPI Code of Practice with clause-level transparency. **Code Clarity Awards Winner, 2024.**
**Approach:** RAG over the ABPI Code corpus with Pinecone vector embeddings; every finding cites the specific clause(s) it relies on, so reviewers can audit each decision.

[![App Store](https://img.shields.io/badge/App_Store-0D96F6?style=flat&logo=app-store&logoColor=white)](https://apps.apple.com/app/medcheckr-abpi/id6737439961)

---

### [PosterLens](https://pharmatools.ai) — Research
Captures scientific posters and generates instant AI summaries. Presented at ESMO AI & Digital Oncology Congress 2025.
**Approach:** mobile vision capture → multimodal LLM extraction into a structured schema (study design, endpoints, results, limitations).

[![App Store](https://img.shields.io/badge/App_Store-0D96F6?style=flat&logo=app-store&logoColor=white)](https://apps.apple.com/app/posterlens/id6744457926)

---

### [BiomarkerFinder](https://pharmatools.ai) — Drug Discovery
AI-powered insights into complex biomarker data, explained in plain language. **Winner at Open Targets Hackathon.**
**Approach:** pulls structured biomarker associations from Open Targets and translates them into plain-language explanations with provenance back to the underlying datasets.

---

### [HushMap](https://pharmatools.ai) — Wellbeing
Helps neurodivergent individuals locate sensory-friendly places nearby. Community contributions and Apple Watch support.

[![App Store](https://img.shields.io/badge/App_Store-0D96F6?style=flat&logo=app-store&logoColor=white)](https://apps.apple.com/app/hushmap/id6742574192)

## 🔧 Open Source

### [PubCrawl](https://github.com/nickjlamb/pubcrawl) — MCP server for biomedical literature
TypeScript MCP server giving LLM clients direct access to PubMed, ClinicalTrials.gov, FDA DailyMed (USPI), and the UK eMC (SmPC) — including a side-by-side US/UK label comparison tool. Built so models retrieve and reason over real biomedical literature rather than rely on parametric memory. Powers retrieval in RefCheckr; published to npm as `@pharmatools/pubcrawl`, and listed in the official MCP registry.

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/nickjlamb/pubcrawl)
[![npm](https://img.shields.io/badge/npm-CB3837?style=flat&logo=npm&logoColor=white)](https://www.npmjs.com/package/@pharmatools/pubcrawl)
[![MCP Registry](https://img.shields.io/badge/MCP_Registry-listed-6E56CF?style=flat)](https://registry.modelcontextprotocol.io/?q=pubcrawl)

---

### [RSI Loop](https://github.com/nickjlamb/rsi-loop) — Validated self-improving detector
A computer-vision pipeline that detects RSI risk and *improves its own detection logic* against a benchmark suite — but is gated by a separate regulatory Auditor that rejects mutations producing test-passing but clinically implausible thresholds. A concrete miniature of specification-gaming / reward-hacking mitigation: optimise freely, accept only iterations that are *simultaneously* accurate **and** within published clinical norms.

```mermaid
flowchart TD
    A["Webcam pose + hand landmarks"] --> D["RSI-risk detector vN"]
    D --> E["Score against benchmark suite"]
    E --> I["Self-improvement proposes vN+1<br/>new thresholds / logic"]
    I --> G{"Auditor: accurate on benchmark<br/>AND within published clinical norms?"}
    G -- no --> R["Reject mutation<br/>specification-gaming blocked"]
    R --> I
    G -- yes --> N["Accept vN+1 as new baseline"]
    N --> D
```

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/nickjlamb/rsi-loop)

## 🛠 Tech Stack

**LLM systems:** Claude API · MCP · RAG (Pinecone) · multimodal · structured outputs · evals

**Application:** Node.js · Python · Swift / SwiftUI · Firebase · Postgres

![Claude API](https://img.shields.io/badge/Claude_API-191919?style=flat&logo=anthropic&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=flat&logo=node.js&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)
![Swift](https://img.shields.io/badge/Swift-FA7343?style=flat&logo=swift&logoColor=white)
![SwiftUI](https://img.shields.io/badge/SwiftUI-0D96F6?style=flat&logo=swift&logoColor=white)
![Firebase](https://img.shields.io/badge/Firebase-FFCA28?style=flat&logo=firebase&logoColor=black)
![Postgres](https://img.shields.io/badge/Postgres-4169E1?style=flat&logo=postgresql&logoColor=white)

## 📫 Get in Touch

- 🌐 [pharmatools.ai](https://pharmatools.ai)
- 🌐 [medcopywriter.com](https://medcopywriter.com)
- ✉️ nick@pharmatools.ai
- 💼 [LinkedIn](https://www.linkedin.com/in/medcopywriter/)
