fastText vector mapper
=====================
This utility works with Facebook's [fastText](https://fasttext.cc) library's `print-word-vectors` function.

The goal is to generate word vectors from sentences and then create a mapping between word vectors generated and the original sentence. This utility is part of a larger Sentiment Analysis project.

Setup:
--------
* Please install **fastText** see [docs](https://github.com/facebookresearch/fastText#building-fasttext) for how to install fastText
* Generate a `model.bin` file or use one of those available for download from the **fastText** website.
* Export the path to your **fastText** executable and `model.bin` path into your environment e.g. `export FASTTEXT_EXE_PATH='/path/to/fasttext'; export MODEL_BIN_PATH='/path/to/model.bin'`

Example:
---------

```
$python vector_mapper.py simple_sentences.txt
```

```
# Outputs a namedTuple object
$ python vector_mapper.py simple_sentences.txt 
[SentenceRecord(id=UUID('2d51528c-e29f-493a-9227-dccde6de02ab'), sentence_string='The cat jumped off the wall', word_vectors_list=[u'The', u'cat', u'jumped', u'off', u'the', u'wall'])]
```

Additional Resources
--------------------
[Full TripAdvisor dataset](https://s3-ap-south-1.amazonaws.com/av-blog-media/wp-content/uploads/2017/04/04080929/Tripadvisor_hotelreviews_Shivambansal.txt)
