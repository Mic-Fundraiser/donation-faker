import pandas as pd
import random
from faker import Faker
import streamlit as st
from io import BytesIO

# Inizializzazione di Faker per l'Italia
fake = Faker('it_IT')

# Funzione per generare dati casuali
def create_random_data(num_records):
    data = []
    for _ in range(num_records):
        # Generazione di un record casuale
        record = {
            "Nome": fake.first_name(),
            "Cognome": fake.last_name(),
            "Email": fake.email(),
            "Data di Nascita": fake.date_of_birth(minimum_age=18, maximum_age=85).strftime("%Y-%m-%d"),
            "Sesso": random.choice(["M", "F"]),
            "Indirizzo": fake.street_address(),
            "Città": fake.city(),
            "Totale Donato": round(random.uniform(10, 1000), 2),
            "Email Optin": random.choice([True, False])
        }
        data.append(record)
    return data

# Widget di input Streamlit per il numero di record
num_records = st.number_input("Inserisci il numero di record da generare:", min_value=1, value=1, step=1)

# Bottone per generare i dati
if st.button('Genera Dati'):
    # Creazione dei dati
    random_data = create_random_data(num_records)

    # Creazione di un DataFrame
    df = pd.DataFrame(random_data)

    # Conversione del DataFrame in CSV
    csv = df.to_csv(index=False, sep=',').encode('utf-8')

    # Creazione di un oggetto BytesIO
    b = BytesIO(csv)

    # Widget di download Streamlit per il file CSV
    st.download_button(
         label="Scarica i dati come CSV",
         data=b,
         file_name='random_data_italy.csv',
         mime='text/csv',
     )

    # Mostra i dati generati (opzionale)
    st.write(df)
