from src.infrastructure.models.language import Language

def load_language(db):
    existing_languages = {lang.code for lang in db.session.query(Language.code).all()}
    languages = [
        Language(name='Qaraqalpaqsha', code='kk'),
        Language(name='Русский', code='ru'),
        Language(name='O‘zbekcha', code='uz')
    ]
    new_languages = [lang for lang in languages if lang.code not in existing_languages]
    if new_languages:
        db.session.bulk_save_objects(new_languages)
        db.session.commit()
