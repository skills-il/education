---
name: israeli-tech-interview-prep
description: Prepare for technical interviews at Israeli tech companies with company-specific processes, question patterns, and Hebrew technical vocabulary. Use when getting ready for interviews at Israeli startups, enterprises, or multinational R&D centers, practicing system design questions relevant to Israeli tech products, or learning Hebrew terms used in technical discussions. Covers interview rounds, coding challenges, behavioral questions, and company culture expectations. Do NOT use for non-technical roles, academic interviews, or interviews at companies outside Israel.
license: MIT
allowed-tools: Bash(python:*) Read
compatibility: Requires Claude Code or compatible AI coding agent
---


# Israeli Tech Interview Prep

## Legal notice

This skill explains interview practice and summarizes publicly published employment-law rules so a candidate knows what to expect. It is not legal advice, it does not assess your particular case, and it is not a substitute for an employment lawyer (עורך דין דיני עבודה) or for the Equal Employment Opportunities Commission (נציבות שוויון הזדמנויות בעבודה). If you believe you were discriminated against in hiring, take advice on your own facts.

## Instructions

### Step 1: Understand the User's Target

Gather the following details from the user:

1. **Target company** (or company type: startup, enterprise, multinational R&D)
2. **Role** (Backend, Frontend, Fullstack, DevOps, Data, Mobile, QA, Product, etc.)
3. **Seniority level** (Junior, Mid, Senior, Staff, Principal)
4. **Timeline** (when is the interview?)
5. **Current experience** (years, tech stack, notable projects)
6. **Known interview stages** (if the user already has information about the process)

If a specific company is named, consult `references/israeli-tech-companies.md` for company-specific interview details. If the company is not listed, use the closest comparable profile.

### Step 2: Map the Interview Process

Based on the target company and role, outline the typical interview process:

1. **Phone screen / HR call** (20-30 minutes): Motivation, salary expectations, availability. In Israel, this is often very casual and in Hebrew.
2. **Technical phone screen** (45-60 minutes): Usually one coding question via a shared code-pair platform (CoderPad, HackerRank, CodeSignal, or sometimes a plain Google Doc at smaller startups). Medium difficulty.
3. **Home assignment** (common at Israeli startups, less so at multinationals): Typically 4-8 hours of work, due within 3-7 days. Often a small project or system design document.
4. **On-site / virtual day** (3-5 hours): Multiple rounds including coding, system design, and behavioral/cultural fit.
5. **Final round** (Senior+ roles): Architecture discussion, leadership assessment, or meeting with VP/CTO.

Note: Israeli companies tend to have shorter processes than US companies (3-4 stages vs. 5-7). Many skip the home assignment in favor of live coding.

### Step 3: Prepare Coding Questions

Generate practice coding questions tailored to the role and company. For each question, provide:

1. **Problem statement** (clear, concise, with examples)
2. **Hints** (progressive, from subtle to explicit)
3. **Optimal solution** with time and space complexity
4. **Follow-up questions** the interviewer might ask
5. **Common mistakes** to avoid

Use `scripts/interview-question-generator.py` to generate questions:

```bash
python scripts/interview-question-generator.py --company wix --role backend --difficulty medium
python scripts/interview-question-generator.py --role fullstack --difficulty hard --topic "system-design"
```

Focus areas by company type:
- **Startups**: Practical problem-solving, system design at startup scale, trade-off discussions
- **Enterprises**: Algorithm efficiency, large-scale systems, security awareness
- **Multinationals**: LeetCode-style problems (medium-hard), system design at global scale

### Step 4: Practice System Design

For Senior+ roles, prepare system design questions relevant to Israeli tech products:

1. **Understand the product**: Research what the target company builds
2. **Design a simplified version**: Walk through requirements, high-level architecture, data model, API design, and scaling considerations
3. **Israeli scale context**: Israel has approximately 10 million people, but many Israeli companies serve global markets (hundreds of millions of users)

Example system design topics by company:
- **Wix**: Design a website builder component (drag-and-drop editor, template system)
- **Monday.com**: Design a collaborative task management board with real-time updates
- **Check Point**: Design a network security policy engine
- **Mobileye**: Design a real-time object detection pipeline for autonomous vehicles
- **Fiverr**: Design a marketplace matching system for freelancers
- **AppsFlyer**: Design a mobile attribution tracking system handling billions of events

### Step 5: Learn Hebrew Technical Vocabulary

Consult `references/hebrew-tech-vocabulary.md` for Hebrew terms commonly used in Israeli tech interviews. Key areas:

1. **Data structures and algorithms** (Hebrew names for common structures)
2. **Architecture terms** (microservices, load balancing, caching in Hebrew context)
3. **Development methodology** (Agile/Scrum terms as used in Israeli teams)
4. **Slang and informal terms** (Israeli tech culture has unique jargon)

While most technical interviews in Israel are conducted in a mix of Hebrew and English, being comfortable with Hebrew technical terms shows cultural fit and comfort.

### Step 6: Prepare for AI Engineering Questions (2026)

AI engineering questions now reach well beyond ML-specialized teams: backend, frontend, and platform candidates are routinely asked about LLM integration patterns. Treat this as a strong prior rather than a certainty, and confirm with the recruiter what the round actually covers. Prepare for:

1. **LLM integration basics**: How to wrap an LLM call with retries, timeouts, structured output (JSON mode, tool calls), and cost controls. Be able to explain token-based pricing and how to estimate spend.
2. **RAG (Retrieval-Augmented Generation)**: When to use RAG vs. fine-tuning vs. prompt engineering. Components: chunking strategy, embedding model choice, vector store (pgvector, Pinecone, Weaviate, Qdrant), retrieval (top-k, hybrid BM25+vector, reranking), context assembly.
3. **Vector databases**: Tradeoffs between pgvector (Postgres-native, simple), Pinecone (managed, scalable), and self-hosted options. Index types (HNSW vs. IVF) and recall vs. latency tradeoffs.
4. **Prompt engineering basics**: System vs. user messages, few-shot examples, chain-of-thought, structured outputs, why prompt injection matters and how to mitigate it (input sanitization, output guardrails, role separation).
5. **Evaluation**: How to evaluate an LLM feature without ground truth (LLM-as-judge, golden sets, regression tests, A/B testing). Israeli candidates are often asked to design an eval harness for a fictional product feature.
6. **Agents and tool use**: When to use a single LLM call vs. an agent loop, the cost/latency/reliability tradeoffs of multi-step agents, and how to bound cost (max steps, budget caps).
7. **Hebrew-language considerations**: Most general-purpose LLMs are weaker in Hebrew than English. Candidates may be asked how they would build a product that works well in Hebrew (model choice, RTL handling, tokenization quirks, evaluation in Hebrew).

This is now a near-universal expectation at the multinational R&D centers (Google, Microsoft, Meta, Apple, Nvidia's expanded Israel operations after the Run:ai acquisition) and at most growth-stage Israeli startups that have shipped any LLM-powered feature. Do not treat any specific AI startup as a stable target employer without checking its status first: the Israeli AI segment consolidated heavily through 2025-2026 (Nvidia acquired Run:ai and later open-sourced the platform; Tricentis acquired Tabnine in July 2026). Verify a company still exists as an independent employer, on CTech or Geektime, before building a prep plan around it.

### Step 7: Prepare for Cultural Fit / Behavioral Questions

Israeli tech interviews include behavioral components that differ from US-style interviews:

1. **Directness is valued**: Be straightforward about your strengths and weaknesses
2. **Military service questions**: Commonly asked (but not about combat details), especially regarding leadership roles, technical units (8200, Mamram, etc.)
3. **Team dynamics**: Israeli teams tend to be flat, informal, and argumentative (in a constructive way). Show you can handle direct feedback.
4. **Adaptability**: Startups value people who can wear multiple hats
5. **Chutzpah**: Having strong opinions and defending them (respectfully) is seen as a positive

Common behavioral questions in Israeli interviews:
- "Tell me about a time you disagreed with your manager and what happened"
- "Describe a project where requirements changed significantly mid-development"
- "How do you handle a situation where you think the team's approach is wrong?"
- "Tell me about your military/national service" (for Israeli candidates)

**What an employer may not lawfully ask or require.** Section 2 of the Equal Employment Opportunities Law, 1988 (חוק שוויון הזדמנויות בעבודה, התשמ"ח-1988) bars an employer from discriminating between job applicants on grounds of sex, sexual orientation, personal status, fertility treatment, pregnancy, parenthood, age, race, religion, nationality, country of origin, political outlook, place of residence, or reserve (miluim) service, in hiring, terms, promotion, training, or dismissal. Two consequences a candidate should know:

1. **A question whose answer is information on a protected ground is itself evidence.** If a candidate later sues for discriminatory hiring, the fact that such a question was asked shifts the burden of proof to the employer to show it did not discriminate. Kol Zchut gives the worked examples of asking a female candidate whether she plans to become pregnant, and asking an employee up for promotion how many miluim days a year he serves.
2. **Military service cannot be used as a threshold hiring condition where the job does not require it.** In בש"א (ת"א) 3863/09 the Tel Aviv Regional Labour Court held that a service requirement Israel Railways imposed on lookout and patrol roles was not shown to follow from the character of the position; setting a condition that ex-service candidates meet almost automatically raises a concern of prohibited discrimination, because it screens out Arab citizens, Haredim, and olim who did not serve.

The same law bans one specific question outright, under the heading "prohibition on demanding a military profile and its use": an employer may not demand a job applicant's or an employee's military profile (פרופיל צבאי), nor make use of it. The exception to the general rule is section 2(c): it is not discrimination where the requirement genuinely follows from the character or nature of the position, which is how genuine security-clearance roles are handled. So the practical coaching is: expect a conversation about service because it is culturally routine, answer it as experience if you want to, but know that a hard service REQUIREMENT unrelated to the job is legally exposed, and that a demand for your military profile is prohibited outright. Candidates who did not serve should prepare to redirect to equivalent civilian experience rather than apologize for the gap.

### Step 8: Run Mock Interview Sessions

Conduct practice interview sessions with the user:

1. **Timed coding sessions**: Present a problem, give 30-45 minutes to solve it, then review
2. **System design walkthroughs**: Present a prompt, guide through 45-minute design discussion
3. **Behavioral question practice**: Ask questions and provide feedback on responses
4. **Debrief**: After each session, highlight strengths and areas for improvement

## Examples

### Example 1: Preparing for a Wix Senior Frontend Interview

User says: "I have an interview at Wix for a Senior Frontend position next week. What should I expect and how do I prepare?"

Actions:
1. Look up Wix's interview process in `references/israeli-tech-companies.md` (typically: HR screen, take-home assignment, technical interview day with 3-4 rounds)
2. Identify Wix's tech stack focus: React, custom rendering engines, performance optimization
3. Generate practice questions using `scripts/interview-question-generator.py --company wix --role frontend --difficulty medium`
4. Prepare a system design exercise: "Design a drag-and-drop website editor component"
5. Review Hebrew technical vocabulary for frontend terms from `references/hebrew-tech-vocabulary.md`
6. Outline behavioral questions typical at Wix (collaborative culture, handling ambiguity)

Result: A complete prep guide with Wix-specific interview timeline (5 stages over 2-3 weeks), 5 practice coding problems focused on DOM manipulation and React performance, a system design walkthrough for a WYSIWYG editor, a list of 10 behavioral questions with example answers, and a cheat sheet of Hebrew frontend terms.

### Example 2: System Design Practice for a Monday.com Backend Role

User says: "I need to practice system design for a backend interview at Monday.com. Can you run a mock session?"

Actions:
1. Select a relevant system design topic from `references/israeli-tech-companies.md` (Monday.com: real-time collaborative board system)
2. Present the problem: "Design a real-time collaborative task board that supports 10M+ users with live updates"
3. Guide through the session: requirements clarification, high-level design, data modeling, API design, real-time sync strategy (WebSocket vs. SSE), scaling to global users, handling conflicts
4. Provide feedback at each stage
5. Compare to Monday.com's known architecture patterns

Result: A 45-minute mock design session covering real-time collaboration architecture (event sourcing, CRDT for conflict resolution, Redis pub/sub for live updates, PostgreSQL for persistence), with detailed feedback on the user's approach, areas that would impress interviewers, and common pitfalls.

### Example 3: First Job Interview at a Cybersecurity Startup

User says: "I'm a junior developer about to interview at a cybersecurity startup in Tel Aviv. I did my military service in a non-technical unit. How do I prepare?"

Actions:
1. Identify typical interview patterns for cybersecurity startups from `references/israeli-tech-companies.md`
2. Generate junior-level coding practice using `scripts/interview-question-generator.py --role backend --difficulty easy`
3. Prepare for the "military service" conversation: frame non-technical service as building leadership, teamwork, and resilience
4. Cover basic security concepts likely to come up (authentication, encryption basics, common vulnerabilities)
5. Review Hebrew tech vocabulary for basic programming terms from `references/hebrew-tech-vocabulary.md`
6. Prepare behavioral answers showing eagerness to learn and ability to grow quickly

Result: A tailored prep plan including 5 easy-to-medium coding problems with security flavor, a primer on cybersecurity fundamentals (OWASP Top 10, network basics), talking points for discussing non-technical military service positively, and practice behavioral answers emphasizing learning ability and team contribution.

## Bundled Resources

### Scripts
- `scripts/interview-question-generator.py` - Generate practice interview questions by company, role, difficulty, and topic. Run: `python scripts/interview-question-generator.py --help`

### References
- `references/israeli-tech-companies.md` - Interview processes for top 20+ Israeli tech companies including typical rounds, question types, tech stacks, and culture expectations. Consult when preparing for a specific company interview.
- `references/hebrew-tech-vocabulary.md` - Hebrew technical terms commonly used in Israeli tech interviews with English equivalents. Consult when a user wants to prepare for Hebrew-language technical discussions.

## Gotchas

- Israeli tech interviews are typically 3-4 stages, not the 5-7 stage US FAANG process. Agents trained on US interview norms will over-prepare candidates for stages that do not exist at most Israeli companies.
- Military service (especially in tech units like 8200, Mamram, or Unit 81) is commonly discussed in Israeli interviews, but agents should not coach candidates to fabricate or embellish military backgrounds. Interviewers from these units will immediately detect inaccuracies.
- Israeli tech culture values directness ("chutzpah") and constructive disagreement. Agents trained on US behavioral interview norms (STAR method, diplomatic phrasing) may coach candidates to be overly polished, which can come across as inauthentic in Israeli interviews.
- Home assignments are far more common at Israeli startups than at US companies. Agents may skip preparation for take-home projects or underestimate their weight in the evaluation. These assignments often carry more weight than a single coding round.
- Salary negotiation in Israel is done in gross NIS monthly, not annual, and the package around the gross figure is large. Under the mandatory-pension extension order, from January 2017 total pension deposits are 18.5% of the determining salary: 6% from the employee and 12.5% from the employer, made up of 6.5% employer contribution to the tagmulim component plus 6% employer contribution to the severance (pitzuim) component. Quoting the employer side as "6.5%" halves it. Keren Hishtalmut is a further 7.5% employer and 2.5% employee, but note that unlike the pension it is contractual rather than statutory: it is the hi-tech norm and a negotiation point, not an entitlement, and the tax exemption on the employer deposit is capped, so a promise of "7.5% on the full salary" is not automatically worth 7.5% net. Agents using US-style annual salary frameworks will miscalculate the true value.
- Ask which unit a number is quoted in. Israeli recruiters quote either gross salary (ברוטו) or total employer cost (עלות מעסיק), and the second is materially larger because it carries the pension and Keren Hishtalmut deposits, the employer national-insurance share, and accrued leave and havraa. A candidate comparing a "gross" number from one company against an "employer cost" number from another is not comparing offers at all. Make the candidate confirm the unit before reacting to any figure.
- Three offer-stage questions this skill's users routinely miss, all of which change the value of the package and none of which an agent should answer for them: whether the severance arrangement is a full Section 14 arrangement under the Severance Pay Law, under which the employer's monthly deposits stand in place of severance pay and the employer does not top them up for later pay rises. Present this as the genuine trade-off it is rather than as a win: the employee keeps the deposited component on resignation, but on a steeply rising hi-tech salary the deposits can end up worth less than a non-Section-14 calculation would have produced, which track an equity grant is issued under and when its holding period started (Israeli employee equity is normally granted through a trustee arrangement under the Income Tax Ordinance, and the track drives the tax rate), and what the vesting schedule and the post-termination exercise window are. Tell the candidate to get these in writing and to take tax advice on the equity, rather than estimating the numbers yourself.
- Do not quote a salary band from memory, and do not let an agent invent one. The only figure here that is published and datable is the Central Bureau of Statistics average: the average Israeli hi-tech wage was NIS 38,467 gross per month in March 2026, up 4.3% from NIS 36,884 in March 2025. That is a sector-wide average across all roles and seniorities inflated by March bonus payments, NOT a band for any one level, so it is a sanity check and not a target. Build the actual range from a named, dated source the candidate can open: a current salary survey, levels.fyi Israel, or role-specific listings on AllJobs. Multinational R&D centers sit above local medians and add RSU equity; startups offer wider option grants with higher dilution risk, so compare total package rather than base.
- The Israeli tech market has not recovered evenly, and in 2026 it is splitting rather than simply rebounding: large, profitable companies are still cutting software headcount while framing it as an AI restructuring (monday.com cut about 20% of its global workforce in July 2026), and the employer roster itself keeps changing hands (Palo Alto Networks completed its acquisition of CyberArk in February 2026). Candidates may be asked about company financial health, and it is reasonable to ask back about cash position, recent funding round date and size, and headcount trajectory. CTech and Geektime track the Israeli layoff and M&A cycle in near real time.
- Company facts in this skill's reference file go stale faster than anything else in it. Before coaching a candidate on a named employer, confirm the company still exists under that name, is still independent, and still has an Israeli R&D site. Recent examples that would mislead a candidate who trusted an old list: CyberArk is now part of Palo Alto Networks, Outbrain and Teads are now one company that appears publicly under both names, and Snyk is headquartered in Boston rather than Tel Aviv and has run repeated layoff rounds affecting its Israeli development center.
- An agent must not coach a candidate to answer a question that is unlawful to base a hiring decision on as though answering were mandatory. Military service, parenthood, pregnancy plans, age, religion, nationality, and place of residence are protected grounds under section 2 of the Equal Employment Opportunities Law, 1988. The correct coaching is to prepare an answer the candidate is comfortable giving AND to tell them the question is evidence in their favour if the process later goes wrong, not to imply refusal is career suicide.

- Reserve duty (miluim) under the Iron Swords war is a real interview-scheduling factor in 2026. Candidates returning from miluim should expect interviewers to ask "when are you fully available" or "are you still on stand-by". Israeli law protects reservists in employment: an employer may not dismiss a worker because of reserve service, because of a call-up, because of expected service, or because of the length or frequency of that service, and may not dismiss the worker at all during the service. For service exceeding two consecutive days the ban extends 30 days past the end of the service, and dismissal in that window requires approval from the Ministry of Defense employment committee. Startups with tight timelines may still delay a start date around miluim. It is fair game to ask about a company's experience employing miluimnikim and any flexibility on Israeli holidays around the war calendar.
- A candidate who is not an Israeli citizen or permanent resident cannot simply be hired. Employment requires a work permit that the EMPLOYER must obtain and sponsor, and Israeli employers frequently decline to sponsor for junior and mid-level roles because of the cost and the minimum-pay conditions attached to foreign-expert permits. Establish sponsorship at the first HR call, before investing in the process, and route the candidate to the Population and Immigration Authority and to an immigration lawyer for the actual requirements rather than guessing them. Candidates eligible under the Law of Return should be told that making aliyah is a different and often faster route to work authorization than a sponsored permit, and is a question for Nefesh B'Nefesh or the Jewish Agency, not for this skill.
- Many Israeli companies now require AI engineering literacy even for non-ML roles. Treat "have you shipped a feature using an LLM?" as a near-default question in 2026, comparable to "have you used Git?" a decade ago.

## Reference Links

| Source | URL | What to Check |
|--------|-----|---------------|
| Glassdoor | https://www.glassdoor.com | Candidate-reported interview questions and processes for specific Israeli companies (search by company name) |
| levels.fyi Israel | https://www.levels.fyi/?country=105 | Self-reported total compensation by level for Israeli tech roles (base, equity, bonus); useful for multinational R&D centers in particular |
| LinkedIn Jobs Israel | https://www.linkedin.com/jobs/search/?geoId=101620260 | Current Israeli tech job listings, company sizes, employee profiles, and networking targets |
| AllJobs Tech | https://www.alljobs.co.il/hitech/ | Active Israeli tech job listings with role requirements and tech stack details |
| CTech (Calcalist English) | https://www.calcalistech.com/ctechnews | English Israeli tech ecosystem coverage, useful when researching multinational R&D moves |
| Geektime | https://geektime.com | Israeli tech ecosystem coverage, funding rounds, company acquisitions, and layoff reporting (Hebrew and English) |
| TheMarker Tech | https://www.themarker.com/technation | Hebrew-language Israeli tech business coverage, useful for company financial-health context before negotiation |
| Glassdoor Israel salaries | https://www.glassdoor.com/Salaries/israel-software-engineer-salary-SRCH_IL.0,6_IN119_KO7,24.htm | Aggregate base salary data by role for Israeli software engineers |
| Kol Zchut: discriminatory interview questions | https://www.kolzchut.org.il/he/%D7%A9%D7%90%D7%9C%D7%95%D7%AA_%D7%94%D7%A2%D7%A9%D7%95%D7%99%D7%95%D7%AA_%D7%9C%D7%94%D7%A6%D7%91%D7%99%D7%A2_%D7%A2%D7%9C_%D7%A9%D7%99%D7%A7%D7%95%D7%9C%D7%99%D7%9D_%D7%9E%D7%A4%D7%9C%D7%99%D7%9D_%D7%91%D7%A8%D7%90%D7%99%D7%95%D7%9F_%D7%A2%D7%91%D7%95%D7%93%D7%94 | The protected grounds under the Equal Employment Opportunities Law and how a question on one of them shifts the burden of proof |
| Kol Zchut: military service as a hiring condition | https://www.kolzchut.org.il/he/%D7%A9%D7%99%D7%A8%D7%95%D7%AA_%D7%A6%D7%91%D7%90%D7%99_%D7%90%D7%99%D7%A0%D7%95_%D7%99%D7%9B%D7%95%D7%9C_%D7%9C%D7%94%D7%95%D7%95%D7%AA_%D7%AA%D7%A0%D7%90%D7%99_%D7%9E%D7%97%D7%99%D7%99%D7%91_%D7%91%D7%A7%D7%91%D7%9C%D7%94_%D7%9C%D7%A2%D7%91%D7%95%D7%93%D7%94 | Case law on military service as a threshold hiring condition (בש"א 3863/09) |
| CBS average hi-tech wage (via Ynetnews) | https://www.ynetnews.com/business/article/h1wizrkbge | The published sector-wide average hi-tech monthly wage, for sanity-checking any salary figure |

## Troubleshooting

### Error: "The company I'm interviewing at is not in the reference data"

Cause: The reference data covers the most well-known Israeli tech companies, but Israel has thousands of tech companies. Smaller or newer companies may not be listed.

Solution: (1) Identify the company's sector (cybersecurity, adtech, fintech, healthtech, etc.) and size (seed, growth, enterprise). (2) Use the closest comparable company profile from the reference data. (3) Research the company on LinkedIn, Glassdoor Israel, and their careers page to understand their tech stack and culture. (4) Most Israeli tech companies follow a similar 3-4 stage process, so general preparation advice applies broadly.

### Error: "Interview question difficulty does not match my level"

Cause: The question generator uses standardized difficulty levels, but different companies calibrate difficulty differently. What counts as "medium" at Google Israel may be "hard" at a small startup.

Solution: (1) Adjust the difficulty flag in the generator. (2) For FAANG R&D centers, add one difficulty level (if preparing for "medium," practice "hard"). (3) For startups, focus on practical questions rather than algorithmic puzzles. (4) Ask the user what kind of questions they expect based on recruiter feedback, and tailor accordingly.

### Error: "Python script fails to run"

Cause: The `interview-question-generator.py` script requires Python 3.6+ and uses only standard library modules, but the `python` command may not be available or may point to Python 2.

Solution: Use `python3 scripts/interview-question-generator.py --help` instead. On macOS, ensure Python 3 is installed via Homebrew or the official installer. The script has no external dependencies.
