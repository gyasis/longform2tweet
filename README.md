# longform2tweet

longform2tweet is a Flask and React application designed to split long form documents into tweet-sized sections. This tool is perfect for authors, bloggers, or anyone who wants to share a large amount of text on Twitter in a structured, easy-to-read format.

## Features

- Split long form text into tweetable sections that adhere to Twitter's character limit.
- A footer is appended to each tweet, indicating the order of the tweets (i.e., "Thread 1 of 3").
- Each section becomes a selectable button in the React app.
- Clicking a button copies that section to the clipboard for easy pasting into Twitter.
- Once a button has been clicked, it stays clicked to ensure that a section is not selected twice.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

To run this project, you will need the following installed:

- Python 3
- pip (Python package installer)
- Node.js and npm
- A clone of this repository on your machine

### Backend Setup

1. Navigate to the `backend` directory.
2. Install the Python dependencies: `pip install -r requirements.txt`
3. Run the Flask server: `python app.py`

### Frontend Setup

1. Navigate to the `frontend` directory.
2. Install the npm packages: `npm install`
3. Run the React development server: `npm start`

The application should now be running! The backend is running at `localhost:5000`, and the frontend is running at `localhost:3000`.

## Built With

- Flask - The web framework used for the backend
- React - The library used for building the user interface
- axios - Used for making HTTP requests from the React app
- textwrap - Python library used for wrapping input paragraph to fit specified width

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.
