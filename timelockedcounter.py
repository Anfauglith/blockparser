import numpy

a = numpy.loadtxt("data.json", dtype=float)

print a[0]
print a[1]
print a[-1]

print "Total {}".format( numpy.sum(a) )