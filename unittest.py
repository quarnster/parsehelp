from parsehelp import *
import time

def myassert(a, b):
    if a != b:
        print "============================================"
        print a
        print "++++++++++++++++++++++++++++++++++++++++++++"
        print b
        print "--------------------------------------------"
    assert a == b

f = open("unittest.cpp")
fulldata = f.read()
f.close()

__start = time.time()

gold_results = [
    (0, 1, 1, 0, '#', '#include <vector>', ''),
    (1, 1, 2, 1, '#i', '#include <vector>', 'include'),
    (2, 1, 3, 2, '#in', '#include <vector>', 'include'),
    (3, 1, 4, 3, '#inc', '#include <vector>', 'include'),
    (4, 1, 5, 4, '#incl', '#include <vector>', 'include'),
    (5, 1, 6, 5, '#inclu', '#include <vector>', 'include'),
    (6, 1, 7, 6, '#includ', '#include <vector>', 'include'),
    (7, 1, 8, 7, '#include', '#include <vector>', 'include'),
    (8, 1, 9, 8, '#include ', '#include <vector>', ''),
    (9, 1, 10, 9, '#include <', '#include <vector>', ''),
    (10, 1, 11, 10, '#include <v', '#include <vector>', 'vector'),
    (11, 1, 12, 11, '#include <ve', '#include <vector>', 'vector'),
    (12, 1, 13, 12, '#include <vec', '#include <vector>', 'vector'),
    (13, 1, 14, 13, '#include <vect', '#include <vector>', 'vector'),
    (14, 1, 15, 14, '#include <vecto', '#include <vector>', 'vector'),
    (15, 1, 16, 15, '#include <vector', '#include <vector>', 'vector'),
    (16, 1, 17, 16, '#include <vector>', '#include <vector>', ''),
    (17, 1, 18, 17, '', '', ''),
    (18, 2, 1, 18, '', '', ''),
    (19, 3, 1, 19, 'c', 'class A', 'class'),
    (20, 3, 2, 20, 'cl', 'class A', 'class'),
    (21, 3, 3, 21, 'cla', 'class A', 'class'),
    (22, 3, 4, 22, 'clas', 'class A', 'class'),
    (23, 3, 5, 23, 'class', 'class A', 'class'),
    (24, 3, 6, 24, 'class ', 'class A', ''),
    (25, 3, 7, 25, 'class A', 'class A', 'A'),
    (26, 3, 8, 26, '', '', ''),
    (27, 4, 1, 27, '{', '{', ''),
    (28, 4, 2, 28, '', '', ''),
    (29, 5, 1, 29, 'p', 'public:', 'public'),
    (30, 5, 2, 30, 'pu', 'public:', 'public'),
    (31, 5, 3, 31, 'pub', 'public:', 'public'),
    (32, 5, 4, 32, 'publ', 'public:', 'public'),
    (33, 5, 5, 33, 'publi', 'public:', 'public'),
    (34, 5, 6, 34, 'public', 'public:', 'public'),
    (35, 5, 7, 35, 'public:', 'public:', ''),
    (36, 5, 8, 36, '', '', ''),
    (37, 6, 1, 37, ' ', '    int test;', ''),
    (38, 6, 2, 38, '  ', '    int test;', ''),
    (39, 6, 3, 39, '   ', '    int test;', ''),
    (40, 6, 4, 40, '    ', '    int test;', ''),
    (41, 6, 5, 41, '    i', '    int test;', 'int'),
    (42, 6, 6, 42, '    in', '    int test;', 'int'),
    (43, 6, 7, 43, '    int', '    int test;', 'int'),
    (44, 6, 8, 44, '    int ', '    int test;', ''),
    (45, 6, 9, 45, '    int t', '    int test;', 'test'),
    (46, 6, 10, 46, '    int te', '    int test;', 'test'),
    (47, 6, 11, 47, '    int tes', '    int test;', 'test'),
    (48, 6, 12, 48, '    int test', '    int test;', 'test'),
    (49, 6, 13, 49, '    int test;', '    int test;', ''),
    (50, 6, 14, 50, '', '', ''),
    (51, 7, 1, 51, '}', '};', ''),
    (52, 7, 2, 52, '};', '};', ''),
    (53, 7, 3, 53, '', '', ''),
    (54, 8, 1, 54, '', '', ''),
    (55, 9, 1, 55, 'A', 'A a;', 'A'),
    (56, 9, 2, 56, 'A ', 'A a;', ''),
    (57, 9, 3, 57, 'A a', 'A a;', 'a'),
    (58, 9, 4, 58, 'A a;', 'A a;', ''),
    (59, 9, 5, 59, '', '', ''),
    (60, 10, 1, 60, 'a', 'a.test;', 'a'),
    (61, 10, 2, 61, 'a.', 'a.test;', ''),
    (62, 10, 3, 62, 'a.t', 'a.test;', 'test'),
    (63, 10, 4, 63, 'a.te', 'a.test;', 'test'),
    (64, 10, 5, 64, 'a.tes', 'a.test;', 'test'),
    (65, 10, 6, 65, 'a.test', 'a.test;', 'test'),
    (66, 10, 7, 66, 'a.test;', 'a.test;', ''),
    (67, 10, 8, 67, '', '', ''),
    (68, 11, 1, 68, '', '', ''),
    (69, 12, 1, 69, 's', 'std::vector<A> v;', 'std'),
    (70, 12, 2, 70, 'st', 'std::vector<A> v;', 'std'),
    (71, 12, 3, 71, 'std', 'std::vector<A> v;', 'std'),
    (72, 12, 4, 72, 'std:', 'std::vector<A> v;', ''),
    (73, 12, 5, 73, 'std::', 'std::vector<A> v;', ''),
    (74, 12, 6, 74, 'std::v', 'std::vector<A> v;', 'vector'),
    (75, 12, 7, 75, 'std::ve', 'std::vector<A> v;', 'vector'),
    (76, 12, 8, 76, 'std::vec', 'std::vector<A> v;', 'vector'),
    (77, 12, 9, 77, 'std::vect', 'std::vector<A> v;', 'vector'),
    (78, 12, 10, 78, 'std::vecto', 'std::vector<A> v;', 'vector'),
    (79, 12, 11, 79, 'std::vector', 'std::vector<A> v;', 'vector'),
    (80, 12, 12, 80, 'std::vector<', 'std::vector<A> v;', ''),
    (81, 12, 13, 81, 'std::vector<A', 'std::vector<A> v;', 'A'),
    (82, 12, 14, 82, 'std::vector<A>', 'std::vector<A> v;', ''),
    (83, 12, 15, 83, 'std::vector<A> ', 'std::vector<A> v;', ''),
    (84, 12, 16, 84, 'std::vector<A> v', 'std::vector<A> v;', 'v'),
    (85, 12, 17, 85, 'std::vector<A> v;', 'std::vector<A> v;', ''),
    (86, 12, 18, 86, '', '', ''),
    (87, 13, 1, 87, '', '', ''),
    (88, 14, 1, 88, 'v', 'v.front().test;', 'v'),
    (89, 14, 2, 89, 'v.', 'v.front().test;', ''),
    (90, 14, 3, 90, 'v.f', 'v.front().test;', 'front'),
    (91, 14, 4, 91, 'v.fr', 'v.front().test;', 'front'),
    (92, 14, 5, 92, 'v.fro', 'v.front().test;', 'front'),
    (93, 14, 6, 93, 'v.fron', 'v.front().test;', 'front'),
    (94, 14, 7, 94, 'v.front', 'v.front().test;', 'front'),
    (95, 14, 8, 95, 'v.front(', 'v.front().test;', ''),
    (96, 14, 9, 96, 'v.front()', 'v.front().test;', ''),
    (97, 14, 10, 97, 'v.front().', 'v.front().test;', ''),
    (98, 14, 11, 98, 'v.front().t', 'v.front().test;', 'test'),
    (99, 14, 12, 99, 'v.front().te', 'v.front().test;', 'test'),
    (100, 14, 13, 100, 'v.front().tes', 'v.front().test;', 'test'),
    (101, 14, 14, 101, 'v.front().test', 'v.front().test;', 'test'),
    (102, 14, 15, 102, 'v.front().test;', 'v.front().test;', ''),
    (103, 14, 16, 103, '', '', ''),
    (104, 15, 1, 104, '', '', ''),
    (105, 16, 1, 105, '', '', ''),
    (106, 17, 1, 106, 't', 'typedef std::vector<A> AV;', 'typedef'),
    (107, 17, 2, 107, 'ty', 'typedef std::vector<A> AV;', 'typedef'),
    (108, 17, 3, 108, 'typ', 'typedef std::vector<A> AV;', 'typedef'),
    (109, 17, 4, 109, 'type', 'typedef std::vector<A> AV;', 'typedef'),
    (110, 17, 5, 110, 'typed', 'typedef std::vector<A> AV;', 'typedef'),
    (111, 17, 6, 111, 'typede', 'typedef std::vector<A> AV;', 'typedef'),
    (112, 17, 7, 112, 'typedef', 'typedef std::vector<A> AV;', 'typedef'),
    (113, 17, 8, 113, 'typedef ', 'typedef std::vector<A> AV;', ''),
    (114, 17, 9, 114, 'typedef s', 'typedef std::vector<A> AV;', 'std'),
    (115, 17, 10, 115, 'typedef st', 'typedef std::vector<A> AV;', 'std'),
    (116, 17, 11, 116, 'typedef std', 'typedef std::vector<A> AV;', 'std'),
    (117, 17, 12, 117, 'typedef std:', 'typedef std::vector<A> AV;', ''),
    (118, 17, 13, 118, 'typedef std::', 'typedef std::vector<A> AV;', ''),
    (119, 17, 14, 119, 'typedef std::v', 'typedef std::vector<A> AV;', 'vector'),
    (120, 17, 15, 120, 'typedef std::ve', 'typedef std::vector<A> AV;', 'vector'),
    (121, 17, 16, 121, 'typedef std::vec', 'typedef std::vector<A> AV;', 'vector'),
    (122, 17, 17, 122, 'typedef std::vect', 'typedef std::vector<A> AV;', 'vector'),
    (123, 17, 18, 123, 'typedef std::vecto', 'typedef std::vector<A> AV;', 'vector'),
    (124, 17, 19, 124, 'typedef std::vector', 'typedef std::vector<A> AV;', 'vector'),
    (125, 17, 20, 125, 'typedef std::vector<', 'typedef std::vector<A> AV;', ''),
    (126, 17, 21, 126, 'typedef std::vector<A', 'typedef std::vector<A> AV;', 'A'),
    (127, 17, 22, 127, 'typedef std::vector<A>', 'typedef std::vector<A> AV;', ''),
    (128, 17, 23, 128, 'typedef std::vector<A> ', 'typedef std::vector<A> AV;', ''),
    (129, 17, 24, 129, 'typedef std::vector<A> A', 'typedef std::vector<A> AV;', 'AV'),
    (130, 17, 25, 130, 'typedef std::vector<A> AV', 'typedef std::vector<A> AV;', 'AV'),
    (131, 17, 26, 131, 'typedef std::vector<A> AV;', 'typedef std::vector<A> AV;', ''),
    (132, 17, 27, 132, '', '', ''),
    (133, 18, 1, 133, '', '', ''),
    (134, 19, 1, 134, 'A', 'AV av;', 'AV'),
    (135, 19, 2, 135, 'AV', 'AV av;', 'AV'),
    (136, 19, 3, 136, 'AV ', 'AV av;', ''),
    (137, 19, 4, 137, 'AV a', 'AV av;', 'av'),
    (138, 19, 5, 138, 'AV av', 'AV av;', 'av'),
    (139, 19, 6, 139, 'AV av;', 'AV av;', ''),
    (140, 19, 7, 140, '', '', ''),
    (141, 20, 1, 141, 'a', 'av.front().test;', 'av'),
    (142, 20, 2, 142, 'av', 'av.front().test;', 'av'),
    (143, 20, 3, 143, 'av.', 'av.front().test;', ''),
    (144, 20, 4, 144, 'av.f', 'av.front().test;', 'front'),
    (145, 20, 5, 145, 'av.fr', 'av.front().test;', 'front'),
    (146, 20, 6, 146, 'av.fro', 'av.front().test;', 'front'),
    (147, 20, 7, 147, 'av.fron', 'av.front().test;', 'front'),
    (148, 20, 8, 148, 'av.front', 'av.front().test;', 'front'),
    (149, 20, 9, 149, 'av.front(', 'av.front().test;', ''),
    (150, 20, 10, 150, 'av.front()', 'av.front().test;', ''),
    (151, 20, 11, 151, 'av.front().', 'av.front().test;', ''),
    (152, 20, 12, 152, 'av.front().t', 'av.front().test;', 'test'),
    (153, 20, 13, 153, 'av.front().te', 'av.front().test;', 'test'),
    (154, 20, 14, 154, 'av.front().tes', 'av.front().test;', 'test'),
    (155, 20, 15, 155, 'av.front().test', 'av.front().test;', 'test'),
    (156, 20, 16, 156, 'av.front().test;', 'av.front().test;', ''),
    (157, 20, 17, 157, '', '', ''),
    (158, 21, 1, 158, '', '', ''),
    (159, 22, 1, 159, 'c', 'class B', 'class'),
    (160, 22, 2, 160, 'cl', 'class B', 'class'),
    (161, 22, 3, 161, 'cla', 'class B', 'class'),
    (162, 22, 4, 162, 'clas', 'class B', 'class'),
    (163, 22, 5, 163, 'class', 'class B', 'class'),
    (164, 22, 6, 164, 'class ', 'class B', ''),
    (165, 22, 7, 165, 'class B', 'class B', 'B'),
    (166, 22, 8, 166, '', '', ''),
    (167, 23, 1, 167, '{', '{', ''),
    (168, 23, 2, 168, '', '', ''),
    (169, 24, 1, 169, 'p', 'public:', 'public'),
    (170, 24, 2, 170, 'pu', 'public:', 'public'),
    (171, 24, 3, 171, 'pub', 'public:', 'public'),
    (172, 24, 4, 172, 'publ', 'public:', 'public'),
    (173, 24, 5, 173, 'publi', 'public:', 'public'),
    (174, 24, 6, 174, 'public', 'public:', 'public'),
    (175, 24, 7, 175, 'public:', 'public:', ''),
    (176, 24, 8, 176, '', '', ''),
    (177, 25, 1, 177, ' ', '    AV variable;', ''),
    (178, 25, 2, 178, '  ', '    AV variable;', ''),
    (179, 25, 3, 179, '   ', '    AV variable;', ''),
    (180, 25, 4, 180, '    ', '    AV variable;', ''),
    (181, 25, 5, 181, '    A', '    AV variable;', 'AV'),
    (182, 25, 6, 182, '    AV', '    AV variable;', 'AV'),
    (183, 25, 7, 183, '    AV ', '    AV variable;', ''),
    (184, 25, 8, 184, '    AV v', '    AV variable;', 'variable'),
    (185, 25, 9, 185, '    AV va', '    AV variable;', 'variable'),
    (186, 25, 10, 186, '    AV var', '    AV variable;', 'variable'),
    (187, 25, 11, 187, '    AV vari', '    AV variable;', 'variable'),
    (188, 25, 12, 188, '    AV varia', '    AV variable;', 'variable'),
    (189, 25, 13, 189, '    AV variab', '    AV variable;', 'variable'),
    (190, 25, 14, 190, '    AV variabl', '    AV variable;', 'variable'),
    (191, 25, 15, 191, '    AV variable', '    AV variable;', 'variable'),
    (192, 25, 16, 192, '    AV variable;', '    AV variable;', ''),
    (193, 25, 17, 193, '', '', ''),
    (194, 26, 1, 194, '', '', ''),
    (195, 27, 1, 195, ' ', '    std::vector<A> variable2;', ''),
    (196, 27, 2, 196, '  ', '    std::vector<A> variable2;', ''),
    (197, 27, 3, 197, '   ', '    std::vector<A> variable2;', ''),
    (198, 27, 4, 198, '    ', '    std::vector<A> variable2;', ''),
    (199, 27, 5, 199, '    s', '    std::vector<A> variable2;', 'std'),
    (200, 27, 6, 200, '    st', '    std::vector<A> variable2;', 'std'),
    (201, 27, 7, 201, '    std', '    std::vector<A> variable2;', 'std'),
    (202, 27, 8, 202, '    std:', '    std::vector<A> variable2;', ''),
    (203, 27, 9, 203, '    std::', '    std::vector<A> variable2;', ''),
    (204, 27, 10, 204, '    std::v', '    std::vector<A> variable2;', 'vector'),
    (205, 27, 11, 205, '    std::ve', '    std::vector<A> variable2;', 'vector'),
    (206, 27, 12, 206, '    std::vec', '    std::vector<A> variable2;', 'vector'),
    (207, 27, 13, 207, '    std::vect', '    std::vector<A> variable2;', 'vector'),
    (208, 27, 14, 208, '    std::vecto', '    std::vector<A> variable2;', 'vector'),
    (209, 27, 15, 209, '    std::vector', '    std::vector<A> variable2;', 'vector'),
    (210, 27, 16, 210, '    std::vector<', '    std::vector<A> variable2;', ''),
    (211, 27, 17, 211, '    std::vector<A', '    std::vector<A> variable2;', 'A'),
    (212, 27, 18, 212, '    std::vector<A>', '    std::vector<A> variable2;', ''),
    (213, 27, 19, 213, '    std::vector<A> ', '    std::vector<A> variable2;', ''),
    (214, 27, 20, 214, '    std::vector<A> v', '    std::vector<A> variable2;', 'variable2'),
    (215, 27, 21, 215, '    std::vector<A> va', '    std::vector<A> variable2;', 'variable2'),
    (216, 27, 22, 216, '    std::vector<A> var', '    std::vector<A> variable2;', 'variable2'),
    (217, 27, 23, 217, '    std::vector<A> vari', '    std::vector<A> variable2;', 'variable2'),
    (218, 27, 24, 218, '    std::vector<A> varia', '    std::vector<A> variable2;', 'variable2'),
    (219, 27, 25, 219, '    std::vector<A> variab', '    std::vector<A> variable2;', 'variable2'),
    (220, 27, 26, 220, '    std::vector<A> variabl', '    std::vector<A> variable2;', 'variable2'),
    (221, 27, 27, 221, '    std::vector<A> variable', '    std::vector<A> variable2;', 'variable2'),
    (222, 27, 28, 222, '    std::vector<A> variable2', '    std::vector<A> variable2;', 'variable2'),
    (223, 27, 29, 223, '    std::vector<A> variable2;', '    std::vector<A> variable2;', ''),
    (224, 27, 30, 224, '', '', ''),
    (225, 28, 1, 225, '}', '};', ''),
    (226, 28, 2, 226, '};', '};', ''),
    (227, 28, 3, 227, '', '', ''),
    (228, 29, 1, 228, '', '', ''),
    (229, 30, 1, 229, 'B', 'B b;', 'B'),
    (230, 30, 2, 230, 'B ', 'B b;', ''),
    (231, 30, 3, 231, 'B b', 'B b;', 'b'),
    (232, 30, 4, 232, 'B b;', 'B b;', ''),
    (233, 30, 5, 233, '', '', ''),
    (234, 31, 1, 234, 'b', 'b.variable.front().test;', 'b'),
    (235, 31, 2, 235, 'b.', 'b.variable.front().test;', ''),
    (236, 31, 3, 236, 'b.v', 'b.variable.front().test;', 'variable'),
    (237, 31, 4, 237, 'b.va', 'b.variable.front().test;', 'variable'),
    (238, 31, 5, 238, 'b.var', 'b.variable.front().test;', 'variable'),
    (239, 31, 6, 239, 'b.vari', 'b.variable.front().test;', 'variable'),
    (240, 31, 7, 240, 'b.varia', 'b.variable.front().test;', 'variable'),
    (241, 31, 8, 241, 'b.variab', 'b.variable.front().test;', 'variable'),
    (242, 31, 9, 242, 'b.variabl', 'b.variable.front().test;', 'variable'),
    (243, 31, 10, 243, 'b.variable', 'b.variable.front().test;', 'variable'),
    (244, 31, 11, 244, 'b.variable.', 'b.variable.front().test;', ''),
    (245, 31, 12, 245, 'b.variable.f', 'b.variable.front().test;', 'front'),
    (246, 31, 13, 246, 'b.variable.fr', 'b.variable.front().test;', 'front'),
    (247, 31, 14, 247, 'b.variable.fro', 'b.variable.front().test;', 'front'),
    (248, 31, 15, 248, 'b.variable.fron', 'b.variable.front().test;', 'front'),
    (249, 31, 16, 249, 'b.variable.front', 'b.variable.front().test;', 'front'),
    (250, 31, 17, 250, 'b.variable.front(', 'b.variable.front().test;', ''),
    (251, 31, 18, 251, 'b.variable.front()', 'b.variable.front().test;', ''),
    (252, 31, 19, 252, 'b.variable.front().', 'b.variable.front().test;', ''),
    (253, 31, 20, 253, 'b.variable.front().t', 'b.variable.front().test;', 'test'),
    (254, 31, 21, 254, 'b.variable.front().te', 'b.variable.front().test;', 'test'),
    (255, 31, 22, 255, 'b.variable.front().tes', 'b.variable.front().test;', 'test'),
    (256, 31, 23, 256, 'b.variable.front().test', 'b.variable.front().test;', 'test'),
    (257, 31, 24, 257, 'b.variable.front().test;', 'b.variable.front().test;', ''),
    (258, 31, 25, 258, '', '', ''),
    (259, 32, 1, 259, 'b', 'b.variable2.front().test;', 'b'),
    (260, 32, 2, 260, 'b.', 'b.variable2.front().test;', ''),
    (261, 32, 3, 261, 'b.v', 'b.variable2.front().test;', 'variable2'),
    (262, 32, 4, 262, 'b.va', 'b.variable2.front().test;', 'variable2'),
    (263, 32, 5, 263, 'b.var', 'b.variable2.front().test;', 'variable2'),
    (264, 32, 6, 264, 'b.vari', 'b.variable2.front().test;', 'variable2'),
    (265, 32, 7, 265, 'b.varia', 'b.variable2.front().test;', 'variable2'),
    (266, 32, 8, 266, 'b.variab', 'b.variable2.front().test;', 'variable2'),
    (267, 32, 9, 267, 'b.variabl', 'b.variable2.front().test;', 'variable2'),
    (268, 32, 10, 268, 'b.variable', 'b.variable2.front().test;', 'variable2'),
    (269, 32, 11, 269, 'b.variable2', 'b.variable2.front().test;', 'variable2'),
    (270, 32, 12, 270, 'b.variable2.', 'b.variable2.front().test;', ''),
    (271, 32, 13, 271, 'b.variable2.f', 'b.variable2.front().test;', 'front'),
    (272, 32, 14, 272, 'b.variable2.fr', 'b.variable2.front().test;', 'front'),
    (273, 32, 15, 273, 'b.variable2.fro', 'b.variable2.front().test;', 'front'),
    (274, 32, 16, 274, 'b.variable2.fron', 'b.variable2.front().test;', 'front'),
    (275, 32, 17, 275, 'b.variable2.front', 'b.variable2.front().test;', 'front'),
    (276, 32, 18, 276, 'b.variable2.front(', 'b.variable2.front().test;', ''),
    (277, 32, 19, 277, 'b.variable2.front()', 'b.variable2.front().test;', ''),
    (278, 32, 20, 278, 'b.variable2.front().', 'b.variable2.front().test;', ''),
    (279, 32, 21, 279, 'b.variable2.front().t', 'b.variable2.front().test;', 'test'),
    (280, 32, 22, 280, 'b.variable2.front().te', 'b.variable2.front().test;', 'test'),
    (281, 32, 23, 281, 'b.variable2.front().tes', 'b.variable2.front().test;', 'test'),
    (282, 32, 24, 282, 'b.variable2.front().test', 'b.variable2.front().test;', 'test'),
    (283, 32, 25, 283, 'b.variable2.front().test;', 'b.variable2.front().test;', ''),
    (284, 32, 26, 284, '', '', ''),
    (285, 33, 1, 285, '', '', ''),
    (286, 34, 1, 286, '', '', ''),
    (287, 35, 1, 287, 'c', 'class B2', 'class'),
    (288, 35, 2, 288, 'cl', 'class B2', 'class'),
    (289, 35, 3, 289, 'cla', 'class B2', 'class'),
    (290, 35, 4, 290, 'clas', 'class B2', 'class'),
    (291, 35, 5, 291, 'class', 'class B2', 'class'),
    (292, 35, 6, 292, 'class ', 'class B2', ''),
    (293, 35, 7, 293, 'class B', 'class B2', 'B2'),
    (294, 35, 8, 294, 'class B2', 'class B2', 'B2'),
    (295, 35, 9, 295, '', '', ''),
    (296, 36, 1, 296, '{', '{', ''),
    (297, 36, 2, 297, '', '', ''),
    (298, 37, 1, 298, 'p', 'public:', 'public'),
    (299, 37, 2, 299, 'pu', 'public:', 'public'),
    (300, 37, 3, 300, 'pub', 'public:', 'public'),
    (301, 37, 4, 301, 'publ', 'public:', 'public'),
    (302, 37, 5, 302, 'publi', 'public:', 'public'),
    (303, 37, 6, 303, 'public', 'public:', 'public'),
    (304, 37, 7, 304, 'public:', 'public:', ''),
    (305, 37, 8, 305, '', '', ''),
    (306, 38, 1, 306, ' ', '    std::vector<AV> variable;', ''),
    (307, 38, 2, 307, '  ', '    std::vector<AV> variable;', ''),
    (308, 38, 3, 308, '   ', '    std::vector<AV> variable;', ''),
    (309, 38, 4, 309, '    ', '    std::vector<AV> variable;', ''),
    (310, 38, 5, 310, '    s', '    std::vector<AV> variable;', 'std'),
    (311, 38, 6, 311, '    st', '    std::vector<AV> variable;', 'std'),
    (312, 38, 7, 312, '    std', '    std::vector<AV> variable;', 'std'),
    (313, 38, 8, 313, '    std:', '    std::vector<AV> variable;', ''),
    (314, 38, 9, 314, '    std::', '    std::vector<AV> variable;', ''),
    (315, 38, 10, 315, '    std::v', '    std::vector<AV> variable;', 'vector'),
    (316, 38, 11, 316, '    std::ve', '    std::vector<AV> variable;', 'vector'),
    (317, 38, 12, 317, '    std::vec', '    std::vector<AV> variable;', 'vector'),
    (318, 38, 13, 318, '    std::vect', '    std::vector<AV> variable;', 'vector'),
    (319, 38, 14, 319, '    std::vecto', '    std::vector<AV> variable;', 'vector'),
    (320, 38, 15, 320, '    std::vector', '    std::vector<AV> variable;', 'vector'),
    (321, 38, 16, 321, '    std::vector<', '    std::vector<AV> variable;', ''),
    (322, 38, 17, 322, '    std::vector<A', '    std::vector<AV> variable;', 'AV'),
    (323, 38, 18, 323, '    std::vector<AV', '    std::vector<AV> variable;', 'AV'),
    (324, 38, 19, 324, '    std::vector<AV>', '    std::vector<AV> variable;', ''),
    (325, 38, 20, 325, '    std::vector<AV> ', '    std::vector<AV> variable;', ''),
    (326, 38, 21, 326, '    std::vector<AV> v', '    std::vector<AV> variable;', 'variable'),
    (327, 38, 22, 327, '    std::vector<AV> va', '    std::vector<AV> variable;', 'variable'),
    (328, 38, 23, 328, '    std::vector<AV> var', '    std::vector<AV> variable;', 'variable'),
    (329, 38, 24, 329, '    std::vector<AV> vari', '    std::vector<AV> variable;', 'variable'),
    (330, 38, 25, 330, '    std::vector<AV> varia', '    std::vector<AV> variable;', 'variable'),
    (331, 38, 26, 331, '    std::vector<AV> variab', '    std::vector<AV> variable;', 'variable'),
    (332, 38, 27, 332, '    std::vector<AV> variabl', '    std::vector<AV> variable;', 'variable'),
    (333, 38, 28, 333, '    std::vector<AV> variable', '    std::vector<AV> variable;', 'variable'),
    (334, 38, 29, 334, '    std::vector<AV> variable;', '    std::vector<AV> variable;', ''),
    (335, 38, 30, 335, '', '', ''),
    (336, 39, 1, 336, ' ', '    std::vector<std::vector<A> > variable2;', ''),
    (337, 39, 2, 337, '  ', '    std::vector<std::vector<A> > variable2;', ''),
    (338, 39, 3, 338, '   ', '    std::vector<std::vector<A> > variable2;', ''),
    (339, 39, 4, 339, '    ', '    std::vector<std::vector<A> > variable2;', ''),
    (340, 39, 5, 340, '    s', '    std::vector<std::vector<A> > variable2;', 'std'),
    (341, 39, 6, 341, '    st', '    std::vector<std::vector<A> > variable2;', 'std'),
    (342, 39, 7, 342, '    std', '    std::vector<std::vector<A> > variable2;', 'std'),
    (343, 39, 8, 343, '    std:', '    std::vector<std::vector<A> > variable2;', ''),
    (344, 39, 9, 344, '    std::', '    std::vector<std::vector<A> > variable2;', ''),
    (345, 39, 10, 345, '    std::v', '    std::vector<std::vector<A> > variable2;', 'vector'),
    (346, 39, 11, 346, '    std::ve', '    std::vector<std::vector<A> > variable2;', 'vector'),
    (347, 39, 12, 347, '    std::vec', '    std::vector<std::vector<A> > variable2;', 'vector'),
    (348, 39, 13, 348, '    std::vect', '    std::vector<std::vector<A> > variable2;', 'vector'),
    (349, 39, 14, 349, '    std::vecto', '    std::vector<std::vector<A> > variable2;', 'vector'),
    (350, 39, 15, 350, '    std::vector', '    std::vector<std::vector<A> > variable2;', 'vector'),
    (351, 39, 16, 351, '    std::vector<', '    std::vector<std::vector<A> > variable2;', ''),
    (352, 39, 17, 352, '    std::vector<s', '    std::vector<std::vector<A> > variable2;', 'std'),
    (353, 39, 18, 353, '    std::vector<st', '    std::vector<std::vector<A> > variable2;', 'std'),
    (354, 39, 19, 354, '    std::vector<std', '    std::vector<std::vector<A> > variable2;', 'std'),
    (355, 39, 20, 355, '    std::vector<std:', '    std::vector<std::vector<A> > variable2;', ''),
    (356, 39, 21, 356, '    std::vector<std::', '    std::vector<std::vector<A> > variable2;', ''),
    (357, 39, 22, 357, '    std::vector<std::v', '    std::vector<std::vector<A> > variable2;', 'vector'),
    (358, 39, 23, 358, '    std::vector<std::ve', '    std::vector<std::vector<A> > variable2;', 'vector'),
    (359, 39, 24, 359, '    std::vector<std::vec', '    std::vector<std::vector<A> > variable2;', 'vector'),
    (360, 39, 25, 360, '    std::vector<std::vect', '    std::vector<std::vector<A> > variable2;', 'vector'),
    (361, 39, 26, 361, '    std::vector<std::vecto', '    std::vector<std::vector<A> > variable2;', 'vector'),
    (362, 39, 27, 362, '    std::vector<std::vector', '    std::vector<std::vector<A> > variable2;', 'vector'),
    (363, 39, 28, 363, '    std::vector<std::vector<', '    std::vector<std::vector<A> > variable2;', ''),
    (364, 39, 29, 364, '    std::vector<std::vector<A', '    std::vector<std::vector<A> > variable2;', 'A'),
    (365, 39, 30, 365, '    std::vector<std::vector<A>', '    std::vector<std::vector<A> > variable2;', ''),
    (366, 39, 31, 366, '    std::vector<std::vector<A> ', '    std::vector<std::vector<A> > variable2;', ''),
    (367, 39, 32, 367, '    std::vector<std::vector<A> >', '    std::vector<std::vector<A> > variable2;', ''),
    (368, 39, 33, 368, '    std::vector<std::vector<A> > ', '    std::vector<std::vector<A> > variable2;', ''),
    (369, 39, 34, 369, '    std::vector<std::vector<A> > v', '    std::vector<std::vector<A> > variable2;', 'variable2'),
    (370, 39, 35, 370, '    std::vector<std::vector<A> > va', '    std::vector<std::vector<A> > variable2;', 'variable2'),
    (371, 39, 36, 371, '    std::vector<std::vector<A> > var', '    std::vector<std::vector<A> > variable2;', 'variable2'),
    (372, 39, 37, 372, '    std::vector<std::vector<A> > vari', '    std::vector<std::vector<A> > variable2;', 'variable2'),
    (373, 39, 38, 373, '    std::vector<std::vector<A> > varia', '    std::vector<std::vector<A> > variable2;', 'variable2'),
    (374, 39, 39, 374, '    std::vector<std::vector<A> > variab', '    std::vector<std::vector<A> > variable2;', 'variable2'),
    (375, 39, 40, 375, '    std::vector<std::vector<A> > variabl', '    std::vector<std::vector<A> > variable2;', 'variable2'),
    (376, 39, 41, 376, '    std::vector<std::vector<A> > variable', '    std::vector<std::vector<A> > variable2;', 'variable2'),
    (377, 39, 42, 377, '    std::vector<std::vector<A> > variable2', '    std::vector<std::vector<A> > variable2;', 'variable2'),
    (378, 39, 43, 378, '    std::vector<std::vector<A> > variable2;', '    std::vector<std::vector<A> > variable2;', ''),
    (379, 39, 44, 379, '', '', ''),
    (380, 40, 1, 380, '}', '};', ''),
    (381, 40, 2, 381, '};', '};', ''),
    (382, 40, 3, 382, '', '', ''),
    (383, 41, 1, 383, '', '', ''),
    (384, 42, 1, 384, 'B', 'B2 b2;', 'B2'),
    (385, 42, 2, 385, 'B2', 'B2 b2;', 'B2'),
    (386, 42, 3, 386, 'B2 ', 'B2 b2;', ''),
    (387, 42, 4, 387, 'B2 b', 'B2 b2;', 'b2'),
    (388, 42, 5, 388, 'B2 b2', 'B2 b2;', 'b2'),
    (389, 42, 6, 389, 'B2 b2;', 'B2 b2;', ''),
    (390, 42, 7, 390, '', '', ''),
    (391, 43, 1, 391, 'b', 'b2.variable.front().back().test;', 'b2'),
    (392, 43, 2, 392, 'b2', 'b2.variable.front().back().test;', 'b2'),
    (393, 43, 3, 393, 'b2.', 'b2.variable.front().back().test;', ''),
    (394, 43, 4, 394, 'b2.v', 'b2.variable.front().back().test;', 'variable'),
    (395, 43, 5, 395, 'b2.va', 'b2.variable.front().back().test;', 'variable'),
    (396, 43, 6, 396, 'b2.var', 'b2.variable.front().back().test;', 'variable'),
    (397, 43, 7, 397, 'b2.vari', 'b2.variable.front().back().test;', 'variable'),
    (398, 43, 8, 398, 'b2.varia', 'b2.variable.front().back().test;', 'variable'),
    (399, 43, 9, 399, 'b2.variab', 'b2.variable.front().back().test;', 'variable'),
    (400, 43, 10, 400, 'b2.variabl', 'b2.variable.front().back().test;', 'variable'),
    (401, 43, 11, 401, 'b2.variable', 'b2.variable.front().back().test;', 'variable'),
    (402, 43, 12, 402, 'b2.variable.', 'b2.variable.front().back().test;', ''),
    (403, 43, 13, 403, 'b2.variable.f', 'b2.variable.front().back().test;', 'front'),
    (404, 43, 14, 404, 'b2.variable.fr', 'b2.variable.front().back().test;', 'front'),
    (405, 43, 15, 405, 'b2.variable.fro', 'b2.variable.front().back().test;', 'front'),
    (406, 43, 16, 406, 'b2.variable.fron', 'b2.variable.front().back().test;', 'front'),
    (407, 43, 17, 407, 'b2.variable.front', 'b2.variable.front().back().test;', 'front'),
    (408, 43, 18, 408, 'b2.variable.front(', 'b2.variable.front().back().test;', ''),
    (409, 43, 19, 409, 'b2.variable.front()', 'b2.variable.front().back().test;', ''),
    (410, 43, 20, 410, 'b2.variable.front().', 'b2.variable.front().back().test;', ''),
    (411, 43, 21, 411, 'b2.variable.front().b', 'b2.variable.front().back().test;', 'back'),
    (412, 43, 22, 412, 'b2.variable.front().ba', 'b2.variable.front().back().test;', 'back'),
    (413, 43, 23, 413, 'b2.variable.front().bac', 'b2.variable.front().back().test;', 'back'),
    (414, 43, 24, 414, 'b2.variable.front().back', 'b2.variable.front().back().test;', 'back'),
    (415, 43, 25, 415, 'b2.variable.front().back(', 'b2.variable.front().back().test;', ''),
    (416, 43, 26, 416, 'b2.variable.front().back()', 'b2.variable.front().back().test;', ''),
    (417, 43, 27, 417, 'b2.variable.front().back().', 'b2.variable.front().back().test;', ''),
    (418, 43, 28, 418, 'b2.variable.front().back().t', 'b2.variable.front().back().test;', 'test'),
    (419, 43, 29, 419, 'b2.variable.front().back().te', 'b2.variable.front().back().test;', 'test'),
    (420, 43, 30, 420, 'b2.variable.front().back().tes', 'b2.variable.front().back().test;', 'test'),
    (421, 43, 31, 421, 'b2.variable.front().back().test', 'b2.variable.front().back().test;', 'test'),
    (422, 43, 32, 422, 'b2.variable.front().back().test;', 'b2.variable.front().back().test;', ''),
    (423, 43, 33, 423, '', '', ''),
    (424, 44, 1, 424, 'b', 'b2.variable2.front().back().test;', 'b2'),
    (425, 44, 2, 425, 'b2', 'b2.variable2.front().back().test;', 'b2'),
    (426, 44, 3, 426, 'b2.', 'b2.variable2.front().back().test;', ''),
    (427, 44, 4, 427, 'b2.v', 'b2.variable2.front().back().test;', 'variable2'),
    (428, 44, 5, 428, 'b2.va', 'b2.variable2.front().back().test;', 'variable2'),
    (429, 44, 6, 429, 'b2.var', 'b2.variable2.front().back().test;', 'variable2'),
    (430, 44, 7, 430, 'b2.vari', 'b2.variable2.front().back().test;', 'variable2'),
    (431, 44, 8, 431, 'b2.varia', 'b2.variable2.front().back().test;', 'variable2'),
    (432, 44, 9, 432, 'b2.variab', 'b2.variable2.front().back().test;', 'variable2'),
    (433, 44, 10, 433, 'b2.variabl', 'b2.variable2.front().back().test;', 'variable2'),
    (434, 44, 11, 434, 'b2.variable', 'b2.variable2.front().back().test;', 'variable2'),
    (435, 44, 12, 435, 'b2.variable2', 'b2.variable2.front().back().test;', 'variable2'),
    (436, 44, 13, 436, 'b2.variable2.', 'b2.variable2.front().back().test;', ''),
    (437, 44, 14, 437, 'b2.variable2.f', 'b2.variable2.front().back().test;', 'front'),
    (438, 44, 15, 438, 'b2.variable2.fr', 'b2.variable2.front().back().test;', 'front'),
    (439, 44, 16, 439, 'b2.variable2.fro', 'b2.variable2.front().back().test;', 'front'),
    (440, 44, 17, 440, 'b2.variable2.fron', 'b2.variable2.front().back().test;', 'front'),
    (441, 44, 18, 441, 'b2.variable2.front', 'b2.variable2.front().back().test;', 'front'),
    (442, 44, 19, 442, 'b2.variable2.front(', 'b2.variable2.front().back().test;', ''),
    (443, 44, 20, 443, 'b2.variable2.front()', 'b2.variable2.front().back().test;', ''),
    (444, 44, 21, 444, 'b2.variable2.front().', 'b2.variable2.front().back().test;', ''),
    (445, 44, 22, 445, 'b2.variable2.front().b', 'b2.variable2.front().back().test;', 'back'),
    (446, 44, 23, 446, 'b2.variable2.front().ba', 'b2.variable2.front().back().test;', 'back'),
    (447, 44, 24, 447, 'b2.variable2.front().bac', 'b2.variable2.front().back().test;', 'back'),
    (448, 44, 25, 448, 'b2.variable2.front().back', 'b2.variable2.front().back().test;', 'back'),
    (449, 44, 26, 449, 'b2.variable2.front().back(', 'b2.variable2.front().back().test;', ''),
    (450, 44, 27, 450, 'b2.variable2.front().back()', 'b2.variable2.front().back().test;', ''),
    (451, 44, 28, 451, 'b2.variable2.front().back().', 'b2.variable2.front().back().test;', ''),
    (452, 44, 29, 452, 'b2.variable2.front().back().t', 'b2.variable2.front().back().test;', 'test'),
    (453, 44, 30, 453, 'b2.variable2.front().back().te', 'b2.variable2.front().back().test;', 'test'),
    (454, 44, 31, 454, 'b2.variable2.front().back().tes', 'b2.variable2.front().back().test;', 'test'),
    (455, 44, 32, 455, 'b2.variable2.front().back().test', 'b2.variable2.front().back().test;', 'test'),
    (456, 44, 33, 456, 'b2.variable2.front().back().test;', 'b2.variable2.front().back().test;', ''),
    (457, 44, 34, 457, '', '', ''),
    (458, 45, 1, 458, '', '', ''),
    (459, 46, 1, 459, '', '', ''),
    (460, 47, 1, 460, 'c', 'class B3', 'class'),
    (461, 47, 2, 461, 'cl', 'class B3', 'class'),
    (462, 47, 3, 462, 'cla', 'class B3', 'class'),
    (463, 47, 4, 463, 'clas', 'class B3', 'class'),
    (464, 47, 5, 464, 'class', 'class B3', 'class'),
    (465, 47, 6, 465, 'class ', 'class B3', ''),
    (466, 47, 7, 466, 'class B', 'class B3', 'B3'),
    (467, 47, 8, 467, 'class B3', 'class B3', 'B3'),
    (468, 47, 9, 468, '', '', ''),
    (469, 48, 1, 469, '{', '{', ''),
    (470, 48, 2, 470, '', '', ''),
    (471, 49, 1, 471, 'p', 'public:', 'public'),
    (472, 49, 2, 472, 'pu', 'public:', 'public'),
    (473, 49, 3, 473, 'pub', 'public:', 'public'),
    (474, 49, 4, 474, 'publ', 'public:', 'public'),
    (475, 49, 5, 475, 'publi', 'public:', 'public'),
    (476, 49, 6, 476, 'public', 'public:', 'public'),
    (477, 49, 7, 477, 'public:', 'public:', ''),
    (478, 49, 8, 478, '', '', ''),
    (479, 50, 1, 479, ' ', '    std::vector<std::vector<AV> > variable;', ''),
    (480, 50, 2, 480, '  ', '    std::vector<std::vector<AV> > variable;', ''),
    (481, 50, 3, 481, '   ', '    std::vector<std::vector<AV> > variable;', ''),
    (482, 50, 4, 482, '    ', '    std::vector<std::vector<AV> > variable;', ''),
    (483, 50, 5, 483, '    s', '    std::vector<std::vector<AV> > variable;', 'std'),
    (484, 50, 6, 484, '    st', '    std::vector<std::vector<AV> > variable;', 'std'),
    (485, 50, 7, 485, '    std', '    std::vector<std::vector<AV> > variable;', 'std'),
    (486, 50, 8, 486, '    std:', '    std::vector<std::vector<AV> > variable;', ''),
    (487, 50, 9, 487, '    std::', '    std::vector<std::vector<AV> > variable;', ''),
    (488, 50, 10, 488, '    std::v', '    std::vector<std::vector<AV> > variable;', 'vector'),
    (489, 50, 11, 489, '    std::ve', '    std::vector<std::vector<AV> > variable;', 'vector'),
    (490, 50, 12, 490, '    std::vec', '    std::vector<std::vector<AV> > variable;', 'vector'),
    (491, 50, 13, 491, '    std::vect', '    std::vector<std::vector<AV> > variable;', 'vector'),
    (492, 50, 14, 492, '    std::vecto', '    std::vector<std::vector<AV> > variable;', 'vector'),
    (493, 50, 15, 493, '    std::vector', '    std::vector<std::vector<AV> > variable;', 'vector'),
    (494, 50, 16, 494, '    std::vector<', '    std::vector<std::vector<AV> > variable;', ''),
    (495, 50, 17, 495, '    std::vector<s', '    std::vector<std::vector<AV> > variable;', 'std'),
    (496, 50, 18, 496, '    std::vector<st', '    std::vector<std::vector<AV> > variable;', 'std'),
    (497, 50, 19, 497, '    std::vector<std', '    std::vector<std::vector<AV> > variable;', 'std'),
    (498, 50, 20, 498, '    std::vector<std:', '    std::vector<std::vector<AV> > variable;', ''),
    (499, 50, 21, 499, '    std::vector<std::', '    std::vector<std::vector<AV> > variable;', ''),
    (500, 50, 22, 500, '    std::vector<std::v', '    std::vector<std::vector<AV> > variable;', 'vector'),
    (501, 50, 23, 501, '    std::vector<std::ve', '    std::vector<std::vector<AV> > variable;', 'vector'),
    (502, 50, 24, 502, '    std::vector<std::vec', '    std::vector<std::vector<AV> > variable;', 'vector'),
    (503, 50, 25, 503, '    std::vector<std::vect', '    std::vector<std::vector<AV> > variable;', 'vector'),
    (504, 50, 26, 504, '    std::vector<std::vecto', '    std::vector<std::vector<AV> > variable;', 'vector'),
    (505, 50, 27, 505, '    std::vector<std::vector', '    std::vector<std::vector<AV> > variable;', 'vector'),
    (506, 50, 28, 506, '    std::vector<std::vector<', '    std::vector<std::vector<AV> > variable;', ''),
    (507, 50, 29, 507, '    std::vector<std::vector<A', '    std::vector<std::vector<AV> > variable;', 'AV'),
    (508, 50, 30, 508, '    std::vector<std::vector<AV', '    std::vector<std::vector<AV> > variable;', 'AV'),
    (509, 50, 31, 509, '    std::vector<std::vector<AV>', '    std::vector<std::vector<AV> > variable;', ''),
    (510, 50, 32, 510, '    std::vector<std::vector<AV> ', '    std::vector<std::vector<AV> > variable;', ''),
    (511, 50, 33, 511, '    std::vector<std::vector<AV> >', '    std::vector<std::vector<AV> > variable;', ''),
    (512, 50, 34, 512, '    std::vector<std::vector<AV> > ', '    std::vector<std::vector<AV> > variable;', ''),
    (513, 50, 35, 513, '    std::vector<std::vector<AV> > v', '    std::vector<std::vector<AV> > variable;', 'variable'),
    (514, 50, 36, 514, '    std::vector<std::vector<AV> > va', '    std::vector<std::vector<AV> > variable;', 'variable'),
    (515, 50, 37, 515, '    std::vector<std::vector<AV> > var', '    std::vector<std::vector<AV> > variable;', 'variable'),
    (516, 50, 38, 516, '    std::vector<std::vector<AV> > vari', '    std::vector<std::vector<AV> > variable;', 'variable'),
    (517, 50, 39, 517, '    std::vector<std::vector<AV> > varia', '    std::vector<std::vector<AV> > variable;', 'variable'),
    (518, 50, 40, 518, '    std::vector<std::vector<AV> > variab', '    std::vector<std::vector<AV> > variable;', 'variable'),
    (519, 50, 41, 519, '    std::vector<std::vector<AV> > variabl', '    std::vector<std::vector<AV> > variable;', 'variable'),
    (520, 50, 42, 520, '    std::vector<std::vector<AV> > variable', '    std::vector<std::vector<AV> > variable;', 'variable'),
    (521, 50, 43, 521, '    std::vector<std::vector<AV> > variable;', '    std::vector<std::vector<AV> > variable;', ''),
    (522, 50, 44, 522, '', '', ''),
    (523, 51, 1, 523, ' ', '    std::vector<std::vector<std::vector<A> > > variable2;', ''),
    (524, 51, 2, 524, '  ', '    std::vector<std::vector<std::vector<A> > > variable2;', ''),
    (525, 51, 3, 525, '   ', '    std::vector<std::vector<std::vector<A> > > variable2;', ''),
    (526, 51, 4, 526, '    ', '    std::vector<std::vector<std::vector<A> > > variable2;', ''),
    (527, 51, 5, 527, '    s', '    std::vector<std::vector<std::vector<A> > > variable2;', 'std'),
    (528, 51, 6, 528, '    st', '    std::vector<std::vector<std::vector<A> > > variable2;', 'std'),
    (529, 51, 7, 529, '    std', '    std::vector<std::vector<std::vector<A> > > variable2;', 'std'),
    (530, 51, 8, 530, '    std:', '    std::vector<std::vector<std::vector<A> > > variable2;', ''),
    (531, 51, 9, 531, '    std::', '    std::vector<std::vector<std::vector<A> > > variable2;', ''),
    (532, 51, 10, 532, '    std::v', '    std::vector<std::vector<std::vector<A> > > variable2;', 'vector'),
    (533, 51, 11, 533, '    std::ve', '    std::vector<std::vector<std::vector<A> > > variable2;', 'vector'),
    (534, 51, 12, 534, '    std::vec', '    std::vector<std::vector<std::vector<A> > > variable2;', 'vector'),
    (535, 51, 13, 535, '    std::vect', '    std::vector<std::vector<std::vector<A> > > variable2;', 'vector'),
    (536, 51, 14, 536, '    std::vecto', '    std::vector<std::vector<std::vector<A> > > variable2;', 'vector'),
    (537, 51, 15, 537, '    std::vector', '    std::vector<std::vector<std::vector<A> > > variable2;', 'vector'),
    (538, 51, 16, 538, '    std::vector<', '    std::vector<std::vector<std::vector<A> > > variable2;', ''),
    (539, 51, 17, 539, '    std::vector<s', '    std::vector<std::vector<std::vector<A> > > variable2;', 'std'),
    (540, 51, 18, 540, '    std::vector<st', '    std::vector<std::vector<std::vector<A> > > variable2;', 'std'),
    (541, 51, 19, 541, '    std::vector<std', '    std::vector<std::vector<std::vector<A> > > variable2;', 'std'),
    (542, 51, 20, 542, '    std::vector<std:', '    std::vector<std::vector<std::vector<A> > > variable2;', ''),
    (543, 51, 21, 543, '    std::vector<std::', '    std::vector<std::vector<std::vector<A> > > variable2;', ''),
    (544, 51, 22, 544, '    std::vector<std::v', '    std::vector<std::vector<std::vector<A> > > variable2;', 'vector'),
    (545, 51, 23, 545, '    std::vector<std::ve', '    std::vector<std::vector<std::vector<A> > > variable2;', 'vector'),
    (546, 51, 24, 546, '    std::vector<std::vec', '    std::vector<std::vector<std::vector<A> > > variable2;', 'vector'),
    (547, 51, 25, 547, '    std::vector<std::vect', '    std::vector<std::vector<std::vector<A> > > variable2;', 'vector'),
    (548, 51, 26, 548, '    std::vector<std::vecto', '    std::vector<std::vector<std::vector<A> > > variable2;', 'vector'),
    (549, 51, 27, 549, '    std::vector<std::vector', '    std::vector<std::vector<std::vector<A> > > variable2;', 'vector'),
    (550, 51, 28, 550, '    std::vector<std::vector<', '    std::vector<std::vector<std::vector<A> > > variable2;', ''),
    (551, 51, 29, 551, '    std::vector<std::vector<s', '    std::vector<std::vector<std::vector<A> > > variable2;', 'std'),
    (552, 51, 30, 552, '    std::vector<std::vector<st', '    std::vector<std::vector<std::vector<A> > > variable2;', 'std'),
    (553, 51, 31, 553, '    std::vector<std::vector<std', '    std::vector<std::vector<std::vector<A> > > variable2;', 'std'),
    (554, 51, 32, 554, '    std::vector<std::vector<std:', '    std::vector<std::vector<std::vector<A> > > variable2;', ''),
    (555, 51, 33, 555, '    std::vector<std::vector<std::', '    std::vector<std::vector<std::vector<A> > > variable2;', ''),
    (556, 51, 34, 556, '    std::vector<std::vector<std::v', '    std::vector<std::vector<std::vector<A> > > variable2;', 'vector'),
    (557, 51, 35, 557, '    std::vector<std::vector<std::ve', '    std::vector<std::vector<std::vector<A> > > variable2;', 'vector'),
    (558, 51, 36, 558, '    std::vector<std::vector<std::vec', '    std::vector<std::vector<std::vector<A> > > variable2;', 'vector'),
    (559, 51, 37, 559, '    std::vector<std::vector<std::vect', '    std::vector<std::vector<std::vector<A> > > variable2;', 'vector'),
    (560, 51, 38, 560, '    std::vector<std::vector<std::vecto', '    std::vector<std::vector<std::vector<A> > > variable2;', 'vector'),
    (561, 51, 39, 561, '    std::vector<std::vector<std::vector', '    std::vector<std::vector<std::vector<A> > > variable2;', 'vector'),
    (562, 51, 40, 562, '    std::vector<std::vector<std::vector<', '    std::vector<std::vector<std::vector<A> > > variable2;', ''),
    (563, 51, 41, 563, '    std::vector<std::vector<std::vector<A', '    std::vector<std::vector<std::vector<A> > > variable2;', 'A'),
    (564, 51, 42, 564, '    std::vector<std::vector<std::vector<A>', '    std::vector<std::vector<std::vector<A> > > variable2;', ''),
    (565, 51, 43, 565, '    std::vector<std::vector<std::vector<A> ', '    std::vector<std::vector<std::vector<A> > > variable2;', ''),
    (566, 51, 44, 566, '    std::vector<std::vector<std::vector<A> >', '    std::vector<std::vector<std::vector<A> > > variable2;', ''),
    (567, 51, 45, 567, '    std::vector<std::vector<std::vector<A> > ', '    std::vector<std::vector<std::vector<A> > > variable2;', ''),
    (568, 51, 46, 568, '    std::vector<std::vector<std::vector<A> > >', '    std::vector<std::vector<std::vector<A> > > variable2;', ''),
    (569, 51, 47, 569, '    std::vector<std::vector<std::vector<A> > > ', '    std::vector<std::vector<std::vector<A> > > variable2;', ''),
    (570, 51, 48, 570, '    std::vector<std::vector<std::vector<A> > > v', '    std::vector<std::vector<std::vector<A> > > variable2;', 'variable2'),
    (571, 51, 49, 571, '    std::vector<std::vector<std::vector<A> > > va', '    std::vector<std::vector<std::vector<A> > > variable2;', 'variable2'),
    (572, 51, 50, 572, '    std::vector<std::vector<std::vector<A> > > var', '    std::vector<std::vector<std::vector<A> > > variable2;', 'variable2'),
    (573, 51, 51, 573, '    std::vector<std::vector<std::vector<A> > > vari', '    std::vector<std::vector<std::vector<A> > > variable2;', 'variable2'),
    (574, 51, 52, 574, '    std::vector<std::vector<std::vector<A> > > varia', '    std::vector<std::vector<std::vector<A> > > variable2;', 'variable2'),
    (575, 51, 53, 575, '    std::vector<std::vector<std::vector<A> > > variab', '    std::vector<std::vector<std::vector<A> > > variable2;', 'variable2'),
    (576, 51, 54, 576, '    std::vector<std::vector<std::vector<A> > > variabl', '    std::vector<std::vector<std::vector<A> > > variable2;', 'variable2'),
    (577, 51, 55, 577, '    std::vector<std::vector<std::vector<A> > > variable', '    std::vector<std::vector<std::vector<A> > > variable2;', 'variable2'),
    (578, 51, 56, 578, '    std::vector<std::vector<std::vector<A> > > variable2', '    std::vector<std::vector<std::vector<A> > > variable2;', 'variable2'),
    (579, 51, 57, 579, '    std::vector<std::vector<std::vector<A> > > variable2;', '    std::vector<std::vector<std::vector<A> > > variable2;', ''),
    (580, 51, 58, 580, '', '', ''),
    (581, 52, 1, 581, '}', '};', ''),
    (582, 52, 2, 582, '};', '};', ''),
    (583, 52, 3, 583, '', '', ''),
    (584, 53, 1, 584, '', '', ''),
    (585, 54, 1, 585, 'B', 'B3 b3;', 'B3'),
    (586, 54, 2, 586, 'B3', 'B3 b3;', 'B3'),
    (587, 54, 3, 587, 'B3 ', 'B3 b3;', ''),
    (588, 54, 4, 588, 'B3 b', 'B3 b3;', 'b3'),
    (589, 54, 5, 589, 'B3 b3', 'B3 b3;', 'b3'),
    (590, 54, 6, 590, 'B3 b3;', 'B3 b3;', ''),
    (591, 54, 7, 591, '', '', ''),
    (592, 55, 1, 592, 'b', 'b3.variable.front().back().front().test;', 'b3'),
    (593, 55, 2, 593, 'b3', 'b3.variable.front().back().front().test;', 'b3'),
    (594, 55, 3, 594, 'b3.', 'b3.variable.front().back().front().test;', ''),
    (595, 55, 4, 595, 'b3.v', 'b3.variable.front().back().front().test;', 'variable'),
    (596, 55, 5, 596, 'b3.va', 'b3.variable.front().back().front().test;', 'variable'),
    (597, 55, 6, 597, 'b3.var', 'b3.variable.front().back().front().test;', 'variable'),
    (598, 55, 7, 598, 'b3.vari', 'b3.variable.front().back().front().test;', 'variable'),
    (599, 55, 8, 599, 'b3.varia', 'b3.variable.front().back().front().test;', 'variable'),
    (600, 55, 9, 600, 'b3.variab', 'b3.variable.front().back().front().test;', 'variable'),
    (601, 55, 10, 601, 'b3.variabl', 'b3.variable.front().back().front().test;', 'variable'),
    (602, 55, 11, 602, 'b3.variable', 'b3.variable.front().back().front().test;', 'variable'),
    (603, 55, 12, 603, 'b3.variable.', 'b3.variable.front().back().front().test;', ''),
    (604, 55, 13, 604, 'b3.variable.f', 'b3.variable.front().back().front().test;', 'front'),
    (605, 55, 14, 605, 'b3.variable.fr', 'b3.variable.front().back().front().test;', 'front'),
    (606, 55, 15, 606, 'b3.variable.fro', 'b3.variable.front().back().front().test;', 'front'),
    (607, 55, 16, 607, 'b3.variable.fron', 'b3.variable.front().back().front().test;', 'front'),
    (608, 55, 17, 608, 'b3.variable.front', 'b3.variable.front().back().front().test;', 'front'),
    (609, 55, 18, 609, 'b3.variable.front(', 'b3.variable.front().back().front().test;', ''),
    (610, 55, 19, 610, 'b3.variable.front()', 'b3.variable.front().back().front().test;', ''),
    (611, 55, 20, 611, 'b3.variable.front().', 'b3.variable.front().back().front().test;', ''),
    (612, 55, 21, 612, 'b3.variable.front().b', 'b3.variable.front().back().front().test;', 'back'),
    (613, 55, 22, 613, 'b3.variable.front().ba', 'b3.variable.front().back().front().test;', 'back'),
    (614, 55, 23, 614, 'b3.variable.front().bac', 'b3.variable.front().back().front().test;', 'back'),
    (615, 55, 24, 615, 'b3.variable.front().back', 'b3.variable.front().back().front().test;', 'back'),
    (616, 55, 25, 616, 'b3.variable.front().back(', 'b3.variable.front().back().front().test;', ''),
    (617, 55, 26, 617, 'b3.variable.front().back()', 'b3.variable.front().back().front().test;', ''),
    (618, 55, 27, 618, 'b3.variable.front().back().', 'b3.variable.front().back().front().test;', ''),
    (619, 55, 28, 619, 'b3.variable.front().back().f', 'b3.variable.front().back().front().test;', 'front'),
    (620, 55, 29, 620, 'b3.variable.front().back().fr', 'b3.variable.front().back().front().test;', 'front'),
    (621, 55, 30, 621, 'b3.variable.front().back().fro', 'b3.variable.front().back().front().test;', 'front'),
    (622, 55, 31, 622, 'b3.variable.front().back().fron', 'b3.variable.front().back().front().test;', 'front'),
    (623, 55, 32, 623, 'b3.variable.front().back().front', 'b3.variable.front().back().front().test;', 'front'),
    (624, 55, 33, 624, 'b3.variable.front().back().front(', 'b3.variable.front().back().front().test;', ''),
    (625, 55, 34, 625, 'b3.variable.front().back().front()', 'b3.variable.front().back().front().test;', ''),
    (626, 55, 35, 626, 'b3.variable.front().back().front().', 'b3.variable.front().back().front().test;', ''),
    (627, 55, 36, 627, 'b3.variable.front().back().front().t', 'b3.variable.front().back().front().test;', 'test'),
    (628, 55, 37, 628, 'b3.variable.front().back().front().te', 'b3.variable.front().back().front().test;', 'test'),
    (629, 55, 38, 629, 'b3.variable.front().back().front().tes', 'b3.variable.front().back().front().test;', 'test'),
    (630, 55, 39, 630, 'b3.variable.front().back().front().test', 'b3.variable.front().back().front().test;', 'test'),
    (631, 55, 40, 631, 'b3.variable.front().back().front().test;', 'b3.variable.front().back().front().test;', ''),
    (632, 55, 41, 632, '', '', ''),
    (633, 56, 1, 633, 'b', 'b3.variable2.front().back().front().test;', 'b3'),
    (634, 56, 2, 634, 'b3', 'b3.variable2.front().back().front().test;', 'b3'),
    (635, 56, 3, 635, 'b3.', 'b3.variable2.front().back().front().test;', ''),
    (636, 56, 4, 636, 'b3.v', 'b3.variable2.front().back().front().test;', 'variable2'),
    (637, 56, 5, 637, 'b3.va', 'b3.variable2.front().back().front().test;', 'variable2'),
    (638, 56, 6, 638, 'b3.var', 'b3.variable2.front().back().front().test;', 'variable2'),
    (639, 56, 7, 639, 'b3.vari', 'b3.variable2.front().back().front().test;', 'variable2'),
    (640, 56, 8, 640, 'b3.varia', 'b3.variable2.front().back().front().test;', 'variable2'),
    (641, 56, 9, 641, 'b3.variab', 'b3.variable2.front().back().front().test;', 'variable2'),
    (642, 56, 10, 642, 'b3.variabl', 'b3.variable2.front().back().front().test;', 'variable2'),
    (643, 56, 11, 643, 'b3.variable', 'b3.variable2.front().back().front().test;', 'variable2'),
    (644, 56, 12, 644, 'b3.variable2', 'b3.variable2.front().back().front().test;', 'variable2'),
    (645, 56, 13, 645, 'b3.variable2.', 'b3.variable2.front().back().front().test;', ''),
    (646, 56, 14, 646, 'b3.variable2.f', 'b3.variable2.front().back().front().test;', 'front'),
    (647, 56, 15, 647, 'b3.variable2.fr', 'b3.variable2.front().back().front().test;', 'front'),
    (648, 56, 16, 648, 'b3.variable2.fro', 'b3.variable2.front().back().front().test;', 'front'),
    (649, 56, 17, 649, 'b3.variable2.fron', 'b3.variable2.front().back().front().test;', 'front'),
    (650, 56, 18, 650, 'b3.variable2.front', 'b3.variable2.front().back().front().test;', 'front'),
    (651, 56, 19, 651, 'b3.variable2.front(', 'b3.variable2.front().back().front().test;', ''),
    (652, 56, 20, 652, 'b3.variable2.front()', 'b3.variable2.front().back().front().test;', ''),
    (653, 56, 21, 653, 'b3.variable2.front().', 'b3.variable2.front().back().front().test;', ''),
    (654, 56, 22, 654, 'b3.variable2.front().b', 'b3.variable2.front().back().front().test;', 'back'),
    (655, 56, 23, 655, 'b3.variable2.front().ba', 'b3.variable2.front().back().front().test;', 'back'),
    (656, 56, 24, 656, 'b3.variable2.front().bac', 'b3.variable2.front().back().front().test;', 'back'),
    (657, 56, 25, 657, 'b3.variable2.front().back', 'b3.variable2.front().back().front().test;', 'back'),
    (658, 56, 26, 658, 'b3.variable2.front().back(', 'b3.variable2.front().back().front().test;', ''),
    (659, 56, 27, 659, 'b3.variable2.front().back()', 'b3.variable2.front().back().front().test;', ''),
    (660, 56, 28, 660, 'b3.variable2.front().back().', 'b3.variable2.front().back().front().test;', ''),
    (661, 56, 29, 661, 'b3.variable2.front().back().f', 'b3.variable2.front().back().front().test;', 'front'),
    (662, 56, 30, 662, 'b3.variable2.front().back().fr', 'b3.variable2.front().back().front().test;', 'front'),
    (663, 56, 31, 663, 'b3.variable2.front().back().fro', 'b3.variable2.front().back().front().test;', 'front'),
    (664, 56, 32, 664, 'b3.variable2.front().back().fron', 'b3.variable2.front().back().front().test;', 'front'),
    (665, 56, 33, 665, 'b3.variable2.front().back().front', 'b3.variable2.front().back().front().test;', 'front'),
    (666, 56, 34, 666, 'b3.variable2.front().back().front(', 'b3.variable2.front().back().front().test;', ''),
    (667, 56, 35, 667, 'b3.variable2.front().back().front()', 'b3.variable2.front().back().front().test;', ''),
    (668, 56, 36, 668, 'b3.variable2.front().back().front().', 'b3.variable2.front().back().front().test;', ''),
    (669, 56, 37, 669, 'b3.variable2.front().back().front().t', 'b3.variable2.front().back().front().test;', 'test'),
    (670, 56, 38, 670, 'b3.variable2.front().back().front().te', 'b3.variable2.front().back().front().test;', 'test'),
    (671, 56, 39, 671, 'b3.variable2.front().back().front().tes', 'b3.variable2.front().back().front().test;', 'test'),
    (672, 56, 40, 672, 'b3.variable2.front().back().front().test', 'b3.variable2.front().back().front().test;', 'test'),
    (673, 56, 41, 673, 'b3.variable2.front().back().front().test;', 'b3.variable2.front().back().front().test;', ''),
    (674, 56, 42, 674, '', '', ''),
    (675, 57, 1, 675, '', '', ''),
    (676, 58, 1, 676, '', '', ''),
    (677, 59, 1, 677, 't', 'template <typename T>', 'template'),
    (678, 59, 2, 678, 'te', 'template <typename T>', 'template'),
    (679, 59, 3, 679, 'tem', 'template <typename T>', 'template'),
    (680, 59, 4, 680, 'temp', 'template <typename T>', 'template'),
    (681, 59, 5, 681, 'templ', 'template <typename T>', 'template'),
    (682, 59, 6, 682, 'templa', 'template <typename T>', 'template'),
    (683, 59, 7, 683, 'templat', 'template <typename T>', 'template'),
    (684, 59, 8, 684, 'template', 'template <typename T>', 'template'),
    (685, 59, 9, 685, 'template ', 'template <typename T>', ''),
    (686, 59, 10, 686, 'template <', 'template <typename T>', ''),
    (687, 59, 11, 687, 'template <t', 'template <typename T>', 'typename'),
    (688, 59, 12, 688, 'template <ty', 'template <typename T>', 'typename'),
    (689, 59, 13, 689, 'template <typ', 'template <typename T>', 'typename'),
    (690, 59, 14, 690, 'template <type', 'template <typename T>', 'typename'),
    (691, 59, 15, 691, 'template <typen', 'template <typename T>', 'typename'),
    (692, 59, 16, 692, 'template <typena', 'template <typename T>', 'typename'),
    (693, 59, 17, 693, 'template <typenam', 'template <typename T>', 'typename'),
    (694, 59, 18, 694, 'template <typename', 'template <typename T>', 'typename'),
    (695, 59, 19, 695, 'template <typename ', 'template <typename T>', ''),
    (696, 59, 20, 696, 'template <typename T', 'template <typename T>', 'T'),
    (697, 59, 21, 697, 'template <typename T>', 'template <typename T>', ''),
    (698, 59, 22, 698, '', '', ''),
    (699, 60, 1, 699, 'c', 'class TempA', 'class'),
    (700, 60, 2, 700, 'cl', 'class TempA', 'class'),
    (701, 60, 3, 701, 'cla', 'class TempA', 'class'),
    (702, 60, 4, 702, 'clas', 'class TempA', 'class'),
    (703, 60, 5, 703, 'class', 'class TempA', 'class'),
    (704, 60, 6, 704, 'class ', 'class TempA', ''),
    (705, 60, 7, 705, 'class T', 'class TempA', 'TempA'),
    (706, 60, 8, 706, 'class Te', 'class TempA', 'TempA'),
    (707, 60, 9, 707, 'class Tem', 'class TempA', 'TempA'),
    (708, 60, 10, 708, 'class Temp', 'class TempA', 'TempA'),
    (709, 60, 11, 709, 'class TempA', 'class TempA', 'TempA'),
    (710, 60, 12, 710, '', '', ''),
    (711, 61, 1, 711, '{', '{', ''),
    (712, 61, 2, 712, '', '', ''),
    (713, 62, 1, 713, 'p', 'public:', 'public'),
    (714, 62, 2, 714, 'pu', 'public:', 'public'),
    (715, 62, 3, 715, 'pub', 'public:', 'public'),
    (716, 62, 4, 716, 'publ', 'public:', 'public'),
    (717, 62, 5, 717, 'publi', 'public:', 'public'),
    (718, 62, 6, 718, 'public', 'public:', 'public'),
    (719, 62, 7, 719, 'public:', 'public:', ''),
    (720, 62, 8, 720, '', '', ''),
    (721, 63, 1, 721, ' ', '    T& GetT() { return mT;}', ''),
    (722, 63, 2, 722, '  ', '    T& GetT() { return mT;}', ''),
    (723, 63, 3, 723, '   ', '    T& GetT() { return mT;}', ''),
    (724, 63, 4, 724, '    ', '    T& GetT() { return mT;}', ''),
    (725, 63, 5, 725, '    T', '    T& GetT() { return mT;}', 'T'),
    (726, 63, 6, 726, '    T&', '    T& GetT() { return mT;}', ''),
    (727, 63, 7, 727, '    T& ', '    T& GetT() { return mT;}', ''),
    (728, 63, 8, 728, '    T& G', '    T& GetT() { return mT;}', 'GetT'),
    (729, 63, 9, 729, '    T& Ge', '    T& GetT() { return mT;}', 'GetT'),
    (730, 63, 10, 730, '    T& Get', '    T& GetT() { return mT;}', 'GetT'),
    (731, 63, 11, 731, '    T& GetT', '    T& GetT() { return mT;}', 'GetT'),
    (732, 63, 12, 732, '    T& GetT(', '    T& GetT() { return mT;}', ''),
    (733, 63, 13, 733, '    T& GetT()', '    T& GetT() { return mT;}', ''),
    (734, 63, 14, 734, '    T& GetT() ', '    T& GetT() { return mT;}', ''),
    (735, 63, 15, 735, '    T& GetT() {', '    T& GetT() { return mT;}', ''),
    (736, 63, 16, 736, '    T& GetT() { ', '    T& GetT() { return mT;}', ''),
    (737, 63, 17, 737, '    T& GetT() { r', '    T& GetT() { return mT;}', 'return'),
    (738, 63, 18, 738, '    T& GetT() { re', '    T& GetT() { return mT;}', 'return'),
    (739, 63, 19, 739, '    T& GetT() { ret', '    T& GetT() { return mT;}', 'return'),
    (740, 63, 20, 740, '    T& GetT() { retu', '    T& GetT() { return mT;}', 'return'),
    (741, 63, 21, 741, '    T& GetT() { retur', '    T& GetT() { return mT;}', 'return'),
    (742, 63, 22, 742, '    T& GetT() { return', '    T& GetT() { return mT;}', 'return'),
    (743, 63, 23, 743, '    T& GetT() { return ', '    T& GetT() { return mT;}', ''),
    (744, 63, 24, 744, '    T& GetT() { return m', '    T& GetT() { return mT;}', 'mT'),
    (745, 63, 25, 745, '    T& GetT() { return mT', '    T& GetT() { return mT;}', 'mT'),
    (746, 63, 26, 746, '    T& GetT() { return mT;', '    T& GetT() { return mT;}', ''),
    (747, 63, 27, 747, '    T& GetT() { return mT;}', '    T& GetT() { return mT;}', ''),
    (748, 63, 28, 748, '', '', ''),
    (749, 64, 1, 749, ' ', '    T mT;', ''),
    (750, 64, 2, 750, '  ', '    T mT;', ''),
    (751, 64, 3, 751, '   ', '    T mT;', ''),
    (752, 64, 4, 752, '    ', '    T mT;', ''),
    (753, 64, 5, 753, '    T', '    T mT;', 'T'),
    (754, 64, 6, 754, '    T ', '    T mT;', ''),
    (755, 64, 7, 755, '    T m', '    T mT;', 'mT'),
    (756, 64, 8, 756, '    T mT', '    T mT;', 'mT'),
    (757, 64, 9, 757, '    T mT;', '    T mT;', ''),
    (758, 64, 10, 758, '', '', ''),
    (759, 65, 1, 759, '}', '};', ''),
    (760, 65, 2, 760, '};', '};', ''),
    (761, 65, 3, 761, '', '', ''),
    (762, 66, 1, 762, '', '', ''),
    (763, 67, 1, 763, 't', 'template <typename T>', 'template'),
    (764, 67, 2, 764, 'te', 'template <typename T>', 'template'),
    (765, 67, 3, 765, 'tem', 'template <typename T>', 'template'),
    (766, 67, 4, 766, 'temp', 'template <typename T>', 'template'),
    (767, 67, 5, 767, 'templ', 'template <typename T>', 'template'),
    (768, 67, 6, 768, 'templa', 'template <typename T>', 'template'),
    (769, 67, 7, 769, 'templat', 'template <typename T>', 'template'),
    (770, 67, 8, 770, 'template', 'template <typename T>', 'template'),
    (771, 67, 9, 771, 'template ', 'template <typename T>', ''),
    (772, 67, 10, 772, 'template <', 'template <typename T>', ''),
    (773, 67, 11, 773, 'template <t', 'template <typename T>', 'typename'),
    (774, 67, 12, 774, 'template <ty', 'template <typename T>', 'typename'),
    (775, 67, 13, 775, 'template <typ', 'template <typename T>', 'typename'),
    (776, 67, 14, 776, 'template <type', 'template <typename T>', 'typename'),
    (777, 67, 15, 777, 'template <typen', 'template <typename T>', 'typename'),
    (778, 67, 16, 778, 'template <typena', 'template <typename T>', 'typename'),
    (779, 67, 17, 779, 'template <typenam', 'template <typename T>', 'typename'),
    (780, 67, 18, 780, 'template <typename', 'template <typename T>', 'typename'),
    (781, 67, 19, 781, 'template <typename ', 'template <typename T>', ''),
    (782, 67, 20, 782, 'template <typename T', 'template <typename T>', 'T'),
    (783, 67, 21, 783, 'template <typename T>', 'template <typename T>', ''),
    (784, 67, 22, 784, '', '', ''),
    (785, 68, 1, 785, 'c', 'class TempB', 'class'),
    (786, 68, 2, 786, 'cl', 'class TempB', 'class'),
    (787, 68, 3, 787, 'cla', 'class TempB', 'class'),
    (788, 68, 4, 788, 'clas', 'class TempB', 'class'),
    (789, 68, 5, 789, 'class', 'class TempB', 'class'),
    (790, 68, 6, 790, 'class ', 'class TempB', ''),
    (791, 68, 7, 791, 'class T', 'class TempB', 'TempB'),
    (792, 68, 8, 792, 'class Te', 'class TempB', 'TempB'),
    (793, 68, 9, 793, 'class Tem', 'class TempB', 'TempB'),
    (794, 68, 10, 794, 'class Temp', 'class TempB', 'TempB'),
    (795, 68, 11, 795, 'class TempB', 'class TempB', 'TempB'),
    (796, 68, 12, 796, '', '', ''),
    (797, 69, 1, 797, '{', '{', ''),
    (798, 69, 2, 798, '', '', ''),
    (799, 70, 1, 799, 'p', 'public:', 'public'),
    (800, 70, 2, 800, 'pu', 'public:', 'public'),
    (801, 70, 3, 801, 'pub', 'public:', 'public'),
    (802, 70, 4, 802, 'publ', 'public:', 'public'),
    (803, 70, 5, 803, 'publi', 'public:', 'public'),
    (804, 70, 6, 804, 'public', 'public:', 'public'),
    (805, 70, 7, 805, 'public:', 'public:', ''),
    (806, 70, 8, 806, '', '', ''),
    (807, 71, 1, 807, ' ', '    T& GetTB() { return mT; }', ''),
    (808, 71, 2, 808, '  ', '    T& GetTB() { return mT; }', ''),
    (809, 71, 3, 809, '   ', '    T& GetTB() { return mT; }', ''),
    (810, 71, 4, 810, '    ', '    T& GetTB() { return mT; }', ''),
    (811, 71, 5, 811, '    T', '    T& GetTB() { return mT; }', 'T'),
    (812, 71, 6, 812, '    T&', '    T& GetTB() { return mT; }', ''),
    (813, 71, 7, 813, '    T& ', '    T& GetTB() { return mT; }', ''),
    (814, 71, 8, 814, '    T& G', '    T& GetTB() { return mT; }', 'GetTB'),
    (815, 71, 9, 815, '    T& Ge', '    T& GetTB() { return mT; }', 'GetTB'),
    (816, 71, 10, 816, '    T& Get', '    T& GetTB() { return mT; }', 'GetTB'),
    (817, 71, 11, 817, '    T& GetT', '    T& GetTB() { return mT; }', 'GetTB'),
    (818, 71, 12, 818, '    T& GetTB', '    T& GetTB() { return mT; }', 'GetTB'),
    (819, 71, 13, 819, '    T& GetTB(', '    T& GetTB() { return mT; }', ''),
    (820, 71, 14, 820, '    T& GetTB()', '    T& GetTB() { return mT; }', ''),
    (821, 71, 15, 821, '    T& GetTB() ', '    T& GetTB() { return mT; }', ''),
    (822, 71, 16, 822, '    T& GetTB() {', '    T& GetTB() { return mT; }', ''),
    (823, 71, 17, 823, '    T& GetTB() { ', '    T& GetTB() { return mT; }', ''),
    (824, 71, 18, 824, '    T& GetTB() { r', '    T& GetTB() { return mT; }', 'return'),
    (825, 71, 19, 825, '    T& GetTB() { re', '    T& GetTB() { return mT; }', 'return'),
    (826, 71, 20, 826, '    T& GetTB() { ret', '    T& GetTB() { return mT; }', 'return'),
    (827, 71, 21, 827, '    T& GetTB() { retu', '    T& GetTB() { return mT; }', 'return'),
    (828, 71, 22, 828, '    T& GetTB() { retur', '    T& GetTB() { return mT; }', 'return'),
    (829, 71, 23, 829, '    T& GetTB() { return', '    T& GetTB() { return mT; }', 'return'),
    (830, 71, 24, 830, '    T& GetTB() { return ', '    T& GetTB() { return mT; }', ''),
    (831, 71, 25, 831, '    T& GetTB() { return m', '    T& GetTB() { return mT; }', 'mT'),
    (832, 71, 26, 832, '    T& GetTB() { return mT', '    T& GetTB() { return mT; }', 'mT'),
    (833, 71, 27, 833, '    T& GetTB() { return mT;', '    T& GetTB() { return mT; }', ''),
    (834, 71, 28, 834, '    T& GetTB() { return mT; ', '    T& GetTB() { return mT; }', ''),
    (835, 71, 29, 835, '    T& GetTB() { return mT; }', '    T& GetTB() { return mT; }', ''),
    (836, 71, 30, 836, '', '', ''),
    (837, 72, 1, 837, ' ', '    T mTB;', ''),
    (838, 72, 2, 838, '  ', '    T mTB;', ''),
    (839, 72, 3, 839, '   ', '    T mTB;', ''),
    (840, 72, 4, 840, '    ', '    T mTB;', ''),
    (841, 72, 5, 841, '    T', '    T mTB;', 'T'),
    (842, 72, 6, 842, '    T ', '    T mTB;', ''),
    (843, 72, 7, 843, '    T m', '    T mTB;', 'mTB'),
    (844, 72, 8, 844, '    T mT', '    T mTB;', 'mTB'),
    (845, 72, 9, 845, '    T mTB', '    T mTB;', 'mTB'),
    (846, 72, 10, 846, '    T mTB;', '    T mTB;', ''),
    (847, 72, 11, 847, '', '', ''),
    (848, 73, 1, 848, '}', '};', ''),
    (849, 73, 2, 849, '};', '};', ''),
    (850, 73, 3, 850, '', '', ''),
    (851, 74, 1, 851, '', '', ''),
    (852, 75, 1, 852, 'T', 'TempA<A> ta;', 'TempA'),
    (853, 75, 2, 853, 'Te', 'TempA<A> ta;', 'TempA'),
    (854, 75, 3, 854, 'Tem', 'TempA<A> ta;', 'TempA'),
    (855, 75, 4, 855, 'Temp', 'TempA<A> ta;', 'TempA'),
    (856, 75, 5, 856, 'TempA', 'TempA<A> ta;', 'TempA'),
    (857, 75, 6, 857, 'TempA<', 'TempA<A> ta;', ''),
    (858, 75, 7, 858, 'TempA<A', 'TempA<A> ta;', 'A'),
    (859, 75, 8, 859, 'TempA<A>', 'TempA<A> ta;', ''),
    (860, 75, 9, 860, 'TempA<A> ', 'TempA<A> ta;', ''),
    (861, 75, 10, 861, 'TempA<A> t', 'TempA<A> ta;', 'ta'),
    (862, 75, 11, 862, 'TempA<A> ta', 'TempA<A> ta;', 'ta'),
    (863, 75, 12, 863, 'TempA<A> ta;', 'TempA<A> ta;', ''),
    (864, 75, 13, 864, '', '', ''),
    (865, 76, 1, 865, 't', 'ta.GetT().test;', 'ta'),
    (866, 76, 2, 866, 'ta', 'ta.GetT().test;', 'ta'),
    (867, 76, 3, 867, 'ta.', 'ta.GetT().test;', ''),
    (868, 76, 4, 868, 'ta.G', 'ta.GetT().test;', 'GetT'),
    (869, 76, 5, 869, 'ta.Ge', 'ta.GetT().test;', 'GetT'),
    (870, 76, 6, 870, 'ta.Get', 'ta.GetT().test;', 'GetT'),
    (871, 76, 7, 871, 'ta.GetT', 'ta.GetT().test;', 'GetT'),
    (872, 76, 8, 872, 'ta.GetT(', 'ta.GetT().test;', ''),
    (873, 76, 9, 873, 'ta.GetT()', 'ta.GetT().test;', ''),
    (874, 76, 10, 874, 'ta.GetT().', 'ta.GetT().test;', ''),
    (875, 76, 11, 875, 'ta.GetT().t', 'ta.GetT().test;', 'test'),
    (876, 76, 12, 876, 'ta.GetT().te', 'ta.GetT().test;', 'test'),
    (877, 76, 13, 877, 'ta.GetT().tes', 'ta.GetT().test;', 'test'),
    (878, 76, 14, 878, 'ta.GetT().test', 'ta.GetT().test;', 'test'),
    (879, 76, 15, 879, 'ta.GetT().test;', 'ta.GetT().test;', ''),
    (880, 76, 16, 880, '', '', ''),
    (881, 77, 1, 881, '', '', ''),
    (882, 78, 1, 882, 'T', 'TempA<TempB<TempA<TempB<A> > > > ta2;', 'TempA'),
    (883, 78, 2, 883, 'Te', 'TempA<TempB<TempA<TempB<A> > > > ta2;', 'TempA'),
    (884, 78, 3, 884, 'Tem', 'TempA<TempB<TempA<TempB<A> > > > ta2;', 'TempA'),
    (885, 78, 4, 885, 'Temp', 'TempA<TempB<TempA<TempB<A> > > > ta2;', 'TempA'),
    (886, 78, 5, 886, 'TempA', 'TempA<TempB<TempA<TempB<A> > > > ta2;', 'TempA'),
    (887, 78, 6, 887, 'TempA<', 'TempA<TempB<TempA<TempB<A> > > > ta2;', ''),
    (888, 78, 7, 888, 'TempA<T', 'TempA<TempB<TempA<TempB<A> > > > ta2;', 'TempB'),
    (889, 78, 8, 889, 'TempA<Te', 'TempA<TempB<TempA<TempB<A> > > > ta2;', 'TempB'),
    (890, 78, 9, 890, 'TempA<Tem', 'TempA<TempB<TempA<TempB<A> > > > ta2;', 'TempB'),
    (891, 78, 10, 891, 'TempA<Temp', 'TempA<TempB<TempA<TempB<A> > > > ta2;', 'TempB'),
    (892, 78, 11, 892, 'TempA<TempB', 'TempA<TempB<TempA<TempB<A> > > > ta2;', 'TempB'),
    (893, 78, 12, 893, 'TempA<TempB<', 'TempA<TempB<TempA<TempB<A> > > > ta2;', ''),
    (894, 78, 13, 894, 'TempA<TempB<T', 'TempA<TempB<TempA<TempB<A> > > > ta2;', 'TempA'),
    (895, 78, 14, 895, 'TempA<TempB<Te', 'TempA<TempB<TempA<TempB<A> > > > ta2;', 'TempA'),
    (896, 78, 15, 896, 'TempA<TempB<Tem', 'TempA<TempB<TempA<TempB<A> > > > ta2;', 'TempA'),
    (897, 78, 16, 897, 'TempA<TempB<Temp', 'TempA<TempB<TempA<TempB<A> > > > ta2;', 'TempA'),
    (898, 78, 17, 898, 'TempA<TempB<TempA', 'TempA<TempB<TempA<TempB<A> > > > ta2;', 'TempA'),
    (899, 78, 18, 899, 'TempA<TempB<TempA<', 'TempA<TempB<TempA<TempB<A> > > > ta2;', ''),
    (900, 78, 19, 900, 'TempA<TempB<TempA<T', 'TempA<TempB<TempA<TempB<A> > > > ta2;', 'TempB'),
    (901, 78, 20, 901, 'TempA<TempB<TempA<Te', 'TempA<TempB<TempA<TempB<A> > > > ta2;', 'TempB'),
    (902, 78, 21, 902, 'TempA<TempB<TempA<Tem', 'TempA<TempB<TempA<TempB<A> > > > ta2;', 'TempB'),
    (903, 78, 22, 903, 'TempA<TempB<TempA<Temp', 'TempA<TempB<TempA<TempB<A> > > > ta2;', 'TempB'),
    (904, 78, 23, 904, 'TempA<TempB<TempA<TempB', 'TempA<TempB<TempA<TempB<A> > > > ta2;', 'TempB'),
    (905, 78, 24, 905, 'TempA<TempB<TempA<TempB<', 'TempA<TempB<TempA<TempB<A> > > > ta2;', ''),
    (906, 78, 25, 906, 'TempA<TempB<TempA<TempB<A', 'TempA<TempB<TempA<TempB<A> > > > ta2;', 'A'),
    (907, 78, 26, 907, 'TempA<TempB<TempA<TempB<A>', 'TempA<TempB<TempA<TempB<A> > > > ta2;', ''),
    (908, 78, 27, 908, 'TempA<TempB<TempA<TempB<A> ', 'TempA<TempB<TempA<TempB<A> > > > ta2;', ''),
    (909, 78, 28, 909, 'TempA<TempB<TempA<TempB<A> >', 'TempA<TempB<TempA<TempB<A> > > > ta2;', ''),
    (910, 78, 29, 910, 'TempA<TempB<TempA<TempB<A> > ', 'TempA<TempB<TempA<TempB<A> > > > ta2;', ''),
    (911, 78, 30, 911, 'TempA<TempB<TempA<TempB<A> > >', 'TempA<TempB<TempA<TempB<A> > > > ta2;', ''),
    (912, 78, 31, 912, 'TempA<TempB<TempA<TempB<A> > > ', 'TempA<TempB<TempA<TempB<A> > > > ta2;', ''),
    (913, 78, 32, 913, 'TempA<TempB<TempA<TempB<A> > > >', 'TempA<TempB<TempA<TempB<A> > > > ta2;', ''),
    (914, 78, 33, 914, 'TempA<TempB<TempA<TempB<A> > > > ', 'TempA<TempB<TempA<TempB<A> > > > ta2;', ''),
    (915, 78, 34, 915, 'TempA<TempB<TempA<TempB<A> > > > t', 'TempA<TempB<TempA<TempB<A> > > > ta2;', 'ta2'),
    (916, 78, 35, 916, 'TempA<TempB<TempA<TempB<A> > > > ta', 'TempA<TempB<TempA<TempB<A> > > > ta2;', 'ta2'),
    (917, 78, 36, 917, 'TempA<TempB<TempA<TempB<A> > > > ta2', 'TempA<TempB<TempA<TempB<A> > > > ta2;', 'ta2'),
    (918, 78, 37, 918, 'TempA<TempB<TempA<TempB<A> > > > ta2;', 'TempA<TempB<TempA<TempB<A> > > > ta2;', ''),
    (919, 78, 38, 919, '', '', ''),
    (920, 79, 1, 920, 't', 'ta2.GetT().GetTB().GetT().GetTB().test;', 'ta2'),
    (921, 79, 2, 921, 'ta', 'ta2.GetT().GetTB().GetT().GetTB().test;', 'ta2'),
    (922, 79, 3, 922, 'ta2', 'ta2.GetT().GetTB().GetT().GetTB().test;', 'ta2'),
    (923, 79, 4, 923, 'ta2.', 'ta2.GetT().GetTB().GetT().GetTB().test;', ''),
    (924, 79, 5, 924, 'ta2.G', 'ta2.GetT().GetTB().GetT().GetTB().test;', 'GetT'),
    (925, 79, 6, 925, 'ta2.Ge', 'ta2.GetT().GetTB().GetT().GetTB().test;', 'GetT'),
    (926, 79, 7, 926, 'ta2.Get', 'ta2.GetT().GetTB().GetT().GetTB().test;', 'GetT'),
    (927, 79, 8, 927, 'ta2.GetT', 'ta2.GetT().GetTB().GetT().GetTB().test;', 'GetT'),
    (928, 79, 9, 928, 'ta2.GetT(', 'ta2.GetT().GetTB().GetT().GetTB().test;', ''),
    (929, 79, 10, 929, 'ta2.GetT()', 'ta2.GetT().GetTB().GetT().GetTB().test;', ''),
    (930, 79, 11, 930, 'ta2.GetT().', 'ta2.GetT().GetTB().GetT().GetTB().test;', ''),
    (931, 79, 12, 931, 'ta2.GetT().G', 'ta2.GetT().GetTB().GetT().GetTB().test;', 'GetTB'),
    (932, 79, 13, 932, 'ta2.GetT().Ge', 'ta2.GetT().GetTB().GetT().GetTB().test;', 'GetTB'),
    (933, 79, 14, 933, 'ta2.GetT().Get', 'ta2.GetT().GetTB().GetT().GetTB().test;', 'GetTB'),
    (934, 79, 15, 934, 'ta2.GetT().GetT', 'ta2.GetT().GetTB().GetT().GetTB().test;', 'GetTB'),
    (935, 79, 16, 935, 'ta2.GetT().GetTB', 'ta2.GetT().GetTB().GetT().GetTB().test;', 'GetTB'),
    (936, 79, 17, 936, 'ta2.GetT().GetTB(', 'ta2.GetT().GetTB().GetT().GetTB().test;', ''),
    (937, 79, 18, 937, 'ta2.GetT().GetTB()', 'ta2.GetT().GetTB().GetT().GetTB().test;', ''),
    (938, 79, 19, 938, 'ta2.GetT().GetTB().', 'ta2.GetT().GetTB().GetT().GetTB().test;', ''),
    (939, 79, 20, 939, 'ta2.GetT().GetTB().G', 'ta2.GetT().GetTB().GetT().GetTB().test;', 'GetT'),
    (940, 79, 21, 940, 'ta2.GetT().GetTB().Ge', 'ta2.GetT().GetTB().GetT().GetTB().test;', 'GetT'),
    (941, 79, 22, 941, 'ta2.GetT().GetTB().Get', 'ta2.GetT().GetTB().GetT().GetTB().test;', 'GetT'),
    (942, 79, 23, 942, 'ta2.GetT().GetTB().GetT', 'ta2.GetT().GetTB().GetT().GetTB().test;', 'GetT'),
    (943, 79, 24, 943, 'ta2.GetT().GetTB().GetT(', 'ta2.GetT().GetTB().GetT().GetTB().test;', ''),
    (944, 79, 25, 944, 'ta2.GetT().GetTB().GetT()', 'ta2.GetT().GetTB().GetT().GetTB().test;', ''),
    (945, 79, 26, 945, 'ta2.GetT().GetTB().GetT().', 'ta2.GetT().GetTB().GetT().GetTB().test;', ''),
    (946, 79, 27, 946, 'ta2.GetT().GetTB().GetT().G', 'ta2.GetT().GetTB().GetT().GetTB().test;', 'GetTB'),
    (947, 79, 28, 947, 'ta2.GetT().GetTB().GetT().Ge', 'ta2.GetT().GetTB().GetT().GetTB().test;', 'GetTB'),
    (948, 79, 29, 948, 'ta2.GetT().GetTB().GetT().Get', 'ta2.GetT().GetTB().GetT().GetTB().test;', 'GetTB'),
    (949, 79, 30, 949, 'ta2.GetT().GetTB().GetT().GetT', 'ta2.GetT().GetTB().GetT().GetTB().test;', 'GetTB'),
    (950, 79, 31, 950, 'ta2.GetT().GetTB().GetT().GetTB', 'ta2.GetT().GetTB().GetT().GetTB().test;', 'GetTB'),
    (951, 79, 32, 951, 'ta2.GetT().GetTB().GetT().GetTB(', 'ta2.GetT().GetTB().GetT().GetTB().test;', ''),
    (952, 79, 33, 952, 'ta2.GetT().GetTB().GetT().GetTB()', 'ta2.GetT().GetTB().GetT().GetTB().test;', ''),
    (953, 79, 34, 953, 'ta2.GetT().GetTB().GetT().GetTB().', 'ta2.GetT().GetTB().GetT().GetTB().test;', ''),
    (954, 79, 35, 954, 'ta2.GetT().GetTB().GetT().GetTB().t', 'ta2.GetT().GetTB().GetT().GetTB().test;', 'test'),
    (955, 79, 36, 955, 'ta2.GetT().GetTB().GetT().GetTB().te', 'ta2.GetT().GetTB().GetT().GetTB().test;', 'test'),
    (956, 79, 37, 956, 'ta2.GetT().GetTB().GetT().GetTB().tes', 'ta2.GetT().GetTB().GetT().GetTB().test;', 'test'),
    (957, 79, 38, 957, 'ta2.GetT().GetTB().GetT().GetTB().test', 'ta2.GetT().GetTB().GetT().GetTB().test;', 'test'),
    (958, 79, 39, 958, 'ta2.GetT().GetTB().GetT().GetTB().test;', 'ta2.GetT().GetTB().GetT().GetTB().test;', ''),
    (959, 79, 40, 959, '', '', ''),
    (960, 80, 1, 960, 't', 'ta2.mT.mTB.mT.mTB.test;', 'ta2'),
    (961, 80, 2, 961, 'ta', 'ta2.mT.mTB.mT.mTB.test;', 'ta2'),
    (962, 80, 3, 962, 'ta2', 'ta2.mT.mTB.mT.mTB.test;', 'ta2'),
    (963, 80, 4, 963, 'ta2.', 'ta2.mT.mTB.mT.mTB.test;', ''),
    (964, 80, 5, 964, 'ta2.m', 'ta2.mT.mTB.mT.mTB.test;', 'mT'),
    (965, 80, 6, 965, 'ta2.mT', 'ta2.mT.mTB.mT.mTB.test;', 'mT'),
    (966, 80, 7, 966, 'ta2.mT.', 'ta2.mT.mTB.mT.mTB.test;', ''),
    (967, 80, 8, 967, 'ta2.mT.m', 'ta2.mT.mTB.mT.mTB.test;', 'mTB'),
    (968, 80, 9, 968, 'ta2.mT.mT', 'ta2.mT.mTB.mT.mTB.test;', 'mTB'),
    (969, 80, 10, 969, 'ta2.mT.mTB', 'ta2.mT.mTB.mT.mTB.test;', 'mTB'),
    (970, 80, 11, 970, 'ta2.mT.mTB.', 'ta2.mT.mTB.mT.mTB.test;', ''),
    (971, 80, 12, 971, 'ta2.mT.mTB.m', 'ta2.mT.mTB.mT.mTB.test;', 'mT'),
    (972, 80, 13, 972, 'ta2.mT.mTB.mT', 'ta2.mT.mTB.mT.mTB.test;', 'mT'),
    (973, 80, 14, 973, 'ta2.mT.mTB.mT.', 'ta2.mT.mTB.mT.mTB.test;', ''),
    (974, 80, 15, 974, 'ta2.mT.mTB.mT.m', 'ta2.mT.mTB.mT.mTB.test;', 'mTB'),
    (975, 80, 16, 975, 'ta2.mT.mTB.mT.mT', 'ta2.mT.mTB.mT.mTB.test;', 'mTB'),
    (976, 80, 17, 976, 'ta2.mT.mTB.mT.mTB', 'ta2.mT.mTB.mT.mTB.test;', 'mTB'),
    (977, 80, 18, 977, 'ta2.mT.mTB.mT.mTB.', 'ta2.mT.mTB.mT.mTB.test;', ''),
    (978, 80, 19, 978, 'ta2.mT.mTB.mT.mTB.t', 'ta2.mT.mTB.mT.mTB.test;', 'test'),
    (979, 80, 20, 979, 'ta2.mT.mTB.mT.mTB.te', 'ta2.mT.mTB.mT.mTB.test;', 'test'),
    (980, 80, 21, 980, 'ta2.mT.mTB.mT.mTB.tes', 'ta2.mT.mTB.mT.mTB.test;', 'test'),
    (981, 80, 22, 981, 'ta2.mT.mTB.mT.mTB.test', 'ta2.mT.mTB.mT.mTB.test;', 'test'),
    (982, 80, 23, 982, 'ta2.mT.mTB.mT.mTB.test;', 'ta2.mT.mTB.mT.mTB.test;', ''),
    (983, 80, 24, 983, '', '', ''),
    (984, 81, 1, 984, '', '', ''),
    (985, 82, 1, 985, 't', 'typedef TempA<TempB<TempA<TempB<A> > > > Tababa;', 'typedef'),
    (986, 82, 2, 986, 'ty', 'typedef TempA<TempB<TempA<TempB<A> > > > Tababa;', 'typedef'),
    (987, 82, 3, 987, 'typ', 'typedef TempA<TempB<TempA<TempB<A> > > > Tababa;', 'typedef'),
    (988, 82, 4, 988, 'type', 'typedef TempA<TempB<TempA<TempB<A> > > > Tababa;', 'typedef'),
    (989, 82, 5, 989, 'typed', 'typedef TempA<TempB<TempA<TempB<A> > > > Tababa;', 'typedef'),
    (990, 82, 6, 990, 'typede', 'typedef TempA<TempB<TempA<TempB<A> > > > Tababa;', 'typedef'),
    (991, 82, 7, 991, 'typedef', 'typedef TempA<TempB<TempA<TempB<A> > > > Tababa;', 'typedef'),
    (992, 82, 8, 992, 'typedef ', 'typedef TempA<TempB<TempA<TempB<A> > > > Tababa;', ''),
    (993, 82, 9, 993, 'typedef T', 'typedef TempA<TempB<TempA<TempB<A> > > > Tababa;', 'TempA'),
    (994, 82, 10, 994, 'typedef Te', 'typedef TempA<TempB<TempA<TempB<A> > > > Tababa;', 'TempA'),
    (995, 82, 11, 995, 'typedef Tem', 'typedef TempA<TempB<TempA<TempB<A> > > > Tababa;', 'TempA'),
    (996, 82, 12, 996, 'typedef Temp', 'typedef TempA<TempB<TempA<TempB<A> > > > Tababa;', 'TempA'),
    (997, 82, 13, 997, 'typedef TempA', 'typedef TempA<TempB<TempA<TempB<A> > > > Tababa;', 'TempA'),
    (998, 82, 14, 998, 'typedef TempA<', 'typedef TempA<TempB<TempA<TempB<A> > > > Tababa;', ''),
    (999, 82, 15, 999, 'typedef TempA<T', 'typedef TempA<TempB<TempA<TempB<A> > > > Tababa;', 'TempB'),
    (1000, 82, 16, 1000, 'typedef TempA<Te', 'typedef TempA<TempB<TempA<TempB<A> > > > Tababa;', 'TempB'),
    (1001, 82, 17, 1001, 'typedef TempA<Tem', 'typedef TempA<TempB<TempA<TempB<A> > > > Tababa;', 'TempB'),
    (1002, 82, 18, 1002, 'typedef TempA<Temp', 'typedef TempA<TempB<TempA<TempB<A> > > > Tababa;', 'TempB'),
    (1003, 82, 19, 1003, 'typedef TempA<TempB', 'typedef TempA<TempB<TempA<TempB<A> > > > Tababa;', 'TempB'),
    (1004, 82, 20, 1004, 'typedef TempA<TempB<', 'typedef TempA<TempB<TempA<TempB<A> > > > Tababa;', ''),
    (1005, 82, 21, 1005, 'typedef TempA<TempB<T', 'typedef TempA<TempB<TempA<TempB<A> > > > Tababa;', 'TempA'),
    (1006, 82, 22, 1006, 'typedef TempA<TempB<Te', 'typedef TempA<TempB<TempA<TempB<A> > > > Tababa;', 'TempA'),
    (1007, 82, 23, 1007, 'typedef TempA<TempB<Tem', 'typedef TempA<TempB<TempA<TempB<A> > > > Tababa;', 'TempA'),
    (1008, 82, 24, 1008, 'typedef TempA<TempB<Temp', 'typedef TempA<TempB<TempA<TempB<A> > > > Tababa;', 'TempA'),
    (1009, 82, 25, 1009, 'typedef TempA<TempB<TempA', 'typedef TempA<TempB<TempA<TempB<A> > > > Tababa;', 'TempA'),
    (1010, 82, 26, 1010, 'typedef TempA<TempB<TempA<', 'typedef TempA<TempB<TempA<TempB<A> > > > Tababa;', ''),
    (1011, 82, 27, 1011, 'typedef TempA<TempB<TempA<T', 'typedef TempA<TempB<TempA<TempB<A> > > > Tababa;', 'TempB'),
    (1012, 82, 28, 1012, 'typedef TempA<TempB<TempA<Te', 'typedef TempA<TempB<TempA<TempB<A> > > > Tababa;', 'TempB'),
    (1013, 82, 29, 1013, 'typedef TempA<TempB<TempA<Tem', 'typedef TempA<TempB<TempA<TempB<A> > > > Tababa;', 'TempB'),
    (1014, 82, 30, 1014, 'typedef TempA<TempB<TempA<Temp', 'typedef TempA<TempB<TempA<TempB<A> > > > Tababa;', 'TempB'),
    (1015, 82, 31, 1015, 'typedef TempA<TempB<TempA<TempB', 'typedef TempA<TempB<TempA<TempB<A> > > > Tababa;', 'TempB'),
    (1016, 82, 32, 1016, 'typedef TempA<TempB<TempA<TempB<', 'typedef TempA<TempB<TempA<TempB<A> > > > Tababa;', ''),
    (1017, 82, 33, 1017, 'typedef TempA<TempB<TempA<TempB<A', 'typedef TempA<TempB<TempA<TempB<A> > > > Tababa;', 'A'),
    (1018, 82, 34, 1018, 'typedef TempA<TempB<TempA<TempB<A>', 'typedef TempA<TempB<TempA<TempB<A> > > > Tababa;', ''),
    (1019, 82, 35, 1019, 'typedef TempA<TempB<TempA<TempB<A> ', 'typedef TempA<TempB<TempA<TempB<A> > > > Tababa;', ''),
    (1020, 82, 36, 1020, 'typedef TempA<TempB<TempA<TempB<A> >', 'typedef TempA<TempB<TempA<TempB<A> > > > Tababa;', ''),
    (1021, 82, 37, 1021, 'typedef TempA<TempB<TempA<TempB<A> > ', 'typedef TempA<TempB<TempA<TempB<A> > > > Tababa;', ''),
    (1022, 82, 38, 1022, 'typedef TempA<TempB<TempA<TempB<A> > >', 'typedef TempA<TempB<TempA<TempB<A> > > > Tababa;', ''),
    (1023, 82, 39, 1023, 'typedef TempA<TempB<TempA<TempB<A> > > ', 'typedef TempA<TempB<TempA<TempB<A> > > > Tababa;', ''),
    (1024, 82, 40, 1024, 'typedef TempA<TempB<TempA<TempB<A> > > >', 'typedef TempA<TempB<TempA<TempB<A> > > > Tababa;', ''),
    (1025, 82, 41, 1025, 'typedef TempA<TempB<TempA<TempB<A> > > > ', 'typedef TempA<TempB<TempA<TempB<A> > > > Tababa;', ''),
    (1026, 82, 42, 1026, 'typedef TempA<TempB<TempA<TempB<A> > > > T', 'typedef TempA<TempB<TempA<TempB<A> > > > Tababa;', 'Tababa'),
    (1027, 82, 43, 1027, 'typedef TempA<TempB<TempA<TempB<A> > > > Ta', 'typedef TempA<TempB<TempA<TempB<A> > > > Tababa;', 'Tababa'),
    (1028, 82, 44, 1028, 'typedef TempA<TempB<TempA<TempB<A> > > > Tab', 'typedef TempA<TempB<TempA<TempB<A> > > > Tababa;', 'Tababa'),
    (1029, 82, 45, 1029, 'typedef TempA<TempB<TempA<TempB<A> > > > Taba', 'typedef TempA<TempB<TempA<TempB<A> > > > Tababa;', 'Tababa'),
    (1030, 82, 46, 1030, 'typedef TempA<TempB<TempA<TempB<A> > > > Tabab', 'typedef TempA<TempB<TempA<TempB<A> > > > Tababa;', 'Tababa'),
    (1031, 82, 47, 1031, 'typedef TempA<TempB<TempA<TempB<A> > > > Tababa', 'typedef TempA<TempB<TempA<TempB<A> > > > Tababa;', 'Tababa'),
    (1032, 82, 48, 1032, 'typedef TempA<TempB<TempA<TempB<A> > > > Tababa;', 'typedef TempA<TempB<TempA<TempB<A> > > > Tababa;', ''),
    (1033, 82, 49, 1033, '', '', ''),
    (1034, 83, 1, 1034, '', '', ''),
    (1035, 84, 1, 1035, 'T', 'Tababa tababa;', 'Tababa'),
    (1036, 84, 2, 1036, 'Ta', 'Tababa tababa;', 'Tababa'),
    (1037, 84, 3, 1037, 'Tab', 'Tababa tababa;', 'Tababa'),
    (1038, 84, 4, 1038, 'Taba', 'Tababa tababa;', 'Tababa'),
    (1039, 84, 5, 1039, 'Tabab', 'Tababa tababa;', 'Tababa'),
    (1040, 84, 6, 1040, 'Tababa', 'Tababa tababa;', 'Tababa'),
    (1041, 84, 7, 1041, 'Tababa ', 'Tababa tababa;', ''),
    (1042, 84, 8, 1042, 'Tababa t', 'Tababa tababa;', 'tababa'),
    (1043, 84, 9, 1043, 'Tababa ta', 'Tababa tababa;', 'tababa'),
    (1044, 84, 10, 1044, 'Tababa tab', 'Tababa tababa;', 'tababa'),
    (1045, 84, 11, 1045, 'Tababa taba', 'Tababa tababa;', 'tababa'),
    (1046, 84, 12, 1046, 'Tababa tabab', 'Tababa tababa;', 'tababa'),
    (1047, 84, 13, 1047, 'Tababa tababa', 'Tababa tababa;', 'tababa'),
    (1048, 84, 14, 1048, 'Tababa tababa;', 'Tababa tababa;', ''),
    (1049, 84, 15, 1049, '', '', ''),
    (1050, 85, 1, 1050, 't', 'tababa.GetT().GetTB().GetT().GetTB().test;', 'tababa'),
    (1051, 85, 2, 1051, 'ta', 'tababa.GetT().GetTB().GetT().GetTB().test;', 'tababa'),
    (1052, 85, 3, 1052, 'tab', 'tababa.GetT().GetTB().GetT().GetTB().test;', 'tababa'),
    (1053, 85, 4, 1053, 'taba', 'tababa.GetT().GetTB().GetT().GetTB().test;', 'tababa'),
    (1054, 85, 5, 1054, 'tabab', 'tababa.GetT().GetTB().GetT().GetTB().test;', 'tababa'),
    (1055, 85, 6, 1055, 'tababa', 'tababa.GetT().GetTB().GetT().GetTB().test;', 'tababa'),
    (1056, 85, 7, 1056, 'tababa.', 'tababa.GetT().GetTB().GetT().GetTB().test;', ''),
    (1057, 85, 8, 1057, 'tababa.G', 'tababa.GetT().GetTB().GetT().GetTB().test;', 'GetT'),
    (1058, 85, 9, 1058, 'tababa.Ge', 'tababa.GetT().GetTB().GetT().GetTB().test;', 'GetT'),
    (1059, 85, 10, 1059, 'tababa.Get', 'tababa.GetT().GetTB().GetT().GetTB().test;', 'GetT'),
    (1060, 85, 11, 1060, 'tababa.GetT', 'tababa.GetT().GetTB().GetT().GetTB().test;', 'GetT'),
    (1061, 85, 12, 1061, 'tababa.GetT(', 'tababa.GetT().GetTB().GetT().GetTB().test;', ''),
    (1062, 85, 13, 1062, 'tababa.GetT()', 'tababa.GetT().GetTB().GetT().GetTB().test;', ''),
    (1063, 85, 14, 1063, 'tababa.GetT().', 'tababa.GetT().GetTB().GetT().GetTB().test;', ''),
    (1064, 85, 15, 1064, 'tababa.GetT().G', 'tababa.GetT().GetTB().GetT().GetTB().test;', 'GetTB'),
    (1065, 85, 16, 1065, 'tababa.GetT().Ge', 'tababa.GetT().GetTB().GetT().GetTB().test;', 'GetTB'),
    (1066, 85, 17, 1066, 'tababa.GetT().Get', 'tababa.GetT().GetTB().GetT().GetTB().test;', 'GetTB'),
    (1067, 85, 18, 1067, 'tababa.GetT().GetT', 'tababa.GetT().GetTB().GetT().GetTB().test;', 'GetTB'),
    (1068, 85, 19, 1068, 'tababa.GetT().GetTB', 'tababa.GetT().GetTB().GetT().GetTB().test;', 'GetTB'),
    (1069, 85, 20, 1069, 'tababa.GetT().GetTB(', 'tababa.GetT().GetTB().GetT().GetTB().test;', ''),
    (1070, 85, 21, 1070, 'tababa.GetT().GetTB()', 'tababa.GetT().GetTB().GetT().GetTB().test;', ''),
    (1071, 85, 22, 1071, 'tababa.GetT().GetTB().', 'tababa.GetT().GetTB().GetT().GetTB().test;', ''),
    (1072, 85, 23, 1072, 'tababa.GetT().GetTB().G', 'tababa.GetT().GetTB().GetT().GetTB().test;', 'GetT'),
    (1073, 85, 24, 1073, 'tababa.GetT().GetTB().Ge', 'tababa.GetT().GetTB().GetT().GetTB().test;', 'GetT'),
    (1074, 85, 25, 1074, 'tababa.GetT().GetTB().Get', 'tababa.GetT().GetTB().GetT().GetTB().test;', 'GetT'),
    (1075, 85, 26, 1075, 'tababa.GetT().GetTB().GetT', 'tababa.GetT().GetTB().GetT().GetTB().test;', 'GetT'),
    (1076, 85, 27, 1076, 'tababa.GetT().GetTB().GetT(', 'tababa.GetT().GetTB().GetT().GetTB().test;', ''),
    (1077, 85, 28, 1077, 'tababa.GetT().GetTB().GetT()', 'tababa.GetT().GetTB().GetT().GetTB().test;', ''),
    (1078, 85, 29, 1078, 'tababa.GetT().GetTB().GetT().', 'tababa.GetT().GetTB().GetT().GetTB().test;', ''),
    (1079, 85, 30, 1079, 'tababa.GetT().GetTB().GetT().G', 'tababa.GetT().GetTB().GetT().GetTB().test;', 'GetTB'),
    (1080, 85, 31, 1080, 'tababa.GetT().GetTB().GetT().Ge', 'tababa.GetT().GetTB().GetT().GetTB().test;', 'GetTB'),
    (1081, 85, 32, 1081, 'tababa.GetT().GetTB().GetT().Get', 'tababa.GetT().GetTB().GetT().GetTB().test;', 'GetTB'),
    (1082, 85, 33, 1082, 'tababa.GetT().GetTB().GetT().GetT', 'tababa.GetT().GetTB().GetT().GetTB().test;', 'GetTB'),
    (1083, 85, 34, 1083, 'tababa.GetT().GetTB().GetT().GetTB', 'tababa.GetT().GetTB().GetT().GetTB().test;', 'GetTB'),
    (1084, 85, 35, 1084, 'tababa.GetT().GetTB().GetT().GetTB(', 'tababa.GetT().GetTB().GetT().GetTB().test;', ''),
    (1085, 85, 36, 1085, 'tababa.GetT().GetTB().GetT().GetTB()', 'tababa.GetT().GetTB().GetT().GetTB().test;', ''),
    (1086, 85, 37, 1086, 'tababa.GetT().GetTB().GetT().GetTB().', 'tababa.GetT().GetTB().GetT().GetTB().test;', ''),
    (1087, 85, 38, 1087, 'tababa.GetT().GetTB().GetT().GetTB().t', 'tababa.GetT().GetTB().GetT().GetTB().test;', 'test'),
    (1088, 85, 39, 1088, 'tababa.GetT().GetTB().GetT().GetTB().te', 'tababa.GetT().GetTB().GetT().GetTB().test;', 'test'),
    (1089, 85, 40, 1089, 'tababa.GetT().GetTB().GetT().GetTB().tes', 'tababa.GetT().GetTB().GetT().GetTB().test;', 'test'),
    (1090, 85, 41, 1090, 'tababa.GetT().GetTB().GetT().GetTB().test', 'tababa.GetT().GetTB().GetT().GetTB().test;', 'test'),
    (1091, 85, 42, 1091, 'tababa.GetT().GetTB().GetT().GetTB().test;', 'tababa.GetT().GetTB().GetT().GetTB().test;', ''),
    (1092, 85, 43, 1092, '', '', ''),
    (1093, 86, 1, 1093, 't', 'tababa.mT.mTB.mT.mTB.test;', 'tababa'),
    (1094, 86, 2, 1094, 'ta', 'tababa.mT.mTB.mT.mTB.test;', 'tababa'),
    (1095, 86, 3, 1095, 'tab', 'tababa.mT.mTB.mT.mTB.test;', 'tababa'),
    (1096, 86, 4, 1096, 'taba', 'tababa.mT.mTB.mT.mTB.test;', 'tababa'),
    (1097, 86, 5, 1097, 'tabab', 'tababa.mT.mTB.mT.mTB.test;', 'tababa'),
    (1098, 86, 6, 1098, 'tababa', 'tababa.mT.mTB.mT.mTB.test;', 'tababa'),
    (1099, 86, 7, 1099, 'tababa.', 'tababa.mT.mTB.mT.mTB.test;', ''),
    (1100, 86, 8, 1100, 'tababa.m', 'tababa.mT.mTB.mT.mTB.test;', 'mT'),
    (1101, 86, 9, 1101, 'tababa.mT', 'tababa.mT.mTB.mT.mTB.test;', 'mT'),
    (1102, 86, 10, 1102, 'tababa.mT.', 'tababa.mT.mTB.mT.mTB.test;', ''),
    (1103, 86, 11, 1103, 'tababa.mT.m', 'tababa.mT.mTB.mT.mTB.test;', 'mTB'),
    (1104, 86, 12, 1104, 'tababa.mT.mT', 'tababa.mT.mTB.mT.mTB.test;', 'mTB'),
    (1105, 86, 13, 1105, 'tababa.mT.mTB', 'tababa.mT.mTB.mT.mTB.test;', 'mTB'),
    (1106, 86, 14, 1106, 'tababa.mT.mTB.', 'tababa.mT.mTB.mT.mTB.test;', ''),
    (1107, 86, 15, 1107, 'tababa.mT.mTB.m', 'tababa.mT.mTB.mT.mTB.test;', 'mT'),
    (1108, 86, 16, 1108, 'tababa.mT.mTB.mT', 'tababa.mT.mTB.mT.mTB.test;', 'mT'),
    (1109, 86, 17, 1109, 'tababa.mT.mTB.mT.', 'tababa.mT.mTB.mT.mTB.test;', ''),
    (1110, 86, 18, 1110, 'tababa.mT.mTB.mT.m', 'tababa.mT.mTB.mT.mTB.test;', 'mTB'),
    (1111, 86, 19, 1111, 'tababa.mT.mTB.mT.mT', 'tababa.mT.mTB.mT.mTB.test;', 'mTB'),
    (1112, 86, 20, 1112, 'tababa.mT.mTB.mT.mTB', 'tababa.mT.mTB.mT.mTB.test;', 'mTB'),
    (1113, 86, 21, 1113, 'tababa.mT.mTB.mT.mTB.', 'tababa.mT.mTB.mT.mTB.test;', ''),
    (1114, 86, 22, 1114, 'tababa.mT.mTB.mT.mTB.t', 'tababa.mT.mTB.mT.mTB.test;', 'test'),
    (1115, 86, 23, 1115, 'tababa.mT.mTB.mT.mTB.te', 'tababa.mT.mTB.mT.mTB.test;', 'test'),
    (1116, 86, 24, 1116, 'tababa.mT.mTB.mT.mTB.tes', 'tababa.mT.mTB.mT.mTB.test;', 'test'),
    (1117, 86, 25, 1117, 'tababa.mT.mTB.mT.mTB.test', 'tababa.mT.mTB.mT.mTB.test;', 'test'),
    (1118, 86, 26, 1118, 'tababa.mT.mTB.mT.mTB.test;', 'tababa.mT.mTB.mT.mTB.test;', ''),
    (1119, 86, 27, 1119, '', '', ''),
    (1120, 87, 1, 1120, '', '', ''),
    (1121, 88, 1, 1121, 'c', 'class Tababa_class', 'class'),
    (1122, 88, 2, 1122, 'cl', 'class Tababa_class', 'class'),
    (1123, 88, 3, 1123, 'cla', 'class Tababa_class', 'class'),
    (1124, 88, 4, 1124, 'clas', 'class Tababa_class', 'class'),
    (1125, 88, 5, 1125, 'class', 'class Tababa_class', 'class'),
    (1126, 88, 6, 1126, 'class ', 'class Tababa_class', ''),
    (1127, 88, 7, 1127, 'class T', 'class Tababa_class', 'Tababa_class'),
    (1128, 88, 8, 1128, 'class Ta', 'class Tababa_class', 'Tababa_class'),
    (1129, 88, 9, 1129, 'class Tab', 'class Tababa_class', 'Tababa_class'),
    (1130, 88, 10, 1130, 'class Taba', 'class Tababa_class', 'Tababa_class'),
    (1131, 88, 11, 1131, 'class Tabab', 'class Tababa_class', 'Tababa_class'),
    (1132, 88, 12, 1132, 'class Tababa', 'class Tababa_class', 'Tababa_class'),
    (1133, 88, 13, 1133, 'class Tababa_', 'class Tababa_class', 'Tababa_class'),
    (1134, 88, 14, 1134, 'class Tababa_c', 'class Tababa_class', 'Tababa_class'),
    (1135, 88, 15, 1135, 'class Tababa_cl', 'class Tababa_class', 'Tababa_class'),
    (1136, 88, 16, 1136, 'class Tababa_cla', 'class Tababa_class', 'Tababa_class'),
    (1137, 88, 17, 1137, 'class Tababa_clas', 'class Tababa_class', 'Tababa_class'),
    (1138, 88, 18, 1138, 'class Tababa_class', 'class Tababa_class', 'Tababa_class'),
    (1139, 88, 19, 1139, '', '', ''),
    (1140, 89, 1, 1140, '{', '{', ''),
    (1141, 89, 2, 1141, '', '', ''),
    (1142, 90, 1, 1142, 'p', 'public:', 'public'),
    (1143, 90, 2, 1143, 'pu', 'public:', 'public'),
    (1144, 90, 3, 1144, 'pub', 'public:', 'public'),
    (1145, 90, 4, 1145, 'publ', 'public:', 'public'),
    (1146, 90, 5, 1146, 'publi', 'public:', 'public'),
    (1147, 90, 6, 1147, 'public', 'public:', 'public'),
    (1148, 90, 7, 1148, 'public:', 'public:', ''),
    (1149, 90, 8, 1149, '', '', ''),
    (1150, 91, 1, 1150, ' ', '    Tababa GetTababa();', ''),
    (1151, 91, 2, 1151, '  ', '    Tababa GetTababa();', ''),
    (1152, 91, 3, 1152, '   ', '    Tababa GetTababa();', ''),
    (1153, 91, 4, 1153, '    ', '    Tababa GetTababa();', ''),
    (1154, 91, 5, 1154, '    T', '    Tababa GetTababa();', 'Tababa'),
    (1155, 91, 6, 1155, '    Ta', '    Tababa GetTababa();', 'Tababa'),
    (1156, 91, 7, 1156, '    Tab', '    Tababa GetTababa();', 'Tababa'),
    (1157, 91, 8, 1157, '    Taba', '    Tababa GetTababa();', 'Tababa'),
    (1158, 91, 9, 1158, '    Tabab', '    Tababa GetTababa();', 'Tababa'),
    (1159, 91, 10, 1159, '    Tababa', '    Tababa GetTababa();', 'Tababa'),
    (1160, 91, 11, 1160, '    Tababa ', '    Tababa GetTababa();', ''),
    (1161, 91, 12, 1161, '    Tababa G', '    Tababa GetTababa();', 'GetTababa'),
    (1162, 91, 13, 1162, '    Tababa Ge', '    Tababa GetTababa();', 'GetTababa'),
    (1163, 91, 14, 1163, '    Tababa Get', '    Tababa GetTababa();', 'GetTababa'),
    (1164, 91, 15, 1164, '    Tababa GetT', '    Tababa GetTababa();', 'GetTababa'),
    (1165, 91, 16, 1165, '    Tababa GetTa', '    Tababa GetTababa();', 'GetTababa'),
    (1166, 91, 17, 1166, '    Tababa GetTab', '    Tababa GetTababa();', 'GetTababa'),
    (1167, 91, 18, 1167, '    Tababa GetTaba', '    Tababa GetTababa();', 'GetTababa'),
    (1168, 91, 19, 1168, '    Tababa GetTabab', '    Tababa GetTababa();', 'GetTababa'),
    (1169, 91, 20, 1169, '    Tababa GetTababa', '    Tababa GetTababa();', 'GetTababa'),
    (1170, 91, 21, 1170, '    Tababa GetTababa(', '    Tababa GetTababa();', ''),
    (1171, 91, 22, 1171, '    Tababa GetTababa()', '    Tababa GetTababa();', ''),
    (1172, 91, 23, 1172, '    Tababa GetTababa();', '    Tababa GetTababa();', ''),
    (1173, 91, 24, 1173, '', '', ''),
    (1174, 92, 1, 1174, ' ', '    Tababa mTababa;', ''),
    (1175, 92, 2, 1175, '  ', '    Tababa mTababa;', ''),
    (1176, 92, 3, 1176, '   ', '    Tababa mTababa;', ''),
    (1177, 92, 4, 1177, '    ', '    Tababa mTababa;', ''),
    (1178, 92, 5, 1178, '    T', '    Tababa mTababa;', 'Tababa'),
    (1179, 92, 6, 1179, '    Ta', '    Tababa mTababa;', 'Tababa'),
    (1180, 92, 7, 1180, '    Tab', '    Tababa mTababa;', 'Tababa'),
    (1181, 92, 8, 1181, '    Taba', '    Tababa mTababa;', 'Tababa'),
    (1182, 92, 9, 1182, '    Tabab', '    Tababa mTababa;', 'Tababa'),
    (1183, 92, 10, 1183, '    Tababa', '    Tababa mTababa;', 'Tababa'),
    (1184, 92, 11, 1184, '    Tababa ', '    Tababa mTababa;', ''),
    (1185, 92, 12, 1185, '    Tababa m', '    Tababa mTababa;', 'mTababa'),
    (1186, 92, 13, 1186, '    Tababa mT', '    Tababa mTababa;', 'mTababa'),
    (1187, 92, 14, 1187, '    Tababa mTa', '    Tababa mTababa;', 'mTababa'),
    (1188, 92, 15, 1188, '    Tababa mTab', '    Tababa mTababa;', 'mTababa'),
    (1189, 92, 16, 1189, '    Tababa mTaba', '    Tababa mTababa;', 'mTababa'),
    (1190, 92, 17, 1190, '    Tababa mTabab', '    Tababa mTababa;', 'mTababa'),
    (1191, 92, 18, 1191, '    Tababa mTababa', '    Tababa mTababa;', 'mTababa'),
    (1192, 92, 19, 1192, '    Tababa mTababa;', '    Tababa mTababa;', ''),
    (1193, 92, 20, 1193, '', '', ''),
    (1194, 93, 1, 1194, '', '', ''),
    (1195, 94, 1, 1195, ' ', '    TempA<TempB<TempA<TempB<A> > > > GetTababa2();', ''),
    (1196, 94, 2, 1196, '  ', '    TempA<TempB<TempA<TempB<A> > > > GetTababa2();', ''),
    (1197, 94, 3, 1197, '   ', '    TempA<TempB<TempA<TempB<A> > > > GetTababa2();', ''),
    (1198, 94, 4, 1198, '    ', '    TempA<TempB<TempA<TempB<A> > > > GetTababa2();', ''),
    (1199, 94, 5, 1199, '    T', '    TempA<TempB<TempA<TempB<A> > > > GetTababa2();', 'TempA'),
    (1200, 94, 6, 1200, '    Te', '    TempA<TempB<TempA<TempB<A> > > > GetTababa2();', 'TempA'),
    (1201, 94, 7, 1201, '    Tem', '    TempA<TempB<TempA<TempB<A> > > > GetTababa2();', 'TempA'),
    (1202, 94, 8, 1202, '    Temp', '    TempA<TempB<TempA<TempB<A> > > > GetTababa2();', 'TempA'),
    (1203, 94, 9, 1203, '    TempA', '    TempA<TempB<TempA<TempB<A> > > > GetTababa2();', 'TempA'),
    (1204, 94, 10, 1204, '    TempA<', '    TempA<TempB<TempA<TempB<A> > > > GetTababa2();', ''),
    (1205, 94, 11, 1205, '    TempA<T', '    TempA<TempB<TempA<TempB<A> > > > GetTababa2();', 'TempB'),
    (1206, 94, 12, 1206, '    TempA<Te', '    TempA<TempB<TempA<TempB<A> > > > GetTababa2();', 'TempB'),
    (1207, 94, 13, 1207, '    TempA<Tem', '    TempA<TempB<TempA<TempB<A> > > > GetTababa2();', 'TempB'),
    (1208, 94, 14, 1208, '    TempA<Temp', '    TempA<TempB<TempA<TempB<A> > > > GetTababa2();', 'TempB'),
    (1209, 94, 15, 1209, '    TempA<TempB', '    TempA<TempB<TempA<TempB<A> > > > GetTababa2();', 'TempB'),
    (1210, 94, 16, 1210, '    TempA<TempB<', '    TempA<TempB<TempA<TempB<A> > > > GetTababa2();', ''),
    (1211, 94, 17, 1211, '    TempA<TempB<T', '    TempA<TempB<TempA<TempB<A> > > > GetTababa2();', 'TempA'),
    (1212, 94, 18, 1212, '    TempA<TempB<Te', '    TempA<TempB<TempA<TempB<A> > > > GetTababa2();', 'TempA'),
    (1213, 94, 19, 1213, '    TempA<TempB<Tem', '    TempA<TempB<TempA<TempB<A> > > > GetTababa2();', 'TempA'),
    (1214, 94, 20, 1214, '    TempA<TempB<Temp', '    TempA<TempB<TempA<TempB<A> > > > GetTababa2();', 'TempA'),
    (1215, 94, 21, 1215, '    TempA<TempB<TempA', '    TempA<TempB<TempA<TempB<A> > > > GetTababa2();', 'TempA'),
    (1216, 94, 22, 1216, '    TempA<TempB<TempA<', '    TempA<TempB<TempA<TempB<A> > > > GetTababa2();', ''),
    (1217, 94, 23, 1217, '    TempA<TempB<TempA<T', '    TempA<TempB<TempA<TempB<A> > > > GetTababa2();', 'TempB'),
    (1218, 94, 24, 1218, '    TempA<TempB<TempA<Te', '    TempA<TempB<TempA<TempB<A> > > > GetTababa2();', 'TempB'),
    (1219, 94, 25, 1219, '    TempA<TempB<TempA<Tem', '    TempA<TempB<TempA<TempB<A> > > > GetTababa2();', 'TempB'),
    (1220, 94, 26, 1220, '    TempA<TempB<TempA<Temp', '    TempA<TempB<TempA<TempB<A> > > > GetTababa2();', 'TempB'),
    (1221, 94, 27, 1221, '    TempA<TempB<TempA<TempB', '    TempA<TempB<TempA<TempB<A> > > > GetTababa2();', 'TempB'),
    (1222, 94, 28, 1222, '    TempA<TempB<TempA<TempB<', '    TempA<TempB<TempA<TempB<A> > > > GetTababa2();', ''),
    (1223, 94, 29, 1223, '    TempA<TempB<TempA<TempB<A', '    TempA<TempB<TempA<TempB<A> > > > GetTababa2();', 'A'),
    (1224, 94, 30, 1224, '    TempA<TempB<TempA<TempB<A>', '    TempA<TempB<TempA<TempB<A> > > > GetTababa2();', ''),
    (1225, 94, 31, 1225, '    TempA<TempB<TempA<TempB<A> ', '    TempA<TempB<TempA<TempB<A> > > > GetTababa2();', ''),
    (1226, 94, 32, 1226, '    TempA<TempB<TempA<TempB<A> >', '    TempA<TempB<TempA<TempB<A> > > > GetTababa2();', ''),
    (1227, 94, 33, 1227, '    TempA<TempB<TempA<TempB<A> > ', '    TempA<TempB<TempA<TempB<A> > > > GetTababa2();', ''),
    (1228, 94, 34, 1228, '    TempA<TempB<TempA<TempB<A> > >', '    TempA<TempB<TempA<TempB<A> > > > GetTababa2();', ''),
    (1229, 94, 35, 1229, '    TempA<TempB<TempA<TempB<A> > > ', '    TempA<TempB<TempA<TempB<A> > > > GetTababa2();', ''),
    (1230, 94, 36, 1230, '    TempA<TempB<TempA<TempB<A> > > >', '    TempA<TempB<TempA<TempB<A> > > > GetTababa2();', ''),
    (1231, 94, 37, 1231, '    TempA<TempB<TempA<TempB<A> > > > ', '    TempA<TempB<TempA<TempB<A> > > > GetTababa2();', ''),
    (1232, 94, 38, 1232, '    TempA<TempB<TempA<TempB<A> > > > G', '    TempA<TempB<TempA<TempB<A> > > > GetTababa2();', 'GetTababa2'),
    (1233, 94, 39, 1233, '    TempA<TempB<TempA<TempB<A> > > > Ge', '    TempA<TempB<TempA<TempB<A> > > > GetTababa2();', 'GetTababa2'),
    (1234, 94, 40, 1234, '    TempA<TempB<TempA<TempB<A> > > > Get', '    TempA<TempB<TempA<TempB<A> > > > GetTababa2();', 'GetTababa2'),
    (1235, 94, 41, 1235, '    TempA<TempB<TempA<TempB<A> > > > GetT', '    TempA<TempB<TempA<TempB<A> > > > GetTababa2();', 'GetTababa2'),
    (1236, 94, 42, 1236, '    TempA<TempB<TempA<TempB<A> > > > GetTa', '    TempA<TempB<TempA<TempB<A> > > > GetTababa2();', 'GetTababa2'),
    (1237, 94, 43, 1237, '    TempA<TempB<TempA<TempB<A> > > > GetTab', '    TempA<TempB<TempA<TempB<A> > > > GetTababa2();', 'GetTababa2'),
    (1238, 94, 44, 1238, '    TempA<TempB<TempA<TempB<A> > > > GetTaba', '    TempA<TempB<TempA<TempB<A> > > > GetTababa2();', 'GetTababa2'),
    (1239, 94, 45, 1239, '    TempA<TempB<TempA<TempB<A> > > > GetTabab', '    TempA<TempB<TempA<TempB<A> > > > GetTababa2();', 'GetTababa2'),
    (1240, 94, 46, 1240, '    TempA<TempB<TempA<TempB<A> > > > GetTababa', '    TempA<TempB<TempA<TempB<A> > > > GetTababa2();', 'GetTababa2'),
    (1241, 94, 47, 1241, '    TempA<TempB<TempA<TempB<A> > > > GetTababa2', '    TempA<TempB<TempA<TempB<A> > > > GetTababa2();', 'GetTababa2'),
    (1242, 94, 48, 1242, '    TempA<TempB<TempA<TempB<A> > > > GetTababa2(', '    TempA<TempB<TempA<TempB<A> > > > GetTababa2();', ''),
    (1243, 94, 49, 1243, '    TempA<TempB<TempA<TempB<A> > > > GetTababa2()', '    TempA<TempB<TempA<TempB<A> > > > GetTababa2();', ''),
    (1244, 94, 50, 1244, '    TempA<TempB<TempA<TempB<A> > > > GetTababa2();', '    TempA<TempB<TempA<TempB<A> > > > GetTababa2();', ''),
    (1245, 94, 51, 1245, '', '', ''),
    (1246, 95, 1, 1246, ' ', '    TempA<TempB<TempA<TempB<A> > > > mTababa2;', ''),
    (1247, 95, 2, 1247, '  ', '    TempA<TempB<TempA<TempB<A> > > > mTababa2;', ''),
    (1248, 95, 3, 1248, '   ', '    TempA<TempB<TempA<TempB<A> > > > mTababa2;', ''),
    (1249, 95, 4, 1249, '    ', '    TempA<TempB<TempA<TempB<A> > > > mTababa2;', ''),
    (1250, 95, 5, 1250, '    T', '    TempA<TempB<TempA<TempB<A> > > > mTababa2;', 'TempA'),
    (1251, 95, 6, 1251, '    Te', '    TempA<TempB<TempA<TempB<A> > > > mTababa2;', 'TempA'),
    (1252, 95, 7, 1252, '    Tem', '    TempA<TempB<TempA<TempB<A> > > > mTababa2;', 'TempA'),
    (1253, 95, 8, 1253, '    Temp', '    TempA<TempB<TempA<TempB<A> > > > mTababa2;', 'TempA'),
    (1254, 95, 9, 1254, '    TempA', '    TempA<TempB<TempA<TempB<A> > > > mTababa2;', 'TempA'),
    (1255, 95, 10, 1255, '    TempA<', '    TempA<TempB<TempA<TempB<A> > > > mTababa2;', ''),
    (1256, 95, 11, 1256, '    TempA<T', '    TempA<TempB<TempA<TempB<A> > > > mTababa2;', 'TempB'),
    (1257, 95, 12, 1257, '    TempA<Te', '    TempA<TempB<TempA<TempB<A> > > > mTababa2;', 'TempB'),
    (1258, 95, 13, 1258, '    TempA<Tem', '    TempA<TempB<TempA<TempB<A> > > > mTababa2;', 'TempB'),
    (1259, 95, 14, 1259, '    TempA<Temp', '    TempA<TempB<TempA<TempB<A> > > > mTababa2;', 'TempB'),
    (1260, 95, 15, 1260, '    TempA<TempB', '    TempA<TempB<TempA<TempB<A> > > > mTababa2;', 'TempB'),
    (1261, 95, 16, 1261, '    TempA<TempB<', '    TempA<TempB<TempA<TempB<A> > > > mTababa2;', ''),
    (1262, 95, 17, 1262, '    TempA<TempB<T', '    TempA<TempB<TempA<TempB<A> > > > mTababa2;', 'TempA'),
    (1263, 95, 18, 1263, '    TempA<TempB<Te', '    TempA<TempB<TempA<TempB<A> > > > mTababa2;', 'TempA'),
    (1264, 95, 19, 1264, '    TempA<TempB<Tem', '    TempA<TempB<TempA<TempB<A> > > > mTababa2;', 'TempA'),
    (1265, 95, 20, 1265, '    TempA<TempB<Temp', '    TempA<TempB<TempA<TempB<A> > > > mTababa2;', 'TempA'),
    (1266, 95, 21, 1266, '    TempA<TempB<TempA', '    TempA<TempB<TempA<TempB<A> > > > mTababa2;', 'TempA'),
    (1267, 95, 22, 1267, '    TempA<TempB<TempA<', '    TempA<TempB<TempA<TempB<A> > > > mTababa2;', ''),
    (1268, 95, 23, 1268, '    TempA<TempB<TempA<T', '    TempA<TempB<TempA<TempB<A> > > > mTababa2;', 'TempB'),
    (1269, 95, 24, 1269, '    TempA<TempB<TempA<Te', '    TempA<TempB<TempA<TempB<A> > > > mTababa2;', 'TempB'),
    (1270, 95, 25, 1270, '    TempA<TempB<TempA<Tem', '    TempA<TempB<TempA<TempB<A> > > > mTababa2;', 'TempB'),
    (1271, 95, 26, 1271, '    TempA<TempB<TempA<Temp', '    TempA<TempB<TempA<TempB<A> > > > mTababa2;', 'TempB'),
    (1272, 95, 27, 1272, '    TempA<TempB<TempA<TempB', '    TempA<TempB<TempA<TempB<A> > > > mTababa2;', 'TempB'),
    (1273, 95, 28, 1273, '    TempA<TempB<TempA<TempB<', '    TempA<TempB<TempA<TempB<A> > > > mTababa2;', ''),
    (1274, 95, 29, 1274, '    TempA<TempB<TempA<TempB<A', '    TempA<TempB<TempA<TempB<A> > > > mTababa2;', 'A'),
    (1275, 95, 30, 1275, '    TempA<TempB<TempA<TempB<A>', '    TempA<TempB<TempA<TempB<A> > > > mTababa2;', ''),
    (1276, 95, 31, 1276, '    TempA<TempB<TempA<TempB<A> ', '    TempA<TempB<TempA<TempB<A> > > > mTababa2;', ''),
    (1277, 95, 32, 1277, '    TempA<TempB<TempA<TempB<A> >', '    TempA<TempB<TempA<TempB<A> > > > mTababa2;', ''),
    (1278, 95, 33, 1278, '    TempA<TempB<TempA<TempB<A> > ', '    TempA<TempB<TempA<TempB<A> > > > mTababa2;', ''),
    (1279, 95, 34, 1279, '    TempA<TempB<TempA<TempB<A> > >', '    TempA<TempB<TempA<TempB<A> > > > mTababa2;', ''),
    (1280, 95, 35, 1280, '    TempA<TempB<TempA<TempB<A> > > ', '    TempA<TempB<TempA<TempB<A> > > > mTababa2;', ''),
    (1281, 95, 36, 1281, '    TempA<TempB<TempA<TempB<A> > > >', '    TempA<TempB<TempA<TempB<A> > > > mTababa2;', ''),
    (1282, 95, 37, 1282, '    TempA<TempB<TempA<TempB<A> > > > ', '    TempA<TempB<TempA<TempB<A> > > > mTababa2;', ''),
    (1283, 95, 38, 1283, '    TempA<TempB<TempA<TempB<A> > > > m', '    TempA<TempB<TempA<TempB<A> > > > mTababa2;', 'mTababa2'),
    (1284, 95, 39, 1284, '    TempA<TempB<TempA<TempB<A> > > > mT', '    TempA<TempB<TempA<TempB<A> > > > mTababa2;', 'mTababa2'),
    (1285, 95, 40, 1285, '    TempA<TempB<TempA<TempB<A> > > > mTa', '    TempA<TempB<TempA<TempB<A> > > > mTababa2;', 'mTababa2'),
    (1286, 95, 41, 1286, '    TempA<TempB<TempA<TempB<A> > > > mTab', '    TempA<TempB<TempA<TempB<A> > > > mTababa2;', 'mTababa2'),
    (1287, 95, 42, 1287, '    TempA<TempB<TempA<TempB<A> > > > mTaba', '    TempA<TempB<TempA<TempB<A> > > > mTababa2;', 'mTababa2'),
    (1288, 95, 43, 1288, '    TempA<TempB<TempA<TempB<A> > > > mTabab', '    TempA<TempB<TempA<TempB<A> > > > mTababa2;', 'mTababa2'),
    (1289, 95, 44, 1289, '    TempA<TempB<TempA<TempB<A> > > > mTababa', '    TempA<TempB<TempA<TempB<A> > > > mTababa2;', 'mTababa2'),
    (1290, 95, 45, 1290, '    TempA<TempB<TempA<TempB<A> > > > mTababa2', '    TempA<TempB<TempA<TempB<A> > > > mTababa2;', 'mTababa2'),
    (1291, 95, 46, 1291, '    TempA<TempB<TempA<TempB<A> > > > mTababa2;', '    TempA<TempB<TempA<TempB<A> > > > mTababa2;', ''),
    (1292, 95, 47, 1292, '', '', ''),
    (1293, 96, 1, 1293, '}', '};', ''),
    (1294, 96, 2, 1294, '};', '};', ''),
    (1295, 96, 3, 1295, '', '', ''),
    (1296, 97, 1, 1296, '', '', ''),
    (1297, 98, 1, 1297, 'T', 'Tababa_class tababa2;', 'Tababa_class'),
    (1298, 98, 2, 1298, 'Ta', 'Tababa_class tababa2;', 'Tababa_class'),
    (1299, 98, 3, 1299, 'Tab', 'Tababa_class tababa2;', 'Tababa_class'),
    (1300, 98, 4, 1300, 'Taba', 'Tababa_class tababa2;', 'Tababa_class'),
    (1301, 98, 5, 1301, 'Tabab', 'Tababa_class tababa2;', 'Tababa_class'),
    (1302, 98, 6, 1302, 'Tababa', 'Tababa_class tababa2;', 'Tababa_class'),
    (1303, 98, 7, 1303, 'Tababa_', 'Tababa_class tababa2;', 'Tababa_class'),
    (1304, 98, 8, 1304, 'Tababa_c', 'Tababa_class tababa2;', 'Tababa_class'),
    (1305, 98, 9, 1305, 'Tababa_cl', 'Tababa_class tababa2;', 'Tababa_class'),
    (1306, 98, 10, 1306, 'Tababa_cla', 'Tababa_class tababa2;', 'Tababa_class'),
    (1307, 98, 11, 1307, 'Tababa_clas', 'Tababa_class tababa2;', 'Tababa_class'),
    (1308, 98, 12, 1308, 'Tababa_class', 'Tababa_class tababa2;', 'Tababa_class'),
    (1309, 98, 13, 1309, 'Tababa_class ', 'Tababa_class tababa2;', ''),
    (1310, 98, 14, 1310, 'Tababa_class t', 'Tababa_class tababa2;', 'tababa2'),
    (1311, 98, 15, 1311, 'Tababa_class ta', 'Tababa_class tababa2;', 'tababa2'),
    (1312, 98, 16, 1312, 'Tababa_class tab', 'Tababa_class tababa2;', 'tababa2'),
    (1313, 98, 17, 1313, 'Tababa_class taba', 'Tababa_class tababa2;', 'tababa2'),
    (1314, 98, 18, 1314, 'Tababa_class tabab', 'Tababa_class tababa2;', 'tababa2'),
    (1315, 98, 19, 1315, 'Tababa_class tababa', 'Tababa_class tababa2;', 'tababa2'),
    (1316, 98, 20, 1316, 'Tababa_class tababa2', 'Tababa_class tababa2;', 'tababa2'),
    (1317, 98, 21, 1317, 'Tababa_class tababa2;', 'Tababa_class tababa2;', ''),
    (1318, 98, 22, 1318, '', '', ''),
    (1319, 99, 1, 1319, 't', 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB().test;', 'tababa2'),
    (1320, 99, 2, 1320, 'ta', 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB().test;', 'tababa2'),
    (1321, 99, 3, 1321, 'tab', 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB().test;', 'tababa2'),
    (1322, 99, 4, 1322, 'taba', 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB().test;', 'tababa2'),
    (1323, 99, 5, 1323, 'tabab', 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB().test;', 'tababa2'),
    (1324, 99, 6, 1324, 'tababa', 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB().test;', 'tababa2'),
    (1325, 99, 7, 1325, 'tababa2', 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB().test;', 'tababa2'),
    (1326, 99, 8, 1326, 'tababa2.', 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB().test;', ''),
    (1327, 99, 9, 1327, 'tababa2.G', 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB().test;', 'GetTababa'),
    (1328, 99, 10, 1328, 'tababa2.Ge', 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB().test;', 'GetTababa'),
    (1329, 99, 11, 1329, 'tababa2.Get', 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB().test;', 'GetTababa'),
    (1330, 99, 12, 1330, 'tababa2.GetT', 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB().test;', 'GetTababa'),
    (1331, 99, 13, 1331, 'tababa2.GetTa', 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB().test;', 'GetTababa'),
    (1332, 99, 14, 1332, 'tababa2.GetTab', 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB().test;', 'GetTababa'),
    (1333, 99, 15, 1333, 'tababa2.GetTaba', 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB().test;', 'GetTababa'),
    (1334, 99, 16, 1334, 'tababa2.GetTabab', 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB().test;', 'GetTababa'),
    (1335, 99, 17, 1335, 'tababa2.GetTababa', 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB().test;', 'GetTababa'),
    (1336, 99, 18, 1336, 'tababa2.GetTababa(', 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB().test;', ''),
    (1337, 99, 19, 1337, 'tababa2.GetTababa()', 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB().test;', ''),
    (1338, 99, 20, 1338, 'tababa2.GetTababa().', 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB().test;', ''),
    (1339, 99, 21, 1339, 'tababa2.GetTababa().G', 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB().test;', 'GetT'),
    (1340, 99, 22, 1340, 'tababa2.GetTababa().Ge', 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB().test;', 'GetT'),
    (1341, 99, 23, 1341, 'tababa2.GetTababa().Get', 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB().test;', 'GetT'),
    (1342, 99, 24, 1342, 'tababa2.GetTababa().GetT', 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB().test;', 'GetT'),
    (1343, 99, 25, 1343, 'tababa2.GetTababa().GetT(', 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB().test;', ''),
    (1344, 99, 26, 1344, 'tababa2.GetTababa().GetT()', 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB().test;', ''),
    (1345, 99, 27, 1345, 'tababa2.GetTababa().GetT().', 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB().test;', ''),
    (1346, 99, 28, 1346, 'tababa2.GetTababa().GetT().G', 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB().test;', 'GetTB'),
    (1347, 99, 29, 1347, 'tababa2.GetTababa().GetT().Ge', 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB().test;', 'GetTB'),
    (1348, 99, 30, 1348, 'tababa2.GetTababa().GetT().Get', 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB().test;', 'GetTB'),
    (1349, 99, 31, 1349, 'tababa2.GetTababa().GetT().GetT', 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB().test;', 'GetTB'),
    (1350, 99, 32, 1350, 'tababa2.GetTababa().GetT().GetTB', 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB().test;', 'GetTB'),
    (1351, 99, 33, 1351, 'tababa2.GetTababa().GetT().GetTB(', 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB().test;', ''),
    (1352, 99, 34, 1352, 'tababa2.GetTababa().GetT().GetTB()', 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB().test;', ''),
    (1353, 99, 35, 1353, 'tababa2.GetTababa().GetT().GetTB().', 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB().test;', ''),
    (1354, 99, 36, 1354, 'tababa2.GetTababa().GetT().GetTB().G', 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB().test;', 'GetT'),
    (1355, 99, 37, 1355, 'tababa2.GetTababa().GetT().GetTB().Ge', 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB().test;', 'GetT'),
    (1356, 99, 38, 1356, 'tababa2.GetTababa().GetT().GetTB().Get', 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB().test;', 'GetT'),
    (1357, 99, 39, 1357, 'tababa2.GetTababa().GetT().GetTB().GetT', 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB().test;', 'GetT'),
    (1358, 99, 40, 1358, 'tababa2.GetTababa().GetT().GetTB().GetT(', 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB().test;', ''),
    (1359, 99, 41, 1359, 'tababa2.GetTababa().GetT().GetTB().GetT()', 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB().test;', ''),
    (1360, 99, 42, 1360, 'tababa2.GetTababa().GetT().GetTB().GetT().', 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB().test;', ''),
    (1361, 99, 43, 1361, 'tababa2.GetTababa().GetT().GetTB().GetT().G', 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB().test;', 'GetTB'),
    (1362, 99, 44, 1362, 'tababa2.GetTababa().GetT().GetTB().GetT().Ge', 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB().test;', 'GetTB'),
    (1363, 99, 45, 1363, 'tababa2.GetTababa().GetT().GetTB().GetT().Get', 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB().test;', 'GetTB'),
    (1364, 99, 46, 1364, 'tababa2.GetTababa().GetT().GetTB().GetT().GetT', 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB().test;', 'GetTB'),
    (1365, 99, 47, 1365, 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB', 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB().test;', 'GetTB'),
    (1366, 99, 48, 1366, 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB(', 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB().test;', ''),
    (1367, 99, 49, 1367, 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB()', 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB().test;', ''),
    (1368, 99, 50, 1368, 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB().', 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB().test;', ''),
    (1369, 99, 51, 1369, 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB().t', 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB().test;', 'test'),
    (1370, 99, 52, 1370, 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB().te', 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB().test;', 'test'),
    (1371, 99, 53, 1371, 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB().tes', 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB().test;', 'test'),
    (1372, 99, 54, 1372, 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB().test', 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB().test;', 'test'),
    (1373, 99, 55, 1373, 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB().test;', 'tababa2.GetTababa().GetT().GetTB().GetT().GetTB().test;', ''),
    (1374, 99, 56, 1374, '', '', ''),
    (1375, 100, 1, 1375, 't', 'tababa2.mTababa.GetT().GetTB().GetT().GetTB().test;', 'tababa2'),
    (1376, 100, 2, 1376, 'ta', 'tababa2.mTababa.GetT().GetTB().GetT().GetTB().test;', 'tababa2'),
    (1377, 100, 3, 1377, 'tab', 'tababa2.mTababa.GetT().GetTB().GetT().GetTB().test;', 'tababa2'),
    (1378, 100, 4, 1378, 'taba', 'tababa2.mTababa.GetT().GetTB().GetT().GetTB().test;', 'tababa2'),
    (1379, 100, 5, 1379, 'tabab', 'tababa2.mTababa.GetT().GetTB().GetT().GetTB().test;', 'tababa2'),
    (1380, 100, 6, 1380, 'tababa', 'tababa2.mTababa.GetT().GetTB().GetT().GetTB().test;', 'tababa2'),
    (1381, 100, 7, 1381, 'tababa2', 'tababa2.mTababa.GetT().GetTB().GetT().GetTB().test;', 'tababa2'),
    (1382, 100, 8, 1382, 'tababa2.', 'tababa2.mTababa.GetT().GetTB().GetT().GetTB().test;', ''),
    (1383, 100, 9, 1383, 'tababa2.m', 'tababa2.mTababa.GetT().GetTB().GetT().GetTB().test;', 'mTababa'),
    (1384, 100, 10, 1384, 'tababa2.mT', 'tababa2.mTababa.GetT().GetTB().GetT().GetTB().test;', 'mTababa'),
    (1385, 100, 11, 1385, 'tababa2.mTa', 'tababa2.mTababa.GetT().GetTB().GetT().GetTB().test;', 'mTababa'),
    (1386, 100, 12, 1386, 'tababa2.mTab', 'tababa2.mTababa.GetT().GetTB().GetT().GetTB().test;', 'mTababa'),
    (1387, 100, 13, 1387, 'tababa2.mTaba', 'tababa2.mTababa.GetT().GetTB().GetT().GetTB().test;', 'mTababa'),
    (1388, 100, 14, 1388, 'tababa2.mTabab', 'tababa2.mTababa.GetT().GetTB().GetT().GetTB().test;', 'mTababa'),
    (1389, 100, 15, 1389, 'tababa2.mTababa', 'tababa2.mTababa.GetT().GetTB().GetT().GetTB().test;', 'mTababa'),
    (1390, 100, 16, 1390, 'tababa2.mTababa.', 'tababa2.mTababa.GetT().GetTB().GetT().GetTB().test;', ''),
    (1391, 100, 17, 1391, 'tababa2.mTababa.G', 'tababa2.mTababa.GetT().GetTB().GetT().GetTB().test;', 'GetT'),
    (1392, 100, 18, 1392, 'tababa2.mTababa.Ge', 'tababa2.mTababa.GetT().GetTB().GetT().GetTB().test;', 'GetT'),
    (1393, 100, 19, 1393, 'tababa2.mTababa.Get', 'tababa2.mTababa.GetT().GetTB().GetT().GetTB().test;', 'GetT'),
    (1394, 100, 20, 1394, 'tababa2.mTababa.GetT', 'tababa2.mTababa.GetT().GetTB().GetT().GetTB().test;', 'GetT'),
    (1395, 100, 21, 1395, 'tababa2.mTababa.GetT(', 'tababa2.mTababa.GetT().GetTB().GetT().GetTB().test;', ''),
    (1396, 100, 22, 1396, 'tababa2.mTababa.GetT()', 'tababa2.mTababa.GetT().GetTB().GetT().GetTB().test;', ''),
    (1397, 100, 23, 1397, 'tababa2.mTababa.GetT().', 'tababa2.mTababa.GetT().GetTB().GetT().GetTB().test;', ''),
    (1398, 100, 24, 1398, 'tababa2.mTababa.GetT().G', 'tababa2.mTababa.GetT().GetTB().GetT().GetTB().test;', 'GetTB'),
    (1399, 100, 25, 1399, 'tababa2.mTababa.GetT().Ge', 'tababa2.mTababa.GetT().GetTB().GetT().GetTB().test;', 'GetTB'),
    (1400, 100, 26, 1400, 'tababa2.mTababa.GetT().Get', 'tababa2.mTababa.GetT().GetTB().GetT().GetTB().test;', 'GetTB'),
    (1401, 100, 27, 1401, 'tababa2.mTababa.GetT().GetT', 'tababa2.mTababa.GetT().GetTB().GetT().GetTB().test;', 'GetTB'),
    (1402, 100, 28, 1402, 'tababa2.mTababa.GetT().GetTB', 'tababa2.mTababa.GetT().GetTB().GetT().GetTB().test;', 'GetTB'),
    (1403, 100, 29, 1403, 'tababa2.mTababa.GetT().GetTB(', 'tababa2.mTababa.GetT().GetTB().GetT().GetTB().test;', ''),
    (1404, 100, 30, 1404, 'tababa2.mTababa.GetT().GetTB()', 'tababa2.mTababa.GetT().GetTB().GetT().GetTB().test;', ''),
    (1405, 100, 31, 1405, 'tababa2.mTababa.GetT().GetTB().', 'tababa2.mTababa.GetT().GetTB().GetT().GetTB().test;', ''),
    (1406, 100, 32, 1406, 'tababa2.mTababa.GetT().GetTB().G', 'tababa2.mTababa.GetT().GetTB().GetT().GetTB().test;', 'GetT'),
    (1407, 100, 33, 1407, 'tababa2.mTababa.GetT().GetTB().Ge', 'tababa2.mTababa.GetT().GetTB().GetT().GetTB().test;', 'GetT'),
    (1408, 100, 34, 1408, 'tababa2.mTababa.GetT().GetTB().Get', 'tababa2.mTababa.GetT().GetTB().GetT().GetTB().test;', 'GetT'),
    (1409, 100, 35, 1409, 'tababa2.mTababa.GetT().GetTB().GetT', 'tababa2.mTababa.GetT().GetTB().GetT().GetTB().test;', 'GetT'),
    (1410, 100, 36, 1410, 'tababa2.mTababa.GetT().GetTB().GetT(', 'tababa2.mTababa.GetT().GetTB().GetT().GetTB().test;', ''),
    (1411, 100, 37, 1411, 'tababa2.mTababa.GetT().GetTB().GetT()', 'tababa2.mTababa.GetT().GetTB().GetT().GetTB().test;', ''),
    (1412, 100, 38, 1412, 'tababa2.mTababa.GetT().GetTB().GetT().', 'tababa2.mTababa.GetT().GetTB().GetT().GetTB().test;', ''),
    (1413, 100, 39, 1413, 'tababa2.mTababa.GetT().GetTB().GetT().G', 'tababa2.mTababa.GetT().GetTB().GetT().GetTB().test;', 'GetTB'),
    (1414, 100, 40, 1414, 'tababa2.mTababa.GetT().GetTB().GetT().Ge', 'tababa2.mTababa.GetT().GetTB().GetT().GetTB().test;', 'GetTB'),
    (1415, 100, 41, 1415, 'tababa2.mTababa.GetT().GetTB().GetT().Get', 'tababa2.mTababa.GetT().GetTB().GetT().GetTB().test;', 'GetTB'),
    (1416, 100, 42, 1416, 'tababa2.mTababa.GetT().GetTB().GetT().GetT', 'tababa2.mTababa.GetT().GetTB().GetT().GetTB().test;', 'GetTB'),
    (1417, 100, 43, 1417, 'tababa2.mTababa.GetT().GetTB().GetT().GetTB', 'tababa2.mTababa.GetT().GetTB().GetT().GetTB().test;', 'GetTB'),
    (1418, 100, 44, 1418, 'tababa2.mTababa.GetT().GetTB().GetT().GetTB(', 'tababa2.mTababa.GetT().GetTB().GetT().GetTB().test;', ''),
    (1419, 100, 45, 1419, 'tababa2.mTababa.GetT().GetTB().GetT().GetTB()', 'tababa2.mTababa.GetT().GetTB().GetT().GetTB().test;', ''),
    (1420, 100, 46, 1420, 'tababa2.mTababa.GetT().GetTB().GetT().GetTB().', 'tababa2.mTababa.GetT().GetTB().GetT().GetTB().test;', ''),
    (1421, 100, 47, 1421, 'tababa2.mTababa.GetT().GetTB().GetT().GetTB().t', 'tababa2.mTababa.GetT().GetTB().GetT().GetTB().test;', 'test'),
    (1422, 100, 48, 1422, 'tababa2.mTababa.GetT().GetTB().GetT().GetTB().te', 'tababa2.mTababa.GetT().GetTB().GetT().GetTB().test;', 'test'),
    (1423, 100, 49, 1423, 'tababa2.mTababa.GetT().GetTB().GetT().GetTB().tes', 'tababa2.mTababa.GetT().GetTB().GetT().GetTB().test;', 'test'),
    (1424, 100, 50, 1424, 'tababa2.mTababa.GetT().GetTB().GetT().GetTB().test', 'tababa2.mTababa.GetT().GetTB().GetT().GetTB().test;', 'test'),
    (1425, 100, 51, 1425, 'tababa2.mTababa.GetT().GetTB().GetT().GetTB().test;', 'tababa2.mTababa.GetT().GetTB().GetT().GetTB().test;', ''),
    (1426, 100, 52, 1426, '', '', ''),
    (1427, 101, 1, 1427, '', '', ''),
    (1428, 102, 1, 1428, '', '', ''),
    (1429, 103, 1, 1429, '#', '#include <string>', ''),
    (1430, 103, 2, 1430, '#i', '#include <string>', 'include'),
    (1431, 103, 3, 1431, '#in', '#include <string>', 'include'),
    (1432, 103, 4, 1432, '#inc', '#include <string>', 'include'),
    (1433, 103, 5, 1433, '#incl', '#include <string>', 'include'),
    (1434, 103, 6, 1434, '#inclu', '#include <string>', 'include'),
    (1435, 103, 7, 1435, '#includ', '#include <string>', 'include'),
    (1436, 103, 8, 1436, '#include', '#include <string>', 'include'),
    (1437, 103, 9, 1437, '#include ', '#include <string>', ''),
    (1438, 103, 10, 1438, '#include <', '#include <string>', ''),
    (1439, 103, 11, 1439, '#include <s', '#include <string>', 'string'),
    (1440, 103, 12, 1440, '#include <st', '#include <string>', 'string'),
    (1441, 103, 13, 1441, '#include <str', '#include <string>', 'string'),
    (1442, 103, 14, 1442, '#include <stri', '#include <string>', 'string'),
    (1443, 103, 15, 1443, '#include <strin', '#include <string>', 'string'),
    (1444, 103, 16, 1444, '#include <string', '#include <string>', 'string'),
    (1445, 103, 17, 1445, '#include <string>', '#include <string>', ''),
    (1446, 103, 18, 1446, '', '', ''),
    (1447, 104, 1, 1447, '#', '#include <boost/shared_ptr.hpp>', ''),
    (1448, 104, 2, 1448, '#i', '#include <boost/shared_ptr.hpp>', 'include'),
    (1449, 104, 3, 1449, '#in', '#include <boost/shared_ptr.hpp>', 'include'),
    (1450, 104, 4, 1450, '#inc', '#include <boost/shared_ptr.hpp>', 'include'),
    (1451, 104, 5, 1451, '#incl', '#include <boost/shared_ptr.hpp>', 'include'),
    (1452, 104, 6, 1452, '#inclu', '#include <boost/shared_ptr.hpp>', 'include'),
    (1453, 104, 7, 1453, '#includ', '#include <boost/shared_ptr.hpp>', 'include'),
    (1454, 104, 8, 1454, '#include', '#include <boost/shared_ptr.hpp>', 'include'),
    (1455, 104, 9, 1455, '#include ', '#include <boost/shared_ptr.hpp>', ''),
    (1456, 104, 10, 1456, '#include <', '#include <boost/shared_ptr.hpp>', ''),
    (1457, 104, 11, 1457, '#include <b', '#include <boost/shared_ptr.hpp>', 'boost'),
    (1458, 104, 12, 1458, '#include <bo', '#include <boost/shared_ptr.hpp>', 'boost'),
    (1459, 104, 13, 1459, '#include <boo', '#include <boost/shared_ptr.hpp>', 'boost'),
    (1460, 104, 14, 1460, '#include <boos', '#include <boost/shared_ptr.hpp>', 'boost'),
    (1461, 104, 15, 1461, '#include <boost', '#include <boost/shared_ptr.hpp>', 'boost'),
    (1462, 104, 16, 1462, '#include <boost/', '#include <boost/shared_ptr.hpp>', ''),
    (1463, 104, 17, 1463, '#include <boost/s', '#include <boost/shared_ptr.hpp>', 'shared_ptr'),
    (1464, 104, 18, 1464, '#include <boost/sh', '#include <boost/shared_ptr.hpp>', 'shared_ptr'),
    (1465, 104, 19, 1465, '#include <boost/sha', '#include <boost/shared_ptr.hpp>', 'shared_ptr'),
    (1466, 104, 20, 1466, '#include <boost/shar', '#include <boost/shared_ptr.hpp>', 'shared_ptr'),
    (1467, 104, 21, 1467, '#include <boost/share', '#include <boost/shared_ptr.hpp>', 'shared_ptr'),
    (1468, 104, 22, 1468, '#include <boost/shared', '#include <boost/shared_ptr.hpp>', 'shared_ptr'),
    (1469, 104, 23, 1469, '#include <boost/shared_', '#include <boost/shared_ptr.hpp>', 'shared_ptr'),
    (1470, 104, 24, 1470, '#include <boost/shared_p', '#include <boost/shared_ptr.hpp>', 'shared_ptr'),
    (1471, 104, 25, 1471, '#include <boost/shared_pt', '#include <boost/shared_ptr.hpp>', 'shared_ptr'),
    (1472, 104, 26, 1472, '#include <boost/shared_ptr', '#include <boost/shared_ptr.hpp>', 'shared_ptr'),
    (1473, 104, 27, 1473, '#include <boost/shared_ptr.', '#include <boost/shared_ptr.hpp>', ''),
    (1474, 104, 28, 1474, '#include <boost/shared_ptr.h', '#include <boost/shared_ptr.hpp>', 'hpp'),
    (1475, 104, 29, 1475, '#include <boost/shared_ptr.hp', '#include <boost/shared_ptr.hpp>', 'hpp'),
    (1476, 104, 30, 1476, '#include <boost/shared_ptr.hpp', '#include <boost/shared_ptr.hpp>', 'hpp'),
    (1477, 104, 31, 1477, '#include <boost/shared_ptr.hpp>', '#include <boost/shared_ptr.hpp>', ''),
    (1478, 104, 32, 1478, '', '', ''),
    (1479, 105, 1, 1479, '', '', ''),
    (1480, 106, 1, 1480, 's', 'std::string str;', 'std'),
    (1481, 106, 2, 1481, 'st', 'std::string str;', 'std'),
    (1482, 106, 3, 1482, 'std', 'std::string str;', 'std'),
    (1483, 106, 4, 1483, 'std:', 'std::string str;', ''),
    (1484, 106, 5, 1484, 'std::', 'std::string str;', ''),
    (1485, 106, 6, 1485, 'std::s', 'std::string str;', 'string'),
    (1486, 106, 7, 1486, 'std::st', 'std::string str;', 'string'),
    (1487, 106, 8, 1487, 'std::str', 'std::string str;', 'string'),
    (1488, 106, 9, 1488, 'std::stri', 'std::string str;', 'string'),
    (1489, 106, 10, 1489, 'std::strin', 'std::string str;', 'string'),
    (1490, 106, 11, 1490, 'std::string', 'std::string str;', 'string'),
    (1491, 106, 12, 1491, 'std::string ', 'std::string str;', ''),
    (1492, 106, 13, 1492, 'std::string s', 'std::string str;', 'str'),
    (1493, 106, 14, 1493, 'std::string st', 'std::string str;', 'str'),
    (1494, 106, 15, 1494, 'std::string str', 'std::string str;', 'str'),
    (1495, 106, 16, 1495, 'std::string str;', 'std::string str;', ''),
    (1496, 106, 17, 1496, '', '', ''),
    (1497, 107, 1, 1497, 's', 'str.c_str();', 'str'),
    (1498, 107, 2, 1498, 'st', 'str.c_str();', 'str'),
    (1499, 107, 3, 1499, 'str', 'str.c_str();', 'str'),
    (1500, 107, 4, 1500, 'str.', 'str.c_str();', ''),
    (1501, 107, 5, 1501, 'str.c', 'str.c_str();', 'c_str'),
    (1502, 107, 6, 1502, 'str.c_', 'str.c_str();', 'c_str'),
    (1503, 107, 7, 1503, 'str.c_s', 'str.c_str();', 'c_str'),
    (1504, 107, 8, 1504, 'str.c_st', 'str.c_str();', 'c_str'),
    (1505, 107, 9, 1505, 'str.c_str', 'str.c_str();', 'c_str'),
    (1506, 107, 10, 1506, 'str.c_str(', 'str.c_str();', ''),
    (1507, 107, 11, 1507, 'str.c_str()', 'str.c_str();', ''),
    (1508, 107, 12, 1508, 'str.c_str();', 'str.c_str();', ''),
    (1509, 107, 13, 1509, '', '', ''),
    (1510, 108, 1, 1510, '', '', ''),
    (1511, 109, 1, 1511, 'b', 'boost::shared_ptr<std::vector<std::string> > strtest;', 'boost'),
    (1512, 109, 2, 1512, 'bo', 'boost::shared_ptr<std::vector<std::string> > strtest;', 'boost'),
    (1513, 109, 3, 1513, 'boo', 'boost::shared_ptr<std::vector<std::string> > strtest;', 'boost'),
    (1514, 109, 4, 1514, 'boos', 'boost::shared_ptr<std::vector<std::string> > strtest;', 'boost'),
    (1515, 109, 5, 1515, 'boost', 'boost::shared_ptr<std::vector<std::string> > strtest;', 'boost'),
    (1516, 109, 6, 1516, 'boost:', 'boost::shared_ptr<std::vector<std::string> > strtest;', ''),
    (1517, 109, 7, 1517, 'boost::', 'boost::shared_ptr<std::vector<std::string> > strtest;', ''),
    (1518, 109, 8, 1518, 'boost::s', 'boost::shared_ptr<std::vector<std::string> > strtest;', 'shared_ptr'),
    (1519, 109, 9, 1519, 'boost::sh', 'boost::shared_ptr<std::vector<std::string> > strtest;', 'shared_ptr'),
    (1520, 109, 10, 1520, 'boost::sha', 'boost::shared_ptr<std::vector<std::string> > strtest;', 'shared_ptr'),
    (1521, 109, 11, 1521, 'boost::shar', 'boost::shared_ptr<std::vector<std::string> > strtest;', 'shared_ptr'),
    (1522, 109, 12, 1522, 'boost::share', 'boost::shared_ptr<std::vector<std::string> > strtest;', 'shared_ptr'),
    (1523, 109, 13, 1523, 'boost::shared', 'boost::shared_ptr<std::vector<std::string> > strtest;', 'shared_ptr'),
    (1524, 109, 14, 1524, 'boost::shared_', 'boost::shared_ptr<std::vector<std::string> > strtest;', 'shared_ptr'),
    (1525, 109, 15, 1525, 'boost::shared_p', 'boost::shared_ptr<std::vector<std::string> > strtest;', 'shared_ptr'),
    (1526, 109, 16, 1526, 'boost::shared_pt', 'boost::shared_ptr<std::vector<std::string> > strtest;', 'shared_ptr'),
    (1527, 109, 17, 1527, 'boost::shared_ptr', 'boost::shared_ptr<std::vector<std::string> > strtest;', 'shared_ptr'),
    (1528, 109, 18, 1528, 'boost::shared_ptr<', 'boost::shared_ptr<std::vector<std::string> > strtest;', ''),
    (1529, 109, 19, 1529, 'boost::shared_ptr<s', 'boost::shared_ptr<std::vector<std::string> > strtest;', 'std'),
    (1530, 109, 20, 1530, 'boost::shared_ptr<st', 'boost::shared_ptr<std::vector<std::string> > strtest;', 'std'),
    (1531, 109, 21, 1531, 'boost::shared_ptr<std', 'boost::shared_ptr<std::vector<std::string> > strtest;', 'std'),
    (1532, 109, 22, 1532, 'boost::shared_ptr<std:', 'boost::shared_ptr<std::vector<std::string> > strtest;', ''),
    (1533, 109, 23, 1533, 'boost::shared_ptr<std::', 'boost::shared_ptr<std::vector<std::string> > strtest;', ''),
    (1534, 109, 24, 1534, 'boost::shared_ptr<std::v', 'boost::shared_ptr<std::vector<std::string> > strtest;', 'vector'),
    (1535, 109, 25, 1535, 'boost::shared_ptr<std::ve', 'boost::shared_ptr<std::vector<std::string> > strtest;', 'vector'),
    (1536, 109, 26, 1536, 'boost::shared_ptr<std::vec', 'boost::shared_ptr<std::vector<std::string> > strtest;', 'vector'),
    (1537, 109, 27, 1537, 'boost::shared_ptr<std::vect', 'boost::shared_ptr<std::vector<std::string> > strtest;', 'vector'),
    (1538, 109, 28, 1538, 'boost::shared_ptr<std::vecto', 'boost::shared_ptr<std::vector<std::string> > strtest;', 'vector'),
    (1539, 109, 29, 1539, 'boost::shared_ptr<std::vector', 'boost::shared_ptr<std::vector<std::string> > strtest;', 'vector'),
    (1540, 109, 30, 1540, 'boost::shared_ptr<std::vector<', 'boost::shared_ptr<std::vector<std::string> > strtest;', ''),
    (1541, 109, 31, 1541, 'boost::shared_ptr<std::vector<s', 'boost::shared_ptr<std::vector<std::string> > strtest;', 'std'),
    (1542, 109, 32, 1542, 'boost::shared_ptr<std::vector<st', 'boost::shared_ptr<std::vector<std::string> > strtest;', 'std'),
    (1543, 109, 33, 1543, 'boost::shared_ptr<std::vector<std', 'boost::shared_ptr<std::vector<std::string> > strtest;', 'std'),
    (1544, 109, 34, 1544, 'boost::shared_ptr<std::vector<std:', 'boost::shared_ptr<std::vector<std::string> > strtest;', ''),
    (1545, 109, 35, 1545, 'boost::shared_ptr<std::vector<std::', 'boost::shared_ptr<std::vector<std::string> > strtest;', ''),
    (1546, 109, 36, 1546, 'boost::shared_ptr<std::vector<std::s', 'boost::shared_ptr<std::vector<std::string> > strtest;', 'string'),
    (1547, 109, 37, 1547, 'boost::shared_ptr<std::vector<std::st', 'boost::shared_ptr<std::vector<std::string> > strtest;', 'string'),
    (1548, 109, 38, 1548, 'boost::shared_ptr<std::vector<std::str', 'boost::shared_ptr<std::vector<std::string> > strtest;', 'string'),
    (1549, 109, 39, 1549, 'boost::shared_ptr<std::vector<std::stri', 'boost::shared_ptr<std::vector<std::string> > strtest;', 'string'),
    (1550, 109, 40, 1550, 'boost::shared_ptr<std::vector<std::strin', 'boost::shared_ptr<std::vector<std::string> > strtest;', 'string'),
    (1551, 109, 41, 1551, 'boost::shared_ptr<std::vector<std::string', 'boost::shared_ptr<std::vector<std::string> > strtest;', 'string'),
    (1552, 109, 42, 1552, 'boost::shared_ptr<std::vector<std::string>', 'boost::shared_ptr<std::vector<std::string> > strtest;', ''),
    (1553, 109, 43, 1553, 'boost::shared_ptr<std::vector<std::string> ', 'boost::shared_ptr<std::vector<std::string> > strtest;', ''),
    (1554, 109, 44, 1554, 'boost::shared_ptr<std::vector<std::string> >', 'boost::shared_ptr<std::vector<std::string> > strtest;', ''),
    (1555, 109, 45, 1555, 'boost::shared_ptr<std::vector<std::string> > ', 'boost::shared_ptr<std::vector<std::string> > strtest;', ''),
    (1556, 109, 46, 1556, 'boost::shared_ptr<std::vector<std::string> > s', 'boost::shared_ptr<std::vector<std::string> > strtest;', 'strtest'),
    (1557, 109, 47, 1557, 'boost::shared_ptr<std::vector<std::string> > st', 'boost::shared_ptr<std::vector<std::string> > strtest;', 'strtest'),
    (1558, 109, 48, 1558, 'boost::shared_ptr<std::vector<std::string> > str', 'boost::shared_ptr<std::vector<std::string> > strtest;', 'strtest'),
    (1559, 109, 49, 1559, 'boost::shared_ptr<std::vector<std::string> > strt', 'boost::shared_ptr<std::vector<std::string> > strtest;', 'strtest'),
    (1560, 109, 50, 1560, 'boost::shared_ptr<std::vector<std::string> > strte', 'boost::shared_ptr<std::vector<std::string> > strtest;', 'strtest'),
    (1561, 109, 51, 1561, 'boost::shared_ptr<std::vector<std::string> > strtes', 'boost::shared_ptr<std::vector<std::string> > strtest;', 'strtest'),
    (1562, 109, 52, 1562, 'boost::shared_ptr<std::vector<std::string> > strtest', 'boost::shared_ptr<std::vector<std::string> > strtest;', 'strtest'),
    (1563, 109, 53, 1563, 'boost::shared_ptr<std::vector<std::string> > strtest;', 'boost::shared_ptr<std::vector<std::string> > strtest;', ''),
    (1564, 109, 54, 1564, '', '', ''),
    (1565, 110, 1, 1565, 's', 'strtest.reset();', 'strtest'),
    (1566, 110, 2, 1566, 'st', 'strtest.reset();', 'strtest'),
    (1567, 110, 3, 1567, 'str', 'strtest.reset();', 'strtest'),
    (1568, 110, 4, 1568, 'strt', 'strtest.reset();', 'strtest'),
    (1569, 110, 5, 1569, 'strte', 'strtest.reset();', 'strtest'),
    (1570, 110, 6, 1570, 'strtes', 'strtest.reset();', 'strtest'),
    (1571, 110, 7, 1571, 'strtest', 'strtest.reset();', 'strtest'),
    (1572, 110, 8, 1572, 'strtest.', 'strtest.reset();', ''),
    (1573, 110, 9, 1573, 'strtest.r', 'strtest.reset();', 'reset'),
    (1574, 110, 10, 1574, 'strtest.re', 'strtest.reset();', 'reset'),
    (1575, 110, 11, 1575, 'strtest.res', 'strtest.reset();', 'reset'),
    (1576, 110, 12, 1576, 'strtest.rese', 'strtest.reset();', 'reset'),
    (1577, 110, 13, 1577, 'strtest.reset', 'strtest.reset();', 'reset'),
    (1578, 110, 14, 1578, 'strtest.reset(', 'strtest.reset();', ''),
    (1579, 110, 15, 1579, 'strtest.reset()', 'strtest.reset();', ''),
    (1580, 110, 16, 1580, 'strtest.reset();', 'strtest.reset();', ''),
    (1581, 110, 17, 1581, '', '', ''),
    (1582, 111, 1, 1582, 's', 'strtest->back()->c_str();', 'strtest'),
    (1583, 111, 2, 1583, 'st', 'strtest->back()->c_str();', 'strtest'),
    (1584, 111, 3, 1584, 'str', 'strtest->back()->c_str();', 'strtest'),
    (1585, 111, 4, 1585, 'strt', 'strtest->back()->c_str();', 'strtest'),
    (1586, 111, 5, 1586, 'strte', 'strtest->back()->c_str();', 'strtest'),
    (1587, 111, 6, 1587, 'strtes', 'strtest->back()->c_str();', 'strtest'),
    (1588, 111, 7, 1588, 'strtest', 'strtest->back()->c_str();', 'strtest'),
    (1589, 111, 8, 1589, 'strtest-', 'strtest->back()->c_str();', ''),
    (1590, 111, 9, 1590, 'strtest->', 'strtest->back()->c_str();', ''),
    (1591, 111, 10, 1591, 'strtest->b', 'strtest->back()->c_str();', 'back'),
    (1592, 111, 11, 1592, 'strtest->ba', 'strtest->back()->c_str();', 'back'),
    (1593, 111, 12, 1593, 'strtest->bac', 'strtest->back()->c_str();', 'back'),
    (1594, 111, 13, 1594, 'strtest->back', 'strtest->back()->c_str();', 'back'),
    (1595, 111, 14, 1595, 'strtest->back(', 'strtest->back()->c_str();', ''),
    (1596, 111, 15, 1596, 'strtest->back()', 'strtest->back()->c_str();', ''),
    (1597, 111, 16, 1597, 'strtest->back()-', 'strtest->back()->c_str();', ''),
    (1598, 111, 17, 1598, 'strtest->back()->', 'strtest->back()->c_str();', ''),
    (1599, 111, 18, 1599, 'strtest->back()->c', 'strtest->back()->c_str();', 'c_str'),
    (1600, 111, 19, 1600, 'strtest->back()->c_', 'strtest->back()->c_str();', 'c_str'),
    (1601, 111, 20, 1601, 'strtest->back()->c_s', 'strtest->back()->c_str();', 'c_str'),
    (1602, 111, 21, 1602, 'strtest->back()->c_st', 'strtest->back()->c_str();', 'c_str'),
    (1603, 111, 22, 1603, 'strtest->back()->c_str', 'strtest->back()->c_str();', 'c_str'),
    (1604, 111, 23, 1604, 'strtest->back()->c_str(', 'strtest->back()->c_str();', ''),
    (1605, 111, 24, 1605, 'strtest->back()->c_str()', 'strtest->back()->c_str();', ''),
    (1606, 111, 25, 1606, 'strtest->back()->c_str();', 'strtest->back()->c_str();', ''),
    (1607, 111, 26, 1607, '', '', ''),
    (1608, 112, 1, 1608, '', '', ''),
    (1609, 113, 1, 1609, 'i', 'int test(AV& v)', 'int'),
    (1610, 113, 2, 1610, 'in', 'int test(AV& v)', 'int'),
    (1611, 113, 3, 1611, 'int', 'int test(AV& v)', 'int'),
    (1612, 113, 4, 1612, 'int ', 'int test(AV& v)', ''),
    (1613, 113, 5, 1613, 'int t', 'int test(AV& v)', 'test'),
    (1614, 113, 6, 1614, 'int te', 'int test(AV& v)', 'test'),
    (1615, 113, 7, 1615, 'int tes', 'int test(AV& v)', 'test'),
    (1616, 113, 8, 1616, 'int test', 'int test(AV& v)', 'test'),
    (1617, 113, 9, 1617, 'int test(', 'int test(AV& v)', ''),
    (1618, 113, 10, 1618, 'int test(A', 'int test(AV& v)', 'AV'),
    (1619, 113, 11, 1619, 'int test(AV', 'int test(AV& v)', 'AV'),
    (1620, 113, 12, 1620, 'int test(AV&', 'int test(AV& v)', ''),
    (1621, 113, 13, 1621, 'int test(AV& ', 'int test(AV& v)', ''),
    (1622, 113, 14, 1622, 'int test(AV& v', 'int test(AV& v)', 'v'),
    (1623, 113, 15, 1623, 'int test(AV& v)', 'int test(AV& v)', ''),
    (1624, 113, 16, 1624, '', '', ''),
    (1625, 114, 1, 1625, '{', '{', ''),
    (1626, 114, 2, 1626, '', '', ''),
    (1627, 115, 1, 1627, ' ', '    v.back().test;', ''),
    (1628, 115, 2, 1628, '  ', '    v.back().test;', ''),
    (1629, 115, 3, 1629, '   ', '    v.back().test;', ''),
    (1630, 115, 4, 1630, '    ', '    v.back().test;', ''),
    (1631, 115, 5, 1631, '    v', '    v.back().test;', 'v'),
    (1632, 115, 6, 1632, '    v.', '    v.back().test;', ''),
    (1633, 115, 7, 1633, '    v.b', '    v.back().test;', 'back'),
    (1634, 115, 8, 1634, '    v.ba', '    v.back().test;', 'back'),
    (1635, 115, 9, 1635, '    v.bac', '    v.back().test;', 'back'),
    (1636, 115, 10, 1636, '    v.back', '    v.back().test;', 'back'),
    (1637, 115, 11, 1637, '    v.back(', '    v.back().test;', ''),
    (1638, 115, 12, 1638, '    v.back()', '    v.back().test;', ''),
    (1639, 115, 13, 1639, '    v.back().', '    v.back().test;', ''),
    (1640, 115, 14, 1640, '    v.back().t', '    v.back().test;', 'test'),
    (1641, 115, 15, 1641, '    v.back().te', '    v.back().test;', 'test'),
    (1642, 115, 16, 1642, '    v.back().tes', '    v.back().test;', 'test'),
    (1643, 115, 17, 1643, '    v.back().test', '    v.back().test;', 'test'),
    (1644, 115, 18, 1644, '    v.back().test;', '    v.back().test;', ''),
    (1645, 115, 19, 1645, '', '', ''),
    (1646, 116, 1, 1646, '}', '}', ''),
    (1647, 116, 2, 1647, '', '', ''),
    (1648, 117, 1, 1648, '', '', ''),
    (1649, 118, 1, 1649, '', '', '')
]
for i in range(len(fulldata)):
    l, c = get_line_and_column_from_offset(fulldata, i)
    i2 = get_offset_from_line_and_column(fulldata, l, c)
    myassert(i, i2)
    result = (i, l, c, i2, extract_line_until_offset(fulldata, i), extract_line_at_offset(fulldata, i), extract_word_at_offset(fulldata, i))
    myassert(result, gold_results[i])

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

myassert(extract_variables(test), [('Type&', 't1'), ('vector<Type2> &', 't2'), ('int', 'itShouldPickupThis')])

test = """Properties prop = new Properties();
int apps = Integer.parseInt(prop."""
myassert(get_type_definition(test), (1, 12, "Properties", "prop", "."))
test = """Properties prop = new Properties();
int apps = Integer.parseInt(prop.getProperty("a")."""
myassert(get_type_definition(test), (1, 12, "Properties", "prop", ".getProperty()."))

myassert(extract_completion("prop.GetColor().Clamp()."), "prop.GetColor().Clamp().")

test = """DVFSStats dvfs = new DVFSStats();
DVFSStats."""
myassert(get_type_definition(test), (-1, -1, "DVFSStats", None, "."))

test = """CPUStats.CPULoad cpuLoad = cpu.new CPULoad();
cpuLoad."""
myassert(get_type_definition(test), (1, 18, "CPUStats.CPULoad", "cpuLoad", "."))

test = """ShortcutIconResource iconRes = Intent.ShortcutIconResource.fromContext(this, R.drawable."""
myassert(get_type_definition(test), (-1, -1, "R", None, ".drawable."))

test = """Intent.FLAG_ACTIVITY_RESET_TASK_IF_NEEDED|Intent."""
myassert(get_type_definition(test), (-1, -1, "Intent", None, "."))

test = """public class LaunchApp
extends Activity
{

    @Override
    public void onCreate(Bundle b)
    {
        super.onCreate(b);
        super."""
myassert(get_type_definition(test), (-1, -1, 'Activity', 'super', '.'))

test = """                for (Class clazz : c.getClasses())
                {
                    clazz."""
myassert(get_type_definition(test), (1, 28, 'Class', 'clazz', '.'))


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

myassert(get_type_definition(test), (-1, -1, 'ContextFactory', 'this', '.'))

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

myassert(get_type_definition(test), (-1, -1, "PMQuadtree", "this", "."))

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
myassert(get_type_definition(test), (1, 8, "String[]", "args", "[]."))

test = """                        foreach (Assembly asm in AssembliesLoaded)
                        {
                            foreach (Type t3 in asm.GetTypes())
                            {
                                if (t3."""
myassert(get_type_definition(test), (3, 43, "Type", "t3", "."))

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
myassert(extract_variables(test), [('int', 'argc'), ('char const *[]', 'argv'), ('MyStruct', 'a'), ('int', 'b'), ('int', 'MyStruct'), ('int', 'z'), ('int', 'q')])

myassert(get_base_type("static const char const *[]"), "char")

test = """CacheCompletionResults* cache_complete_startswith(Cache* cache, const char *prefix)
{
    cache->complete(const char *prefix)->entries."""
myassert(get_type_definition(test), (1, 58, 'Cache*', 'cache', '->complete()->entries.'))

test = """CacheCompletionResults* cache_complete_startswith(Cache* cache, const char *prefix)
{
    cache->complete(const char *prefix)->entries[10]->"""
myassert(get_type_definition(test), (1, 58, 'Cache*', 'cache', '->complete()->entries[]->'))

test = """bool Mesh::CopyToVBO ( UInt32 wantedChannels, VBO& vbo )
{
    std::vector<abc> test();
    {
        something here
"""
myassert(extract_class_from_function(test), "Mesh")


test = """using namespace std;
using namespace std2;
using namespace some::long::namespace as s;
namespace std3
{

};

namespace std4
{"""

myassert(extract_namespace(test), "std4")

myassert(extract_used_namespaces(test), ['std', 'std2', 'some::long::namespace as s'])

test = "ArrayList<ArrayList<Integer> >"
data = solve_template(test)
myassert(data, ('ArrayList', [('ArrayList', [('Integer', None)])]))

myassert(make_template(data), test)

test = "ArrayList<Integer>"
data = solve_template(test)
myassert(data, ('ArrayList', [('Integer', None)]))

myassert(make_template(data), test)

test = "Integer"
data = solve_template(test)
myassert(data, ('Integer', None))

myassert(make_template(data), test)

test = """Type[] generic = m.getGenericParameterTypes();
generic."""
myassert(get_type_definition(test), (1, 8, 'Type[]', 'generic', '.'))

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
myassert(get_type_definition(test), (9, 130, 'P2<Node, Rectangle2D.Double>', 'p', '.'))

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
myassert(get_type_definition(test), (3, 42, 'Foo<Foo<String, String>, String>', 'foo', '.'))

myassert(make_template((u'Foo', [('java.lang.String', None), ('java.lang.String', None)])), "Foo<java.lang.String, java.lang.String>")


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
myassert(get_type_definition(test), (3, 42, 'Foo<Foo<String, String>, String>', 'foo', '.f().'))

test = """Foo<java.lang.String, Foo<Foo<java.lang.String, java.lang.String>, java.lang.String> >"""
myassert(solve_template(test), ('Foo', [('java.lang.String', None), ('Foo', [('Foo', [('java.lang.String', None), ('java.lang.String', None)]), ('java.lang.String', None)])]))

myassert(make_template(solve_template(test)), test)

test = """Tests.Tests$Foo<java.lang.String, Tests.Tests$Foo<Tests.Tests$Foo<java.lang.String, java.lang.String>, java.lang.String> >"""
myassert(solve_template(test), ('Tests.Tests$Foo', [('java.lang.String', None), ('Tests.Tests$Foo', [('Tests.Tests$Foo', [('java.lang.String', None), ('java.lang.String', None)]), ('java.lang.String', None)])]))

myassert(make_template(solve_template(test)), test)

test = """string[] argv = arg[0].Split(new string[] {sep},  StringSplitOptions.None);
            foreach (string a in argv)
            {
                argv."""
myassert(get_type_definition(test), (1, 10, 'string[]', 'argv', '.'))

test = """        public CityNew nearestCity( final Point2D p, final PriorityQueue<P2<Node, Rectangle2D.Double>> queue ) {
            if( mPoints.isNotEmpty() ) {
                return mPoints.index( 0 );
            }
            else {
                queue."""
myassert(get_type_definition(test), (1, 104, 'PriorityQueue<P2<Node, Rectangle2D.Double>>', 'queue', '.'))

test = """Archive<T1, T2> a;
    test = a << 8 | b << 16;
    test2 = a >> test | b >> 8;
    a."""
myassert(get_type_definition(test), (1, 17, 'Archive<T1, T2>', 'a', '.'))

test = """Archive<T1, T2> a;
    test = a << 8 | b << 16;
    test2 = a >> test | b >> 8;
    a->"""
myassert(get_type_definition(test), (1, 17, 'Archive<T1, T2>', 'a', '->'))

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
myassert(get_type_definition(test), (7, 104, 'PriorityQueue<P2<Node, Rectangle2D.Double>>', 'queue', '.'))

test = """    private static String getInstancedType(Class<?> c, String gen, String ret, String[] templateParam)
    {
        if (gen.startsWith("class "))
            gen = gen.substring("class ".length());
        {
            this."""
myassert(get_type_definition(test), (-1, -1, None, 'this', '.'))

test = "System.Collections.Generic.Dictionary<System.String, System.String>.ValueCollection"
myassert(solve_template(test), ('System.Collections.Generic.Dictionary', [('System.String', None), ('System.String', None)], ('ValueCollection', None)))

myassert(make_template(solve_template(test)), test)

test = "std::vector<std::string>::iterator"
myassert(solve_template(test), ('std::vector', [('std::string', None)], ('iterator', None)))

myassert(make_template(solve_template(test), "::"), test)

test = """Dictionary<string,string>.ValueCollection t;
t."""
myassert(get_type_definition(test), (1, 43, 'Dictionary<string,string>.ValueCollection', 't', '.'))

test = """std::vector<int>::iterator i;
i."""
myassert(get_type_definition(test), (1, 28, 'std::vector<int>::iterator', 'i', '.'))

test = """struct hostent *server = gethostbyname("localhost");"""
myassert(extract_variables(test), [('struct hostent *', 'server')])

myassert(get_base_type("struct hostent *"), "hostent")

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
myassert(extract_namespace(test), None)

myassert(extract_used_namespaces(test), ["android"])

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
myassert(extract_namespace(test), "one::three")

test = """
    Parcel data, reply, moredata, test;
    int a, b, c;
    reply."""
myassert(get_type_definition(test), (2, 18, 'Parcel', 'reply', '.'))

test = """
    Parcel data, reply, moredata, test;
    int a, b, c;
    moredata."""
myassert(get_type_definition(test), (2, 25, 'Parcel', 'moredata', '.'))

test = """
    Parcel data, reply, moredata, test;
    int a = 1, b = 2, c = 3;
    test."""
myassert(get_type_definition(test), (2, 35, 'Parcel', 'test', '.'))

myassert(extract_variables(test), [('Parcel', 'data'), ('Parcel', 'reply'), ('Parcel', 'moredata'), ('Parcel', 'test'), ('int', 'a'), ('int', 'b'), ('int', 'c')])

test = """    NamespaceFinder(CXCursor base, const char ** ns, unsigned int nsLength)
    : mBase(base), namespaces(ns), namespaceCount(nsLength)
    {

    }
    virtual void execute()
    {

"""
myassert(extract_variables(test), [])

test = """void OpenGLRenderer::Render(RenderNode* node)
{
    this->"""
myassert(get_type_definition(test), (-1, -1, 'OpenGLRenderer', 'this', '->'))

test = """    const SmartPointer<Attribute> &index = node->GetMesh()->GetAttribute(mIndexID);
    index."""
myassert(extract_variables(test), [('const SmartPointer<Attribute> &', 'index')])

myassert(get_type_definition(test), (1, 36, 'const SmartPointer<Attribute> &', 'index', '.'))

test = """void something(const SmartPointer<Attribute> &index) {
    index."""
myassert(extract_variables(test), [('const SmartPointer<Attribute> &', 'index')])

myassert(get_type_definition(test), (1, 47, 'const SmartPointer<Attribute> &', 'index', '.'))

test = """        std::vector<Entity*> t;
        t."""
myassert(get_type_definition(test), (1, 30, 'std::vector<Entity*>', 't', '.'))

test = """Vector3 normal(0,0,0);
normal."""
myassert(extract_variables(test), [('Vector3', 'normal')])

test = """Vector3 pos(camera->GetWorldTransform().getOrigin());"""
myassert(extract_variables(test), [('Vector3', 'pos')])

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
myassert(extract_variables(test), [('const Property', 'prop'), ('const GLTexture *', 'tex')])

test = """default: int test;"""
myassert(extract_variables(test), [('int', 'test')])

test = """BOOST_FOREACH(const Stacktrace* s, list)
    {
        GetAddresses(ss, s);
    }
    s."""
myassert(get_type_definition(test), (-1, -1, 's', None, '.'))

test = """Call::Call(const char *name, Call* parent, int callDepth)
: mName(name), mOverhead(0), mTotalTime(0), mChildTime(0), mCallCount(0), mParent(parent), mCallDepth(callDepth)
{
    """
myassert(extract_class_from_function(test), "Call")

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
myassert(get_type_definition(test), (31, 13, 'JNIEnv*', 'env', '->'))

myassert(get_type_definition("C c; c[0]."), (1, 3, 'C', 'c', '[].'))

myassert(get_type_definition("tripleA[0]."), (-1, -1, "tripleA", None, "[]."))

myassert(get_type_definition("tripleA[0]->"), (-1, -1, "tripleA", None, "[]->"))

myassert(get_type_definition("tripleA[0][0]."), (-1, -1, "tripleA", None, "[][]."))

myassert(get_type_definition("tripleA[0][0]->"), (-1, -1, "tripleA", None, "[][]->"))

myassert(get_type_definition("tripleA[0][0][0]."), (-1, -1, "tripleA", None, "[][][]."))

myassert(get_type_definition("tripleA[0][0][0]->"), (-1, -1, "tripleA", None, "[][][]->"))

myassert(get_type_definition("tripleA[0][0][0][0]."), (-1, -1, "tripleA", None, "[][][][]."))

myassert(dereference("Test**"), "Test*")
myassert(dereference("Test*"), "Test")

myassert(get_base_type("mystruct"), "mystruct")
myassert(get_base_type("myclass"), "myclass")
myassert(get_base_type("mystatic"), "mystatic")
myassert(get_base_type("struct A"), "A")
myassert(get_base_type("static A"), "A")

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
myassert(extract_variables(test), [])

test = """std::vector<int> a, b;"""
myassert(extract_variables(test), [('std::vector<int>', 'a'), ('std::vector<int>', 'b')])

myassert(get_type_definition("struct timeval t; a+t."), (1, 16, 'timeval', 't', '.'))
myassert(get_type_definition("struct timeval t; a|t."), (1, 16, 'timeval', 't', '.'))
myassert(get_type_definition("struct timeval t; a-t."), (1, 16, 'timeval', 't', '.'))
myassert(get_type_definition("struct timeval t; a*t."), (1, 16, 'timeval', 't', '.'))
myassert(get_type_definition("struct timeval t; a/t."), (1, 16, 'timeval', 't', '.'))

test = """SwapBuffersData& data = (*i).second;
        if (++data."""
myassert(get_type_definition(test), (1, 18, 'SwapBuffersData&', 'data', '.'))

test = """SwapBuffersData& data = (*i).second;
end.tv_usec-data."""
myassert(get_type_definition(test), (1, 18, 'SwapBuffersData&', 'data', '.'))

myassert(get_type_definition("[Hello "), (-1, -1, 'Hello', None, ' '))
myassert(get_type_definition("Hello *h; [h "), (1, 8, 'Hello *', 'h', ' '))
myassert(get_type_definition("World * w; [[w world] "), (1, 9, 'World *', 'w', ' world] '))
myassert(get_type_definition("World2 * w; [[[w world2] world] "), (1, 10, 'World2 *', 'w', ' world2] world] '))
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
myassert(extract_class(test), "Class3")

test = """@implementation World2
- (World*) world2
{
    [self """
myassert(get_type_definition(test), (-1, -1, 'World2', 'self', ' '))

test = """static FrameStats::Timestamp skindelta = 0;
    static int calls = 0; """
myassert(extract_variables(test), [('static FrameStats::Timestamp', 'skindelta'), ('static int', 'calls')])

myassert(get_type_definition("""Test.GetSomething2<string, int, int, int>(a, b, c)."""), (-1, -1, 'Test', None, '.GetSomething2<string, int, int, int>().'))

myassert(get_type_definition("Test t[10]; t[0]."), (1, 6, 'Test[]', 't', '[].'))

myassert(get_type_definition("Test t[10][20]; t."), (1, 6, 'Test[][]', 't', '.'))

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
myassert(extract_variables(test), [('struct mystruct', 'm'), ('enum', 'myenum'), ('static int', 'variable')])

myassert(get_type_definition("nms::function()."), (-1, -1, "nms", None, "::function()."))

test = """private static String[] getCompletion() {} String."""
myassert(get_type_definition(test), (-1, -1, 'String', None, '.'))

test = """  URL url = classLoader.getResource(s + "/" + packageName);
            if (url != null)
                return true;
            else
                url = classLoader.getResource(s);
            url."""
myassert(get_type_definition(test), (1, 7, 'URL', 'url', '.'))

test = """case kSomethingSomethingSomething:
            break;
        case kSomethingSomethingSomt"""
start = time.time()
myassert(extract_variables(test), [])
end = time.time() - start
assert end <= 0.01

myassert(extract_namespace("void Test::Class::function() {"), "Test")

test = """namespace lir
{
    #define NO_ARGUMENT lir::b()

    class a
    {
        bool operator==(const a &other) const
        {
            other."""
myassert(extract_class_from_function(test), None)
test = """Test t[1]; t[0]."""
myassert(get_type_definition(test), (1, 6, 'Test[]', 't', '[].'))

test = """typedef struct
{
    int something;
} Test;
Test t[1]; t[0]."""
myassert(get_type_definition(test), (5, 6, 'Test[]', 't', '[].'))

myassert(extract_variables("char foo[LENGTH];"), [('char[]', 'foo')])
myassert(get_type_definition("Test t; [t.context "), (1, 6, 'Test', 't', '.context '))
myassert(get_type_definition("Test t; [t.context->b "), (1, 6, 'Test', 't', '.context->b '))
myassert(get_type_definition("Test t; [[t.context->b something] "), (1, 6, 'Test', 't', '.context->b something] '))
myassert(get_type_definition("Test t; [[t.context->b something] something2]->"), (1, 6, 'Test', 't', '.context->b something] something2]->'))
myassert(get_type_definition("Test t; [[t.context->b something] something2]."), (1, 6, 'Test', 't', '.context->b something] something2].'))

data = "\n".join("\tENUM_%d = %d," % (a, a) for a in range(5000))
start = time.time()
myassert(extract_variables(data), [])
end = time.time() - start
assert end < 0.09

for char in "!+-*/[&<>(;,":
    myassert(get_type_definition("A a; %ca." %  char), (1, 3, 'A', 'a', '.'))

end = time.time() - __start
print "Tests took %f seconds" % end
assert end < 0.300

print "all is well"
