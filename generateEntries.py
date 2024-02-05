from openai import OpenAI
from tqdm import tqdm
import os

client = OpenAI(api_key="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")

# This program will generate artifical journal entries for a range of dates.
# The entries are stored in a folder in the same directory called `entries`.
# The entries are stored in a file called `entry-<date>.txt` where `<date>` is the date of the entry.


def createEntry(date):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a 21 year old named Jason journalling about the events in his life."},
            {"role": "user", "content": "Write about a day in the life of Jason on " + date + "."},
        ],
    )

    return completion.choices[0].message.content

def main():
    if not os.path.exists("entries"):
        os.makedirs("entries")

    for i in tqdm(range(1, 32)):
        date = "2024-01-" + str(i).zfill(2)
        entry = createEntry(date)
        with open("entries/entry-" + date + ".txt", "w") as file:
            file.write(entry)

if __name__ == "__main__":
    main()
