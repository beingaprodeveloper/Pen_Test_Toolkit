from port_scanner import scan_ports
from brute_forcer import brute_force
from whois_lookup import lookup
from dir_scanner import scan_directories

def main():
    print("Penetration Testing Toolkit")
    print("1. Port Scanner")
    print("2. Brute Forcer")
    print("3. Whois Lookup")
    print("4. Directory Scanner")

    choice = input("Enter your choice: ")
    
    if choice == "1":
        target = input("Enter target IP: ")
        ports = range(20, 1025)
        scan_ports(target, ports)

    elif choice == "2":
        url = input("Enter login URL: ")
        username = input("Enter username: ")
        password_list = ["admin", "123456", "password", "admin123"]
        brute_force(url, username, password_list)

    elif choice == "3":
        domain = input("Enter domain (e.g. example.com): ")
        lookup(domain)

    elif choice == "4":
        url = input("Enter target URL (e.g. http://example.com): ")
        wordlist = ["admin", "login", "dashboard", "uploads"]
        scan_directories(url, wordlist)

    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()

