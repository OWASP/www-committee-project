# Project Promotion Screening

This skill provides instructions and criteria for pre-screening OWASP project promotion applications. It automates the verification of requirements defined in `tab_promotions.md` and `_includes/good_practices.md`.

## Trigger
Use this skill when you are asked to review a project promotion application, provided either as a **PDF file** or a **Jira Service Desk ticket URL** (e.g., `https://owasporg.atlassian.net/servicedesk/customer/portal/4/PPS-###`).

## Workflow

### 1. Information Gathering
*   **For Jira Tickets**: Use browser tools or available Atlassian APIs to scrape the ticket description, comments, and all provided links.
*   **For PDFs**: Extract all text and identify URLs within the document.
*   **Mandatory Link Exploration & Proof Collection**: Visit and analyze the following links to gather evidence/proof for matching:
    *   **Project Website** (`www-project-<name>`): Check for up-to-date roadmap, release info, and OWASP branding.
    *   **GitHub Repository/Organization**: Analyze release history (Activity), Issue/PR management (Support/Contributions), and `CONTRIBUTING.md`.
    *   **OSSF Best Practices Badge**: Verify the current status (registered/passing).
    *   **Slack Channel** (`#project-<name>`): Confirm existence and activity level.
    *   **Social Media accounts**: Check for vendor neutrality and branding.
*   **AI/Boilerplate Scrutiny**: Look for signs of "hallucinated depth" or excessive AI-generated boilerplate:
    - High ratio of verbose documentation/buzzwords to actual functional code.
    - Use of non-standard, complex-sounding security jargon (e.g., "Communication Integrity Layer", "Entropy Phase Analysis").
    - Overly formal or repetitive language common in LLM outputs.
    - Claims of guidance or endorsement from prominent figures that seem exaggerated or unverified.
    - Core logic that is trivial or relies on "Security by Obscurity" despite the sophisticated framing.

### 2. Matching Against Maturity Levels (`tab_promotions.md`)
Evaluate the project against the requirements for the **requested** maturity level.

**Important**: Maturity progression is strictly sequential. A project cannot jump levels (e.g., from Incubator straight to Production). 
*   **Incubator projects** can only apply for **Lab** status.
*   **Lab projects** can apply for **Production** status.

| Requirement | Incubator | Lab | Production |
| :--- | :--- | :--- | :--- |
| **Activity** | - | ≥1 major release | ≥1 major release/year + regular updates |
| **Documentation** | Website with intent/purpose | Instructions for install/usage | Full usage docs + contrib guidelines |
| **Support** | - | Slack/queue exists; GitHub issues handled | Slack/queue managed; issues active |
| **Contributions** | - | Contrib guidelines; PRs handled | Contributor onboarding; GSoC/Summit; PRs managed |
| **Usage** | - | - | Evidence of significant use (stats) |
| **Age** | - | 3-6 months | >1 year |
| **Good Practice**| Known & considered | Mostly taken into account | Fully taken into account |
| **OSSF Best Prac**| - | Registered & self-cert started | Passing level badge fulfilled |

### 3. Checking OWASP Good Practices (`_includes/good_practices.md`)
Check for adherence to the following:
*   **Uniqueness**: Does it have a USP? Is it redundant with existing projects?
*   **Vendor Neutrality**: 
    *   No paywalls for features.
    *   Neutral naming (not commercial services).
    *   Multiple Project Leaders from different companies (Red Flag if all same).
    *   Social media not tied to commercial accounts.
*   **GitHub**: 
    *   Under `github.com/OWASP` (or dedicated org).
    *   Leaders have Admin access.
    *   Responsive to community (Issues/PRs).
*   **Website**:
    *   `www-project-<name>` site exists and is up-to-date.
    *   Clear OWASP branding and link to official project page.
*   **Community**: Official Slack channel exists.

### 4. Output Generation
Generate a comprehensive pre-screening report using the following Markdown template. This ensures consistency and makes it easier for the project committee to review. 

**Storage**: Save the generated report in `.ai/promotion-screening/reports/[PPS-###]-[Project-Name].md`.

---

## OWASP Project Pre-Screening Report: [Project Name]
**Application ID:** [PPS-### or Link]
**Requested Level:** [Lab / Production]

### 🚩 Red Flags (Critical)
*   *List mandatory requirements from `tab_promotions.md` that are not met (Activity, Documentation, Support, Contributions, Usage, Age, OSSF Best Practices).*
*   *If none, state: "No red flags identified."*

### ⚠️ Non-Critical Concerns
*   *List any violations of OWASP Good Practices (`_includes/good_practices.md`).*
*   *List minor issues, missing documentation, or suggestions for improvement.*
*   *If none, state: "No non-critical concerns identified."*

### 📋 Requirement Checklist
| Requirement | Status | Evidence/Notes |
| :--- | :--- | :--- |
| **Activity** | [✅/❌] | [Brief note] |
| **Documentation** | [✅/❌] | [Brief note] |
| **Support** | [✅/❌] | [Brief note] |
| **Contributions** | [✅/❌] | [Brief note] |
| **Usage** | [✅/❌] | [Brief note] |
| **Age** | [✅/❌] | [Brief note] |
| **Good Practice** | [✅/❌] | [Brief note] |
| **OSSF Best Prac** | [✅/❌] | [Brief note] |

### ⚖️ Verdict & Recommendations
*   **Proposed Verdict**: [Approve / Conditional / Deny]
*   **Reasoning**: [Brief summary of findings]
*   **Recommendations**: 
    *   *Actionable step 1*
    *   *Actionable step 2*

---

## Resource Paths
*   Promotion Rules: `tab_promotions.md`
*   Good Practices: `_includes/good_practices.md`
