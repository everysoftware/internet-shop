from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.goods.schemes import GoodCreate, GoodRead, GoodUpdate
from app.core import async_session_factory
from app.core.models import Good

router = APIRouter()


@router.post("/goods/")
async def create_good(good: GoodCreate, db: AsyncSession = Depends(async_session_factory)):
    good = Good(name=good.name, presence=good.presence, price=good.price)
    db.add(good)
    await db.commit()
    await db.refresh(good)
    return good


@router.get("/goods/{good_id}", response_model=GoodRead)
async def read_good(good_id: int, db: AsyncSession = Depends(async_session_factory)):
    good = await db.get(Good, good_id)
    if good is None:
        raise HTTPException(status_code=404, detail="Good not found")
    return good


@router.put("/goods/{good_id}", response_model=GoodRead)
async def update_good(good_id: int, good: GoodUpdate, db: AsyncSession = Depends(async_session_factory)):
    db_good = await db.get(Good, good_id)

    if db_good is None:
        raise HTTPException(status_code=404, detail="Good not found")

    if good.name is not None:
        db_good.name = good.name
    if good.presence is not None:
        db_good.presence = good.presence
    if good.price is not None:
        db_good.price = good.price

    # for key, value in good.__dict__.items():
    #    setattr(db_good, key, value)

    await db.merge(db_good)

    await db.commit()
    return db_good


@router.delete("/goods/{good_id}")
async def delete_good(good_id: int, db: AsyncSession = Depends(async_session_factory)):
    good = await db.get(Good, good_id)
    if good is None:
        raise HTTPException(status_code=404, detail="Good not found")
    await db.delete(good)
    await db.commit()
    return {"detail": "Good deleted"}
