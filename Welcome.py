"""The Task
Think of a way to store the languages as a database (eg an object). The languages are listed below so you can copy and paste!
Write a 'welcome' function that takes a parameter 'language' (always a string), and returns a greeting - if you have it in your database. It should default to English if the language is not in the database, or in the event of an invalid input."""

def greet(language):
    db = {'english': 'Welcome','czech': 'Vitejte','danish': 'Velkomst','dutch': 'Welkom','estonian': 'Tere tulemast','finnish': 'Tervetuloa','flemish': 'Welgekomen','french': 'Bienvenue','german': 'Willkommen','irish': 'Failte','italian': 'Benvenuto','latvian': 'Gaidits','lithuanian': 'Laukiamas',"polish": 'Witamy','spanish': 'Bienvenido','swedish': 'Valkommen','welsh': 'Croeso'}
    if language == "IP_ADDRESS_INVALID" or language == "IP_ADDRESS_NOT_FOUND" or language=="IP_ADDRESS_REQUIRED" or language == "" or type(language) == int:
        return "Welcome"
    else:
        return db[language]
