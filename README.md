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

## Contributing

Contributions are welcome. Please open an issue first to discuss major changes.

## License

Specify a license (e.g., MIT) in a LICENSE file.

## Contact

If you have questions, open an issue or contact the repository owner.
