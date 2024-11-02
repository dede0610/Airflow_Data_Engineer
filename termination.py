from datetime import date

today = date.today() 
formatted_date = today.strftime('%d %B %Y')

print(f"DAG was successfully terminated after running for current day: {formatted_date}")

