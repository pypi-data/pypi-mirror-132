""" Collection of importers.
"""

# Imports

# Third party
import camelot
from dateutil.parser import parse
from pandas import concat


def extract_cembra(filename):
    entries = []

    tables = camelot.read_pdf(filename, pages='2-end')

    for page, pdf_table in enumerate(tables):
        df = tables[page].df
        for _, row in df.iterrows():
            try:
                date = parse(row[1].strip(), dayfirst=True).date()
                _ = parse(row[0].strip(), dayfirst=True).date()
                text = row[2]
                credit = row[3].replace('\'', '')
                debit = row[4].replace('\'', '')
                amount = -float(debit) if debit else float(credit)
                entries.append([date, amount, text])
            except ValueError:
                pass

    return entries


def extract_cashback(filename):
    entries = []

    # noinspection PyUnresolvedReferences
    table1 = camelot.read_pdf(
        filename,
        pages='1',
        flavor='stream',
        table_areas=['50,320,560,50'],
        columns=['120,530']
    )
    table2 = camelot.read_pdf(
        filename,
        pages='2-end',
        flavor='stream',
        table_areas=['50,800,560,50'],
        columns=['120,530']
    )

    df = concat([table1[0].df, table2[0].df])

    for index, row in df.iterrows():
        try:
            date = parse(row[0].strip(), dayfirst=True).date()
            text = row[1].replace("\n", " ")
            amount = -float(row[2].replace("'", ""))

            if text == "YOUR PAYMENT – THANK YOU":
                amount = -amount

            entries.append([date, amount, text])
        except ValueError:
            pass

    return entries
