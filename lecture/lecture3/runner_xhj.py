"""
Train retrieval-based chatbot on xiaohuangji subtitle dataset.

Use python 3
"""

import os
import sys
sys.path.append(os.getcwd())
sys.path.append(os.getcwd()+'/chatbot')
sys.path.append(os.getcwd()+'/chatbot/corpus')

args_in = '--device gpu0 '\
        '--modelTag xhj_2l_lr002_dr09_emb256_len20_vocab4000 '\
        '--vocabularySize 4000 --maxLength 20 '\
        '--learningRate 0.002 --dropout 0.9 '\
        '--rootDir  /your/path/to/lecture3 '\
        '--datasetTag xhj --corpus xiaohuangji'.split()

from rankbot import Rankbot
chatbot = Rankbot()
chatbot.main(args_in)
