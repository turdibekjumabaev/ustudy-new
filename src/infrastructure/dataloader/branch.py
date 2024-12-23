from src.infrastructure.models.branch import Branch


def init_nukus_branch(db):
    nukus_data = {
        'name': {
            'uz': 'Nukus',
            'kk': 'Nókis',
            'ru': 'Нукус'
        },
        'address': {
            'uz': 'A.Shamuratova 94',
            'kk': 'A.Shamuratova 94',
            'ru': 'А.Шамуратова 92'
        },
        'landmark': {
            'uz': 'Nukus city turatjoy muajimosi',
            'kk': 'Nókis city úyleri',
            'ru': 'Жилой комплекс Нукус Сити'
        },
        'phone_number': '998555015353',
        'open_time': {
            "weekdays": {
                "monday"   : True ,
                "tuesday"  : True ,
                "wednesday": True ,
                "thursday" : True ,
                "friday"   : True ,
                "saturday" : True ,
                "sunday"   : False
            },
            "hour": {"from": "09:00", "to": "19:00"}
        },
        'banner': 'banner-nukus.png',
        'latitude': 42.45869871350882,
        'longitude': 59.611836070126266
    }

    branch = Branch.query.filter_by(phone_number=nukus_data['phone_number']).first()
    if not branch:
        nukus_branch = Branch(**nukus_data)
        db.session.add(nukus_branch)
        db.session.commit()
