# Flight Price Monitoring System

The Flight Price Monitoring System is a Python project designed to monitor and notify users about low flight prices. It integrates with Sheety, Tequila, and Twilio APIs to manage flight data, search for flights, and send notifications.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [File Descriptions](#file-descriptions)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project helps users monitor flight prices for various destinations and receive notifications when low prices are detected. It utilizes the Sheety API to manage flight data, the Tequila API for flight searches, and the Twilio API for SMS notifications.

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/cheap_flight_finder.git
   ```

2. Navigate to the project directory:

  ```bash
   cd cheap_flight_finder
  ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a .env file in the project root and add the necessary environment variables:

   ```bash
   TEQUILA_API_KEY=your_tequila_api_key
   TWILIO_SID=your_twilio_sid
   TWILIO_AUTH_TOKEN=your_twilio_auth_token
   TWILIO_VIRTUAL_NUMBER=your_twilio_virtual_number
   TWILIO_VERIFIED_NUMBER=your_twilio_verified_number
   ```

## Usage

Run the main script to initiate the flight price monitoring system:

```bash
python main.py
```

The system will fetch destination data, check for low-price flights, update the Sheety API, and send SMS notifications if applicable.

## Configuration

- **Tequila API:** Obtain the Tequila API key by creating an account on the [Tequila Kiwi Developer Portal](https://tequila.kiwi.com/portal/getting-started).
- **Twilio API:** Create a [Twilio](https://www.twilio.com/en-us) account to obtain the SID, Auth Token, and Virtual/Verified phone numbers.

## File Description

1. data_manager.py:
- Manages flight data using the Sheety API.

2. flight_data.py:
- Defines the FlightData class for organizing flight details.

3. flight_search.py:
- Searches for flights using the Tequila API.

4. notification_manager.py:
- Manages notifications, specifically sending SMS using the Twilio API.

5. main.py:
- Integrates functionalities from other files to monitor and notify about low flight prices.

## Contribution

Contributions are welcome! Feel free to open issues or pull requests.

## License

MIT
