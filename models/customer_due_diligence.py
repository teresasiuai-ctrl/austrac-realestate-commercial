def check_cdd(data):

    issues = []

    if not data["buyer_name"]:
        issues.append("Buyer name missing")

    if not data["property"]:
        issues.append("Property details missing")

    if data["amount"] <= 0:
        issues.append("Transaction amount missing")

    if not data["source_of_funds"]:
        issues.append("Source of funds not provided")

    if data["pep"]:
        issues.append("PEP requires Enhanced Due Diligence")

    if data["sanctions"]:
        issues.append("Possible sanctions match")

    return issues
