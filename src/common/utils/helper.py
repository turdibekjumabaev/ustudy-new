def fill_missing_translations(data, available_languages=None):
    """
    Bir tildegi mánis arqalı basqa tillerdegi mánisler toltırıladı.
    """
    if available_languages is None:
        available_languages = ["uz", "ru", "kk"]

    base_value = next((value for lang, value in data.items() if value), None)
    
    if base_value is None:
        raise ValueError("Hech qaysi til uchun qiymat berilmagan")

    filled_data = {lang: data.get(lang, base_value) for lang in available_languages}
    
    return filled_data
