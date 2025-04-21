
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, crud, database

router = APIRouter()

@router.post("/bookings/", response_model=schemas.Booking)
def create_booking(booking: schemas.BookingCreate, db: Session = Depends(database.get_db)):
    return crud.create_booking(db, booking)

@router.get("/bookings/", response_model=list[schemas.Booking])
def read_bookings(db: Session = Depends(database.get_db)):
    return crud.get_bookings(db)
