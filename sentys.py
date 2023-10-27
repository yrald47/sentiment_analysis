from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')
# nltk.download('vader_lexicon')
# nltk.download('stopwords')
from tqdm.notebook import tqdm

sia = SentimentIntensityAnalyzer()

print(sia.polarity_scores('I am so happy'))

input_str = "Solidnya peningkatan kredit salah satunya didorong oleh pelaksanaan BCA Expo 2023 di kuartal III tahun ini, melanjutkan kesuksesan BCA Expoversary 2023 pada Februari lalu. Kami melihat permintaan kredit konsumer yang masih solid, tercermin dari pelaksanaan dua kali expo di tahun ini yang mampu mengumpulkan total aplikasi KPR dan KKB senilai Rp 46 triliun, atau meningkat lebih dari 50% dibandingkan capaian tahun 2022"

stop_words = set(stopwords.words("indonesian"))
tokens = word_tokenize(input_str)
print(len(tokens))

result = [i for i in tokens if not i in stop_words]
print (len(result))
# result = [i for i in tokens if not i in stop_words]
# print (result)
