from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.models.restaurant import Restaurant
from app.database import get_session

router = APIRouter()

@router.post("/restaurants/", response_model=Restaurant)
def create_restaurant(restaurant: Restaurant, session: Session = Depends(get_session)):
    session.add(restaurant)
    session.commit()
    session.refresh(restaurant)
    return restaurant

@router.get("/restaurants/", response_model=list[Restaurant])
def read_restaurants(session: Session = Depends(get_session)):
    restaurants = session.exec(select(Restaurant)).all()
    return restaurants

@router.put("/restaurants/{restaurant_id}", response_model=Restaurant)
def update_restaurant(restaurant_id: int, updated_restaurant: Restaurant, session: Session = Depends(get_session)):
    db_restaurant = session.get(Restaurant, restaurant_id)
    if not db_restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")

    db_restaurant.name = updated_restaurant.name
    db_restaurant.location = updated_restaurant.location
    db_restaurant.owner_id = updated_restaurant.owner_id

    session.add(db_restaurant)
    session.commit()
    session.refresh(db_restaurant)
    return db_restaurant

@router.delete("/restaurants/{restaurant_id}")
def delete_restaurant(restaurant_id: int, session: Session = Depends(get_session)):
    db_restaurant = session.get(Restaurant, restaurant_id)
    if not db_restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")

    session.delete(db_restaurant)
    session.commit()
    return {"message": f"Restaurant {restaurant_id} deleted"}