from parsehelp import *

f = open("unittest.cpp")
fulldata = f.read()
f.close()

offset = 10
line, column = get_line_and_column_from_offset(fulldata, offset)
offset2 = get_offset_from_line_and_column(fulldata, line, column)
if offset != offset2:
    raise Exception("Offset to line and column conversion failed, %d != %d" % (offset, offset2))

offset = 100
line, column = get_line_and_column_from_offset(fulldata, offset)
offset2 = get_offset_from_line_and_column(fulldata, line, column)
if offset != offset2:
    raise Exception("Offset to line and column conversion failed, %d != %d" % (offset, offset2))

offset = 200
line, column = get_line_and_column_from_offset(fulldata, offset)
offset2 = get_offset_from_line_and_column(fulldata, line, column)
if offset != offset2:
    raise Exception("Offset to line and column conversion failed, %d != %d" % (offset, offset2))

if extract_line_at_offset(fulldata, get_offset_from_line_and_column(fulldata, 12, 4)) != "std::vector<A> v;":
    raise Exception("Line extraction didn't work")

if extract_word_at_offset(fulldata, get_offset_from_line_and_column(fulldata, 84, 11)) != "tababa":
    raise Exception("Word extraction didn't work")

if extract_word_at_offset(fulldata, get_offset_from_line_and_column(fulldata, 85, 5)) != "tababa":
    raise Exception("Word extraction didn't work")

test = """/*
 testing some stuff
*/
// Will it pick this up as variables?\\
How about this?
#include <stdio.h>
// And this? /*
int itShouldPickupThis;
// */
static void Test::Something(Type& t1, vector<Type2> &t2)"""
match = get_var_type(test, "t2")
if match == None or match.group(1) != "vector<Type2> &":
    raise Exception("Couldn't extract type properly: %s" % (match.group(1) if match else "None"))

match = get_var_type(test, "t1")
if match == None or match.group(1).strip() != "Type&":
    raise Exception("Couldn't extract type properly: %s" % (match.group(1) if match else "None"))

if extract_variables(test) != [('int', 'itShouldPickupThis'), ('Type&', 't1'), ('vector<Type2> &', 't2')]:
    raise Exception("Didn't extract variables correctly")

test = """Properties prop = new Properties();
int apps = Integer.parseInt(prop."""
if get_type_definition(test, "int apps = Integer.parseInt(prop.") != (1, 12, "Properties", "prop", "."):
    raise Exception("Didn't get type definition properly")
test = """Properties prop = new Properties();
int apps = Integer.parseInt(prop.getProperty("a")."""
if get_type_definition(test, """int apps = Integer.parseInt(prop.getProperty("a").""") != (1, 12, "Properties", "prop", ".getProperty()."):
    raise Exception("Didn't get type definition properly")

if extract_completion("prop.GetColor().Clamp().") != "prop.GetColor().Clamp().":
    raise Exception("Didn't extract completion properly")

test = """DVFSStats dvfs = new DVFSStats();
DVFSStats."""
if get_type_definition(test, test.split("\n")[1]) != (-1, -1, "DVFSStats", None, "."):
    raise Exception("Couldn't parse type definition properly")

test = """CPUStats.CPULoad cpuLoad = cpu.new CPULoad();
cpuLoad."""
if get_type_definition(test, test.split("\n")[1]) != (1, 18, "CPUStats.CPULoad", "cpuLoad", "."):
    raise Exception("Couldn't parse type definition properly")

test = """ShortcutIconResource iconRes = Intent.ShortcutIconResource.fromContext(this, R.drawable.);"""
if get_type_definition(test, test[:-2]) != (-1, -1, "R", None, ".drawable."):
    raise Exception("Couldn't parse type definition properly")

print "all is well"