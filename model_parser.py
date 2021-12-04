import re


def get_file_data(filename: str) -> str:
    with open(filename) as f:
        return f.read()


def parse_condition(condition) -> dict:
    var_prefixes = {}
    parsed_data = re.findall(r'^(\+)?(\-)?\\frac\{(\d+)\}\{(\d+)\}x_\{(\d+)\}(.+?)$', condition)
    if parsed_data:
        _, minus, upper, lower, number, condition = parsed_data[0]

        prefix = int(upper) / int(lower)
        if minus:
            prefix = -prefix
        var_prefixes[int(number)] = prefix
        if condition:
            var_prefixes.update(parse_condition(condition))

        return var_prefixes

    parsed_data = re.findall(r'^(\+)?(\-)?(\d+)?x_\{(\d+)\}(.+?)$', condition)
    if parsed_data:
        _, minus, prefix, number, condition = parsed_data[0]

        if not prefix:
            prefix = 1
        prefix = int(prefix)
        if minus:
            prefix = -prefix
        var_prefixes[int(number)] = prefix
        if condition:
            var_prefixes.update(parse_condition(condition))

        return var_prefixes

    parsed_data = re.findall(r'^((\\leq)|(=)|(\\geq))(\-)?(\d+)$', condition)
    if parsed_data:
        _, leq, eq, geq, minus, b = parsed_data[0]

        b = int(b)
        if minus:
            b = -b
        var_prefixes['b'] = {'<=': bool(leq), '=': bool(eq), '>=': bool(geq), 'value': b}

        return var_prefixes

    return var_prefixes


def get_addition_variables(conditions: list):
    addition_variables = {}
    for condition in conditions:
        if condition['b']['<=']:
            addition_variables[len(addition_variables.keys()) + 1] = 1
            condition['b']['additional_variable_num'] = len(addition_variables.keys())
        elif condition['b']['>=']:
            addition_variables[len(addition_variables.keys()) + 1] = -1
            condition['b']['additional_variable_num'] = len(addition_variables.keys())
    return addition_variables





def parse(filename: str) -> list:
    file_data = get_file_data(filename)
    file_data = re.sub(r'[\t\s\n]', '', file_data)
    conditions = re.findall(r'\\begin\{.+?\}(.+?)\\end\{.+?\}', file_data)[0].split('\\\\')
    conditions = [parse_condition(i) for i in conditions]
    conditions = [i for i in conditions if i]
    addition_variables = get_addition_variables(conditions)
    max_var_num = max([max([key for key in i.keys() if type(key) is int] or [0]) for i in conditions])

    _, max_, min_, expression = re.findall(r'\\((max)|(min))\s*f\s*=((\s*(\+)?(\-)?\s*x_\{(\d+)\})*)', file_data)[0][:4]
    maximum = bool(max_)
    func = parse_condition(expression)

    result = []
    for condition in conditions:
        result.append([condition['b']['value']] + [condition.get(i) or 0 for i in range(1, max_var_num + 1)] + [v if condition['b'].get('additional_variable_num') == k else 0 for k, v in addition_variables.items()])

    result.append([0] + [-(func.get(i) or 0) for i in range(1, max_var_num + 1)] + [0 for k, v in addition_variables.items()])




    return maximum, result