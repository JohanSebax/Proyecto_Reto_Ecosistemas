import json
import pandas as pd
from compute_rules import generate_summary_for_all_commerce
from send_email import send_email_with_attachment

selected_year_months = ['2024-07']  # July
all_summaries_july = generate_summary_for_all_commerce(year_months=selected_year_months)


selected_year_months = ['2024-08']  # August
all_summaries_august = generate_summary_for_all_commerce(year_months=selected_year_months)


# Print the summaries in JSON format
# print(json.dumps(all_summaries_july, indent=4))
# print(json.dumps(all_summaries_august, indent=4))

# Create a helper function to build a list of dictionaries 
def extract_rows(data_dict):
    rows = []
    for _, val in data_dict.items():
        fecha_mes = val["date"][0] if val.get("date") else ""
        nombre = val.get("commerce_name", "")
        nit = val.get("commerce_nit", "")
        correo = val.get("commerce_email", "")
        
        costs = val.get("costs", {})
        valor_comision = costs.get("base_cost", 0)
        valor_iva = costs.get("iva", 0)
        valor_total = costs.get("total_cost", 0)
        
        rows.append({
            "Fecha-Mes": fecha_mes,
            "Nombre": nombre,
            "Nit": nit,
            "Valor_comision": valor_comision,
            "Valor_iva": valor_iva,
            "Valor_Total": valor_total,
            "Correo": correo
        })
    return rows

# Build a DataFrame from each JSON dictionary and combine
df1 = pd.DataFrame(extract_rows(all_summaries_july))
df2 = pd.DataFrame(extract_rows(all_summaries_august))

# Combine them into a single DataFrame (append vertically)
df_combined = pd.concat([df1, df2], ignore_index=True)

# Print summaries in Pandas Dataframe
print(df_combined)

# Write the combined DataFrame to Excel
df_combined.to_excel("reporte_comisiones.xlsx", sheet_name="Data", index=False)

print("Excel file 'reporte_comisiones.xlsx' has been created successfully.")

# Email configuration
recipient = 'jhoansebax10@gmail.com'   # Input recipient´s email to test it


sender = 'jhoansebax10@gmail.com'  # Input sender email 
subject = 'Reporte de Comisiones'
body = 'Adjunto encontrarás el reporte de comisiones en formato Excel.'
attachment = 'reporte_comisiones.xlsx'

# Send the email with the Excel attachment
send_email_with_attachment(sender, recipient, subject, body, attachment)