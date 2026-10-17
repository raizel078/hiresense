import pymupdf
import spacy
from sympy.abc import lamda

nlp = spacy.load(
    "/home/nowa/Desktop/Project/models/resume_model/textcat_model/model-best"
)

def normalize(page_index ,blocks):
    result =[]
    for block in blocks:
        x0, y0,x1, y1 = block[0], block[1],block[2],block[3]
        text = block[4]

        dic = {'page':page_index,
               'x0':x0,
               'y0':y0,
               'x1':x1,
               'y1':y1,
               'text':text}

        result.append(dic)


    return  result



def extract_pdf(rowi):
    data = rowi.read()

    doc = pymupdf.open(stream=data, filetype ='pdf')
    all_blocks = []

    for page in doc:
        blocks = page.get_text('blocks')
        data = normalize(page.number , blocks)
        all_blocks.extend(data)

        for blocks in all_blocks:
            text = blocks['text']

            class_identity = nlp(text)
            scores = class_identity.cats
            category = max(scores, key= lambda name:scores[name])
            print(f'cat:{category} text Passed:{class_identity}/n')

