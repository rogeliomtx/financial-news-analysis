# Sentimental Analysis using FinBert
* https://huggingface.co/ProsusAI/finbert

## How to use
0. Due to github restrictions, you have to dowload one of the models from here:
https://drive.google.com/drive/folders/1uEjaVTLU6gCKuYFx5850KQ4NH1w74LyV?usp=sharing

1. Create and activate a virtual environment
```sh
virtialenv .venv
source .venv/bin/activate
```

1. Install dependencies
```sh
pip install -r requirements.txt
```

### The scrapper
3. Run the scrapper to collect new headings. This will create or update a csv file.
```
python -m scrapper/forbes.py
```

### The model (streamlit)
4. Run the app
```sh
python -m streamlit run app.py
```

## Fine-tuning using Bert
* https://huggingface.co/google-bert/bert-base-uncased

## Credits
* Rogelio Martinez - BTS
* Tehreem Fatima - BTS
* Anastasia Alexandra - BTS
* Dr. Ernesto Lee - https://drlee.io/fine-tuning-hugging-faces-bert-transformer-for-sentiment-analysis-69b976e6ac5d
* ChatGPTv4.0 ~ https://chat.openai.com/
* Github Copilot ~ https://github.com/features/copilot