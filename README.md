# CARBON_FOOTPRINT_API

A simple API to estimate carbon footprints for activities and travel. This repository provides endpoints to calculate emissions, convert units, and integrate with other services.

## Features

- Calculate carbon emissions for travel (car, flight, train)
- Estimate emissions for activities and energy usage
- Simple JSON REST API with clear endpoints

## Getting Started

### Prerequisites

- Node.js (>=14) or the runtime used by the project
- npm or yarn

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Akshat77O/CARBON_FOOTPRINT_API.git
   cd CARBON_FOOTPRINT_API
   ```

2. Install dependencies:

   ```bash
   npm install
   # or
   yarn install
   ```

3. Copy and configure environment variables:

   ```bash
   cp .env.example .env
   # then edit .env
   ```

## Usage

Start the server (adjust command if different in this project):

```bash
npm start
# or
npm run dev
```

Then open the API base URL (by default http://localhost:3000)

## API Endpoints (examples)

- `GET /health` — health check
- `POST /api/v1/estimate` — calculate carbon footprint. Example request body:

```json
{
  "type": "flight",
  "distance_km": 1500,
  "class": "economy"
}
```

Example response:

```json
{
  "type": "flight",
  "distance_km": 1500,
  "emissions_kg_co2": 210.5
}
```

Adjust endpoint paths to match the project code.

## Environment variables

List any environment variables your project expects in `.env.example`, for example:

```
PORT=3000
NODE_ENV=development
API_KEY=your_api_key_here
```

## Future Enhancements

Planned improvements and features for upcoming releases:

- Support unit conversions (kg/lbs, km/miles).
- Add user authentication and save calculation history.
- Improve UI with accessibility and responsive design.
- Provide carbon footprint reduction tips based on shipment details.
- Deploy both frontend and backend on cloud platforms.

## Screenshots

Below are sample outputs from the frontend UI. The images are expected to be added to `assets/screenshots/` as `screenshot1.png` and `screenshot2.png`.

<img width="679" height="795" alt="image" src="https://github.com/user-attachments/assets/e5fb901a-7121-42a3-898a-a0a68abd2780" />

<img width="664" height="811" alt="image" src="https://github.com/user-attachments/assets/92250ec0-a439-434e-8de0-d755b7e074d0" />


If you want, I can upload the provided PNGs into `assets/screenshots/` and update these paths now — tell me to proceed and I'll add them.

## Contributing

Contributions are welcome. Please open an issue first to discuss major changes.

## License

Specify a license (e.g., MIT) in a LICENSE file.

## Contact

If you have questions, open an issue or contact the repository owner.
