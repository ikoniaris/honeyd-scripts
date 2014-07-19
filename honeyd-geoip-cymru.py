#!/usr/bin/python
from cymruwhois import Client
import sys

#log file location hard coded, change to suit environment
logfile = open('/var/log/honeypot/honeyd.log','r')
source = []
for line in logfile:
	source.append(line.split(' ')[3])

src_country = []
src_count = []
c = Client()

results = c.lookupmany_dict( set(source) )

for res in results:
	country =  results[res].cc
	try:
		pos = src_country.index( country )
		src_count[pos] += 1
	except:
		src_country.append( country )
		src_count.append( 1 )

for i in range( 0, ( len( src_country ) - 1 ) ):
	sys.stdout.write( "%s:\t%i\n" %( src_country[i], src_count[i] ) )

