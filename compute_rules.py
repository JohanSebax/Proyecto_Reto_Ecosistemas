import sqlite3
from datetime import datetime

# Connect to the SQLite database
conn = sqlite3.connect('database.sqlite')
cursor = conn.cursor()

# Generic function to query by commerce_id and count rows grouped by ask_status with optional year-month filtering
def get_api_call_summary(commerce_id, year_months=None):
    query = """
    SELECT ask_status, COUNT(*) AS count
    FROM apicall
    WHERE commerce_id = ?
    """
    params = [commerce_id]
    
    # Add filtering by year-month(s) if provided
    if year_months:
        year_month_conditions = " OR ".join(["strftime('%Y-%m', date_api_call) = ?"] * len(year_months))
        query += f" AND ({year_month_conditions})"
        params.extend(year_months)
    
    query += " GROUP BY ask_status"
    
    cursor.execute(query, params)
    result = cursor.fetchall()
    
    # Format the results
    summary = {row[0]: row[1] for row in result}
    return summary

# Function to get all commerce IDs from the commerce table
def get_all_commerce_ids():
    query = "SELECT commerce_id, commerce_name, commerce_nit, commerce_email FROM commerce WHERE commerce_status = 'Active'"
    cursor.execute(query)
    return cursor.fetchall()

# Compute costs based on contracts and discount rules
def compute_costs(commerce_id, summary):
    successful_count = summary.get("Successful", 0)
    unsuccessful_count = summary.get("Unsuccessful", 0)

    # Get contract rules for this commerce
    contract_query = """
    SELECT min_requests, max_requests, rate
    FROM contracts
    WHERE commerce_id = ?
    """
    cursor.execute(contract_query, (commerce_id,))
    contract_rules = cursor.fetchall()

    # Calculate base costs
    base_cost = 0
    for rule in contract_rules:
        min_requests, max_requests, rate = rule
        if max_requests is None:  # No upper limit
            if successful_count >= min_requests:
                base_cost += successful_count * rate
        elif min_requests <= successful_count <= max_requests:
            base_cost += successful_count * rate

    # Apply discounts based on unsuccessful API calls
    discount = 0
    discount_query = """
    SELECT min_unsuccessful_requests, max_unsuccessful_requests, discount_percentage
    FROM discount_rules
    WHERE commerce_id = ?
    """
    cursor.execute(discount_query, (commerce_id,))
    discount_rules = cursor.fetchall()

    for rule in discount_rules:
        min_unsuccessful_requests, max_unsuccessful_requests, discount_percentage = rule
        if max_unsuccessful_requests is None:  # No upper limit
            if unsuccessful_count >= min_unsuccessful_requests:
                discount = discount_percentage/100 * base_cost
        elif min_unsuccessful_requests <= unsuccessful_count <= max_unsuccessful_requests:
            discount = discount_percentage/100 * base_cost

    # Compute final costs (Valor Total)
    iva = 0.19 * base_cost  # IVA (19%)
    total_cost = base_cost + iva - discount

    return {
        "successful_count": successful_count,
        "unsuccessful_count": unsuccessful_count,
        "base_cost": base_cost,
        "iva": iva,
        "discount": discount,
        "total_cost": total_cost
    }

# Iterate over all commerce IDs and generate summaries with optional year-month filtering
def generate_summary_for_all_commerce(year_months=None):
    commerce_ids = get_all_commerce_ids()
    all_summaries = {}
    
    for commerce_id, commerce_name, commerce_nit, commerce_email in commerce_ids:
        summary = get_api_call_summary(commerce_id, year_months)
        costs = compute_costs(commerce_id, summary)
        all_summaries[commerce_id] = {
            "date": year_months,
            "commerce_name": commerce_name,
            "commerce_nit": commerce_nit,
            "commerce_email": commerce_email,
            "summary": summary,
            "costs": costs
        }
    
    return all_summaries