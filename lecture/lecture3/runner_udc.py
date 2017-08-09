"""
Train retrieval based chatbot on Ubuntu Dialog Corpus.

Use python 3
"""

import os
import sys
sys.path.append(os.getcwd())
sys.path.append(os.getcwd()+'/chatbot')
sys.path.append(os.getcwd()+'/chatbot/corpus')

args_in = '--device gpu0 '\
        '--modelTag udc_2l_lr002_dr09_emb256_len50_vocab10000 '\
        '--vocabularySize 10000 --maxLength 50 '\
        '--learningRate 0.002 --dropout 0.9 '\
        '--rootDir /your/path/to/lecture3 '\
        '--datasetTag round3_7 --corpus ubuntu'.split()

from rankbot import Rankbot
chatbot = Rankbot()
chatbot.main(args_in)
