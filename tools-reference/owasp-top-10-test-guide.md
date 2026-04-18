# OWASP Top 10:2021 — Quick Test Guide

> Concise reference for testing each OWASP Top 10 vulnerability. Use during Phase 4 fieldwork.

---

| # | Vulnerability | Quick Test | Common Tools | CVSS Range |
|---|--------------|-----------|-------------|-----------|
| A01 | Broken Access Control | IDOR via ID manipulation; force-browse admin paths; test role escalation | Burp + Autorize extension | 6.5–9.8 |
| A02 | Cryptographic Failures | Check HTTPS enforcement; cookie flags; sensitive data in responses | Burp, SSLyze, testssl.sh | 5.0–9.1 |
| A03 | Injection (SQL/CMD/LDAP) | Fuzz all inputs with `'`, `"`, `;--`, SLEEP() payloads | SQLmap, Burp intruder, manual | 7.5–10.0 |
| A04 | Insecure Design | Business logic flaws; race conditions; missing workflow validation | Manual, Burp Repeater | 4.0–9.0 |
| A05 | Security Misconfiguration | Default credentials; unnecessary features enabled; stack traces | Nikto, manual, Google dorks | 5.0–9.8 |
| A06 | Vulnerable Components | Check `package.json`, `pom.xml`, `requirements.txt` for CVEs | Retire.js, OWASP Dependency-Check | 5.0–10.0 |
| A07 | Auth Failures | Brute force; session fixation; MFA bypass; weak password policy | Burp intruder, Hydra, manual | 5.0–9.8 |
| A08 | Software & Data Integrity | Check CI/CD pipeline security; unsigned updates; deserialization | Manual, ysoserial | 7.0–10.0 |
| A09 | Security Logging Failures | Verify audit trails exist; test if attacks are logged | Manual, check SIEM/logs | N/A (detection gap) |
| A10 | SSRF | Inject URLs in webhook/preview fields; test for cloud metadata access | Burp Collaborator, manual | 7.5–10.0 |

---

## Quick Win Checks (High Value, Low Effort)

```bash
# 1. Check for default credentials
admin:admin, admin:password, root:root

# 2. Check robots.txt and sitemap.xml for sensitive paths
curl https://target.com/robots.txt
curl https://target.com/sitemap.xml

# 3. Check for exposed .git directory
curl https://target.com/.git/config

# 4. Check security headers
curl -I https://target.com | grep -i "x-frame-options\|content-security-policy\|strict-transport"

# 5. Check for server version disclosure
curl -I https://target.com | grep -i "server\|x-powered-by"

# 6. Test for HTTP methods
curl -X OPTIONS https://target.com -v

# 7. API documentation exposure
curl https://target.com/api/swagger.json
curl https://target.com/api/docs
curl https://target.com/openapi.json
```

---
*Reference: OWASP Testing Guide v4.2 | https://owasp.org/www-project-web-security-testing-guide/*
