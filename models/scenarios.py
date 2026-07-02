def calculate_risk(data):

    score = 0
    reasons = []

    # Transaction amount
    if data["amount"] >= 1000000:
        score += 25
        reasons.append("High value property transaction")

    # Cash payment
    if data["cash_payment"]:
        score += 30
        reasons.append("Cash payment involved")

    # Overseas funds
    if data["overseas_funds"]:
        score += 20
        reasons.append("Overseas source of funds")

    # PEP
    if data["pep"]:
        score += 30
        reasons.append("Politically Exposed Person")

    # Sanctions
    if data["sanctions"]:
        score += 100
        reasons.append("Possible sanctions match")

    # Trust
    if data["buyer_type"] == "Trust":
        score += 10
        reasons.append("Trust structure")

    # Company
    if data["buyer_type"] == "Company":
        score += 5
        reasons.append("Company purchaser")

    score = min(score, 100)

    if score >= 70:
        level = "HIGH"
    elif score >= 40:
        level = "MEDIUM"
    else:
        level = "LOW"

    return score, level, reasons
