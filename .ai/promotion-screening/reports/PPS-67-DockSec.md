# OWASP Project Pre-Screening Report: DockSec
**Application ID:** PPS-67
**Requested Level:** Lab (Current: Incubator)

### 🚩 Red Flags (Critical)
*   **OSSF Best Practices Registration**: There is no evidence that the project has registered for the OSSF Best Practices badge. Registration and starting the self-certification process is a mandatory requirement for Lab status.

### ⚠️ Non-Critical Concerns
*   **GitHub Organization**: The primary repository is hosted under a personal account (`https://github.com/advaitpatel/DockSec`) rather than the official `OWASP` organization. OWASP projects are required to live under the OWASP organization or a dedicated project organization.
*   **Leadership**: The project currently has only one listed leader (`Advait Patel`). OWASP Good Practices require multiple leaders (ideally from different employers) to ensure project continuity and vendor neutrality.
*   **Official Slack Channel**: No official OWASP Slack channel (e.g., `#project-docksec`) was identified. This is a recommendation for Lab status as per OWASP Good Practices.
*   **Vendor Neutrality (Social Media)**: Ensure any social media presence is independent of commercial accounts, although none were explicitly flagged in the application.

### 📋 Requirement Checklist (Lab Level)
| Requirement | Status | Evidence/Notes |
| :--- | :--- | :--- |
| **Activity** | ✅ | Very active development; recent release v2026.2.23. |
| **Documentation** | ✅ | Reasonable instructions for installation and usage exist in README. |
| **Support** | ✅ | GitHub issues are managed; however, missing an official OWASP Slack channel (see Good Practices). |
| **Contributions** | ✅ | `CONTRIBUTING.md` exists and PRs are being handled. |
| **Usage** | ✅ | (Not a requirement for Lab level). |
| **Age** | ✅ | Active since 2025 (>6 months). |
| **Good Practice** | ❌ | Fails on repo location and multi-leader requirements. |
| **OSSF Best Prac** | ❌ | Project not registered/self-certification not started. |

### ⚖️ Verdict & Recommendations
*   **Proposed Verdict**: Conditional / Deny
*   **Reasoning**: The project is technically strong and active, but fails the mandatory OSSF Best Practices registration for Lab status. Additionally, it does not yet adhere to several key OWASP Good Practices regarding repository location, leadership diversity, and official communication channels.
*   **Recommendations**: 
    *   **Repository Migration**: Move the `DockSec` repository to the official `OWASP` GitHub organization.
    *   **Expand Leadership**: Recruit at least one additional co-leader, preferably from a different organization, to meet the multi-leader requirement.
    *   **Establish Slack Channel**: Create and monitor an official `#project-docksec` channel on the OWASP Slack.
    *   **OSSF Registration**: Register the project on the OSSF Best Practices site and begin the self-certification process.

---
*Report generated on 2026-05-28 by Junie (Project Committee Assistant)*
