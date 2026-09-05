## General Strategy: "Write as You Go"

- Continuous Documentation: Reporting must begin at the onset of the assessment, not at the end. Use downtime during long discovery scans to complete static template sections (e.g., contact info, client name, scope).
    
- Real-time Evidence Capture: Write up the attack chain and individual findings with all required evidence during active testing to prevent scrambling for data after the testing window closes.
    
- Template Hygiene: Always start from a blank report template tailored to the specific assessment type. Never modify a previous client’s report, as this introduces severe risks of leaving legacy client data or names in the new deliverable.
    

## Microsoft Word Operational Standards

### Basic Core Features

- Platform Restriction: Use Word for Windows exclusively. Word for Mac lacks the VB Editor for macros, lacks vital features, trims document margins natively, and breaks hyperlinks when exporting to PDF.
    
- Font and Table Styles: Avoid all direct formatting (manually clicking bold, underline, colors, etc.). Utilize global Document Styles for text and tables so cosmetic or structural changes can be updated globally across the entire document instantly.
    
- Captions: Apply the native "Insert Caption" feature to all images and tables. This ensures numbers automatically update if figures are inserted or deleted later.
    
- Navigation Elements:
    
    - Include Page Numbers to allow precise cross-referencing during client reviews.
        
    - Implement an automated Table of Contents (ToC) and optional List of Figures/Tables tied directly to document styles and captions.
        
- Customization Settings:
    
    - Bookmarks: Use to create internal document hyperlinks or to mark sections for automated deletion via macros.
        
    - Custom Dictionary: Use to extend AutoCorrect and prevent professional typos (e.g., automatically replacing "pubic" with "public"). Note that this configuration does not travel with the template and must be set up per user profile.
        
    - Language Settings: Apply custom language properties to code blocks and terminal evidence text styles, explicitly selecting the option to ignore spelling and grammar checking to avoid cluttering the spellchecker.
        
    - Custom Numbering: Set up custom numbering fields to automatically order findings and appendices.
        

### Quick Access Toolbar Configuration

Configure the Quick Access Toolbar via File > Options > Quick Access Toolbar and pull useful commands from the "Commands Not in the Ribbon" dropdown:

- Back: Instantly jumps the cursor back to the original text location after clicking an internal hyperlink to verify its destination.
    
- Undo/Redo & Save: Keeps basic controls easily accessible if keyboard shortcuts are not used.
    

### Essential Hotkeys

- `F4`: Repeats the last action taken (e.g., applying a specific font style to newly highlighted text).
    
- `Ctrl + A` then `F9`: Selects the entire document and forces a global update of all fields, including the ToC, List of Figures, and List of Tables (Use at own risk as it updates all document fields).
    
- `Ctrl + S`: Saves the document frequently to mitigate data loss from software crashes.
    
- `Ctrl + Alt + S`: Splits the active window into two separate, independently scrollable panes to view different sections of the report simultaneously.
    
- `Shift + F5`: Immediately jumps the cursor back to the location where the last revision was made.
    

## Macro Automation

- Format Requirement: Templates must be developed and saved using the macro-enabled `.dotm` file format within a Windows environment.
    
- Automated Prompts: Program macros to launch pop-up prompt windows upon initialization to collect key details (Client Name, Dates, Scope Details, Testing Type, Environment/App Names) and auto-populate designated template placeholder variables.
    
- Template Consolidation: Combine multiple assessment variations into a single master template, using a macro to automatically strip away entire sections marked by bookmarks if they do not apply to the specific assessment type.
    

## Findings Databases & Platforms

- The Problem: Manually rewriting identical findings across multiple assessments wastes time, introduces variance in technical descriptions, and causes inconsistent reporting quality across a team.
    
- Baseline Management: Maintain a dedicated, offline master document containing sanitized versions of common vulnerabilities ready for copy-paste deployment, which must still be customized to the target environment where applicable.
    
- Centralized Reporting Tooling: Deploy dedicated reporting platforms to automate assembly, standardizing outputs across consultants.
    

|**Free Platforms**|**Paid Platforms**|
|---|---|
|Ghostwriter|AttackForge|
|Dradis|PlexTrac|
|VECTR (Security Risk Advisors)|Rootshell Prism|
|WriteHat||

## Screenshot & Evidence Sanitization Rules

- Narrative Continuity: Aim to tell a cohesive story. Explicitly explain the impact of the flaws (e.g., why a Kerberoasting attack or default credentials on an application matter in context).
    
- Evidence Balance: Provide enough command output and screenshots to clearly demonstrate reproducibility without adding verbose, unnecessary clutter.
    
- Annotation: Use screenshot tools (like Greenshot) to overlay explicit arrows or colored boxes highlighting the exact area of interest, adding textual explanations directly below the image.
    
- Data Redaction:
    
    - Completely mask all sensitive data—including cleartext passwords, hashes, secrets, and client-sensitive information—using solid colored shapes. Never use blurring utilities, as they can sometimes be reversed.
        
    - Sanitize raw tool outputs to remove informal default text that could appear unprofessional to non-hackers (e.g., removing or changing the default `(Pwn3d!)` text string in the CrackMapExec configuration file).
        
    - Inspect password cracking outputs (e.g., Hashcat logs) to ensure no crude, offensive, or unprofessional candidate passwords from public wordlists remain in the report text; swap them out for safe, innocuous placeholders.
        
- Console Aesthetics: Terminal screenshots must be solid black (no transparency showing background wallpapers/tools) with a clean theme (black background with white or green text). Alternatively, use light backgrounds with dark text to avoid exhausting client printer ink cartridges.
    
- Professional Hostnames: Keep all testing infrastructure hostnames and prompts strictly formal; never include prompts like `azzkicker@clientsmasher`.
    

## Quality Assurance (QA) & Versioning

### Review Framework

- Review Quota: Reports must undergo at least one, and ideally two, rounds of peer review by individuals other than the author.
    
- Solo Operator Protocol: If working independently without peer resources, sleep on the draft and perform the review the following morning with fresh eyes.
    
- Checklist Enforcement: Insert a temporary QA checklist directly into the report template detailing formatting, style guide rules, grammar, and structural checks, removing it only when the final draft is signed off.
    
- Data Privacy: Exercise caution with cloud-based grammar tools (e.g., Grammarly, LanguageTool); ensure corporate approval is obtained and data-sharing features used to "learn" are disabled to avoid uploading confidential client vulnerabilities to third-party clouds.
    
- Scalability Tracking: Use structured tracking tools (like Google Sheets for small teams or Jira tickets for larger organizations with Project Managers) along with a centralized document repository to track reports through the pipeline.
    

### Responsibility Boundaries & Changes

- Author Accountable: The QA reviewer should only patch minor typos or phrasing adjustments directly to expedite the process. If evidence is missing, findings are poorly illustrated, or the Executive Summary is weak, the report must be returned to the author to fix.
    
- Continuous Improvement: Always review QA modifications with Track Changes enabled to actively learn and prevent repeating the same errors in future engagements.
    

### Document Lifecycle

1. Draft Release: Complete the QA pipeline internally and issue the report to the client explicitly marked as a Draft version.
    
2. Report Review Meeting: Allow the client approximately one week to ingest the findings internally. Conduct a formal review meeting to step through technical findings one by one, address questions, and gather feedback.
    
3. Final Release: Apply any necessary, mutually agreed-upon updates, remove the "Draft" status, change the designation to Final, and deliver the final artifact.
    
4. Archival: Cleanly archive all testing data securely in accordance with company data retention policies.
    

## Client Communications Protocols

### Formal Engagement Notifications

Maintain constant contact throughout the testing lifecycle to reinforce your position as a trusted advisor.

- Start Notification Email: Transmit formally prior to execution, containing:
    
    - Assigned tester name(s).
        
    - Clear description of engagement scope and type.
        
    - Origin testing IP addresses (public external source IPs or internal static IPs).
        
    - Anticipated testing window dates.
        
    - Primary and secondary emergency contact details (phone and email).
        
- Daily Stop Notification Email: Transmit at the conclusion of each day's testing window to signal a pause in activity. This email should outline a high-level summary of findings to prevent the client from being blindsided by the final report, while setting clear expectations for report delivery dates. These notifications also provide the client's defensive teams with precise timestamps to cross-reference security alerts.
    

### Out-of-Band Critical Escalations

Do not wait for formal report timelines to communicate high-impact events:

- Scope Modifications: If additional subnets or subdomains are discovered, consult the client to check if they want to adjust the scope, provided it fits the allotted testing time.
    
- Critical Vulnerabilities: If high-risk vulnerabilities like Remote Code Execution (RCE) or SQL Injection are discovered on external assets, stop testing immediately and formally notify the client to establish a path forward.
    
- Host Status Issues: If a core target system appears down during scanning, notify the client immediately and transparently.
    
- Critical Compromise (Domain/Enterprise Admin): Inform the client immediately upon gaining Domain Admin privileges so they are aware in the event internal alerting triggers, and to allow them to prepare executive management for the report findings. Ask if they require specific focus shifted onto high-value target assets, or if certain sensitive servers should remain out-of-bounds despite holding administrative privileges.
    

### Defensive Deflection & Logging

- Activity Logging: Maintain complete, timestamped tool logs and raw scanner outputs. If a client experiences a production outage during the window, you must be able to definitively present logged evidence showing your exact activities to prove whether your tools caused the disruption.
