#!/usr/bin/env python

from collections import namedtuple
from os import environ, unlink
from argparse import ArgumentParser
from subprocess import check_output
from tempfile import NamedTemporaryFile
from uuid import uuid4

FASTTEXT_EXE_PATH = environ.get('FASTTEXT_EXE', '/path/to/fasttext_binary')
MODEL_BIN_PATH = 'model.bin'

SentenceRecord = namedtuple('SentenceRecord', 'id sentence_string word_vectors_list')
sentence_to_vector_list = []


def parse_input_file(input_file_name):
    input_file_contents = open(input_file_name, 'r').readlines()
    for sentence in input_file_contents:
        sentence = sentence.replace('\n', '')
        sentence_record_id = uuid4()

        with NamedTemporaryFile(delete=False) as temp_sentence_file:
            temp_sentence_file.file.write(str.encode(sentence))
            temp_sentence_file.close()
            output = check_output(
                "{fasttext_exe} print-word-vectors {model_bin} < {filename}".format(fasttext_exe=FASTTEXT_EXE_PATH,
                                                                                    model_bin=MODEL_BIN_PATH,
                                                                                    filename=temp_sentence_file.name),
                shell=True)
            unlink(temp_sentence_file.name)

            if output:
                word_vectors_for_sentence = retrieve_word_vectors_from_output(output)

                sentence_record = SentenceRecord(
                    id=sentence_record_id,
                    sentence_string=sentence,
                    word_vectors_list=word_vectors_for_sentence
                )

        sentence_to_vector_list.append(sentence_record)


def retrieve_word_vectors_from_output(output):
    confirmed_vectors_list = []
    output_vectors_list = output.decode().split(' ')
    for possible_vector in output_vectors_list:
        try:
            possible_vector = possible_vector.replace('\n', '').strip()
            possible_vector = float(possible_vector)
        except Exception as e:
            confirmed_vectors_list.append(possible_vector)

    return confirmed_vectors_list


if __name__ == '__main__':
    parser = ArgumentParser(description='Map word vectors from input file to original sentence')
    parser.add_argument('input_file', type=str, help='File containing sentences on each line')
    args = parser.parse_args()
    parse_input_file(args.input_file)
    print(sentence_to_vector_list)
