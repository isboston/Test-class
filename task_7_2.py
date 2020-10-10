def inch_to_cm(inch):
    convert_inch_to_cm = inch * 2.54
    print(convert_inch_to_cm)
    return convert_inch_to_cm


def cm_to_inch(cm):
    convert_cm_to_inch = cm * 0.39
    print(convert_cm_to_inch)
    return convert_cm_to_inch


def mile_to_km(mile):
    convert_mile_to_km = mile * 1.61
    print(convert_mile_to_km)
    return convert_mile_to_km


def km_to_mile(km):
    convert_km_to_mile = km * 0.62
    print(convert_km_to_mile)
    return convert_km_to_mile


def pound_to_kg(pound):
    convert_pound_to_kg = pound * 0.45
    print(convert_pound_to_kg)
    return convert_pound_to_kg


def kg_to_pound(kg):
    convert_kg_to_pound = kg * 2.2
    print(convert_kg_to_pound)
    return convert_kg_to_pound


def ounces_to_grams(ounces):
    convert_ounces_to_grams = ounces * 28.35
    print(convert_ounces_to_grams)
    return convert_ounces_to_grams


def grams_to_ounces(grams):
    convert_grams_to_ounces = grams * 0.035
    print(convert_grams_to_ounces)
    return convert_grams_to_ounces


def gallon_in_liters(gallon):
    convert_gallon_in_liters = gallon * 4.55
    print(convert_gallon_in_liters)
    return convert_gallon_in_liters


def liters_in_gallon(liters):
    convert_liters_in_gallon = liters * 0.22
    print(convert_liters_in_gallon)
    return convert_liters_in_gallon


def pints_in_liters(pints):
    convert_pints_in_liters = pints * 0.57
    print(convert_pints_in_liters)
    return convert_pints_in_liters


def liters_in_pints(liters):
    convert_liters_in_pints = liters * 1.76
    print(convert_liters_in_pints)
    return convert_liters_in_pints


while True:
    options_conversion = int(input('Enter one of the conversion options (1-12):\n'))
    number_conversion = int(input('Enter a number for conversion:\n'))
    if options_conversion == 1:
        inch_to_cm(number_conversion)
    elif options_conversion == 2:
        cm_to_inch(number_conversion)
    elif options_conversion == 3:
        mile_to_km(number_conversion)
    elif options_conversion == 4:
        km_to_mile(number_conversion)
    elif options_conversion == 5:
        pound_to_kg(number_conversion)
    elif options_conversion == 6:
        kg_to_pound(number_conversion)
    elif options_conversion == 7:
        ounces_to_grams(number_conversion)
    elif options_conversion == 8:
        grams_to_ounces(number_conversion)
    elif options_conversion == 9:
        gallon_in_liters(number_conversion)
    elif options_conversion == 10:
        liters_in_gallon(number_conversion)
    elif options_conversion == 11:
        pints_in_liters(number_conversion)
    elif options_conversion == 12:
        liters_in_pints(number_conversion)
    elif options_conversion == 0:
        break
