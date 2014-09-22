import PyOpenWorm as P
import rdflib as R
import unittest
import os

P.connect("default.conf")

#create new muscle object
m = P.Muscle()

#save muscle to graph (and infer new triples to it, based on rules)
m.save()

#get the graph associated with th muscle cell
graph = m.rdf.serialize(format="n3")

P.disconnect()

#remove unnecessary files from directory
os.remove("worm.db")
os.remove("worm.db.tmp")
os.remove("worm.db.lock")
os.remove("worm.db.index")

class InferenceTest(unittest.TestCase):

    def testIfInferred(self):
        #this will fail unless "TestClass" is in the graph
        self.failUnless("<http://openworm.org/entities/TestClass>" in graph)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
