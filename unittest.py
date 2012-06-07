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

if extract_variables(test) != [('Type&', 't1'), ('vector<Type2> &', 't2'), ('int', 'itShouldPickupThis')]:
    raise Exception("Didn't extract variables correctly")

test = """Properties prop = new Properties();
int apps = Integer.parseInt(prop."""
if get_type_definition(test) != (1, 12, "Properties", "prop", "."):
    raise Exception("Didn't get type definition properly")
test = """Properties prop = new Properties();
int apps = Integer.parseInt(prop.getProperty("a")."""
if get_type_definition(test) != (1, 12, "Properties", "prop", ".getProperty()."):
    raise Exception("Didn't get type definition properly")

if extract_completion("prop.GetColor().Clamp().") != "prop.GetColor().Clamp().":
    raise Exception("Didn't extract completion properly")

test = """DVFSStats dvfs = new DVFSStats();
DVFSStats."""
if get_type_definition(test) != (-1, -1, "DVFSStats", None, "."):
    raise Exception("Couldn't parse type definition properly")

test = """CPUStats.CPULoad cpuLoad = cpu.new CPULoad();
cpuLoad."""
if get_type_definition(test) != (1, 18, "CPUStats.CPULoad", "cpuLoad", "."):
    raise Exception("Couldn't parse type definition properly")

test = """ShortcutIconResource iconRes = Intent.ShortcutIconResource.fromContext(this, R.drawable."""
if get_type_definition(test) != (-1, -1, "R", None, ".drawable."):
    raise Exception("Couldn't parse type definition properly")

test = """Intent.FLAG_ACTIVITY_RESET_TASK_IF_NEEDED|Intent."""
if get_type_definition(test) != (-1, -1, "Intent", None, "."):
    raise Exception("Couldn't parse type definition properly")

test = """public class LaunchApp
extends Activity
{

    @Override
    public void onCreate(Bundle b)
    {
        super.onCreate(b);
        super."""
if get_type_definition(test) != (-1, -1, 'Activity', 'super', '.'):
    raise Exception("Couldn't parse type definition properly")

test = """                for (Class clazz : c.getClasses())
                {
                    clazz."""
if get_type_definition(test) != (1, 28, 'Class', 'clazz', '.'):
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

if get_type_definition(test) != (-1, -1, 'ContextFactory', 'this', '.'):
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

if get_type_definition(test) != (-1, -1, "PMQuadtree", "this", "."):
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
if get_type_definition(test) != (1, 8, "String", "args", "[]."):
    raise Exception("Couldn't parse type definition properly")

test = """                        foreach (Assembly asm in AssembliesLoaded)
                        {
                            foreach (Type t3 in asm.GetTypes())
                            {
                                if (t3."""
if get_type_definition(test) != (3, 43, "Type", "t3", "."):
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
if get_type_definition(test) != (1, 58, 'Cache*', 'cache', '->complete()->entries.'):
    raise Exception("Couldn't parse type definition properly")

test = """CacheCompletionResults* cache_complete_startswith(Cache* cache, const char *prefix)
{
    cache->complete(const char *prefix)->entries[10]->"""
if get_type_definition(test) != (1, 58, 'Cache*', 'cache', '->complete()->entries[]->'):
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
if get_type_definition(test) != (1, 8, 'Type[]', 'generic', '.'):
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
if get_type_definition(test) != (9, 130, 'P2<Node, Rectangle2D.Double>', 'p', '.'):
    raise Exception("Couldn't get the type definition")

test = """public class Tests {
    public static void main( String[] args ) {
        Foo<Foo<String, String>, String> foo = bar.f( "foo" );
        Foo<Foo<String, String>, String> foo2 = bar.f( "foo2" );
        System.out.println( foo.f( new Foo<String, String>() {
            @Override
            public String f( final String string ) {
                return string;
            }
        }) ) ; // <--- if you type a . in this code (like this: }). ); ) you'll get an error
        foo."""
if get_type_definition(test) != (3, 42, 'Foo<Foo<String, String>, String>', 'foo', '.'):
    raise Exception("Couldn't get the type definition")

if make_template((u'Foo', [('java.lang.String', None), ('java.lang.String', None)])) != "Foo<java.lang.String, java.lang.String>":
    raise Exception("Couldn't make template")


test = """public class Tests {
    public static void main( String[] args ) {
        Foo<Foo<String, String>, String> foo = bar.f( "foo" );
        Foo<Foo<String, String>, String> foo2 = bar.f( "foo2" );
        System.out.println( foo.f( new Foo<String, String>() {
            @Override
            public String f( final String string ) {
                return string;
            }
        })."""
if get_type_definition(test) != (3, 42, 'Foo<Foo<String, String>, String>', 'foo', '.f().'):
    raise Exception("Couldn't get the type definition")

test = """Foo<java.lang.String, Foo<Foo<java.lang.String, java.lang.String>, java.lang.String> >"""
if solve_template(test) != ('Foo', [('java.lang.String', None), ('Foo', [('Foo', [('java.lang.String', None), ('java.lang.String', None)]), ('java.lang.String', None)])]):
    raise Exception("Didn't solve template properly")

if make_template(solve_template(test)) != test:
    raise Exception("Didn't make template properly")

test = """Tests.Tests$Foo<java.lang.String, Tests.Tests$Foo<Tests.Tests$Foo<java.lang.String, java.lang.String>, java.lang.String> >"""
if solve_template(test) != ('Tests.Tests$Foo', [('java.lang.String', None), ('Tests.Tests$Foo', [('Tests.Tests$Foo', [('java.lang.String', None), ('java.lang.String', None)]), ('java.lang.String', None)])]):
    raise Exception("Didn't solve template properly")

if make_template(solve_template(test)) != test:
    raise Exception("Didn't make template properly")

test = """string[] argv = arg[0].Split(new string[] {sep},  StringSplitOptions.None);
            foreach (string a in argv)
            {
                argv."""
if get_type_definition(test) != (1, 10, 'string[]', 'argv', '.'):
    raise Exception("Couldn't get the type definition")

test = """        public CityNew nearestCity( final Point2D p, final PriorityQueue<P2<Node, Rectangle2D.Double>> queue ) {
            if( mPoints.isNotEmpty() ) {
                return mPoints.index( 0 );
            }
            else {
                queue."""
if get_type_definition(test) != (1, 104, 'PriorityQueue<P2<Node, Rectangle2D.Double>>', 'queue', '.'):
    raise Exception("Couldn't get the type definition")

test = """Archive<T1, T2> a;
    test = a << 8 | b << 16;
    test2 = a >> test | b >> 8;
    a."""
if get_type_definition(test) != (1, 17, 'Archive<T1, T2>', 'a', '.'):
    raise Exception("Couldn't get the type definition")

test = """Archive<T1, T2> a;
    test = a << 8 | b << 16;
    test2 = a >> test | b >> 8;
    a->"""
if get_type_definition(test) != (1, 17, 'Archive<T1, T2>', 'a', '->'):
    raise Exception("Couldn't get the type definition")

test = """import fj.*;
import fj.data.fingertrees.*;
import  java.awt.geom.Rectangle2D;
import java.util.*;

        @Override
        public CityNew nearestCity( final Point2D p, final PriorityQueue<P2<Node, Rectangle2D.Double>> queue ) {
            if( mPoints.isNotEmpty() ) {
                return mPoints.index( 0 );
            }
            else {
                queue."""
if get_type_definition(test) != (7, 104, 'PriorityQueue<P2<Node, Rectangle2D.Double>>', 'queue', '.'):
    raise Exception("Couldn't get the type definition")

test = """    private static String getInstancedType(Class<?> c, String gen, String ret, String[] templateParam)
    {
        if (gen.startsWith("class "))
            gen = gen.substring("class ".length());
        {
            this."""
if get_type_definition(test) != (-1, -1, None, 'this', '.'):
    raise Exception("Couldn't get the type definition")

test = "System.Collections.Generic.Dictionary<System.String, System.String>.ValueCollection"
if solve_template(test) != ('System.Collections.Generic.Dictionary', [('System.String', None), ('System.String', None)], ('ValueCollection', None)):
    raise Exception("Couldn't solve the template")

if make_template(solve_template(test)) != test:
    raise Exception("Couldn't make the template")

test = "std::vector<std::string>::iterator"
if solve_template(test) != ('std::vector', [('std::string', None)], ('iterator', None)):
    raise Exception("Couldn't solve the template")

if make_template(solve_template(test), "::") != test:
    raise Exception("Couldn't make the template")

test = """Dictionary<string,string>.ValueCollection t;
t."""
if get_type_definition(test) != (1, 43, 'Dictionary<string,string>.ValueCollection', 't', '.'):
    raise Exception("Couldn't get the type definition")

test = """std::vector<int>::iterator i;
i."""
if get_type_definition(test) != (1, 28, 'std::vector<int>::iterator', 'i', '.'):
    raise Exception("Couldn't get the type definition")

test = """struct hostent *server = gethostbyname("localhost");"""
if extract_variables(test) != [('struct hostent *', 'server')]:
    raise Exception("Couldn't get the type definition")

if get_base_type("struct hostent *") != "hostent":
    raise Exception("Didn't properly get the base type")

test = """
namespace arne
{
    class C
    {

        arne::
    };
    class A {};
    class B {};

}
using namespace android;
int getFrames()
{
    """
if extract_namespace(test) != None:
    raise Exception("Namespace isn't None")

if extract_used_namespaces(test) != ["android"]:
    raise Exception("Wrong namespace")

test = """
namespace one
{

    namespace two
    {
        class A {};
    }

    namespace three
    {
        class B
        {
            """
if extract_namespace(test) != "one::three":
    raise Exception("Wrong namespace")

test = """
    Parcel data, reply, moredata, test;
    int a, b, c;
    reply."""
if get_type_definition(test) != (2, 18, 'Parcel', 'reply', '.'):
    raise Exception("Couldn't get the type definition")

test = """
    Parcel data, reply, moredata, test;
    int a, b, c;
    moredata."""
if get_type_definition(test) != (2, 25, 'Parcel', 'moredata', '.'):
    raise Exception("Couldn't get the type definition")

test = """
    Parcel data, reply, moredata, test;
    int a = 1, b = 2, c = 3;
    test."""
if get_type_definition(test) != (2, 35, 'Parcel', 'test', '.'):
    raise Exception("Couldn't get the type definition")

if extract_variables(test) != [('Parcel', 'data'), ('Parcel', 'reply'), ('Parcel', 'moredata'), ('Parcel', 'test'), ('int', 'a'), ('int', 'b'), ('int', 'c')]:
    raise Exception("Couldn't extract variables properly")

test = """    NamespaceFinder(CXCursor base, const char ** ns, unsigned int nsLength)
    : mBase(base), namespaces(ns), namespaceCount(nsLength)
    {

    }
    virtual void execute()
    {

"""
if extract_variables(test) != []:
    raise Exception("Couldn't extract variables properly")

test = """void OpenGLRenderer::Render(RenderNode* node)
{
    this->"""
if get_type_definition(test) != (-1, -1, 'OpenGLRenderer', 'this', '->'):
    raise Exception("Couldn't get the type definition")

test = """    const SmartPointer<Attribute> &index = node->GetMesh()->GetAttribute(mIndexID);
    index."""
if extract_variables(test) != [('const SmartPointer<Attribute> &', 'index')]:
    raise Exception("Couldn't extract variables properly")

if get_type_definition(test) != (1, 36, 'const SmartPointer<Attribute> &', 'index', '.'):
    raise Exception("Couldn't get the type definition")

test = """void something(const SmartPointer<Attribute> &index) {
    index."""
if extract_variables(test) != [('const SmartPointer<Attribute> &', 'index')]:
    raise Exception("Couldn't extract variables properly")

if get_type_definition(test) != (1, 47, 'const SmartPointer<Attribute> &', 'index', '.'):
    raise Exception("Couldn't get the type definition")

test = """        std::vector<Entity*> t;
        t."""
if get_type_definition(test) != (1, 30, 'std::vector<Entity*>', 't', '.'):
    raise Exception("Couldn't get the type definition")

test = """Vector3 normal(0,0,0);
normal."""
if extract_variables(test) != [('Vector3', 'normal')]:
    raise Exception("Couldn't extract variables properly")

test = """Vector3 pos(camera->GetWorldTransform().getOrigin());"""
if extract_variables(test) != [('Vector3', 'pos')]:
    raise Exception("Couldn't extract variables properly")

test = """
            const Property prop = node->GetProperty(a.GetName());
            if (!prop.IsNull())
            {
                switch (prop.GetType())
                {
                    case Property::FLOAT: glUniform1f(a.GetId(), prop.GetFloat()); break;
                    case Property::RESOURCE:
                    {
                        const GLTexture *tex = (GLTexture*) prop.GetResource();"""
if extract_variables(test) != [('const Property', 'prop'), ('const GLTexture *', 'tex')]:
    raise Exception("Couldn't extract variables properly")

test = """default: int test;"""
if extract_variables(test) != [('int', 'test')]:
    raise Exception("Couldn't extract variables properly")

test = """BOOST_FOREACH(const Stacktrace* s, list)
    {
        GetAddresses(ss, s);
    }
    s."""
if get_type_definition(test) != (-1, -1, 's', None, '.'):
    raise Exception("Got a type definition when it shouldn't have")

test = """Call::Call(const char *name, Call* parent, int callDepth)
: mName(name), mOverhead(0), mTotalTime(0), mChildTime(0), mCallCount(0), mParent(parent), mCallDepth(callDepth)
{
    """
if extract_class_from_function(test) != "Call":
    raise Exception("Failed to extract class")

test = """#include <lua.hpp>
#include <jni.h>
#include <string.h>
#include <android/log.h>
#include <sys/stat.h>
#include <unistd.h>
#include <pthread.h>
#include <nv_thread/nv_thread.h>

static lua_State *L = NULL;
static char luafile[512];
static jobject thiz;
long long lastMod = 0;

static long long getModtime(const char *name)
{

    if (!access(name, R_OK))
    {
        struct stat s;
        stat(name, &s);
        return s.st_mtime;
    }
    return -1;
}

extern "C"
{
int set_line_width(lua_State *L)
{
    JNIEnv* env = NVThreadGetCurrentJNIEnv();
    env->"""
if get_type_definition(test) != (31, 13, 'JNIEnv*', 'env', '->'):
    raise Exception("Couldn't get the type definition")

if get_type_definition("C c; c[0].") != (1, 3, 'C', 'c', '[].'):
    raise Exception("Couldn't get the type definition")

if get_type_definition("tripleA[0].") != (-1, -1, "tripleA", None, "[]."):
    raise Exception("Couldn't get the type definition")

if get_type_definition("tripleA[0]->") != (-1, -1, "tripleA", None, "[]->"):
    raise Exception("Couldn't get the type definition")

if get_type_definition("tripleA[0][0].") != (-1, -1, "tripleA", None, "[][]."):
    raise Exception("Couldn't get the type definition")

if get_type_definition("tripleA[0][0]->") != (-1, -1, "tripleA", None, "[][]->"):
    raise Exception("Couldn't get the type definition")

if get_type_definition("tripleA[0][0][0].") != (-1, -1, "tripleA", None, "[][][]."):
    raise Exception("Couldn't get the type definition")

if get_type_definition("tripleA[0][0][0]->") != (-1, -1, "tripleA", None, "[][][]->"):
    raise Exception("Couldn't get the type definition")

if get_type_definition("tripleA[0][0][0][0].") != (-1, -1, "tripleA", None, "[][][][]."):
    raise Exception("Couldn't get the type definition")

if dereference("Test**") != "Test*":
    raise Exception("Couldn't dereference")
if dereference("Test*") != "Test":
    raise Exception("Couldn't dereference")

if get_base_type("mystruct") != "mystruct":
    raise Exception("Couldn't get the base type")
if get_base_type("myclass") != "myclass":
    raise Exception("Couldn't get the base type")
if get_base_type("mystatic") != "mystatic":
    raise Exception("Couldn't get the base type")
if get_base_type("struct A") != "A":
    raise Exception("Couldn't get the base type")
if get_base_type("static A") != "A":
    raise Exception("Couldn't get the base type")

test = """
typedef std::vector<something> somethingelse;
template<class blah>
void myfunc (int i )
{
}

class Test
{
public:
    """
if extract_variables(test) != []:
    raise Exception("Didn't extract variables properly")

test = """std::vector<int> a, b;"""
if extract_variables(test) != [('std::vector<int>', 'a'), ('std::vector<int>', 'b')]:
    raise Exception("Didn't extract variables properly")

if get_type_definition("struct timeval t; a+t.") != (1, 16, 'timeval', 't', '.'):
    raise Exception("Couldn't get the type definition")
if get_type_definition("struct timeval t; a|t.") != (1, 16, 'timeval', 't', '.'):
    raise Exception("Couldn't get the type definition")
if get_type_definition("struct timeval t; a-t.") != (1, 16, 'timeval', 't', '.'):
    raise Exception("Couldn't get the type definition")
if get_type_definition("struct timeval t; a*t.") != (1, 16, 'timeval', 't', '.'):
    raise Exception("Couldn't get the type definition")
if get_type_definition("struct timeval t; a/t.") != (1, 16, 'timeval', 't', '.'):
    raise Exception("Couldn't get the type definition")

test = """SwapBuffersData& data = (*i).second;
        if (++data."""
if get_type_definition(test) != (1, 18, 'SwapBuffersData&', 'data', '.'):
    raise Exception("Couldn't get the type definition")

test = """SwapBuffersData& data = (*i).second;
end.tv_usec-data."""
if get_type_definition(test) != (1, 18, 'SwapBuffersData&', 'data', '.'):
    raise Exception("Couldn't get the type definition")

if get_type_definition("[Hello ") != (-1, -1, 'Hello', None, ' '):
    raise Exception("Couldn't get the type definition")
if get_type_definition("Hello *h; [h ") != (1, 8, 'Hello *', 'h', ' '):
    raise Exception("Couldn't get the type definition")
if get_type_definition("World * w; [[w world] ") != (1, 9, 'World *', 'w', ' world] '):
    raise Exception("Couldn't get the type definition")
if get_type_definition("World2 * w; [[[w world2] world] ") != (1, 10, 'World2 *', 'w', ' world2] world] '):
    raise Exception("Couldn't get the type definition")
test = """@implementation Class1
- something
{

}
@end
@implementation Class2
@end
@implementation Class3
- samethingelse
{
"""
if extract_class(test) != "Class3":
    raise Exception("Couldn't extract the class properly")

test = """@implementation World2
- (World*) world2
{
    [self """
if get_type_definition(test) != (-1, -1, 'World2', 'self', ' '):
    raise Exception("Couldn't get the type definition")

test = """static FrameStats::Timestamp skindelta = 0;
    static int calls = 0; """
if extract_variables(test) != [('static FrameStats::Timestamp', 'skindelta'), ('static int', 'calls')]:
    raise Exception("Couldn't extract variables")
print "all is well"
