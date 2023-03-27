---

layout: col-document
title: Lifecycle
document: Project Handbook
tags: Project Handbook
order: 3

---

{% include draft.md %}
  
### Project Levels

Projects are divided into 3 levels representing maturity of the project. The levels from lowest maturity to the highest level of maturity are:

<span class="fa-stack fa-2x">
    <i class="fas fa-circle fa-stack-2x" style="color:#53AAE5"></i>
    <i class="fas fa-egg fa-stack-1x fa-inverse"></i>
</span> **Incubator**

Projects that represent the experimental playground where projects are still being designed, ideas are still being proven, and development is still underway. The label gives Project Leaders the opportunity to leverage the OWASP brand name and resources while their project is still maturing. 

---

<span class="fa-stack fa-2x">
    <i class="fas fa-circle fa-stack-2x" style="color:#FFA500"></i>
    <i class="fas fa-flask fa-stack-1x fa-inverse"></i>
</span>
**Lab**

Projects that are much farther along and just lack a bit of polish to get them production-ready. There may be errors or some minor instability but they tend to be reliable for most uses and have produced a deliverable of significant value.

---

<span class="fa-stack fa-2x">
    <i class="fas fa-circle fa-stack-2x" style="color:#800080"></i>
    <i class="fas fa-city fa-stack-1x fa-inverse"></i>
</span>
**Production**
    
Projects that can be considered production-ready with high reliability. Furthermore, these projects provide a polished user experience, good documentation, and, preferably, some amount of internationalization.

---

<span class="fa-stack fa-2x">
    <i class="fas fa-circle fa-stack-2x" style="color:#38a047"></i>
    <i class="fas fa-flag fa-stack-1x fa-inverse"></i>
</span>
**Flagship** 

Flagship is **NOT a maturity level** but is, rather, an indication of the project's strategic important to the OWASP mission. Flagship projects are recommended for such by the Project Committee to the OWASP Board of Directors. 

### Setting up the Initial Repository
Once a new project has been accepted, a repository will be created for the project. This repository is the **webpage** repository and will be the initial page visitors will see when browsing the project. The initial repository will provide a set of files that need to be updated with the relevant project information. These files include:
- index.md 
- info.md
- leaders.md
- tab_example.md

The contents of these files and explanations to what they affect as well as information on local editing of these files can be found at [Website Migration Information and Tutoral](https://owasp.org/migration/)

In addition to these files, projects should also include:
- LICENSE.md : indicating the license under which the project operates
- CONTRIBUTING.md : helpful file indicating to users how to contribute to the project
- README.md : a quick description that somewhat perusing the github repository (instead of the webpage) would see

### Applying for Promotion
When a project wishes to be promoted from one level to the next, the project leaders should review the information from the Project Committee on [Promotions](https://owasp.org/www-committee-project/#div-promotions). Be sure to consider all aspects related to the level **the project wishes to acquire**. When ready for promotion, use the form or method indicated on the Project Committee [Promotions](https://owasp.org/www-committee-project/#div-promotions) page.

### Retiring the Project
Projects at OWASP might be retired for several reasons. Among the reasons include abandonment of the project by the project leaders, a lack of interest in the topic, and a natural progression of the project where the topic has been overcome by time or events. Projects that have not had any activity after a number of years may be archived and removed from the OWASP Project Inventory. 

### Leaving OWASP
Projects that join the OWASP organization are considered material assets of the organization. A project whose leaders choose to leave the organization are expected to leave the project with the organization but may fork the source and continue working on the forked source outside the organization provided that the project leaders remove any references to being an OWASP project. Further, the name associated with the OWASP project remains with the OWASP organization; the forked project should be renamed.
