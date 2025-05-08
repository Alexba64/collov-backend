from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Modello per la richiesta JSON
class ImageRequest(BaseModel):
    image_url: str
    style: str
    room_type: str

# Route per la richiesta GET
@app.get("/")
def read_root():
    return {"message": "Hello World"}

# Aggiungi la route POST per /generate
@app.post("/generate")
async def generate_image(request: ImageRequest):
    # Simula l'elaborazione dell'immagine
    print(f"URL immagine: {request.image_url}")
    print(f"Stile: {request.style}")
    print(f"Tipo di stanza: {request.room_type}")
    
    # Restituisci una risposta di successo con una URL immagine di esempio
    return {"message": "Immagine generata con successo", "output": "url_dell_immagine_generata"}
