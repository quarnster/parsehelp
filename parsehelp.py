"""
Copyright (c) 2012 Fredrik Ehnbom

This software is provided 'as-is', without any express or implied
warranty. In no event will the authors be held liable for any damages
arising from the use of this software.

Permission is granted to anyone to use this software for any purpose,
including commercial applications, and to alter it and redistribute it
freely, subject to the following restrictions:

   1. The origin of this software must not be misrepresented; you must not
   claim that you wrote the original software. If you use this software
   in a product, an acknowledgment in the product documentation would be
   appreciated but is not required.

   2. Altered source versions must be plainly marked as such, and must not be
   misrepresented as being the original software.

   3. This notice may not be removed or altered from any source
   distribution.
"""
import re


def count_brackets(data):
    even = 0
    for i in range(len(data)):
        if data[i] == '{':
            even += 1
        elif data[i] == '}':
            even -= 1
    return even


def collapse_brackets(before):
    i = len(before)
    count = 0
    end = -1
    min = 0
    while i >= 0:
        a = before.rfind("}", 0, i)
        b = before.rfind("{", 0, i)
        i = max(a, b)
        if i == -1:
            break
        if before[i] == '}':
            count += 1
            if end == -1:
                end = i
        elif before[i] == '{':
            count -= 1
            if count < min:
                min = count

        if count == min and end != -1:
            before = "%s%s" % (before[:i+1], before[end:])
            end = -1
    return before


def collapse_ltgt(before):
    i = len(before)
    count = 0
    end = -1
    while i >= 0:
        a = before.rfind(">", 0, i)
        b = before.rfind("<", 0, i)
        i = max(a, b)
        if i == -1:
            break
        if before[i] == '>':
            collapse = True
            if i > 0 and before[i-1] == '>':
                # Don't want to collapse a statement such as 'std::cout << "hello world!!" << std::endl;
                data = before[:i-1]
                match = re.search("([\\w\\s,.:<]+)$", data)
                if match:
                    if match.group(1).count("<") < 2:
                        collapse = False
                else:
                    collapse = False

            if not collapse or before[i-1] == '-' or \
                    (before[i-1] == ' ' and i >=2 and before[i-2] != '>'):
                i -= 1
            else:
                count += 1
                if end == -1:
                    end = i
        elif before[i] == '<':
            if i > 0 and (before[i-1] == '<' or before[i-1] == ' '):
                i -= 1
            else:
                count -= 1
                if count == 0 and end != -1:
                    before = "%s%s" % (before[:i+1], before[end:])
                    end = -1
    return before


def collapse_parenthesis(before):
    i = len(before)
    count = 0
    end = -1
    while i >= 0:
        a = before.rfind("(", 0, i)
        b = before.rfind(")", 0, i)
        i = max(a, b)
        if i == -1:
            break
        if before[i] == ')':
            count += 1
            if end == -1:
                end = i
        elif before[i] == '(':
            count -= 1
            if count == 0 and end != -1:
                before = "%s%s" % (before[:i+1], before[end:])
                end = -1
    return before


def collapse_strings(before):
    i = len(before)
    count = 0
    end = -1
    while i >= 0:
        i = before.rfind("\"", 0, i)
        if i == -1:
            break
        if before[i] == '\"':
            if i > 0 and before[i-1] == '\\':
                i -= 1
            elif count > 0:
                before = "%s%s" % (before[:i+1], before[end:])
                count = 0
            else:
                count += 1
                end = i
    return before


def collapse_square_brackets(before):
    i = len(before)
    count = 0
    end = -1
    while i >= 0:
        a = before.rfind("[", 0, i)
        b = before.rfind("]", 0, i)
        i = max(a, b)
        if i == -1:
            break
        if before[i] == ']':
            count += 1
            if end == -1:
                end = i
        elif before[i] == '[':
            count -= 1
            if count == 0 and end != -1:
                before = "%s%s" % (before[:i+1], before[end:])
                end = -1
    return before


def extract_completion(before):
    before = collapse_parenthesis(before)
    before = collapse_square_brackets(before)
    before = before.split("\n")[-1]
    ret = ""
    while True:
        match = re.search("((\.|\->)?([^|.,\ \[\]\(\)\t]+(\(\)|\[\])*)(\.|\->))$", before)
        if not match:
            break
        ret = match.group(3) + match.group(5) + ret
        before = before[:-len(match.group(3))-len(match.group(5))].strip()
    return ret

_keywords = ["return", "new", "delete", "class", "define", "using", "void", "template", "public:", "protected:", "private:", "public", "private", "protected", "typename", "in"]


def extract_package(data):
    data = remove_preprocessing(data)
    match = re.search(r"package\s([\w.]+);", data)
    if match:
        return match.group(1)
    return None


def extract_used_namespaces(data):
    regex = re.compile("\s*using\s+(namespace\s+)?([^;]+)", re.MULTILINE)
    ret = []
    for match in regex.finditer(data):
        toadd = match.group(2)
        if match.group(1) == None:
            toadd = toadd[:toadd.rfind("::")]
        ret.append(toadd)
    return ret


def extract_namespace(data):
    data = remove_preprocessing(data)
    data = collapse_brackets(data)
    data = remove_namespaces(data)
    regex = re.compile("namespace\s+([^{\s]+)\s*\{", re.MULTILINE)
    ret = ""
    for match in regex.finditer(data):
        if len(ret):
            ret += "::"
        ret += match.group(1)
    if len(ret.strip()) == 0:
        ret = None
    return ret


def extract_class_from_function(data):
    data = collapse_brackets(data)
    data = remove_functions(data)
    ret = None
    for match in re.finditer("(.*?)(\w+)::~?(\w+)\\s*\([^)]*\)\s*(const)?\s*\{", data, re.MULTILINE):
        ret = match.group(2)
    return ret


def extract_class(data):
    data = remove_preprocessing(data)
    data = collapse_brackets(data)
    data = collapse_strings(data)
    data = remove_classes(data)
    regex = re.compile("class\s+([^;{\\s:]+)\\s*(:|;|\{|extends|implements)", re.MULTILINE)
    ret = None
    for match in regex.finditer(data):
        ret = match.group(1)
    return ret


def extract_inheritance(data, classname):
    data = remove_preprocessing(data)
    data = collapse_brackets(data)
    data = remove_classes(data)
    regex = re.compile("class\s+%s\\s*(:|extends)\\s+([^\\s,\{]+)" % classname, re.MULTILINE)
    match = regex.search(data)
    if match != None:
        return match.group(2)
    return None


def remove_classes(data):
    regex = re.compile("class\s+[^{]+{\}\s*;?", re.MULTILINE)
    return regex.sub("", data)


def remove_functions(data):
    regex = re.compile("\S+\s*\([^\)]*\)\s*(const)?\s*\{\}", re.MULTILINE)
    return regex.sub("", data)


def remove_namespaces(data):
    regex = re.compile("\s*namespace\s+[^{]+\s*\{\}\s*", re.MULTILINE)
    return regex.sub("", data)


def sub(exp, data):
    regex = re.compile(exp, re.MULTILINE|re.DOTALL)
    while True:
        olddata = data
        data = regex.sub("", data)
        if olddata == data:
            break
    return data


def remove_preprocessing(data):
    data = data.replace("\\\n", " ")
    data = sub("\#\s*define[^\n]+\\n", data)
    data = sub("\#\s*(ifndef|ifdef|if|endif|else|elif|pragma|include)[^\\n]*\\n", data)
    data = sub("//[^\n]+\\n", data)
    data = sub("/\\*.*?\\*/", data)
    return data


def remove_includes(data):
    regex = re.compile("""\#\s*include\s+(<|")[^>"]+(>|")""")
    while True:
        old = data
        data = regex.sub("", data)
        if old == data:
            break
    return data

_invalid = """\\(\\s\\{,\\*\\&\\-\\+\\/;=%\)\"!"""


def extract_variables(data):
    origdata = data
    data = remove_preprocessing(data)
    data = remove_includes(data)
    data = collapse_brackets(data)
    data = collapse_ltgt(data)
    data = remove_functions(data)
    data = remove_namespaces(data)
    data = remove_classes(data)
    data = re.sub("\([^)]*?\)\\s*;", "()", data, re.MULTILINE)

    endpattern = "\;|,|\)|=|\["
    pattern = "(^\\s*|,|\()\\s*((struct\s*)?\\b[^%s]+[\\s*&]+(const)?[\\s*&]*)(\\b[^%s\[\>]+)\\s*(?=%s)" % (_invalid, _invalid, endpattern)
    regex = re.compile(pattern, re.MULTILINE)
    regex2 = re.compile("[^)]+\)+\s+\{")
    ret = []
    for m in regex.finditer(data):
        type = get_base_type(m.group(2))
        if type in _keywords or type.startswith("template"):
            continue
        pat = "%s\\s*%s\\s*(%s)" % (m.group(2).replace("*", "\\*"), m.group(5), endpattern)
        end = re.search(pat, data)
        if end.group(1) == "(":
            # Remove the declaration if it's inside of a () {}?
            left = data[end.end():]
            if regex.match(left) or regex2.match(left, re.MULTILINE):
                continue
        var = m.group(5).strip()
        type = m.group(2).strip()
        if end.group(1) == "[":
            type += re.search("([\\[\\]]+)", data[end.start():]).group(1)
        if var != None:
            if "<" in type and ">" in type:
                s = "\\b(%s.+%s)(const)?[ \\t*&]*(%s)" % (type[:type.find("<")+1], type[type.find(">"):], var)
                regex = re.compile(s)
                match = None
                for m in regex.finditer(origdata):
                    match = m
                type = match.group(1)

            ret.append((type, var))
    return ret


def get_base_type(data):
    data = re.sub(r"\s*const\s*", "", data)
    data = re.sub(r"\s*static\s*", "", data)
    data = re.sub(r"\s*struct\s*", "", data)
    data = data.strip()
    data = data.replace("&", "").replace("*", "").replace("[]", "")
    data = data.strip()
    return data


def get_var_type(data, var):
    regex = re.compile("\\b([^%s]+[ \s\*\&]+)(%s)\s*(\[|\(|\;|,|\)|=|:|in\s+)" % (_invalid, var))

    origdata = data
    data = remove_preprocessing(data)
    data = collapse_ltgt(data)
    data = collapse_brackets(data)

    match = None

    for m in regex.finditer(data):
        t = m.group(1).strip()
        if t in _keywords:
            continue
        match = m
    if match and match.group(1):
        key = get_base_type(match.group(1))
        if "<>" in key:
            name = key[:key.find("<")]
            end = key[key.find(">")+1:]
            regex = re.compile(r"(%s<.+>%s[\s*&]+)(%s)" % (name, end, var))
            match = None
            for m in regex.finditer(origdata):
                key = get_base_type(m.group(1))
                if key in _keywords:
                    continue
                match = m
            if match:
                data = origdata[match.start(1):match.end(1)]
                i = len(data)-1
                count = 0
                while i > 0:
                    a = data.rfind(">", 0, i)
                    b = data.rfind("<", 0, i)
                    i = max(a, b)
                    if i == -1:
                        break
                    if data[i] == ">":
                        count += 1
                    elif data[i] == "<":
                        count -= 1
                        if count == 0:
                            data = data[i:]
                            break
                regex = re.compile("(%s%s)(%s)" % (name, data, var))
                for m in regex.finditer(origdata):
                    match = m

    if match and match.group(1):
        # Just so that it reports the correct location in the file
        regex = re.compile("(%s)(%s)(\(|\;|,|\)|=)" % (re.escape(match.group(1)), re.escape(match.group(2))))
        for m in regex.finditer(origdata):
            match = m
    return match


def remove_empty_classes(data):
    data = sub("\s*class\s+[^\{]+\s*\{\}", data)
    return data


def get_type_definition(data):
    before = extract_completion(data)
    match = re.search("([^\.\-:]+)[^\.\-:]*(\.|->|::)(.*)", before)
    var = match.group(1)
    extra = ""
    if var.endswith("[]"):
        extra = var[var.find("["):]
        var = var[:var.find("[")]
    tocomplete = before[match.start(2):match.end(3)]

    if var == "this":
        clazz = extract_class(data)
        line = column = -1  # TODO
        return line, column, clazz, var, tocomplete
    elif var == "super":
        clazz = extract_class(data)
        if clazz:
            sup = extract_inheritance(data, clazz)
            return -1, -1, sup, var, tocomplete
    elif match.group(2) == "::":
        return 0, 0, var, var, tocomplete
    else:
        match = get_var_type(data, var)
    if match == None:
        return -1, -1, var, None, tocomplete
    line = data[:match.start(2)].count("\n") + 1
    column = len(data[:match.start(2)].split("\n")[-1])+1
    typename = match.group(1).strip()
    return line, column, typename+extra, var, tocomplete


def template_split(data):
    if data == None:
        return None
    ret = []
    origdata = data
    data = collapse_ltgt(data)
    data = [a.strip() for a in data.split(",")]
    exp = ""
    for var in data:
        exp += "(%s)\\s*,?\\s*" % (re.escape(var).replace("\\<\\>", "<.*>").strip())

    match = re.search(exp, origdata)
    ret = list(match.groups())

    return ret


def solve_template(typename):
    args = []
    template = re.search(r"([^<]+)(<(.+)>)?((::|.)(.+))?$", typename)
    args = template_split(template.group(3))
    if args:
        for i in range(len(args)):
            if "<" in args[i]:
                args[i] = solve_template(args[i])
            else:
                args[i] = (args[i], None)
    if template.group(6):
        return template.group(1), args, solve_template(template.group(6))
    return template.group(1), args


def make_template(data, concat="."):
    if data[1] != None:
        ret = ""
        for param in data[1]:
            sub = make_template(param, concat)
            if len(ret):
                ret += ", "
            ret += sub
        temp = "%s<%s%s>" % (data[0], ret, ' ' if ret[-1] == '>' else '')
        if len(data) == 3:
            temp += concat + make_template(data[2], concat)
        return temp
    return data[0]


def extract_line_until_offset(data, offset):
    return data[:offset].split("\n")[-1]


def extract_line_at_offset(data, offset):
    line = data[:offset].count("\n")
    return data.split("\n")[line]


def extract_word_at_offset(data, offset):
    line, column = get_line_and_column_from_offset(data, offset)
    line = extract_line_at_offset(data, offset)
    begin = 0
    end = 0
    match = re.search("\\b\w*$", line[0:column-1])
    if match:
        begin = match.start()
    match = re.search("^\w*", line[begin:])
    if match:
        end = begin+match.end()
    word = line[begin:end]
    return word


def extract_extended_word_at_offset(data, offset):
    line, column = get_line_and_column_from_offset(data, offset)
    line = extract_line_at_offset(data, offset)
    match = re.search("^\w*", line[column:])
    if match:
        column = column + match.end()
    extword = line[0:column]
    return extword


def get_line_and_column_from_offset(data, offset):
    data = data[:offset].split("\n")
    line = len(data)
    column = len(data[-1])
    if line > 1:
        column += 1
    return line, column


def get_offset_from_line_and_column(data, line, column):
    data = data.split("\n")
    offset = len("\n".join(data[:line-1])) + column
    return offset
