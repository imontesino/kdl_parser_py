#!/usr/bin/env python

import os
import sys

import kdl_parser.urdf
import unittest

PKG = "kdl_parser_py"
NAME = "test_kdl_parser"

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

class TestKdlParser(unittest.TestCase):
    def runTest(self):
        filename = "test.urdf"
        (ok, tree) = kdl_parser.urdf.treeFromFile(filename)
        self.assertTrue(ok)
        # KDL doesn't count fixed joints (since they aren't kinematic)
        self.assertEqual(tree.getNrOfJoints(), 8)
        # KDL doesn't count base link (since it's attached by fixed links
        self.assertEqual(tree.getNrOfSegments(), 10)
        chain = tree.getChain("base_link", "right_gripper")
        self.assertEqual(chain.getNrOfSegments(), 2)
        self.assertEqual(chain.getNrOfJoints(), 2)
        self.assertEqual(chain.getSegment(0).getName(), "gripper_pole")
        self.assertEqual(chain.getSegment(0).getJoint().getName(), "gripper_extension")
        self.assertEqual(chain.getSegment(1).getName(), "right_gripper")
        self.assertEqual(chain.getSegment(1).getJoint().getName(), "right_gripper_joint")

        inertia = chain.getSegment(1).getInertia()
        self.assertAlmostEqual(inertia.getCOG().z(), 3.0)

if __name__ == "__main__":
     unittest.main()
