# Hi, I'm Nick Lamb 👋

**Applied AI engineer** building LLM systems for healthcare — clinical writing, regulatory review, patient communication.

Particularly interested in *constraining* model behaviour to reduce harm in high-stakes domains (the subject of my recent publication, below). Founder of [PharmaTools.AI](https://pharmatools.ai), a suite of production AI tools used by clinicians, medical writers, and patients.

## 📄 Research

**Lamb NJ.** *Translation, not Interpretation: Rethinking Language Model Design for Healthcare.* SN Comprehensive Clinical Medicine. 2026;8:71. [![DOI](https://img.shields.io/badge/DOI-10.1007/s42399--026--02316--9-blue)](https://doi.org/10.1007/s42399-026-02316-9) [![Open Access](https://img.shields.io/badge/Open_Access-CC_BY_4.0-green)](https://doi.org/10.1007/s42399-026-02316-9)

> Argues that LLMs in healthcare should be **constrained to translational tasks** — restructuring information across clinical, scientific, regulatory and patient-facing domains — rather than performing open-ended interpretation. A scoping argument aligned with capability-control approaches to AI safety: narrower model surface, clearer accountability, lower harm ceiling.

## 🏆 Featured Products

### [Patiently AI](https://getpatiently.ai) — Patient Communication
Transforms complex medical notes into clear, patient-friendly language.
**Approach:** constrained translation prompting with reading-level targets; constraints prevent over-simplification and hallucinated reassurance.

**5× Award Winner:**
- PMEA Awards 2025 (Innovation & Patient Education)
- Communiqué Awards 2025 Progress Award
- HTN AI & Data Awards 2025 Highly Commended
- Best Mobile App Awards Winner

[![App Store](https://img.shields.io/badge/App_Store-0D96F6?style=flat&logo=app-store&logoColor=white)](https://apps.apple.com/app/patiently-ai/id6670164706)
[![Play Store](https://img.shields.io/badge/Google_Play-34A853?style=flat&logo=google-play&logoColor=white)](https://play.google.com/store/apps/details?id=ai.patiently.app)
[![Web App](https://img.shields.io/badge/Web_App-2A8B7F?style=flat&logo=pwa&logoColor=white)](https://getpatiently.ai)

---

### [RefCheckr](https://refcheckr.pharmatools.ai) — Medical Writing
Verifies clinical claims against supporting references for medical writers and MLR reviewers.
**Approach:** claim extraction → retrieval across PubMed, ClinicalTrials.gov and DailyMed → LLM verification with span-level citations → annotated PDF export. OCR fallback for scanned references.

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
TypeScript MCP server giving LLM clients direct access to PubMed, ClinicalTrials.gov, FDA DailyMed (USPI), and the UK eMC (SmPC) — including a side-by-side US/UK label comparison tool. Powers retrieval in RefCheckr. Published to npm as `@pharmatools/pubcrawl`.

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/nickjlamb/pubcrawl)
[![npm](https://img.shields.io/badge/npm-CB3837?style=flat&logo=npm&logoColor=white)](https://www.npmjs.com/package/@pharmatools/pubcrawl)

---

### [RSI Loop](https://github.com/nickjlamb/rsi-loop) — Validated self-improving detector
A computer-vision pipeline that detects RSI risk and *improves its own detection logic* against a benchmark suite — but is gated by a separate regulatory Auditor that rejects mutations producing test-passing but clinically implausible thresholds. A concrete miniature of specification-gaming / reward-hacking mitigation: optimise freely, accept only iterations that are *simultaneously* accurate **and** within published clinical norms.

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
- 💼 [LinkedIn](https://linkedin.com/in/nickjlamb)
