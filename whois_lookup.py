import whois

def lookup(domain):
    try:
        w = whois.whois(domain)
        print("Domain Name:", w.domain_name)
        print("Registrar:", w.registrar)
        print("Creation Date:", w.creation_date)
        print("Expiry Date:", w.expiration_date)
    except Exception as e:
        print("Error:", e)
