import nltk
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
nltk.download('words')
from nltk.sentiment import SentimentIntensityAnalyzer
from tqdm.notebook import tqdm

text_to_tokenize = "Produknya biasa aja, tak ada yang spesial yang menjadi nilai lebih dibanding produk serupa. Iklannya aja yang berlebihan"
tokenized = nltk.word_tokenize(text_to_tokenize)
print(tokenized)
tagged = nltk.pos_tag(tokenized)
print(tagged)

chunked = nltk.chunk.ne_chunk(tagged)
print(chunked)

sia = SentimentIntensityAnalyzer()
print(sia.polarity_scores("the product is good"))
