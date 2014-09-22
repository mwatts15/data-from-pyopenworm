import PyOpenWorm as P
import rdflib as R

P.connect("default.conf")

c = P.Cell()

#prints inferred triples for demo
c.save()

#removes demo cell from db
c.retract()