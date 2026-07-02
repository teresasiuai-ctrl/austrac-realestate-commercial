## Objective
Develop a production-ready AI engine for the AUSTRAC Real Estate Compliance SaaS Platform. This module will centralize all AI functionality and integrate with the Risk Engine, Customer Due Diligence, Case Management, Dashboard, and AUSTRAC Report Generator.

## AI Provider
- Google Gemini API
- Read API key from Streamlit Secrets.
- If not found, read from environment variable.
- Support future model upgrades without changing the rest of the application.

## Fail-Safe Mode
The application must never crash.

Automatically switch to a built-in rule-based engine when:
- API key is missing
- Gemini service is unavailable
- Rate limit or quota exceeded
- Network timeout
- Invalid response
- Any unexpected exception

The user should continue using the application normally.

## Core Functions

Implement production-ready functions including:

- assess_risk()
- explain_risk()
- customer_due_diligence()
- generate_smr_report()
- generate_case_summary()
- generate_compliance_recommendations()
- summarise_transaction()
- generate_dashboard_summary()

## AI Capabilities

Generate:

- Risk assessment
- Risk explanations
- AML/CTF recommendations
- Customer Due Diligence guidance
- Enhanced Due Diligence recommendations
- Suspicious Matter Report draft
- Compliance summaries
- Executive summaries
- Case notes
- Officer recommendations

## Output Format

Return structured Python dictionaries with consistent keys.

Example sections:

- risk_score
- risk_level
- reasons
- recommendations
- narrative
- summary
- warnings
- confidence

## Error Handling

Include:

- input validation
- logging
- retries
- timeout handling
- graceful degradation
- meaningful error messages

Never expose API errors directly to the user.

## Security

- Never hardcode API keys.
- Never log secrets.
- Validate all inputs.
- Sanitize AI prompts before sending.
- Prevent prompt injection where practical.

## Performance

- Modular functions
- Efficient API usage
- Reusable prompt templates
- Minimal duplicate code
- Optimized for Streamlit

## Compatibility

Fully compatible with:

- Streamlit
- SQLite
- Existing project structure
- Desktop
- Tablet
- Mobile

## Code Standards

- Production-ready Python
- Well documented
- Type hints where appropriate
- Clean architecture
- Reusable functions
- No placeholder code
- No TODO comments
- Commercial SaaS quality

## Deliverable

Return one complete, production-ready `utils/ai.py` file ready for copy-and-paste into the repository.
