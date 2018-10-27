# Definition for a binary tree node.
# Warm up, 10-26-2018
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, x):
        self._root = TreeNode(x)
    
    def insert(self, x):
        node = TreeNode(x)
        parent = self._root
        found_position = False
        while not found_position:
            if x <= parent.val and parent.left is not None:
                parent = parent.left
            elif x <= parent.val and parent.left is None:
                parent.left = node
                found_position = True
            elif x > parent.val and parent.right is not None:
                parent = parent.right
            elif x > parent.val and parent.right is None:
                parent.right = node
                found_position = True
    
    def preorder(self, node="first call", depth=0):
        if node == "first call":
            node = self._root
        curr = node
        if curr is None:
            return
        else:
            print("|      " * depth + "+--" + str(node.val))
            self.preorder(node=curr.left, depth=depth+1)
            self.preorder(node=curr.right, depth=depth+1)

    def depth(self, node="first_call"):
        if node == "first_call":
            node = self._root
        if node.left is None and node.right is None:
            return 0
        elif node.left is None and node.right is not None:
            return self.depth(node.right) + 1
        elif node.left is not None and node.right is None:
            return self.depth(node.left) + 1
        else:
            return max(self.depth(node.left), self.depth(node.right)) + 1

    def serialize(self):
        depth = self.depth(self._root)
        serial = [None] * (2 ** (depth + 1) - 1)
        serial[0] = self._root.val
        self._serializer(node=self._root, parent_pos=0, serial=serial)
        return serial

    def _serializer(self, node, parent_pos, serial):
        if node.left is not None:
            serial[2*parent_pos+1] = node.left.val
            self._serializer(node.left, 2*parent_pos+1, serial)
        if node.right is not None:
            serial[2*parent_pos+2] = node.right.val
            self._serializer(node.right, 2*parent_pos+2, serial)

    def deserialize(self, serial):
        head = TreeNode(serial[0])
        self._deserializer(parent_node=head, parent_position=0, serial=serial)
        return head

    def _deserializer(self, parent_node, parent_position, serial):
        if serial[parent_position*2+1] is not None:
            parent_node.left = TreeNode(serial[parent_position*2+1])
            if parent_position * 2 + 1 < len(serial) // 2:
                self._deserializer(parent_node=parent_node.left, parent_position=parent_position*2+1, serial=serial)
        if serial[parent_position*2+2] is not None:
            parent_node.right = TreeNode(serial[parent_position*2+2])
            if parent_position * 2 + 2 < len(serial) // 2:
                self._deserializer(parent_node=parent_node.right, parent_position=parent_position*2+2, serial=serial)
        
        

    


# Tree test

# serial = binary_tree.serialize()

serial = [1,None ,2,None ,3,None ,4,None ,5,None ,6,None ,7,None ,8,None ,9,None ,10,None ,11,None ,12,None ,13,None ,14,None ,15,None ,16,None ,17,None ,18,None ,19,None ,20,None ,21,None ,22,None ,23,None ,24,None ,25,None ,26,None ,27,None ,28,None ,29,None ,30,None ,31,None ,32,None ,33,None ,34,None ,35,None ,36,None ,37,None ,38,None ,39,None ,40,None ,41,None ,42,None ,43,None ,44,None ,45,None ,46,None ,47,None ,48,None ,49,None ,50,None ,51,None ,52,None ,53,None ,54,None ,55,None ,56,None ,57,None ,58,None ,59,None ,60,None ,61,None ,62,None ,63,None ,64,None ,65,None ,66,None ,67,None ,68,None ,69,None ,70,None ,71,None ,72,None ,73,None ,74,None ,75,None ,76,None ,77,None ,78,None ,79,None ,80,None ,81,None ,82,None ,83,None ,84,None ,85,None ,86,None ,87,None ,88,None ,89,None ,90,None ,91,None ,92,None ,93,None ,94,None ,95,None ,96,None ,97,None ,98,None ,99,None ,100,None ,101,None ,102,None ,103,None ,104,None ,105,None ,106,None ,107,None ,108,None ,109,None ,110,None ,111,None ,112,None ,113,None ,114,None ,115,None ,116,None ,117,None ,118,None ,119,None ,120,None ,121,None ,122,None ,123,None ,124,None ,125,None ,126,None ,127,None ,128,None ,129,None ,130,None ,131,None ,132,None ,133,None ,134,None ,135,None ,136,None ,137,None ,138,None ,139,None ,140,None ,141,None ,142,None ,143,None ,144,None ,145,None ,146,None ,147,None ,148,None ,149,None ,150,None ,151,None ,152,None ,153,None ,154,None ,155,None ,156,None ,157,None ,158,None ,159,None ,160,None ,161,None ,162,None ,163,None ,164,None ,165,None ,166,None ,167,None ,168,None ,169,None ,170,None ,171,None ,172,None ,173,None ,174,None ,175,None ,176,None ,177,None ,178,None ,179,None ,180,None ,181,None ,182,None ,183,None ,184,None ,185,None ,186,None ,187,None ,188,None ,189,None ,190,None ,191,None ,192,None ,193,None ,194,None ,195,None ,196,None ,197,None ,198,None ,199,None ,200,None ,201,None ,202,None ,203,None ,204,None ,205,None ,206,None ,207,None ,208,None ,209,None ,210,None ,211,None ,212,None ,213,None ,214,None ,215,None ,216,None ,217,None ,218,None ,219,None ,220,None ,221,None ,222,None ,223,None ,224,None ,225,None ,226,None ,227,None ,228,None ,229,None ,230,None ,231,None ,232,None ,233,None ,234,None ,235,None ,236,None ,237,None ,238,None ,239,None ,240,None ,241,None ,242,None ,243,None ,244,None ,245,None ,246,None ,247,None ,248,None ,249,None ,250,None ,251,None ,252,None ,253,None ,254,None ,255,None ,256,None ,257,None ,258,None ,259,None ,260,None ,261,None ,262,None ,263,None ,264,None ,265,None ,266,None ,267,None ,268,None ,269,None ,270,None ,271,None ,272,None ,273,None ,274,None ,275,None ,276,None ,277,None ,278,None ,279,None ,280,None ,281,None ,282,None ,283,None ,284,None ,285,None ,286,None ,287,None ,288,None ,289,None ,290,None ,291,None ,292,None ,293,None ,294,None ,295,None ,296,None ,297,None ,298,None ,299,None ,300,None ,301,None ,302,None ,303,None ,304,None ,305,None ,306,None ,307,None ,308,None ,309,None ,310,None ,311,None ,312,None ,313,None ,314,None ,315,None ,316,None ,317,None ,318,None ,319,None ,320,None ,321,None ,322,None ,323,None ,324,None ,325,None ,326,None ,327,None ,328,None ,329,None ,330,None ,331,None ,332,None ,333,None ,334,None ,335,None ,336,None ,337,None ,338,None ,339,None ,340,None ,341,None ,342,None ,343,None ,344,None ,345,None ,346,None ,347,None ,348,None ,349,None ,350,None ,351,None ,352,None ,353,None ,354,None ,355,None ,356,None ,357,None ,358,None ,359,None ,360,None ,361,None ,362,None ,363,None ,364,None ,365,None ,366,None ,367,None ,368,None ,369,None ,370,None ,371,None ,372,None ,373,None ,374,None ,375,None ,376,None ,377,None ,378,None ,379,None ,380,None ,381,None ,382,None ,383,None ,384,None ,385,None ,386,None ,387,None ,388,None ,389,None ,390,None ,391,None ,392,None ,393,None ,394,None ,395,None ,396,None ,397,None ,398,None ,399,None ,400,None ,401,None ,402,None ,403,None ,404,None ,405,None ,406,None ,407,None ,408,None ,409,None ,410,None ,411,None ,412,None ,413,None ,414,None ,415,None ,416,None ,417,None ,418,None ,419,None ,420,None ,421,None ,422,None ,423,None ,424,None ,425,None ,426,None ,427,None ,428,None ,429,None ,430,None ,431,None ,432,None ,433,None ,434,None ,435,None ,436,None ,437,None ,438,None ,439,None ,440,None ,441,None ,442,None ,443,None ,444,None ,445,None ,446,None ,447,None ,448,None ,449,None ,450,None ,451,None ,452,None ,453,None ,454,None ,455,None ,456,None ,457,None ,458,None ,459,None ,460,None ,461,None ,462,None ,463,None ,464,None ,465,None ,466,None ,467,None ,468,None ,469,None ,470,None ,471,None ,472,None ,473,None ,474,None ,475,None ,476,None ,477,None ,478,None ,479,None ,480,None ,481,None ,482,None ,483,None ,484,None ,485,None ,486,None ,487,None ,488,None ,489,None ,490,None ,491,None ,492,None ,493,None ,494,None ,495,None ,496,None ,497,None ,498,None ,499,None ,500,None ,501,None ,502,None ,503,None ,504,None ,505,None ,506,None ,507,None ,508,None ,509,None ,510,None ,511,None ,512,None ,513,None ,514,None ,515,None ,516,None ,517,None ,518,None ,519,None ,520,None ,521,None ,522,None ,523,None ,524,None ,525,None ,526,None ,527,None ,528,None ,529,None ,530,None ,531,None ,532,None ,533,None ,534,None ,535,None ,536,None ,537,None ,538,None ,539,None ,540,None ,541,None ,542,None ,543,None ,544,None ,545,None ,546,None ,547,None ,548,None ,549,None ,550,None ,551,None ,552,None ,553,None ,554,None ,555,None ,556,None ,557,None ,558,None ,559,None ,560,None ,561,None ,562,None ,563,None ,564,None ,565,None ,566,None ,567,None ,568,None ,569,None ,570,None ,571,None ,572,None ,573,None ,574,None ,575,None ,576,None ,577,None ,578,None ,579,None ,580,None ,581,None ,582,None ,583,None ,584,None ,585,None ,586,None ,587,None ,588,None ,589,None ,590,None ,591,None ,592,None ,593,None ,594,None ,595,None ,596,None ,597,None ,598,None ,599,None ,600,None ,601,None ,602,None ,603,None ,604,None ,605,None ,606,None ,607,None ,608,None ,609,None ,610,None ,611,None ,612,None ,613,None ,614,None ,615,None ,616,None ,617,None ,618,None ,619,None ,620,None ,621,None ,622,None ,623,None ,624,None ,625,None ,626,None ,627,None ,628,None ,629,None ,630,None ,631,None ,632,None ,633,None ,634,None ,635,None ,636,None ,637,None ,638,None ,639,None ,640,None ,641,None ,642,None ,643,None ,644,None ,645,None ,646,None ,647,None ,648,None ,649,None ,650,None ,651,None ,652,None ,653,None ,654,None ,655,None ,656,None ,657,None ,658,None ,659,None ,660,None ,661,None ,662,None ,663,None ,664,None ,665,None ,666,None ,667,None ,668,None ,669,None ,670,None ,671,None ,672,None ,673,None ,674,None ,675,None ,676,None ,677,None ,678,None ,679,None ,680,None ,681,None ,682,None ,683,None ,684,None ,685,None ,686,None ,687,None ,688,None ,689,None ,690,None ,691,None ,692,None ,693,None ,694,None ,695,None ,696,None ,697,None ,698,None ,699,None ,700,None ,701,None ,702,None ,703,None ,704,None ,705,None ,706,None ,707,None ,708,None ,709,None ,710,None ,711,None ,712,None ,713,None ,714,None ,715,None ,716,None ,717,None ,718,None ,719,None ,720,None ,721,None ,722,None ,723,None ,724,None ,725,None ,726,None ,727,None ,728,None ,729,None ,730,None ,731,None ,732,None ,733,None ,734,None ,735,None ,736,None ,737,None ,738,None ,739,None ,740,None ,741,None ,742,None ,743,None ,744,None ,745,None ,746,None ,747,None ,748,None ,749,None ,750,None ,751,None ,752,None ,753,None ,754,None ,755,None ,756,None ,757,None ,758,None ,759,None ,760,None ,761,None ,762,None ,763,None ,764,None ,765,None ,766,None ,767,None ,768,None ,769,None ,770,None ,771,None ,772,None ,773,None ,774,None ,775,None ,776,None ,777,None ,778,None ,779,None ,780,None ,781,None ,782,None ,783,None ,784,None ,785,None ,786,None ,787,None ,788,None ,789,None ,790,None ,791,None ,792,None ,793,None ,794,None ,795,None ,796,None ,797,None ,798,None ,799,None ,800,None ,801,None ,802,None ,803,None ,804,None ,805,None ,806,None ,807,None ,808,None ,809,None ,810,None ,811,None ,812,None ,813,None ,814,None ,815,None ,816,None ,817,None ,818,None ,819,None ,820,None ,821,None ,822,None ,823,None ,824,None ,825,None ,826,None ,827,None ,828,None ,829,None ,830,None ,831,None ,832,None ,833,None ,834,None ,835,None ,836,None ,837,None ,838,None ,839,None ,840,None ,841,None ,842,None ,843,None ,844,None ,845,None ,846,None ,847,None ,848,None ,849,None ,850,None ,851,None ,852,None ,853,None ,854,None ,855,None ,856,None ,857,None ,858,None ,859,None ,860,None ,861,None ,862,None ,863,None ,864,None ,865,None ,866,None ,867,None ,868,None ,869,None ,870,None ,871,None ,872,None ,873,None ,874,None ,875,None ,876,None ,877,None ,878,None ,879,None ,880,None ,881,None ,882,None ,883,None ,884,None ,885,None ,886,None ,887,None ,888,None ,889,None ,890,None ,891,None ,892,None ,893,None ,894,None ,895,None ,896,None ,897,None ,898,None ,899,None ,900,None ,901,None ,902,None ,903,None ,904,None ,905,None ,906,None ,907,None ,908,None ,909,None ,910,None ,911,None ,912,None ,913,None ,914,None ,915,None ,916,None ,917,None ,918,None ,919,None ,920,None ,921,None ,922,None ,923,None ,924,None ,925,None ,926,None ,927,None ,928,None ,929,None ,930,None ,931,None ,932,None ,933,None ,934,None ,935,None ,936,None ,937,None ,938,None ,939,None ,940,None ,941,None ,942,None ,943,None ,944,None ,945,None ,946,None ,947,None ,948,None ,949,None ,950,None ,951,None ,952,None ,953,None ,954,None ,955,None ,956,None ,957,None ,958,None ,959,None ,960,None ,961,None ,962,None ,963,None ,964,None ,965,None ,966,None ,967,None ,968,None ,969,None ,970,None ,971,None ,972,None ,973,None ,974,None ,975,None ,976,None ,977,None ,978,None ,979,None ,980,None ,981,None ,982,None ,983,None ,984,None ,985,None ,986,None ,987,None ,988,None ,989,None ,990,None ,991,None ,992,None ,993,None ,994,None ,995,None ,996,None ,997,None ,998,None ,999,None ,1000]
print(len(serial))
# length == 1999
# obviously, it is not a heap
binary_tree = BinaryTree(0)
head = binary_tree.deserialize(serial)
depth = binary_tree.depth(node=head)
print(depth)
binary_tree.preorder(head)







# 0297 Solution
# 10-26-2018

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def depth(self, node):
        if node.left is None and node.right is None:
            return 0
        elif node.left is None and node.right is not None:
            return self.depth(node.right) + 1
        elif node.left is not None and node.right is None:
            return self.depth(node.left) + 1
        else:
            return max(self.depth(node.left), self.depth(node.right)) + 1
        
    def serialize(self, root):
        if root is None:
            return []
        elif root.left is None and root.right is None:
            return [root.val]
        depth = self.depth(root)
        serial = [None] * (2 ** (depth + 1) - 1)
        serial[0] = root.val
        self._serializer(node=root, parent_pos=0, serial=serial)
        return serial

    def _serializer(self, node, parent_pos, serial):
        if node.left is not None:
            serial[2*parent_pos+1] = node.left.val
            self._serializer(node.left, 2*parent_pos+1, serial)
        if node.right is not None:
            serial[2*parent_pos+2] = node.right.val
            self._serializer(node.right, 2*parent_pos+2, serial)
        

    def deserialize(self, serial):
        if not serial:
            return None
        elif len(serial) == 1:
            return TreeNode(serial[0])
        head = TreeNode(serial[0])
        self._deserializer(parent_node=head, parent_position=0, serial=serial)
        return head

    def _deserializer(self, parent_node, parent_position, serial):
        if serial[parent_position*2+1] is not None:
            parent_node.left = TreeNode(serial[parent_position*2+1])
            if parent_position * 2 + 1 < len(serial) // 2:
                self._deserializer(parent_node=parent_node.left, parent_position=parent_position*2+1, serial=serial)
        if serial[parent_position*2+2] is not None:
            parent_node.right = TreeNode(serial[parent_position*2+2])
            if parent_position * 2 + 2 < len(serial) // 2:
                self._deserializer(parent_node=parent_node.right, parent_position=parent_position*2+2, serial=serial)
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))



