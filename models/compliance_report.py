def generate_smr_report(case):
    """
    case = row from DB (tuple)
    """

    case_id = case[0]
    property_id = case[1]
    amount = case[2]
    buyer_name = case[3]
    buyer_type = case[4]
    source_of_funds = case[5]
    cash_payment = case[6]
    overseas_funds = case[7]
    pep = case[8]
    sanctions = case[9]
    risk_score = case[10]
    risk_level = case[11]

    risk_band = "LOW"
    if risk_score >= 70:
        risk_band = "HIGH"
    elif risk_score >= 40:
        risk_band = "MEDIUM"

    report = f"""
AUSTRAC SUSPICIOUS MATTER REPORT (DRAFT)

CASE ID: {case_id}

PROPERTY:
{property_id}

BUYER:
{buyer_name} ({buyer_type})

TRANSACTION:
Amount: ${amount}
Source of Funds: {source_of_funds}

RISK ASSESSMENT:
- Risk Score: {risk_score}
- Risk Level: {risk_level}
- Risk Band: {risk_band}

RED FLAGS:
{"- Cash payment involved" if cash_payment else ""}
{"- Overseas source of funds" if overseas_funds else ""}
{"- Politically Exposed Person (PEP)" if pep else ""}
{"- Potential sanctions match" if sanctions else ""}

ANALYSIS:
This transaction has been assessed using automated risk scoring and CDD screening.

The case has been classified as {risk_band.lower()} risk based on combined indicators.

RECOMMENDATION:
{"ESCALATE TO AUSTRAC (SMR REQUIRED)" if risk_score >= 70 else "Continue monitoring under standard compliance procedures"}

END OF REPORT
"""
    return report
