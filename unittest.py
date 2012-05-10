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

test = """Intent.FLAG_ACTIVITY_RESET_TASK_IF_NEEDED|Intent."""
if get_type_definition(test, test) != (-1, -1, "Intent", None, "."):
    raise Exception("Couldn't parse type definition properly")

test = """public class LaunchApp
extends Activity
{

    @Override
    public void onCreate(Bundle b)
    {
        super.onCreate(b);
        super."""
if get_type_definition(test, test.split("\n")[-1]) != (-1, -1, 'Activity', 'super', '.'):
    raise Exception("Couldn't parse type definition properly")

test = """                for (Class clazz : c.getClasses())
                {
                    clazz."""
if get_type_definition(test, test.split("\n")[-1]) != (1, 28, 'Class', 'clazz', '.'):
    raise Exception("Couldn't parse type definition properly")


test = """package com.a.b;

public class TestActivity
    extends Activity
{

    class A
    {

    }

    private static class ContextFactory implements GLSurfaceView.EGLContextFactory {
        class Blah
        {
            public int test()
            {
                return 0x1337;
            }

        }
        public EGLContext createContext(EGL10 egl, EGLDisplay display, EGLConfig eglConfig) {
            this."""

if get_type_definition(test, test.split("\n")[-1]) != (-1, -1, 'ContextFactory', 'this', '.'):
    raise Exception("Couldn't parse type definition properly")

test = """package a.b.c;
public class PMQuadtree {
    /// Stuff
    public abstract class Node {
        // Node Stuff
    }

    public class White extends Node {
    }

    public class Black extends Node {
    }

    public class Gray extends Node {
    }

    public PMQuadtree(final Validator validator, final int spatialWidth,
            final int spatialHeight, final int order) {
        this."""

if get_type_definition(test, test.split("\n")[-1]) != (-1, -1, "PMQuadtree", "this", "."):
    raise Exception("Couldn't parse type definition properly")

test = """String args[] = cmd.split(" ");
                System.err.println(args.length);
                for (int i = 0; i < args.length; i++)
                {
                    System.err.println(args[i]);
                }

                try
                {
                    if (args[0].equals("-quit"))
                    {
                        args[0]."""
if get_type_definition(test, test.split("\n")[-1]) != (1, 8, "String[]", "args", "."):
    raise Exception("Couldn't parse type definition properly")

test = """                        foreach (Assembly asm in AssembliesLoaded)
                        {
                            foreach (Type t3 in asm.GetTypes())
                            {
                                if (t3."""
if get_type_definition(test, test.split("\n")[-1]) != (3, 43, "Type", "t3", "."):
    raise Exception("Couldn't parse type definition properly")

test = """class MyStruct
{
public:
    int type;

};

int main(int argc, char const *argv[])
{
    MyStruct a;
    int b = 0;
    int MyStruct = 0;
    printf("%d, %d\n", MyStruct, a.type);
    while (int y = 1)
    {
        y++;
    }
    for (int i = 0; i < 10; i++)
    {

    }
    int z = MyStruct* b;
    int q = z & b;
    printf("%d\n", q* z);
    printf("%d\n", q& z);"""
if extract_variables(test) != [('int', 'argc'), ('char const *[]', 'argv'), ('MyStruct', 'a'), ('int', 'b'), ('int', 'MyStruct'), ('int', 'z'), ('int', 'q')]:
    raise Exception("Couldn't extract variables properly")

if get_base_type("static const char const *[]") != "char":
    raise Exception("Couldn't properly get the base type")

test = """CacheCompletionResults* cache_complete_startswith(Cache* cache, const char *prefix)
{
    cache->complete(const char *prefix)->entries."""
if get_type_definition(test, test.split("\n")[-1]) != (1, 58, 'Cache*', 'cache', '->complete()->entries.'):
    raise Exception("Couldn't parse type definition properly")

test = """CacheCompletionResults* cache_complete_startswith(Cache* cache, const char *prefix)
{
    cache->complete(const char *prefix)->entries[10]->"""
if get_type_definition(test, test.split("\n")[-1]) != (1, 58, 'Cache*', 'cache', '->complete()->entries[]->'):
    raise Exception("Couldn't parse type definition properly")

test = """bool Mesh::CopyToVBO ( UInt32 wantedChannels, VBO& vbo )
{
    std::vector<abc> test();
    {
        something here
"""
if extract_class_from_function(test) != "Mesh":
    raise Exception("Failed to extract class")


test = """using namespace std;
using namespace std2;
using namespace some::long::namespace as s;
namespace std3
{

};

namespace std4
{"""

if extract_namespace(test) != "std4":
    raise Exception("Failed to extract the right namespace")

if extract_used_namespaces(test) != ['std', 'std2', 'some::long::namespace as s']:
    raise Exception("Faild to extract the right used namespaces")

test = "ArrayList<ArrayList<Integer> >"
data = solve_template(test)
if data != ('ArrayList', [('ArrayList', [('Integer', None)])]):
    raise Exception("Couldn't solve template properly")

if make_template(data) != test:
    raise Exception("Couldn't make template properly")

test = "ArrayList<Integer>"
data = solve_template(test)
if data != ('ArrayList', [('Integer', None)]):
    raise Exception("Couldn't solve template properly")

if make_template(data) != test:
    raise Exception("Couldn't make template properly")

test = "Integer"
data = solve_template(test)
if data != ('Integer', None):
    raise Exception("Couldn't solve template properly")

if make_template(data) != test:
    raise Exception("Couldn't make template properly")

test = """Type[] generic = m.getGenericParameterTypes();
generic."""
if get_type_definition(test, test.split("\n")[-1]) != (1, 8, 'Type[]', 'generic', '.'):
    raise Exception("Couldn't get type definition")

test = """class Test
{
    protected final P1<F2<RoadNew, P2<Node, Rectangle2D.Double>, Either<Throwable, P2<Node, Rectangle2D.Double>>>> fAdd =
        new P1<F2<RoadNew, P2<Node, Rectangle2D.Double>, Either<Throwable, P2<Node, Rectangle2D.Double>>>>() {
        @Override
        public F2<RoadNew, P2<Node, Rectangle2D.Double>, Either<Throwable, P2<Node, Rectangle2D.Double>>> _1() {
                return new F2<RoadNew, P2<Node, Rectangle2D.Double>, Either<Throwable, P2<Node, Rectangle2D.Double>>>() {
                @Override
                public Either<Throwable, P2<Node, Rectangle2D.Double>> f( final RoadNew road, final P2<Node, Rectangle2D.Double> p ) {
                    if( Inclusive2DIntersectionVerifier.intersects( road, p._2() ) ) {
                        p."""
if get_type_definition(test, test.split("\n")[-1]) != (9, 130, 'P2<Node, Rectangle2D.Double>', 'p', '.'):
    raise Exception("Couldn't get the type definition")
print "all is well"
