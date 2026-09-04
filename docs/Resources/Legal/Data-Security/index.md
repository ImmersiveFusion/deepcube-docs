# Data Security

Immersive Fusion is committed to protecting your data. This document outlines our security practices, certifications, and how we handle your telemetry and account data.

## Security Architecture

### Infrastructure Security

DeepCube is hosted on enterprise-grade cloud infrastructure with:

- **Multi-region capable** - additional regions can be provisioned for redundancy
  or data residency, subject to service availability and capacity
- **Network isolation** using virtual private clouds
- **DDoS protection** at the network edge
- **Web Application Firewall (WAF)** for application-layer protection

### Data Encryption

| Data State | Encryption Method |
|------------|-------------------|
| In transit | TLS 1.2+ (HTTPS) |
| At rest | AES-256 |
| Backups | AES-256 with separate key management |

### Access Controls

- **Role-based access control (RBAC)** for all platform features
- **Multi-factor authentication (MFA)** available for all accounts
- **Single Sign-On (SSO)** integration for Enterprise plans
- **API key management** with scoped permissions

## Data Handling

### Telemetry Data

Your application telemetry (traces, metrics, logs) is:

- **Isolated** - Each customer's data is logically separated
- **Retained** - According to your subscription plan settings
- **Deletable** - You can request data deletion at any time
- **Exportable** - Available for export in standard formats

### Data Residency

DeepCube telemetry is stored and processed in the United States. AI-assisted
features are processed in a separate United States region.

| Region | Status |
|--------|--------|
| United States | Available |
| Other regions | On request, subject to service availability and capacity |

Additional regions can be provisioned where the required services and capacity
are available. [Contact sales](../../../contact.md) to discuss specific
requirements.

### Data Processing

We process telemetry data to:

- Provide visualization and analysis features
- Generate alerts and insights
- Improve service performance
- Support AI-assisted diagnostics (opt-in)

We do **not**:

- Sell your data to third parties
- Use your data for advertising
- Share data between customers

## Compliance

### Security Certifications

Immersive Fusion maintains the following certifications and compliance:

| Standard | Status |
|----------|--------|
| SOC 2 Type II | In progress |
| GDPR | Compliant |
| CCPA | Compliant |

### Audit and Logging

- **Access logs** - All data access is logged
- **Change tracking** - Configuration changes are recorded
- **Retention** - Audit logs retained for 1 year minimum

## Operational Security

### Employee Access

- Background checks for all employees with data access
- Principle of least privilege for system access
- Regular access reviews and revocation
- Security awareness training

### Incident Response

Our incident response process includes:

1. **Detection** - Automated monitoring and alerting
2. **Containment** - Immediate isolation of affected systems
3. **Investigation** - Root cause analysis
4. **Notification** - Customer communication within 72 hours for data breaches
5. **Remediation** - Fix and prevent recurrence

### Vulnerability Management

- Regular security assessments
- Automated vulnerability scanning
- Responsible disclosure program
- Timely patching of dependencies

## Your Responsibilities

As a DeepCube customer, you are responsible for:

- **Account security** - Protecting your login credentials
- **Access management** - Managing user permissions appropriately
- **Data classification** - Not sending prohibited data types
- **Compliance** - Ensuring your use complies with applicable laws

### Data You Should Not Send

Do not instrument your applications to send:

- Payment card numbers (PCI DSS data)
- Social Security numbers
- Healthcare records (PHI/HIPAA data)
- Passwords or authentication tokens
- Other sensitive personal information

Use attribute filtering to remove sensitive data before export.

## Security Resources

### Reporting Security Issues

If you discover a security vulnerability, please report it to:

- **Email:** [security@immersivefusion.com](mailto:security@immersivefusion.com)

We appreciate responsible disclosure and will acknowledge your report within 48 hours.

### Security Documentation

For additional security documentation (SOC 2 reports, security questionnaires), Enterprise customers can contact their account representative.

## Contact

For security-related questions:

- **Security team:** [security@immersivefusion.com](mailto:security@immersivefusion.com)
- **Privacy inquiries:** [privacy@immersivefusion.com](mailto:privacy@immersivefusion.com)
