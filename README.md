# 🔓 VAPT Methodology for Web Applications

> **Professional web application penetration testing methodology — built from real-world red team and VAPT engagements. Covers scoping through reporting for BFSI, Defence, Energy, and Technology sectors.**

[![OWASP](https://img.shields.io/badge/OWASP-Top_10_2021-red?style=flat-square)](https://owasp.org/Top10/)
[![PTES](https://img.shields.io/badge/PTES-Methodology-orange?style=flat-square)](http://www.pentest-standard.org/)
[![MITRE ATT&CK](https://img.shields.io/badge/MITRE_ATT%26CK-Mapped-blue?style=flat-square)](https://attack.mitre.org/)
[![CVSS](https://img.shields.io/badge/CVSS-v3.1_Scoring-green?style=flat-square)](https://www.first.org/cvss/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)

> ⚠️ **Ethical Use Only.** This methodology is for authorised security testing only. Unauthorised testing is illegal. Always obtain written authorisation before any testing activity.

---

## 🎯 About

This repository documents a **battle-tested web application VAPT methodology** developed from real engagement experience. It bridges technical depth with GRC governance — rare in the market.

**What makes this different:**
- Written by a GRC practitioner with hands-on offensive security experience (red team, malware analysis, VAPT)
- Every phase includes **sector-specific considerations** — BFSI testing is different from healthcare or OT
- **Evidence and documentation templates** included — reporting is 50% of a VAPT engagement
- MITRE ATT&CK TTP mapping throughout

---

## 📁 Structure

```
vapt-methodology-webapp/
├── phases/
│   ├── 01-scoping-and-rules-of-engagement.md   ← Legal foundation
│   ├── 02-reconnaissance-and-osint.md           ← Passive + active recon
│   ├── 03-vulnerability-scanning.md             ← Tool-based discovery
│   ├── 04-manual-exploitation.md                ← OWASP Top 10 testing
│   ├── 05-post-exploitation.md                  ← Pivoting, persistence, cleanup
│   └── 06-reporting-and-remediation.md          ← Professional report writing
├── tools-reference/
│   ├── kali-tools-quick-reference.md            ← Essential Kali tools cheatsheet
│   └── owasp-top-10-test-guide.md               ← Per-vulnerability test procedures
├── scripts/
│   ├── port_scanner.py                          ← Python port scanner demo
│   └── web_recon.py                             ← Web reconnaissance helper
└── sector-guides/
    ├── bfsi-banking-vapt-notes.md               ← PCI DSS scoped testing
    ├── defence-vapt-notes.md                    ← CMMC, classified env considerations
    └── healthcare-vapt-notes.md                 ← HIPAA compliance testing
```

---

## 🔬 Engagement Lifecycle

```
Phase 1: SCOPING (Days 1–2)
  ├── Rules of Engagement (ROE) document
  ├── Scope confirmation (in-scope / out-of-scope URLs, IPs)
  ├── Testing window agreement
  └── Emergency contacts defined

Phase 2: RECONNAISSANCE (Days 2–3)
  ├── Passive: OSINT, WHOIS, DNS, Certificate Transparency
  ├── Active: Port scan, service enumeration, web crawl
  └── Threat modelling based on findings

Phase 3: VULNERABILITY SCANNING (Day 3–4)
  ├── Automated scanning: Burp Suite Pro, OWASP ZAP, Nikto
  ├── CMS-specific scanners (WPScan, Droopescan)
  └── CVE database cross-reference

Phase 4: MANUAL EXPLOITATION (Days 4–7)
  ├── OWASP Top 10 manual testing
  ├── Business logic testing
  ├── Authentication and session management
  └── API security testing (OWASP API Top 10)

Phase 5: POST-EXPLOITATION (Days 7–8, if authorised)
  ├── Privilege escalation attempts
  ├── Lateral movement assessment
  └── Data exfiltration path mapping

Phase 6: REPORTING (Days 8–10)
  ├── Technical findings report
  ├── Executive summary
  └── Remediation roadmap
```

---

## 🏆 Deliverables Produced

| Deliverable | Audience | Format |
|-------------|----------|--------|
| Executive Summary | C-suite, Board | 2–3 page brief |
| Technical Findings Report | CISO, Dev Team | Full detail with PoC |
| Vulnerability Register | Security team | Spreadsheet / GRC tool |
| Remediation Roadmap | Dev/IT Manager | Prioritised action list |
| Re-test Report | CISO | Pass/fail on remediated findings |

---

## ✍️ Author

**Akshaya** | CIAP (DRDO/MoD) | ISO 27001 LA | Manager, Risk & Compliance

*Technical roots: Red team operations, VAPT, malware analysis, reverse engineering, adversary simulation, dark web monitoring. GRC built on top of genuine offensive security knowledge — which is why the controls I design actually work.*

📧 akshayshrm39@gmail.com
