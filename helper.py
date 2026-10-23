import pymupdf
import spacy
import pymupdf.layout
import pymupdf4llm

nlp = spacy.load(
    "/home/nowa/Desktop/Project/models/resume_model/textcat_model/model-best"
)

def extract_pdf(rowi):
    data = rowi.read()
    doc = pymupdf.open(stream=data, filetype='pdf')

    md = pymupdf4llm.to_markdown(doc)
    print(md)










