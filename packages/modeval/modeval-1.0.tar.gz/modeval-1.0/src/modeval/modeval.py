import operator


class Ruleset:
    def __init__(self):
        self.functions = []
        self.operators = []
        self.variables = []


default_ruleset = Ruleset()
default_ruleset.operators = [
    [('^', operator.pow), ('**', operator.pow)],
    [('*', operator.mul), ('/', operator.truediv)],
    [('+', operator.add), ('-', operator.sub)]
]


class Parser:
    def __init__(self, ruleset=None, rounding=8):
        if ruleset is None:
            ruleset = default_ruleset

        self.ruleset = ruleset
        self.rounding = rounding

        # Initialize operators in different formats for eval function.
        self.translateList = {}
        self.op_lookup = {}
        self.op_filter = []
        self.ops = []
        for group in self.ruleset.operators:
            new_group = []
            for op in group:
                symbol = op[0]
                new_group.append(symbol)
                self.op_lookup[symbol] = op[1]
                if len(symbol) == 1:
                    self.op_filter.append(symbol)
                else:
                    # Convert multi character operators to unique single unicode character.
                    self.translateList[symbol] = chr(1000 + len(self.translateList))
                    self.op_filter.append(self.translateList[symbol])
            self.ops.append(new_group)

        # Initialize functions in different formats for eval function.
        self.funTranslateList = {}
        self.fun_lookup = {}
        self.functions = []
        for fun in self.ruleset.functions:
            name = fun[0]
            self.funTranslateList[name] = chr(5000 + len(self.funTranslateList))
            self.fun_lookup[name] = fun[1]
            self.functions.append(name)

        self.var_lookup = {}
        self.variables = []
        for var in self.ruleset.variables:
            name = var[0]
            self.var_lookup[name] = var[1]
            self.variables.append(name)

    def _push(self, obj, l, depth):
        while depth:
            l = l[-1]
            depth -= 1

        l.append(obj)

    def _parse_parentheses(self, s):
        groups = []
        depth = 0

        try:
            for char in s:
                if char == '(':
                    self._push([], groups, depth)
                    depth += 1
                elif char == ')':
                    depth -= 1
                else:
                    self._push(char, groups, depth)
        except IndexError:
            raise ValueError('Parentheses mismatch')

        if depth > 0:
            raise ValueError('Parentheses mismatch')
        else:
            return groups

    def _clean(self, grouped_expr):
        clean_expr = []

        buffer = ''
        for seg in grouped_expr:
            if not isinstance(seg, list):
                if seg in '1234567890.':
                    buffer += seg
                elif buffer != '':
                    buffer = float(buffer)
                    clean_expr.append(buffer)
                    buffer = ''

                if seg in [*self.op_filter, *self.functions]:
                    clean_expr.append(seg)
            else:
                clean_expr.append(self._clean(seg))

        if buffer != '':
            clean_expr.append(float(buffer))

        for i, n in enumerate(clean_expr):
            if isinstance(n, str):
                for k, v in self.translateList.items():
                    if n == v:
                        clean_expr[i] = n.replace(v, k)

        return clean_expr

    def _fun(self, grouped_expr):
        for i, n in enumerate(grouped_expr):
            if isinstance(n, str):
                for k, v in self.funTranslateList.items():
                    if n == v:
                        grouped_expr[i] = n.replace(v, k)
            elif isinstance(n, list):
                grouped_expr[i] = self._fun(n)

        return grouped_expr

    def _operate(self, a, symbol, b):
        return self.op_lookup[symbol](a, b)

    def _function(self, fun_name, a):
        return self.fun_lookup[fun_name](a)

    def _calc(self, arr):
        for ops in self.ops:
            i = 0
            a = None
            op = None
            negate = False
            while i < len(arr):
                if isinstance(arr[i], float):
                    if negate:
                        arr[i] *= -1
                        negate = False
                    if op is None:
                        a = arr[i]
                    else:
                        i -= 2
                        arr.pop(i)
                        arr.pop(i)
                        arr[i] = self._operate(a, op, arr[i])
                        a = arr[i]
                        op = None
                elif isinstance(arr[i], str):
                    if arr[i] == "-" and (i == 0 or isinstance(arr[i - 1], str) and arr[i - 1] in self.op_filter):
                        negate = not negate
                        arr.pop(i)
                        i -= 1
                    elif arr[i] in ops:
                        op = arr[i]
                    elif arr[i] in self.functions:
                        if isinstance(arr[i+1], list):
                            arr[i] = self._function(arr[i], self._calc(arr[i+1]))
                            arr.pop(i+1)
                        else:
                            raise ValueError('Test')
                elif isinstance(arr[i], list):
                    arr[i] = self._calc(arr[i])
                    i -= 1
                i += 1

        return arr[0]

    def eval(self, raw_in: str):
        raw_in = raw_in.replace(' ', '')

        var_fill = raw_in
        for var in self.variables:
            var_fill = var_fill.replace(var, str(self.var_lookup[var]))

        translated_in = var_fill
        for k, v in [*self.translateList.items(), *self.funTranslateList.items()]:
            translated_in = translated_in.replace(k, v)

        raw_grouped = self._parse_parentheses(translated_in)

        fun_grouped = self._fun(raw_grouped)

        clean_grouped = self._clean(fun_grouped)

        calc = self._calc(clean_grouped)

        if self.rounding > 0:
            result = round(calc, self.rounding)
            if result.is_integer():
                result = int(result)
            return result

        result = calc
        if result.is_integer():
            result = int(result)
        return result


if __name__ == '__main__':
    p = Parser()
    try:
        while True:
            print(p.eval(input('> ')))
    except KeyboardInterrupt:
        pass
