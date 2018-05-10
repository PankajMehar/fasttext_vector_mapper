#!/usr/bin/env python

from os import environ
from uuid import uuid4
from tempfile import NamedTemporaryFile
from subprocess import Popen, check_output, PIPE
from collections import namedtuple

FASTTEXT_EXE_PATH = environ.get('FASTTEXT_EXE', '/path/to/fastText')
MODEL_BIN_PATH = 'model.bin'

SentenceRecord = namedtuple('SentenceRecord', 'id sentence_string word_vectors_list')
sentence_to_vector_list = []


def parse_input_file(input_file_name):
    input_file_contents = open(input_file_name, 'r').readlines()
    for sentence in input_file_contents:
        sentence = sentence.replace('\n', '')
        sentence_record_id = uuid4()

        temp_sentence_file = NamedTemporaryFile(delete=False)
        temp_sentence_file.file.write(str.encode(sentence))
        output = check_output([FASTTEXT_EXE_PATH, 'print-word-vectors', MODEL_BIN_PATH],
                              stdin=open(temp_sentence_file.name, 'r'))

        print(output)
        exit()

        if output:
            word_vectors_for_sentence = retrieve_word_vectors_from_output(output)

            sentence_record = SentenceRecord(
                id=sentence_record_id,
                sentence_string=sentence,
                word_vectors_list=word_vectors_for_sentence
            )

        # sentence_to_vector_list.append(sentence_record)


def retrieve_word_vectors_from_output(output):
    output_vectors_list = output.decode().split(' ')
    vectors_found = [possible_vector for possible_vector in output_vectors_list if isinstance(possible_vector, str)]
    return vectors_found


if __name__ == '__main__':
    parse_input_file('simple_sentences.txt')
    print(sentence_to_vector_list)
