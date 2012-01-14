#!/usr/bin/env python

# Project Euler
# http://projecteuler.net/problem=29

# Problem 29
# How many distinct terms are in the sequence generated by a^b for
# 2 <= a <= 100 and 2 <= b <= 100?

if __name__ == "__main__":
	terms=[]
	for a in xrange(2,100+1): # example on the webpage
		for b in xrange(2,100+1):
			atob=a**b
			if not atob in terms: terms.append(atob)
	print len(terms)
