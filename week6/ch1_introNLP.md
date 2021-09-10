# 1강 intro NLP
## What is NLP
이번 강의에서는 NLP란 무엇인지, NLP의 task가 무엇이 있는지 설명을 합니다.
### NLP의 task들
- low level parsing
  - Tokenization, stemming
- Word and phrase level
  - Named entity recognition(NER), part-of-speech(POS) tagging, noung-phrase chunking, dependency parsing, croeference resolution
- Sentence level
  - Sentiment analysis, machine translation
- Multi-setence and paragraph level
  - Entailment prediction, question answering, dialog systems, summarization

### Text Mining
- Extract useful information and insights from text and document data
  - e.g. analyzing the trends of AI-related keywords from massive news data
- Document clustering (e.g., topic modeling)
  - e.g., clustering news data and grouping into different subjects
- Highly related to computational social science
  - e.g., analyzing the evolution of people's political tendency based on social media data

- Information retrieval (major conferences: SIGIR, WSDM, CIKM, RecSys)
  - Highly related to computational social science
  - This area is not actively studied now
  - It has evolved into a recommendation system, which is still an active area of research

### Trends of NLP
- each word can be represented as a vector (w2v, GloVe)
- RNN-family models(LSTM and GRU) are the main architecture of NLP tasks.
- Transformer models, which replaced RNNs with self-attention

## Bag-of -Words
