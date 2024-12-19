
def fill_missing_translations(uz_val, kaa_val, ru_val):
        """
        Eger mánislerdiń tek birewi kirgizilgen bolsa,
        qalǵan tiller ushın da usı mánisti belgileydi.
        """
        values = [uz_val, kaa_val, ru_val]
        default_value = next((v for v in values if v is not None), "")
        return tuple(v if v is not None else default_value for v in values)
