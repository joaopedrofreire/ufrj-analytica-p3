from datetime import datetime

def calculate_age(born, date):
    return date.year - born.year - ((date.month, date.day) < (born.month, born.day))

def get_quote(args):
        name = args['name']
        birthdate = datetime.strptime(args['birthdate'], '%Y-%m-%d')
        date = datetime.strptime(args['date'], '%Y-%m-%d')
        date_format = datetime.strftime(date, '%d/%m/%Y')
        age_now = calculate_age(birthdate, datetime.today())
        age_then = calculate_age(birthdate, date)
        
        if date < datetime.now():
            return {
                'message': {
                    'date': 'A data escolhida deve ser no futuro'
                    }
                }, 400

        response = {
                "quote": f"Olá, {name}! Você tem {age_now} anos e em {date_format} você terá {age_then} anos.",
                "ageNow": age_now,
                "ageThen": age_then
        }

        return response