import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_db_session
from app.repositories.user_repo import UserRepository
from app.schemas.user import UserCreate, UserRead

router = APIRouter(prefix="/users", tags=["users"])


def get_repo(db: AsyncSession = Depends(get_async_db_session)) -> UserRepository:
    return UserRepository(db)


@router.post("/", response_model=UserRead, status_code=201)
async def create_user(data: UserCreate, repo: UserRepository = Depends(get_repo)):
    return await repo.create(data)


@router.get("/", response_model=list[UserRead])
async def list_users(repo: UserRepository = Depends(get_repo)):
    return await repo.get_all()


@router.get("/{user_id}", response_model=UserRead)
async def get_user(user_id: uuid.UUID, repo: UserRepository = Depends(get_repo)):
    user = await repo.get_by_id(user_id)
    if not user:
        raise HTTPException(404, "Usuario no encontrado")
    return user


@router.delete("/{user_id}", status_code=204)
async def delete_user(user_id: uuid.UUID, repo: UserRepository = Depends(get_repo)):
    if not await repo.delete(user_id):
        raise HTTPException(404, "Usuario no encontrado")
