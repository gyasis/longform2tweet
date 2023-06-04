# longform2tweet

longform2tweet is a Flask web application designed to split long form texts into tweet-sized sections that adhere to Twitter's character limit, including hashtags and optional thread titles. This tool is useful for authors, bloggers, journalists or anyone who wants to share a large amount of text on Twitter in a structured, readable format. This tool may be sort of a niche use case, but it was a fun project to build and I learned a lot about Flask and web development in general. This is also an experiment to see how difficult it is to build web and mobile applications using Python and Flask, as opposed to JavaScript and Node.js.It's a work in progress.
## Features

- Splits long form text into tweetable sections that fit within Twitter's character limit.
- Append a unique footer to each tweet, indicating the tweet order in the thread.
- Thread titles and hashtags can be added as optional elements to customize the thread.
- Display generated tweets in stylized "Twitter cards".
- Each card has a "copy to clipboard" function for easy pasting into Twitter.
- Cards change color once copied, preventing accidental duplication.
- The application state is persisted across sessions, and threads can be saved and retrieved from a SQLite database.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

To run this project, you will need the following installed:

- Python 3
- pip (Python package installer)
- SQLite
- A clone of this repository on your machine

### Setup

1. Navigate to the project directory.
2. Install the Python dependencies: `pip install -r requirements.txt`
3. Run the Flask server: `python app.py`

The application should now be running at `localhost:5000`.

### Setting up the database

The application uses SQLite to store threads. Ensure that SQLite is installed and properly configured on your system. The application automatically handles the creation and management of the database and tables.

## Built With

- Flask - The web framework used for the backend
- Bootstrap - The library used for building the user interface
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
