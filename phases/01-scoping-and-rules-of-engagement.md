# Phase 1: Scoping & Rules of Engagement

> **The most important phase. A poorly scoped engagement creates legal liability, wasted effort, and missed critical findings. Never skip or rush this phase.**

---

## 1.1 Pre-Engagement Checklist

Before any testing begins, the following MUST be completed:

- [ ] **Written authorisation obtained** from appropriate authority (CISO, CIO, or Board-level sign-off)
- [ ] **Legal entity confirmation**: Authoriser has legal authority over all in-scope systems
- [ ] **Scope document signed** by client and engagement lead
- [ ] **Rules of Engagement (ROE)** document executed
- [ ] **Emergency contact list** exchanged and tested
- [ ] **NDA/Confidentiality agreement** signed
- [ ] **Insurance verification**: Professional indemnity and cyber liability confirmed
- [ ] **Third-party systems identified**: Any shared hosting, CDN, cloud providers require separate authorisation
- [ ] **Notification to SOC/IT team**: Internal teams aware testing is occurring (avoid false positives causing IR mobilisation)

---

## 1.2 Scope Definition

### In-Scope Targets

Document every in-scope target explicitly:

```
EXAMPLE SCOPE DOCUMENT:

In-Scope:
✅ Primary web application: https://app.example.com (Production)
✅ API endpoints: https://api.example.com/v1/* and /v2/*
✅ Authentication portal: https://login.example.com
✅ Admin panel: https://admin.example.com (with test credentials provided)
✅ Mobile API backend: https://mobile-api.example.com

IP Ranges In-Scope:
✅ 203.0.113.0/24 (web servers)
✅ 198.51.100.10-20 (API servers)

Out-of-Scope (EXPLICIT — do not test):
❌ https://partner.example.com (third-party system)
❌ Production database servers (access test only — no data exfiltration)
❌ AWS Management Console
❌ Any system not listed above
```

### Scope Creep Prevention
- Any new targets identified during testing require written approval before testing
- Document all out-of-scope findings as observations, not test results
- If testing discovers access to out-of-scope systems, STOP and notify client immediately

---

## 1.3 Rules of Engagement (ROE)

### Testing Window
| Parameter | Value |
|-----------|-------|
| Permitted testing hours | [e.g., 18:00–06:00 local time weekdays] |
| Permitted weekends | [Yes/No] |
| Blackout dates | [e.g., payment processing peak dates] |
| Maximum bandwidth consumption | [e.g., No DoS/DDoS testing] |

### Permitted Testing Activities
- [ ] Passive reconnaissance (OSINT, DNS, certificate transparency)
- [ ] Active scanning (port scanning, web crawling)
- [ ] Vulnerability scanning (authenticated and unauthenticated)
- [ ] Manual web application testing (OWASP Top 10)
- [ ] Authenticated testing (with provided credentials)
- [ ] API testing
- [ ] Business logic testing
- [ ] Social engineering (if explicitly authorised)
- [ ] Physical testing (if explicitly authorised)

### Prohibited Activities (Unless Explicitly Authorised)
- ❌ Denial of Service attacks
- ❌ Data exfiltration (demonstrate access path only)
- ❌ Modification or deletion of production data
- ❌ Persistent backdoors / implants
- ❌ Testing of out-of-scope systems
- ❌ Testing from outside agreed IP ranges

---

## 1.4 Emergency Response Protocol

If during testing you discover:
- **Active ongoing breach**: Stop testing immediately. Notify client emergency contact. Document evidence.
- **Critical vulnerability exploited**: Notify within 1 business hour.
- **Accidental data exposure**: Notify immediately. Preserve evidence. Do not copy/retain data.
- **Accidental system disruption**: Notify immediately. Provide full technical detail.

### Emergency Contacts (Fill in)
| Role | Name | Phone | Email |
|------|------|-------|-------|
| Client Primary Contact | | | |
| Client CISO | | | |
| Client IT Manager | | | |
| Engagement Lead (Tester) | | | |
| Engagement Manager | | | |

---

## 1.5 Sector-Specific Scoping Considerations

### 🏦 BFSI / Banking
- **PCI DSS scope**: If testing cardholder data environment, PCI DSS testing requirements apply (QSA may need to be involved)
- **Core banking systems**: Typically out of scope or require special authorisation and change management process
- **SWIFT network**: Usually requires dedicated authorisation; separate from web app scope
- **Production vs. staging**: Strong preference for staging; production requires additional safeguards
- **Time-critical systems**: Wire transfer systems, trading platforms — coordinate blackout windows carefully

### 🛡️ Defence
- **Classified systems**: Government-issued clearance required for testers; separate authorisation chain
- **ITAR restrictions**: Certain testing methodologies may be export-controlled
- **Network segmentation**: Explicitly define which network zones are in scope
- **Reporting classification**: Findings report may require classification markings

### 🏥 Healthcare
- **PHI exposure**: Any testing that could expose patient data requires HIPAA-compliant handling
- **Medical devices**: Usually out of scope unless explicitly authorised by biomedical engineering
- **Availability sensitivity**: Healthcare systems are life-critical — DoS strictly prohibited
- **Test accounts**: Must be synthetic data only; never test with real patient accounts

---

*Phase 1 must be completed and signed before any active testing commences.*
