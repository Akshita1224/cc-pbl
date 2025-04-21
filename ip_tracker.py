import requests

def track_ip(ip=None):
    # Use own IP if none provided
    url = f"https://ipinfo.io/{ip}/json" if ip else "https://ipinfo.io/json"
    response = requests.get(url)

    if response.status_code != 200:
        print("❌ Failed to fetch data. Check the IP or your internet.")
        return

    data = response.json()

    print("\n🌐 IP Geolocation Information")
    print("-" * 35)
    print(f"IP Address: {data.get('ip', 'N/A')}")
    print(f"City:       {data.get('city', 'N/A')}")
    print(f"Region:     {data.get('region', 'N/A')}")
    print(f"Country:    {data.get('country', 'N/A')}")
    print(f"Location:   {data.get('loc', 'N/A')}")
    print(f"ISP/Org:    {data.get('org', 'N/A')}")
    print("-" * 35)

if __name__ == "__main__":
    print("=== IP Geolocation Tracker ===")
    user_ip = input("Enter IP address (leave blank to detect your own): ")
    track_ip(user_ip.strip())

