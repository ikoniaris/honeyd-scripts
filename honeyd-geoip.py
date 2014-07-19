#!/usr/bin/python
import GeoIP
import sys

#log file location hard coded, change to suit environment
logfile = open('/var/log/honeypot/honeyd.log','r')
source = []
for line in logfile:
	source.append(line.split(' ')[3])

#http://www.maxmind.com/app/python
#http://code.google.com/p/pygeoip/
gi = GeoIP.new(GeoIP.GEOIP_MEMORY_CACHE)

src_country = []
src_count = []
for src in set(source):
	country =  gi.country_name_by_addr( src )
	try:
		pos = src_country.index( country )
		src_count[pos] += 1
	except:
		src_country.append( country )
		src_count.append( 1 )

for i in range( 0, ( len( src_country ) - 1 ) ):
	sys.stdout.write( "%s:\t%i\n" %( src_country[i], src_count[i] ) )

