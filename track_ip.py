import time
import os
import requests
import webbrowser
import shutil
from colorama import Fore, init
import pyfiglet
import geoip2.database
import folium

init(autoreset=True)

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def get_your_ip():
    try:
        response = requests.get("https://api64.ipify.org?format=text")
        response.raise_for_status()  # Verifica se la richiesta ha avuto successo
        return response.text  # Restituisce l'IP pubblico
    except requests.RequestException as e:
        print(Fore.RED + f"Error retrieving IP: {e}")
        return None

def get_terminal_size():
    try:
        columns, rows = shutil.get_terminal_size()
        return columns, rows
    except AttributeError:
        return 80, 24

def print_ascii_art():
    track_art = pyfiglet.figlet_format("Track")
    ip_art = pyfiglet.figlet_format("IP")
    
    track_lines = track_art.splitlines()
    ip_lines = ip_art.splitlines()

    combined_lines = [
        track_lines[i] + ' ' * (len(ip_lines[i]) - len(track_lines[i])) + ip_lines[i] 
        for i in range(len(track_lines))
    ]
    
    columns, rows = get_terminal_size()

    top_padding = (rows - len(track_lines)) // 4

    print("\n" * top_padding, end="")

    for line in combined_lines:
        centered_line = line.center(columns)
        print("\033[38;5;214m" + centered_line[:len(track_lines[0])] + Fore.BLUE + centered_line[len(track_lines[0]):])

def print_menu(ip):
    columns, rows = get_terminal_size()

    print("\n" * 2)

    print((Fore.YELLOW + " " * 19 + "Version 1.0.0").center(columns))

    print((Fore.CYAN + "=" * 50).center(columns))

    print((Fore.CYAN + f"Your IP: {ip}").center(columns))

    print((Fore.GREEN + "1. Track an IP or a list of IPs").center(columns))
    print((Fore.GREEN + "2. Show searched IP addresses").center(columns))
    print((Fore.RED + "3. Exit").center(columns))

    print((Fore.CYAN + "=" * 50).center(columns))

def show_ip_details(ip, geoip_database, use_geoip2=False):
    try:
        if use_geoip2:
            client = geoip2.database.Reader(geoip_database)
        else:
            client = geoip2.database.Reader(geoip_database)

        response = client.city(ip)
        
        print("\n" + "-" * 50)
        print(Fore.GREEN + f"IP: {ip}")
        print(Fore.CYAN + f"Country: {response.country.name}")
        print(Fore.CYAN + f"City: {response.city.name}")
        print(Fore.CYAN + f"Latitude: {response.location.latitude}")
        print(Fore.CYAN + f"Longitude: {response.location.longitude}")
        print(Fore.CYAN + f"Region: {response.subdivisions.most_specific.name}")
        print(Fore.CYAN + f"Postal Code: {response.postal.code}")
        print("-" * 50)

        create_map(ip, response.location.latitude, response.location.longitude)

    except geoip2.errors.AddressNotFoundError:
        print(Fore.RED + "IP address not found in the database.")
    except Exception as e:
        print(Fore.RED + f"Error searching IP: {e}")

def create_map(ip, latitude, longitude):
    m = folium.Map(location=[latitude, longitude], zoom_start=10)
    folium.Marker([latitude, longitude], popup=f"IP: {ip}\nLat: {latitude}\nLon: {longitude}").add_to(m)
    map_file = "mappa.html"
    m.save(map_file)
    webbrowser.open(f'file://{os.path.realpath(map_file)}')

def start_process(ip, geoip_database):
    searched_ips = []  # To store searched IPs

    while True:
        clear_screen()
        
        print_ascii_art()
        print_menu(ip)

        choice = input(Fore.YELLOW + "What would you like to do? (1, 2, or 3): ").strip()

        if choice == '1':
            ip_input = input("\nEnter an IP address or a list of IPs separated by commas:\n").strip()
            
            ip_list = [ip.strip() for ip in ip_input.split(",") if ip.strip()]
            
            if ip_list:
                for ip in ip_list:
                    print(Fore.GREEN + f"Tracking IP: {ip}")
                    show_ip_details(ip, geoip_database, use_geoip2=True)  # Modify this depending on user choice
                    searched_ips.append(ip)
            else:
                print(Fore.RED + "No IP entered!\n")

        elif choice == '2':
            if searched_ips:
                print(Fore.MAGENTA + "Searched IP addresses:")
                for ip in searched_ips:
                    print(Fore.YELLOW + ip)
            else:
                print(Fore.RED + "No IPs have been searched yet.")

        elif choice == '3':
            print(Fore.GREEN + "\nThank you for using the tool!\n")
            break

        else:
            print(Fore.RED + "Invalid selection! Please choose one of the available options.\n")

        input(Fore.YELLOW + "\nPress Enter to return to the menu...")

def select_geoip_version():
    while True:
        choice = input(Fore.YELLOW + "Select GeoIP version:\n1. GeoLite2\n2. GeoIP2\n3. Exit\nChoice (1/2/3): ").strip()

        if choice == '1':
            geoip_database = 'GeoLite2-City.mmdb'  # Assumed to be in the same directory
            return geoip_database, False  # False for GeoLite2
        elif choice == '2':
            geoip_database = 'GeoIP2-City.mmdb'  # Assumed to be in the same directory
            return geoip_database, True  # True for GeoIP2
        elif choice == '3':
            print(Fore.GREEN + "\nExiting...")
            exit(0)
        else:
            print(Fore.RED + "Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    ip = get_your_ip()

    if ip is None:
        print(Fore.RED + "Unable to retrieve your public IP. Exiting...")
    else:
        geoip_database, use_geoip2 = select_geoip_version()  # Prompt user for GeoIP version
        start_process(ip, geoip_database)
