# smart_search modules

default_model = 'all-mpnet-base-v2'

# Identified symmetric models in order of Sentence Embedding Score
symmetric_models = ['all-mpnet-base-v2',
                    'multi-qa-mpnet-base-dot-v1',
                    'all-distilroberta-v1',
                    'all-MiniLM-L12-v2',
                    'multi-qa-distilbert-cos-v1',
                    'all-MiniLM-L6-v2',
                    'multi-qa-MiniLM-L6-cos-v1',
                    'paraphrase-albert-small-v2',
                    'paraphrase-MiniLM-L3-v2']

# Identified asymmetric models for cosine-similarity
asymmetric_cosine_similarity_models = ['msmarco-distilbert-base-v4',
                            'msmarco-roberta-base-v3',
                            'msmarco-distilbert-base-v3',
                            'msmarco-MiniLM-L-6-v3',
                            'msmarco-MiniLM-L-12-v3']

# Identified asymmetric models for dot-product
asymmetric_dot_product_models = ['msmarco-distilbert-base-tas-b',
                            'msmarco-distilbert-base-dot-prod-v3',
                            'msmarco-roberta-base-ance-firstp']   

# Identified cross-encoder models
cross_encoder_models = ['cross-encoder/ms-marco-MiniLM-L-12-v2',
                        'cross-encoder/ms-marco-MiniLM-L-6-v2',
                        'cross-encoder/ms-marco-MiniLM-L-4-v2',
                        'cross-encoder/ms-marco-MiniLM-L-2-v2'
                        'cross-encoder/ms-marco-TinyBERT-L-2-v2',
                        'cross-encoder/mmarco-mdeberta-v3-base-5negs-v1']

# Multilingual Models
multilingual_models = ['intfloat/multilingual-e5-large',
                       'intfloat/multilingual-e5-base',
                       'intfloat/multilingual-e5-small',
                       'distiluse-base-multilingual-cased-v2',
                       'multi-qa-MiniLM-L6-cos-v1',
                       'stsb-xlm-r-multilingual'
                      ]
                        
sentence_models = ['all-distilroberta-v1',
                   'allenai-specter',
                   'all-mpnet-base-v1',
                   'all-mpnet-base-v2',
                   'all-MiniLM-L6-v2',
                   'all-MiniLM-L12-v1',
                   'all-MiniLM-L12-v2',
                   'all-roberta-large-v1',
                   'average_word_embeddings_komninos',
                   'average_word_embeddings_levy_dependency',
                   'bert-base-nli-cls-token',
                   'bert-base-nli-max-tokens',
                   'bert-base-nli-mean-tokens',
                   'bert-base-nli-stsb-mean-tokens',
                   'bert-base-wikipedia-sections-mean-tokens',
                   'bert-large-nli-cls-token',
                   'bert-large-nli-stsb-mean-tokens',
                   'bert-large-nli-max-tokens',
                   'bert-large-nli-mean-tokens',
                   'clip-ViT-B-32',
                   'clip-ViT-L-14',
                   'clip-ViT-B-16',
                   'distilbert-base-nli-stsb-mean-tokens',
                   'distilbert-base-nli-stsb-quora-ranking',
                   'distilroberta-base-msmarco-v1',
                   'distilroberta-base-msmarco-v2',
                   'distilroberta-base-paraphrase-v1',
                   'facebook-dpr-ctx_encoder-multiset-base',
                   'facebook-dpr-ctx_encoder-single-nq-base',
                   'facebook-dpr-question_encoder-multiset-base',
                   'facebook-dpr-question_encoder-single-nq-base',
                   'gtr-t5-base',
                   'gtr-t5-large',
                   'gtr-t5-xl',
                   'gtr-t5-xxl',
                   'LaBSE',
                   'msmarco-bert-base-dot-v5',
                   'msmarco-bert-co-condensor',
                   'msmarco-distilbert-base-dot-prod-v3',
                   'msmarco-distilbert-base-tas-b',
                   'msmarco-distilbert-base-v2',
                   'msmarco-distilbert-base-v3',
                   'msmarco-distilbert-base-v4',
                   'msmarco-distilbert-dot-v5',
                   'msmarco-distilbert-cos-v5',
                   'msmarco-distilroberta-base-v2',
                   'msmarco-MiniLM-L-6-v3',
                   'msmarco-MiniLM-L-12-v3',
                   'msmarco-MiniLM-L6-cos-v5',
                   'msmarco-MiniLM-L12-cos-v5',
                   'msmarco-roberta-base-ance-firstp',
                   'msmacro-roberta-base-v2',
                   'msmarco-roberta-base-v3',
                   'multi-qa-distilbert-cos-v1',
                   'multi-qa-distilbert-dot-v1',
                   'multi-qa-MiniLM-L6-dot-v1',
                   'multi-qa-MiniLM-L6-cos-v1',
                   'multi-qa-mpnet-base-cos-v1',
                   'multi-qa-mpnet-base-dot-v1',
                   'nli-bert-base',
                   'nli-bert-base-cls-pooling',
                   'nli-bert-base-max-pooling',
                   'nli-bert-large',
                   'nli-bert-large-cls-pooling',
                   'nli-bert-large-max-pooling',
                   'nli-distilbert-base',
                   'nli-distilroberta-base-v2',
                   'nli-distilbert-base-max-pooling',
                   'nli-mpnet-base-v2',
                   'nli-roberta-base',
                   'nli-roberta-base-v2',
                   'nli-roberta-large',
                   'paraphrase-albert-base-v2',
                   'paraphrase-distilroberta-base-v1',
                   'paraphrase-distilroberta-base-v2',
                   'paraphrase-mpnet-base-v2',
                   'paraphrase-MiniLM-L3-v2',
                   'paraphrase-MiniLM-L6-v2',
                   'paraphrase-MiniLM-L12-v2',
                   'paraphrase-mpnet-base-v2',
                   'paraphrase-TinyBERT-L6-v2',
                   'quora-distilbert-base',
                   'roberta-base-nli-mean-tokens',
                   'roberta-base-nli-stsb-mean-tokens',
                   'roberta-large-nli-mean-tokens',
                   'roberta-large-nli-stsb-mean-tokens',
                   'sentence-t5-base',
                   'sentence-t5-large',
                   'sentence-t5-xl',
                   'sentence-t5-xxl',
                   'stsb-bert-base',
                   'stsb-bert-large',
                   'stsb-distilbert-base',
                   'stsb-distilroberta-base-v2',
                   'stsb-mpnet-base-v2',
                   'stsb-roberta-base-v2',
                   'stsb-roberta-base',
                   'stsb-roberta-large',
                   'xlm-r-bert-base-nli-mean-tokens',
                   'xlm-r-bert-base-nli-stsb-mean-tokens',
                   'xlm-r-distilroberta-base-paraphrase-v1']