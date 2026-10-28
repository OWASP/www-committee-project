# OWASP Project Pre-Screening Report: OWASP Threat Dragon
**Application ID:** PPS-110
**Requested Level:** Production (Current: Lab)

### 🚩 Red Flags (Critical)
*   **Activity (Major Release Frequency)**: The project does not meet the requirement of ≥1 major release per year. The last major release (v2.x) was in February 2023. As of May 2026, no new major release has occurred. The project strategy deliberately avoids frequent major releases to prevent breaking changes, which conflicts with the Production maturity requirement.
*   **Contributions (Event Participation)**: There is no evidence of participation in GSoC, OWASP Project Summit, or similar events, which is a mandatory requirement for Production status.

### ⚠️ Non-Critical Concerns
*   **No non-critical concerns identified.** The project adheres well to OWASP Good Practices, including vendor neutrality, multi-leadership, and official communication channels.

### 📋 Requirement Checklist
| Requirement | Status | Evidence/Notes |
| :--- | :--- | :--- |
| **Activity** | ❌ | Fails "1 major release/year" (last major Feb 2023). |
| **Documentation** | ✅ | Comprehensive documentation on website and GitHub. |
| **Support** | ✅ | Active Slack channel (#threat-dragon) and GitHub issues management. |
| **Contributions** | ❌ | PRs managed; however, no proof of GSoC/Summit participation. |
| **Usage** | ✅ | Evidence of significant use: 1.4k+ stars and 370+ forks on GitHub. |
| **Age** | ✅ | Project exists since 2016 (>1 year). |
| **Good Practice** | ✅ | Fully taken into account; vendor neutral with multiple leaders. |
| **OSSF Best Prac** | ✅ | Fulfilled (Passing level badge reached). |

### ⚖️ Verdict & Recommendations
*   **Proposed Verdict**: Conditional / Deny
*   **Reasoning**: Threat Dragon is an exceptionally stable and high-quality project with significant community adoption. However, it currently fails to meet two mandatory criteria for Production status: major release frequency and community event participation.
*   **Recommendations**: 
    *   **GSoC/Summit Participation**: Provide evidence of past participation or plan to participate in the next available GSoC or OWASP Summit cycle.
    *   **Release Strategy Justification**: Seek a waiver for the major release frequency requirement from the Project Committee, citing the project's stability and consistent minor/patch release cycle.

---
*Report generated on 2026-05-28 by Junie (Project Committee Assistant)*
