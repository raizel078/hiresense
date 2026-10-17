from fastapi import FastAPI, File, UploadFile
from helper import extract_pdf


app = FastAPI()

@app.post("/cv/")
async def create_file(file:UploadFile):
    rowi = file.file

    extract_pdf(rowi)





    return {'filename':file.filename}


