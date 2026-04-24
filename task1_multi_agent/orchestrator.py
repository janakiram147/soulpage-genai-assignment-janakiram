from data_agent import get_company_data
from analyst_agent import analyze_company

def run_system(company):
    # Step 1: Get data
    data = get_company_data(company)

    # Step 2: Analyze
    result = analyze_company(data)

    return result
