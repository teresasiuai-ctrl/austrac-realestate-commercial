# 🏢 AUSTRAC Real Estate AI Agent  
### Commercial SaaS Compliance Intelligence Platform

AI-powered AML/CTF risk detection, case management, audit logging, and compliance reporting system for real estate workflows.

---

## 🚀 Overview

The AUSTRAC Real Estate AI Agent is a **SaaS-style compliance simulation platform** designed to help real estate organisations identify financial risk, manage compliance cases, and generate structured draft reports.

> ⚠️ This system is for simulation, training, and internal compliance support only. It is not a legal or regulatory reporting tool.

---

## ✨ Key Features

### 🔐 Authentication
- Secure login system (demo credentials)
- Session-based user tracking

### ⚠️ Risk Engine
- Real-time transaction risk scoring (0–100)
- Automatic HIGH / LOW risk classification
- Rule-based compliance logic

### 📁 Case Management
- Auto-created compliance cases
- Status tracking (OPEN / REVIEWING / CLOSED)
- Filtering and search tools

### 📊 Compliance Dashboard
- KPI monitoring (cases, risk, exposure)
- Risk analytics and charts
- Transaction overview

### 🧾 Audit Logging
- Logs all system actions
- Tracks logins, risk checks, and case creation
- Full compliance audit trail simulation

### 📄 Draft SMR Report Generator
- Generates Suspicious Matter Report (SMR) drafts
- Structured compliance reasoning
- Internal review-ready format per case

---

## 🧠 Core Value

- Reduces manual compliance workload
- Standardises AML/CTF workflows
- Improves audit visibility
- Supports compliance decision-making
- Automates draft reporting

---
## 🏗️ System Architecture

Streamlit Frontend (UI Dashboard)
↓
Python Application Layer (app.py)
↓
Business Logic Layer (Risk Engine + Case System)
↓
SQLite Database (Cases + Audit Logs)

---

## 📁 Project Structure

app.py
utils/
├── db.py
├── auth.py

assets/
├── logo.png

requirements.txt
README.md

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/austrac-realestate-ai-agent.git
cd austrac-realestate-ai-agent

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
streamlit run app.py

---
🔐 Demo Login
Username: admin
Password: admin
📊 Modules Overview
📌 Dashboard
KPI overview
Risk analytics charts
Case summaries
⚠️ Risk Engine
Input Property ID + transaction amount
Generates risk score (0–100)
Automatically creates compliance case
📁 Case Management
View all cases
Filter by risk level and status
Search by Property ID
🧾 Audit Log
System activity tracking
Login history
Risk check history
📄 Compliance Report Generator
Generates draft SMR reports
Structured compliance justification
Internal review support
⚠️ Disclaimer

This system is a simulation tool only.

It does not:

Provide legal or financial advice
Replace AUSTRAC obligations
Guarantee compliance outcomes

Users are responsible for regulatory compliance.

🚀 Intended Use
Real estate compliance training
AML/CTF workflow simulation
SaaS prototype demonstration
Internal risk analysis support
📌 Roadmap
Multi-user roles (Admin / Analyst)
PDF export for SMR reports
PostgreSQL database upgrade
AI-powered risk explanations
Production SaaS deployment
