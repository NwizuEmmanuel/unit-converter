from pint import UnitRegistry

ureg = UnitRegistry()

def convert_measure(from_unit, to_unit, x, convert_type):
    if convert_type == 'temperature':
        ureg.formatter.default_format = '.3f'
        Q_ = ureg.Quantity
        home = Q_(x, ureg(from_unit))
        return home.to(to_unit)
    else:
        result = x * ureg(from_unit)
        return result.to(to_unit)

def get_unit(str):
    units = {'degC': 'degree_Celsius', 'degF': 'Fahrenheit'}
    if str == 'kelvin':
        return 'kelvin'
    else:
        return units[str]