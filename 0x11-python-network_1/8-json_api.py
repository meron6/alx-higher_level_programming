#!/usr/bin/python3
"""Sends a POST request to http://0.0.0.0:5000/search_user with a given letter.
Usage: ./custom_script.py <letter>
  - The letter is sent as the value of the variable `q`.
  - If no letter is provided, sends `q=""`.
"""
import sys
import requests


def main():
    if len(sys.argv) < 2:
        letter = ""
    else:
        letter = sys.argv[1]

    payload = {"q": letter}

    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)

    try:
        response = r.json()
        if response:
            print("[{}] {}".format(response.get("id"), response.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    main()
