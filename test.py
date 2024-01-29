from pprint import pprint
import maxminddb

ip = "152.216.7.110"

reader = maxminddb.open_database("layer/GeoLite2-City.mmdb")
pprint(reader.get(ip))
assert "city" in reader.get(ip)

reader = maxminddb.open_database("layer/GeoLite2-ASN.mmdb")
pprint(reader.get(ip))
assert "autonomous_system_number" in reader.get(ip)

reader = maxminddb.open_database("layer/GeoLite2-Country.mmdb")
pprint(reader.get(ip))
assert "country" in reader.get(ip)
