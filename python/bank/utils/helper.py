from datetime import date, datetime

def date_to_str(date_obj: date) -> str:
    return date_obj.strftime('%d/%m/%Y')

def str_to_date(date_string: str) -> date:
    return datetime.strptime(date_string, '%d/%m/%Y')

def format_float_to_currency(value: float) -> str:
    return f'{value:,.2f}€'
