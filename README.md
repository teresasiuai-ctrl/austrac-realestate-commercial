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

---

### ⚠️ Risk Engine
- Real-time transaction risk scoring (0–100)
- Automatic HIGH / LOW risk classification
- Rule-based compliance logic
- Auto-creates compliance cases

---

### 📁 Case Management
- View all compliance cases
- Track case status (OPEN / REVIEWING / CLOSED)
- Filter by risk level
- Search by Property ID

---

### 📊 Dashboard Analytics
- KPI overview (cases, risk, exposure)
- Risk distribution charts
- Transaction insights

---

### 🧾 Audit Logging
- System activity tracking
- Login history
- Risk check history
- Case creation history

---

### 📄 Compliance Report Generator
- Generates draft SMR (Suspicious Matter Report)
- Structured compliance reasoning
- Internal review support
- Case-based report generation

---

## 🔐 Demo Login

- Username: **admin**
- Password: **admin**

---

## 🧠 Core Value

- Reduces manual compliance workload
- Standardises AML/CTF workflows
- Improves audit visibility
- Supports compliance decision-making
- Automates draft reporting

---

## 🏗️ System Architecture

**User Interface Layer**
→ Streamlit Dashboard (Web App)

**Application Layer**
→ Python Backend (app.py)

**Business Logic Layer**
→ Risk Engine + Case Management System

**Data Layer**
→ SQLite Database (Cases + Audit Logs)

---

### 📁 Project Structure

app.py
utils/
  ├── db.py
  ├── auth.py

assets/
  ├── logo.png

requirements.txt
README.md

---

### ⚙️ Installation & Run

git clone https://github.com/your-username/austrac-realestate-ai-agent.git
cd austrac-realestate-ai-agent

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
streamlit run app.py

---

### 🔐 Demo Login

Username: admin
Password: admin

---

### 📊 Modules

Dashboard
KPI overview
Risk charts
Case summaries
Risk Engine
Input property ID + transaction amount
Generates risk score
Creates compliance case automatically
Case Management
View all cases
Filter by risk and status
Search by property ID
Audit Log
System activity tracking
Login and action history
Compliance Report Generator
Generates draft SMR reports
Structured compliance justification
Internal review support

---

### ⚠️ Disclaimer

This system is a simulation tool only.

It does not:

Provide legal or financial advice
Replace AUSTRAC obligations
Guarantee compliance outcomes

Users are responsible for regulatory compliance.

---

### 🚀 Intended Use

Real estate compliance training
AML/CTF workflow simulation
SaaS prototype demonstration
Internal risk analysis support

---
### 📌 Roadmap

Multi-user role system (Admin / Analyst)
PDF export for SMR reports
PostgreSQL cloud upgrade
AI-powered risk explanations
Production SaaS deployment
