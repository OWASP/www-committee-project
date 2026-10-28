# OWASP Project Pre-Screening Report: OWASP PTK
**Application ID:** PPS-85
**Requested Level:** Production (Current: Lab)

### 🚩 Red Flags (Critical)
*   **Good Practice (Leadership)**: The project lists only one leader (Denis Podgurskii). Production status requires multiple project leaders, ideally from different organizations, to ensure project sustainability and vendor neutrality.
*   **Good Practice (GitHub Location)**: The primary repository is located in a personal account (`DenisPodgurskii/pentestkit`) rather than under the official `OWASP` GitHub organization.
*   **Contributions (Event Participation)**: No evidence was found of the project's participation in GSoC, OWASP Project Summit, or similar community events, which is a mandatory requirement for Production level.
*   **OSSF Best Practices**: There is no evidence that the project has fulfilled the criteria for the OSSF Best Practices *passing* level badge.

### ⚠️ Non-Critical Concerns
*   **No non-critical concerns identified.** The project demonstrates exceptional usage statistics and active maintenance.

### 📋 Requirement Checklist
| Requirement | Status | Evidence/Notes |
| :--- | :--- | :--- |
| **Activity** | ✅ | Very active with recent releases (v9.8.x) in March/April 2026. |
| **Documentation** | ✅ | Usage documentation and contribution guidelines are available on GitHub and the project website. |
| **Support** | ✅ | Active issue management on GitHub; Slack channel mentioned in application. |
| **Contributions** | ❌ | Fails mandatory requirement for participation in GSoC, OWASP Summit, or similar events. |
| **Usage** | ✅ | Significant evidence of use: >20,000 Chrome users and 800+ Firefox users. |
| **Age** | ✅ | Project has existed for >8 years. |
| **Good Practice** | ❌ | Only one leader; repository not in OWASP GitHub organization. |
| **OSSF Best Prac** | ❌ | No "passing" level badge verified. |

### ⚖️ Verdict & Recommendations
*   **Proposed Verdict**: Deny
*   **Reasoning**: OWASP PTK is a highly successful and widely used project with an impressive track record. However, it currently does not meet several formal requirements for Production maturity, specifically regarding leadership diversity, repository hosting, community engagement through events, and OSSF certification.
*   **Recommendations**: 
    *   **Onboard Additional Leaders**: Recruit at least one more project leader, preferably from a different organization, to meet the multi-leadership requirement.
    *   **Migrate to OWASP GitHub Org**: Transfer the repository to the `OWASP` organization (or create a dedicated org as per OWASP guidelines).
    *   **OSSF Certification**: Complete the OSSF Best Practices self-certification to reach the *passing* level badge.
    *   **Community Participation**: Apply for participation in a future GSoC cycle or OWASP Summit to fulfill the community engagement requirement for Production status.

---
*Report generated on 2026-06-03 by Junie (Project Committee Assistant)*
