"""
Instructions from your teacher:
You are given a dictionary of words that indicate what sentiment score they have.
Given a list of strings, output a list of integers that indicates what total sentiment score the strings have.
Not all words are given a sentiment score, so some words or parts of words will not contribute to the sentiment score.

Example:

sentiments = {
 "amazing": 0.4,
 "sad": -0.8,
 "great": 0.8,
 "no": -0.1,
 "yes": 0.1,
 "angry": -0.7,
 "happy": 0.8
}

texts = [
  "that makes me so happy! amazing.", 
  "I'm so angry about this sad thing.", 
  "sad but true, amazing",
  "yes that is great, and amazing"
]
"""


Should output:
[1.2000000000000002, -1.5, -0.4, 1.3]

def sentiment_scores(sentiments, texts):
  result = [0] * len(texts)
  print(sentiments)
  
  for i in range(len(texts)):
    for word in texts[i].split():
      # print(word)
      word = word.strip("?!.,").lower()
      if word in sentiments:
        result[i] += sentiments.get(word)
  
  return result

print(sentiment_scores({
 "amazing": 0.4,
 "sad": -0.8,
 "great": 0.8,
 "no": -0.1,
 "yes": 0.1,
 "angry": -0.7,
 "happy": 0.8
}, [
  "that makes me so happy! amazing.", 
  "I'm so angry about this sad thing.", 
  "sad but true, amazing",
  "yes that is great, and amazing"
]))