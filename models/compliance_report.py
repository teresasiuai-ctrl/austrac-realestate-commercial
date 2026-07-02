def generate_smr_report(case):

    return f"""
AUSTRAC SUSPICIOUS MATTER REPORT (DRAFT)

CASE ID: {case[0]}

PROPERTY: {case[1]}
AMOUNT: ${case[2]}

BUYER: {case[3]} ({case[4]})
SOURCE OF FUNDS: {case[5]}

RISK INDICATORS:
- Cash Payment: {case[6]}
- Overseas Funds: {case[7]}
- PEP: {case[8]}
- Sanctions: {case[9]}

RISK ASSESSMENT:
- Risk Score: {case[10]}
- Risk Level: {case[11]}

CASE STATUS: {case[12]}

ANALYSIS:
This case was assessed using automated AUSTRAC compliance rules.

Multiple risk factors were evaluated including:
CDD indicators, transaction behaviour, and exposure risk flags.

RECOMMENDATION:
{"ESCALATE TO SMR SUBMISSION" if case[10] >= 70 else "CONTINUE MONITORING UNDER ENHANCED DUE DILIGENCE"}

END OF REPORT
"""
