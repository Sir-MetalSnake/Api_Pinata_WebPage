from pydantic import BaseModel

class ContactBaseModel(BaseModel):
    idContacto: int
    Direccion: str
    Telefono: str

class ContactResponse(ContactBaseModel):
    idContacto: int