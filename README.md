# AUSTRAC Real Estate Compliance SaaS Platform

## Overview

This is a production-ready compliance system for Australian real estate AML/CTF monitoring, risk assessment, and AUSTRAC reporting.

It provides:

- AI-powered risk scoring (Google Gemini)
- Customer Due Diligence (CDD / EDD)
- Case Management system
- AUSTRAC Suspicious Matter Report (SMR) generator
- Compliance dashboard
- Audit logging
- Scenario-based risk simulation
- Voice input and text-to-speech support

## Features

### Risk Engine
- Real-time AML/CTF risk scoring
- AI + rule-based hybrid analysis
- Risk explanations and recommendations

### Case Management
- Track compliance cases
- Update status and notes
- Assign officers
- Export case summaries

### AI Compliance Assistant
- Powered by Google Gemini API
- Generates:
  - Risk explanations
  - Compliance recommendations
  - SMR draft reports
  - Case summaries

### Customer Due Diligence
- PEP detection
- Sanctions screening logic
- Source of funds analysis
- Enhanced Due Diligence recommendations

### Dashboard
- KPI overview
- Risk distribution charts
- Case statistics
- Executive summaries

### Reporting
- AUSTRAC SMR draft generator
- Internal compliance reports
- Export-ready structured reports

### Voice Features
- Speech-to-text input
- Text-to-speech output for results

## Tech Stack

- Streamlit
- SQLite
- Python
- Google Gemini API
- Pandas
- Plotly

## Installation

```bash
pip install -r requirements.txt
