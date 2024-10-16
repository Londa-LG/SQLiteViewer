# SQLiteViewer

This is a Sqlite database GUI viewer.

## Why this exist?

I was working on a test taking app and found that reading the database everytime I made a change was getting complicated and got in the way of making progress so I built this.

## Quick Start

Clone this repo

```bash
git clone https://github.com/Londa-LG/SQLiteViewer.git
```

Create a virtual environment

```bash
python3 -m venv env
```

Activate it.

```bash
source env/bin/activate
```

Install requirments

```bash
pip install customtkinter
```

Run app.py from the directory with your database.

```bash
python ../SQLiteViewer/app.py
```

Or copy the database ,that you want to read, to this directory (the one with this repos files) then run app.py

```bash
python app.py
```

## Usage

Run the application

![screenshot of app](./Screenshots/running1.png)

Type the local sqlite database name

![screenshot of app](./Screenshots/running2.png)

Click connect. Then every time you make a change click refresh to see it.

![screenshot of app](./Screenshots/running3.png)

## Contributions

If you'd like to contribute, please fork the repository and open a pull request.
