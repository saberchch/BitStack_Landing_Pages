# Bitstack Landing Pages

Bitstack is a modern digital growth ecosystem designed to connect learning, knowledge sharing, freelancing, and real-world opportunity within one unified platform.

This repository contains the landing pages for the Bitstack ecosystem, built with a lightweight Python Flask backend and styled using vanilla HTML/CSS via a Tailwind CDN. 

## Features

The landing pages outline the 5 main pillars of the Bitstack ecosystem:
1. **Learn**: Structured academic and skill-based support through mentoring.
2. **Earn**: Monetize expertise through mentoring and teaching.
3. **Freelance**: Work on real digital projects and collaborate with clients securely.
4. **Institutes**: Integration for educational institutes and training organizations.
5. **Library**: A structured educational resource system.

## Tech Stack
- **Backend:** Python (Flask)
- **Frontend:** HTML5, Tailwind CSS (via CDN), Google Material Symbols

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd BitStack_Landing_pages
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the requirements:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```

5. **View the site:**
   Open your browser and navigate to `http://localhost:8000` (or the port specified in your console output).

## Project Structure
- `app.py`: The main Flask routing file.
- `requirements.txt`: Python dependencies.
- `templates/`: Contains all HTML files (using Jinja2 templating syntax).
- `static/`: Contains static assets like images and custom CSS (e.g., `index.css`).
- `generate_colors.py`: A utility script used during development to generate consistent UI color shades.

## License
MIT License
# BitStack_Landing_Pages
