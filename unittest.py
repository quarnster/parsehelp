from parsehelp import *
import time

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

assert extract_line_at_offset(fulldata, get_offset_from_line_and_column(fulldata, 12, 4)) == "std::vector<A> v;"
assert extract_word_at_offset(fulldata, get_offset_from_line_and_column(fulldata, 84, 11)) == "tababa"
assert extract_word_at_offset(fulldata, get_offset_from_line_and_column(fulldata, 85, 5)) == "tababa"
assert extract_word_at_offset(fulldata, get_offset_from_line_and_column(fulldata, 10, 1)) == "a"
assert extract_word_at_offset(fulldata, get_offset_from_line_and_column(fulldata, 10, 2)) == ""
assert extract_word_at_offset(fulldata, get_offset_from_line_and_column(fulldata, 10, 3)) == "test"

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

assert extract_variables(test) == [('Type&', 't1'), ('vector<Type2> &', 't2'), ('int', 'itShouldPickupThis')]

test = """Properties prop = new Properties();
int apps = Integer.parseInt(prop."""
assert get_type_definition(test) == (1, 12, "Properties", "prop", ".")
test = """Properties prop = new Properties();
int apps = Integer.parseInt(prop.getProperty("a")."""
assert get_type_definition(test) == (1, 12, "Properties", "prop", ".getProperty().")

assert extract_completion("prop.GetColor().Clamp().") == "prop.GetColor().Clamp()."

test = """DVFSStats dvfs = new DVFSStats();
DVFSStats."""
assert get_type_definition(test) == (-1, -1, "DVFSStats", None, ".")

test = """CPUStats.CPULoad cpuLoad = cpu.new CPULoad();
cpuLoad."""
assert get_type_definition(test) == (1, 18, "CPUStats.CPULoad", "cpuLoad", ".")

test = """ShortcutIconResource iconRes = Intent.ShortcutIconResource.fromContext(this, R.drawable."""
assert get_type_definition(test) == (-1, -1, "R", None, ".drawable.")

test = """Intent.FLAG_ACTIVITY_RESET_TASK_IF_NEEDED|Intent."""
assert get_type_definition(test) == (-1, -1, "Intent", None, ".")

test = """public class LaunchApp
extends Activity
{

    @Override
    public void onCreate(Bundle b)
    {
        super.onCreate(b);
        super."""
assert get_type_definition(test) == (-1, -1, 'Activity', 'super', '.')

test = """                for (Class clazz : c.getClasses())
                {
                    clazz."""
assert get_type_definition(test) == (1, 28, 'Class', 'clazz', '.')


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

assert get_type_definition(test) == (-1, -1, 'ContextFactory', 'this', '.')

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

assert get_type_definition(test) == (-1, -1, "PMQuadtree", "this", ".")

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
assert get_type_definition(test) == (1, 8, "String[]", "args", "[].")

test = """                        foreach (Assembly asm in AssembliesLoaded)
                        {
                            foreach (Type t3 in asm.GetTypes())
                            {
                                if (t3."""
assert get_type_definition(test) == (3, 43, "Type", "t3", ".")

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
assert extract_variables(test) == [('int', 'argc'), ('char const *[]', 'argv'), ('MyStruct', 'a'), ('int', 'b'), ('int', 'MyStruct'), ('int', 'z'), ('int', 'q')]

assert get_base_type("static const char const *[]") == "char"

test = """CacheCompletionResults* cache_complete_startswith(Cache* cache, const char *prefix)
{
    cache->complete(const char *prefix)->entries."""
assert get_type_definition(test) == (1, 58, 'Cache*', 'cache', '->complete()->entries.')

test = """CacheCompletionResults* cache_complete_startswith(Cache* cache, const char *prefix)
{
    cache->complete(const char *prefix)->entries[10]->"""
assert get_type_definition(test) == (1, 58, 'Cache*', 'cache', '->complete()->entries[]->')

test = """bool Mesh::CopyToVBO ( UInt32 wantedChannels, VBO& vbo )
{
    std::vector<abc> test();
    {
        something here
"""
assert extract_class_from_function(test) == "Mesh"


test = """using namespace std;
using namespace std2;
using namespace some::long::namespace as s;
namespace std3
{

};

namespace std4
{"""

assert extract_namespace(test) == "std4"

assert extract_used_namespaces(test) == ['std', 'std2', 'some::long::namespace as s']

test = "ArrayList<ArrayList<Integer> >"
data = solve_template(test)
assert data == ('ArrayList', [('ArrayList', [('Integer', None)])])

assert make_template(data) == test

test = "ArrayList<Integer>"
data = solve_template(test)
assert data == ('ArrayList', [('Integer', None)])

assert make_template(data) == test

test = "Integer"
data = solve_template(test)
assert data == ('Integer', None)

assert make_template(data) == test

test = """Type[] generic = m.getGenericParameterTypes();
generic."""
assert get_type_definition(test) == (1, 8, 'Type[]', 'generic', '.')

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
assert get_type_definition(test) == (9, 130, 'P2<Node, Rectangle2D.Double>', 'p', '.')

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
assert get_type_definition(test) == (3, 42, 'Foo<Foo<String, String>, String>', 'foo', '.')

assert make_template((u'Foo', [('java.lang.String', None), ('java.lang.String', None)])) == "Foo<java.lang.String, java.lang.String>"


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
assert get_type_definition(test) == (3, 42, 'Foo<Foo<String, String>, String>', 'foo', '.f().')

test = """Foo<java.lang.String, Foo<Foo<java.lang.String, java.lang.String>, java.lang.String> >"""
assert solve_template(test) == ('Foo', [('java.lang.String', None), ('Foo', [('Foo', [('java.lang.String', None), ('java.lang.String', None)]), ('java.lang.String', None)])])

assert make_template(solve_template(test)) == test

test = """Tests.Tests$Foo<java.lang.String, Tests.Tests$Foo<Tests.Tests$Foo<java.lang.String, java.lang.String>, java.lang.String> >"""
assert solve_template(test) == ('Tests.Tests$Foo', [('java.lang.String', None), ('Tests.Tests$Foo', [('Tests.Tests$Foo', [('java.lang.String', None), ('java.lang.String', None)]), ('java.lang.String', None)])])

assert make_template(solve_template(test)) == test

test = """string[] argv = arg[0].Split(new string[] {sep},  StringSplitOptions.None);
            foreach (string a in argv)
            {
                argv."""
assert get_type_definition(test) == (1, 10, 'string[]', 'argv', '.')

test = """        public CityNew nearestCity( final Point2D p, final PriorityQueue<P2<Node, Rectangle2D.Double>> queue ) {
            if( mPoints.isNotEmpty() ) {
                return mPoints.index( 0 );
            }
            else {
                queue."""
assert get_type_definition(test) == (1, 104, 'PriorityQueue<P2<Node, Rectangle2D.Double>>', 'queue', '.')

test = """Archive<T1, T2> a;
    test = a << 8 | b << 16;
    test2 = a >> test | b >> 8;
    a."""
assert get_type_definition(test) == (1, 17, 'Archive<T1, T2>', 'a', '.')

test = """Archive<T1, T2> a;
    test = a << 8 | b << 16;
    test2 = a >> test | b >> 8;
    a->"""
assert get_type_definition(test) == (1, 17, 'Archive<T1, T2>', 'a', '->')

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
assert get_type_definition(test) == (7, 104, 'PriorityQueue<P2<Node, Rectangle2D.Double>>', 'queue', '.')

test = """    private static String getInstancedType(Class<?> c, String gen, String ret, String[] templateParam)
    {
        if (gen.startsWith("class "))
            gen = gen.substring("class ".length());
        {
            this."""
assert get_type_definition(test) == (-1, -1, None, 'this', '.')

test = "System.Collections.Generic.Dictionary<System.String, System.String>.ValueCollection"
assert solve_template(test) == ('System.Collections.Generic.Dictionary', [('System.String', None), ('System.String', None)], ('ValueCollection', None))

assert make_template(solve_template(test)) == test

test = "std::vector<std::string>::iterator"
assert solve_template(test) == ('std::vector', [('std::string', None)], ('iterator', None))

assert make_template(solve_template(test), "::") == test

test = """Dictionary<string,string>.ValueCollection t;
t."""
assert get_type_definition(test) == (1, 43, 'Dictionary<string,string>.ValueCollection', 't', '.')

test = """std::vector<int>::iterator i;
i."""
assert get_type_definition(test) == (1, 28, 'std::vector<int>::iterator', 'i', '.')

test = """struct hostent *server = gethostbyname("localhost");"""
assert extract_variables(test) == [('struct hostent *', 'server')]

assert get_base_type("struct hostent *") == "hostent"

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
assert extract_namespace(test) == None

assert extract_used_namespaces(test) == ["android"]

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
assert extract_namespace(test) == "one::three"

test = """
    Parcel data, reply, moredata, test;
    int a, b, c;
    reply."""
assert get_type_definition(test) == (2, 18, 'Parcel', 'reply', '.')

test = """
    Parcel data, reply, moredata, test;
    int a, b, c;
    moredata."""
assert get_type_definition(test) == (2, 25, 'Parcel', 'moredata', '.')

test = """
    Parcel data, reply, moredata, test;
    int a = 1, b = 2, c = 3;
    test."""
assert get_type_definition(test) == (2, 35, 'Parcel', 'test', '.')

assert extract_variables(test) == [('Parcel', 'data'), ('Parcel', 'reply'), ('Parcel', 'moredata'), ('Parcel', 'test'), ('int', 'a'), ('int', 'b'), ('int', 'c')]

test = """    NamespaceFinder(CXCursor base, const char ** ns, unsigned int nsLength)
    : mBase(base), namespaces(ns), namespaceCount(nsLength)
    {

    }
    virtual void execute()
    {

"""
assert extract_variables(test) == []

test = """void OpenGLRenderer::Render(RenderNode* node)
{
    this->"""
assert get_type_definition(test) == (-1, -1, 'OpenGLRenderer', 'this', '->')

test = """    const SmartPointer<Attribute> &index = node->GetMesh()->GetAttribute(mIndexID);
    index."""
assert extract_variables(test) == [('const SmartPointer<Attribute> &', 'index')]

assert get_type_definition(test) == (1, 36, 'const SmartPointer<Attribute> &', 'index', '.')

test = """void something(const SmartPointer<Attribute> &index) {
    index."""
assert extract_variables(test) == [('const SmartPointer<Attribute> &', 'index')]

assert get_type_definition(test) == (1, 47, 'const SmartPointer<Attribute> &', 'index', '.')

test = """        std::vector<Entity*> t;
        t."""
assert get_type_definition(test) == (1, 30, 'std::vector<Entity*>', 't', '.')

test = """Vector3 normal(0,0,0);
normal."""
assert extract_variables(test) == [('Vector3', 'normal')]

test = """Vector3 pos(camera->GetWorldTransform().getOrigin());"""
assert extract_variables(test) == [('Vector3', 'pos')]

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
assert extract_variables(test) == [('const Property', 'prop'), ('const GLTexture *', 'tex')]

test = """default: int test;"""
assert extract_variables(test) == [('int', 'test')]

test = """BOOST_FOREACH(const Stacktrace* s, list)
    {
        GetAddresses(ss, s);
    }
    s."""
assert get_type_definition(test) == (-1, -1, 's', None, '.')

test = """Call::Call(const char *name, Call* parent, int callDepth)
: mName(name), mOverhead(0), mTotalTime(0), mChildTime(0), mCallCount(0), mParent(parent), mCallDepth(callDepth)
{
    """
assert extract_class_from_function(test) == "Call"

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
assert get_type_definition(test) == (31, 13, 'JNIEnv*', 'env', '->')

assert get_type_definition("C c; c[0].") == (1, 3, 'C', 'c', '[].')

assert get_type_definition("tripleA[0].") == (-1, -1, "tripleA", None, "[].")

assert get_type_definition("tripleA[0]->") == (-1, -1, "tripleA", None, "[]->")

assert get_type_definition("tripleA[0][0].") == (-1, -1, "tripleA", None, "[][].")

assert get_type_definition("tripleA[0][0]->") == (-1, -1, "tripleA", None, "[][]->")

assert get_type_definition("tripleA[0][0][0].") == (-1, -1, "tripleA", None, "[][][].")

assert get_type_definition("tripleA[0][0][0]->") == (-1, -1, "tripleA", None, "[][][]->")

assert get_type_definition("tripleA[0][0][0][0].") == (-1, -1, "tripleA", None, "[][][][].")

assert dereference("Test**") == "Test*"
assert dereference("Test*") == "Test"

assert get_base_type("mystruct") == "mystruct"
assert get_base_type("myclass") == "myclass"
assert get_base_type("mystatic") == "mystatic"
assert get_base_type("struct A") == "A"
assert get_base_type("static A") == "A"

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
assert extract_variables(test) == []

test = """std::vector<int> a, b;"""
assert extract_variables(test) == [('std::vector<int>', 'a'), ('std::vector<int>', 'b')]

assert get_type_definition("struct timeval t; a+t.") == (1, 16, 'timeval', 't', '.')
assert get_type_definition("struct timeval t; a|t.") == (1, 16, 'timeval', 't', '.')
assert get_type_definition("struct timeval t; a-t.") == (1, 16, 'timeval', 't', '.')
assert get_type_definition("struct timeval t; a*t.") == (1, 16, 'timeval', 't', '.')
assert get_type_definition("struct timeval t; a/t.") == (1, 16, 'timeval', 't', '.')

test = """SwapBuffersData& data = (*i).second;
        if (++data."""
assert get_type_definition(test) == (1, 18, 'SwapBuffersData&', 'data', '.')

test = """SwapBuffersData& data = (*i).second;
end.tv_usec-data."""
assert get_type_definition(test) == (1, 18, 'SwapBuffersData&', 'data', '.')

assert get_type_definition("[Hello ") == (-1, -1, 'Hello', None, ' ')
assert get_type_definition("Hello *h; [h ") == (1, 8, 'Hello *', 'h', ' ')
assert get_type_definition("World * w; [[w world] ") == (1, 9, 'World *', 'w', ' world] ')
assert get_type_definition("World2 * w; [[[w world2] world] ") == (1, 10, 'World2 *', 'w', ' world2] world] ')
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
assert extract_class(test) == "Class3"

test = """@implementation World2
- (World*) world2
{
    [self """
assert get_type_definition(test) == (-1, -1, 'World2', 'self', ' ')

test = """static FrameStats::Timestamp skindelta = 0;
    static int calls = 0; """
assert extract_variables(test) == [('static FrameStats::Timestamp', 'skindelta'), ('static int', 'calls')]

assert get_type_definition("""Test.GetSomething2<string, int, int, int>(a, b, c).""") == (-1, -1, 'Test', None, '.GetSomething2<string, int, int, int>().')

assert get_type_definition("Test t[10]; t[0].") == (1, 6, 'Test[]', 't', '[].')

assert get_type_definition("Test t[10][20]; t.") == (1, 6, 'Test[][]', 't', '.')

test = """struct mystruct {float x; float y; float z;} m;
typedef struct {float a; float b; float c; } mystruct2;

enum myenum
{
    I1,
    I2,
    I3
};

class A
{
public:
    enum
    {
        E1,
        E2,
        E3
    };

    union
    {
        float f;
        int i;
    };
    mystruct2 ms;
};


static int variable;
class MyStaticClass
{
public:
    static int publicStaticField;
    int publicField;
protected:
    static int protectedStaticField;
    int protectedField;
private:
    static int privateStaticField;
    int privateField;
};

class Child : public MyStaticClass
{

};
"""
assert extract_variables(test) == [('struct mystruct', 'm'), ('enum', 'myenum'), ('static int', 'variable')]

assert get_type_definition("nms::function().") == (-1, -1, "nms", None, "::function().")

test = """private static String[] getCompletion() {} String."""
assert get_type_definition(test) == (-1, -1, 'String', None, '.')

test = """  URL url = classLoader.getResource(s + "/" + packageName);
            if (url != null)
                return true;
            else
                url = classLoader.getResource(s);
            url."""
assert get_type_definition(test) == (1, 7, 'URL', 'url', '.')

test = """case kSomethingSomethingSomething:
            break;
        case kSomethingSomethingSomt"""
start = time.time()
assert extract_variables(test) == []
end = time.time() - start
if end > 0.01:
    raise Exception("Test didn't finish in time")

assert extract_namespace("void Test::Class::function() {") == "Test"

test = """namespace lir
{
    #define NO_ARGUMENT lir::b()

    class a
    {
        bool operator==(const a &other) const
        {
            other."""
assert extract_class_from_function(test) == None
test = """Test t[1]; t[0]."""
assert get_type_definition(test) == (1, 6, 'Test[]', 't', '[].')

test = """typedef struct
{
    int something;
} Test;
Test t[1]; t[0]."""
assert get_type_definition(test) == (5, 6, 'Test[]', 't', '[].')

assert extract_variables("char foo[LENGTH];") == [('char[]', 'foo')]
assert get_type_definition("Test t; [t.context ") == (1, 6, 'Test', 't', '.context ')
assert get_type_definition("Test t; [t.context->b ") == (1, 6, 'Test', 't', '.context->b ')
assert get_type_definition("Test t; [[t.context->b something] ") == (1, 6, 'Test', 't', '.context->b something] ')
assert get_type_definition("Test t; [[t.context->b something] something2]->") == (1, 6, 'Test', 't', '.context->b something] something2]->')
assert get_type_definition("Test t; [[t.context->b something] something2].") == (1, 6, 'Test', 't', '.context->b something] something2].')

print "all is well"
