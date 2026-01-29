# Rabbi Quotes - Flask Web App

A simple Flask web application that displays daily inspirational quotes from Rabbi Menachem Mendel Schneerson (the Lubavitcher Rebbe), with English and Hebrew versions.

## Features
- Random quote selection on each refresh / button click
- Beautiful portrait of the Rebbe
- Bilingual display (English + Hebrew with proper RTL support)
- Fully containerized with Docker
- Clean, responsive and minimalistic design

## Technologies
- **Backend**: Python + Flask
- **Frontend**: Jinja2 templates + CSS (no heavy frameworks)
- **Containerization**: Docker
- **Data**: Static JSON file (`data/Rabbiquotes.json`)

## Project Structure

7-FinalDevops/
├── view.py                # Main Flask application
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker configuration
├── data/
│   └── Rabbiquotes.json   # Quotes database (English + Hebrew)
├── templates/
│   └── index.html         # Main HTML template
└── README.md

## Local Development (without Docker)

1. Create and activate virtual environment
```bash
python3 -m venv venv
source venv/bin/activate`

2. Install dependencies
bash
pip install -r requirements.txt

3. Run the application

python view.py

Open: http://localhost:5000

##Docker Usage

1. Build the image

docker build -t rabbi-quotes-app .

2. Run the container (foreground)

docker run -p 5000:5000 rabbi-quotes-app

or Background (detached mode)

docker run -d -p 5000:5000 --name rabbi-quotes-container rabbi-quotes-app

3. Run with data persistence 

docker run -d \
  -p 5000:5000 \
  -v $(pwd)/data:/app/data \
  --name rabbi-quotes-container \
  rabbi-quotes-app

and Access: http://localhost:5000

4. Stop / Remove 

docker stop rabbi-quotes-container
docker rm rabbi-quotes-container   # if you want to remove it
