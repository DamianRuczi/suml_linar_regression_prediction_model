import streamlit as st
import pandas as pd
import time
import matplotlib as plt
import os
# zaczynamy od zaimportowania bibliotek

st.success('Gratulacje! Z powodzeniem uruchomiłeś aplikację')
# streamlit jest wykorzystywany do tworzenia aplikacji
# z tego powodu dobrą praktyką jest informowanie użytkownika o postępie, błędach, etc.

# Inne przykłady do wypróbowania:
# st.balloons() # animowane balony ;)
# st.error('Błąd!') # wyświetla informację o błędzie
# st.warning('Ostrzeżenie, działa, ale chyba tak sobie...')
# st.info('Informacja...')
# st.success('Udało się!')

# st.spinner()
# with st.spinner(text='Pracuję...'):
    # time.sleep(2)
    # st.success('Done')
# możemy dzięki temu "ukryć" późniejsze ładowanie aplikacji

st.title('Lab05. Streamlit')
# title, jak sama nazwa wskazuje, używamy do wyświetlenia tytułu naszej aplikacji

st.header('Wprowadzenie do zajęć')
# header to jeden z podtytułów wykorzystywnaych w Streamlit

st.subheader('O Streamlit')
# subheader to jeden z podtytułów wykorzystywnaych w Streamlit

st.text('To przykładowa aplikacja z wykorzystaniem Streamlit')
# text używamy do wyświetlenia dowolnego tekstu. Można korzystać z polskich znaków.

st.write('Streamlit jest biblioteką pozwalającą na uruchomienie modeli uczenia maszynowego.')
# write używamy również do wyświetlenia tekstu, różnica polega na formatowaniu.

st.code("st.write()", language='python')
# code może nam się czasami przydać, jeżeli chcielibyśmy pokazać np. klientowi fragment kodu, który wykorzystujemy w aplikacji

with st.echo():
    st.write("Echo")
# możemy też to zrobić prościej używając echo - pokazujemy kod i równocześnie go wykonujemy

df = pd.read_csv("DSP_4.csv", sep = ';')
st.dataframe(df)
# musimy tylko pamiętać o właściwym określeniu separatora (w tym wypadku to średnik)
# masz problem z otworzeniem pliku? sprawdź w jakim katalogu pracujesz i dodaj tam plik
# os.getcwd() # pokaż bieżący katalog
# os.chdir("") # zmiana katalogu

st.header('Wprowadzenie do aplikacji - Przetwarzanie języka naturalnego')
st.subheader('Do czego służy aplikacja?')
st.text('To prosta aplikacja z wykorzystaniem Streamlit i Hugging Face.')
st.write('Aplikacja pozwala sprawdzić wydźwięk emocjonalny tekstu po angielsku oraz przetłumaczyć tekst z języka angielskiego na niemiecki.')

st.info('Instrukcja: wybierz opcję, wpisz tekst po angielsku i kliknij przycisk.')

import streamlit as st
from transformers import pipeline

option = st.selectbox(
    'Opcje',
    [
        'Wydźwięk emocjonalny tekstu (eng)',
        'Tłumaczenie tekstu (eng -> de)',
    ],
)

text = st.text_area(label='Wpisz tekst')

if st.button('Uruchom'):
    if not text.strip():
        st.warning('Wpisz tekst, aby uruchomić model.')
    else:
        try:
            with st.spinner(text='Tłumaczenie trwa...'):
                time.sleep(1)

                if option == 'Wydźwięk emocjonalny tekstu (eng)':
                    classifier = pipeline('sentiment-analysis')
                    answer = classifier(text)
                    st.success('Analiza została wykonana poprawnie.')
                    st.write(answer)

                if option == 'Tłumaczenie tekstu (eng -> de)':
                    translator = pipeline('translation_en_to_de', model='Helsinki-NLP/opus-mt-en-de')
                    answer = translator(text)
                    st.success('Tłumaczenie zostało wykonane poprawnie.')
                    st.write(answer[0]['translation_text'])
        except Exception as e:
            st.error('Wystąpił błąd podczas działania aplikacji.')
            st.write(e)

st.subheader('Zadanie do wykonania')
st.write('s27499')