IP Tracker Script

This script tracks IP addresses and provides geographic information about them. It uses either GeoLite2 or GeoIP2 databases to fetch the details. It allows you to search multiple IPs and displays the results, including a map showing the location of the tracked IPs.
Features

Get your public IP address.
Search for IP addresses and get detailed information such as location, organization, and more.
Show IP details in a human-readable format.
Generate an HTML map to visually represent the IP locations.
Allows choosing between GeoLite2 and GeoIP2 databases.

Installation

Follow these steps to install the required dependencies and run the script:
1. Clone the Repository

You can clone the repository using the following command:

    git clone https://github.com/your-username/track-ip.git

2. Install Dependencies

The script requires some Python libraries. You can install the necessary dependencies by using the requirements.txt file.
Install pip (Python's package manager):

Windows: Download Python from https://www.python.org/downloads/ and follow the installation instructions. Ensure to     check the box to add Python to PATH during installation.
macOS: Open the terminal and install Homebrew if it's not already installed by running:

    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

Then, install Python with Homebrew:

    brew install python3

Linux (Ubuntu/Debian): Open the terminal and run:

    sudo apt install python3-pip

Install required packages:

After cloning the repository, navigate to the project directory and run:

    pip install -r requirements.txt

3. Download the GeoLite2/GeoIP2 Database Files

You need to download either the GeoLite2 or GeoIP2 databases.

GeoLite2 Database:
        Download from: https://dev.maxmind.com/geoip/geoip2/geolite2/
        You will need the GeoLite2-City.mmdb file.

GeoIP2 Database (requires an account on MaxMind):
        Download from: https://www.maxmind.com/en/accounts
        You will need the GeoIP2-City.mmdb file.

Place the downloaded .mmdb files in the same directory as the script.
4. Run the Script

Once everything is set up, you can run the script with:

`python track_ip.py`

5. Using the Script

When running the script, you will be prompted to:

Select the database to use (GeoLite2 or GeoIP2).
Enter the IPs you wish to track.
View detailed geographic information about the IPs.

Contributing

This repository is read-only. No one is allowed to modify or contribute to the codebase. The repository is maintained solely by the creator and cannot be altered or updated by other users.

If you have any suggestions or bug reports, please create an issue on GitHub. The creator will review it for potential updates.
License

This script is open-source and available under the MIT License.
