# WHOIS domain lookup using 'whois' module

import whois

# Input domain
domain = input("Enter domain name (e.g. example.com): ")

# Perform lookup
info = whois.whois(domain)

# Display basic info
print("\nDomain info:")
print("Domain name:", info.domain_name)
print("Registrar:", info.registrar)
print("Creation date:", info.creation_date)
print("Expiration date:", info.expiration_date)
