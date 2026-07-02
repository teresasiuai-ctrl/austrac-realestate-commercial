## Objective
Create a production-ready AI module for the AUSTRAC Real Estate Compliance SaaS Platform using the Google Gemini API. This module will centralize all AI functionality and be used by the Risk Engine, Customer Due Diligence, Case Management, and Compliance Report Generator.

## Requirements

- Use Google Gemini API.
- Read the API key from Streamlit Secrets first, then fall back to an environment variable.
- Automatically fall back to a built-in rule-based engine if:
  - no API key exists,
  - Gemini is unavailable,
  - quota is exceeded,
  - network errors occur.
- Never crash the application if AI is unavailable.

## Functions

Implement reusable functions including:

- assess_risk()
- explain_risk()
- customer_due_diligence()
- generate_smr_report()
- generate_case_summary()
- generate_compliance_recommendations()
- summarise_transaction()

## Output

Each function should return structured Python dictionaries using consistent keys so they can be displayed directly in Streamlit.

## Error Handling

Include:

- exception handling
- logging
- timeout handling
- validation of missing inputs
- graceful fallback responses

## Compatibility

The module must work with:

- Streamlit
- SQLite
- Existing project structure
- Desktop and mobile versions

## Coding Standards

- Clean, modular Python
- Well-documented functions
- Type hints where appropriate
- Production-ready code
- No placeholder functions
- No TODO comments
- Ready for commercial deployment
