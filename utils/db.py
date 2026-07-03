# Replace File: utils/db.py

## Objective

Replace the entire file with a production-ready SQLite database module for the AUSTRAC Real Estate Compliance SaaS Platform.

This will become the single database layer used by every module in the application.

## Database

Database filename:

app.db

Automatically create the database and all tables if they do not already exist.

Implement a single initialization function named:

init_db()

which safely creates every table using CREATE TABLE IF NOT EXISTS.

## Tables

### cases

Include fields for:

- id
- property_id
- property_address
- buyer_name
- buyer_type
- seller_name
- purchase_price
- deposit_amount
- cash_payment
- source_of_funds
- source_of_wealth
- overseas_funds
- foreign_buyer
- pep
- sanctions
- trust_purchase
- company_purchase
- crypto_payment
- third_party_payment
- settlement_date
- country
- risk_score
- risk_level
- ai_summary
- status
- assigned_to
- notes
- created_at
- updated_at

### compliance_reports

Include:

- id
- case_id
- report_type
- report_text
- created_by
- created_at

### audit_log

Include:

- id
- username
- action
- details
- created_at

### users

Include:

- id
- username
- password
- full_name
- email
- role
- active
- created_at

## CRUD Functions

Implement reusable functions including:

- connect()
- init_db()

Cases

- add_case()
- get_cases()
- get_case()
- update_case()
- update_case_status()
- delete_case()

Reports

- save_report()
- get_reports()
- get_reports_by_case()

Audit

- log_action()
- get_audit_log()

Users

- create_user()
- authenticate_user()
- get_users()
- update_user()
- delete_user()

## Error Handling

Include:

- input validation
- sqlite exception handling
- logging
- automatic connection closing
- graceful failures

## Performance

Use:

- context managers where appropriate
- parameterized SQL
- reusable helper functions

## Compatibility

Fully compatible with:

- streamlit_app.py
- dashboard.py
- risk_engine.py
- case_management.py
- customer_due_diligence.py
- compliance_report.py
- scenarios.py
- utils/ai.py

## Code Standards

- Production-ready Python
- Fully documented
- Modular
- Clean architecture
- No placeholder code
- No TODO comments
- Commercial SaaS quality

## Deliverable

Return one complete production-ready replacement for utils/db.py.
