from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import base64
from io import BytesIO
from PIL import Image

# Crea l'app FastAPI
app = FastAPI()

# Configura CORS per permettere richieste da specifici domini
origins = [
    "http://localhost",  # Per il test in locale
    "https://tuo-frontend.com",  # Il dominio del frontend in produzione
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Consente richieste da questi domini
    allow_credentials=True,
    allow_methods=["*"],  # Consente tutti i metodi HTTP
    allow_headers=["*"],  # Consente tutti gli header
)

# Modello Pydantic per la richiesta
class ImageRequest(BaseModel):
    image_url: str  # L'immagine sarà inviata come stringa base64
    style: str
    room_type: str

@app.post("/generate")
async def generate_image(request: ImageRequest):
    try:
        # Decodifica l'immagine base64
        img_data = base64.b64decode(request.image_url.split(',')[1])
        img = Image.open(BytesIO(img_data))
        
        # Logica di elaborazione dell'immagine (aggiungi manipolazioni, salvataggio, etc.)
        # Per esempio, puoi salvare l'immagine sul server o passare a un modello di AI
        
        # Per il momento, ritorniamo un URL fittizio per l'immagine generata
        return {"generatedImageUrl": "https://example.com/path/to/generated-image.jpg"}
    
    except Exception as e:
        raise HTTPException(status_code=422, detail=f"Errore durante l'elaborazione: {str(e)}")

# Pagina di test
@app.get("/")
def read_root():
    return {"message": "Hello World"}

